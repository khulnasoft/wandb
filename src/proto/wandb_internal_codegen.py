#!/usr/bin/env python

import os
import pathlib
import subprocess
from typing import Any, Dict, Optional

import grpc_tools  # type: ignore
from grpc_tools import protoc  # type: ignore
import pkg_resources


def generate_deprecated_class_definition() -> None:
    """
    Generate a class definition listing the deprecated features.
    This is to allow static checks to ensure that proper field names are used.
    """
    from wandb.proto.wandb_telemetry_pb2 import Deprecated  # type: ignore[import]

    deprecated_features = Deprecated.DESCRIPTOR.fields_by_name.keys()

    code: str = (
        "# Generated by src/proto/wandb_internal_codegen.py.  DO NOT EDIT!\n\n\n"
        "import sys\n\n\n"
        "if sys.version_info >= (3, 8):\n"
        "    from typing import Literal\n"
        "else:\n"
        "    from typing_extensions import Literal\n\n\n"
        "DEPRECATED_FEATURES = Literal[\n"
        + ",\n".join(f'    "{feature}"' for feature in deprecated_features)
        + "\n"
        + "]\n\n\n"
        "class Deprecated:\n"
        + "".join(
            [
                f'    {feature}: DEPRECATED_FEATURES = "{feature}"\n'
                for feature in deprecated_features
            ]
        )
    )
    with open("src/proto/wandb_deprecated.py", "w") as f:
        f.write(code)


def get_pip_package_version(package_name: str) -> str:
    out = subprocess.check_output(("pip", "show", package_name))
    info: Dict[str, Any] = dict(
        [line.split(": ", 2) for line in out.decode().rstrip("\n").split("\n")]  # type: ignore[misc]
    )
    return info["Version"]


def get_min_required_version(requirements_file_name: str, package_name: str) -> str:
    with open(requirements_file_name) as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split(">=")
            if tokens[0] == package_name:
                if len(tokens) == 2:
                    return tokens[1]
                else:
                    raise ValueError(
                        f"Minimum version not specified for package `{package_name}`"
                    )
    raise ValueError(f"Package `{package_name}` not found in requirements file")


package: str = "grpcio-tools"
package_version = get_pip_package_version(package)
requirements_file: str = "../../requirements_build.txt"
requirements_min_version = get_min_required_version(requirements_file, package)
# check that the installed version of the package is at least the required version
assert pkg_resources.parse_version(package_version) >= pkg_resources.parse_version(
    requirements_min_version
), f"Package {package} found={package_version} required>={requirements_min_version}"


protobuf_version = pkg_resources.parse_version(get_pip_package_version("protobuf"))

proto_root = os.path.join(os.path.dirname(grpc_tools.__file__), "_proto")
tmp_out: pathlib.Path = pathlib.Path(f"src/proto/v{protobuf_version.major}/")

os.chdir("../..")
for proto_file in [
    "wandb_base.proto",
    "wandb_internal.proto",
    "wandb_telemetry.proto",
]:
    ret = protoc.main(
        (
            "",
            "-I",
            proto_root,
            "-I",
            ".",
            f"--python_out={tmp_out}",
            f"--mypy_out={tmp_out}",
            f"src/proto/{proto_file}",
        )
    )
    assert not ret


ret = protoc.main(
    (
        "",
        "-I",
        proto_root,
        "-I",
        ".",
        f"--python_out={tmp_out}",
        f"--grpc_python_out={tmp_out}",
        f"--mypy_out={tmp_out}",
        f"--mypy_grpc_out={tmp_out}",
        "src/proto/wandb_server.proto",
    )
)
assert not ret


# clean up tmp dirs
for p in (tmp_out / "src" / "proto").glob("*pb2*"):
    p.rename(tmp_out / p.name)
os.rmdir(tmp_out / "src" / "proto")
os.rmdir(tmp_out / "src")

generate_deprecated_class_definition()
