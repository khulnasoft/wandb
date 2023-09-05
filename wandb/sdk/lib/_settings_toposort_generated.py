# DO NOT EDIT -- GENERATED BY: `generate-tool.py --generate`
__all__ = ("SETTINGS_TOPOLOGICALLY_SORTED", "_Setting")

import sys
from typing import Tuple

if sys.version_info >= (3, 8):
    from typing import Final, Literal
else:
    from typing_extensions import Final, Literal


_Setting = Literal[
    "_args",
    "_aws_lambda",
    "_async_upload_concurrency_limit",
    "_cli_only_mode",
    "_colab",
    "_cuda",
    "_disable_meta",
    "_disable_service",
    "_disable_setproctitle",
    "_disable_stats",
    "_disable_viewer",
    "_except_exit",
    "_executable",
    "_extra_http_headers",
    "_file_stream_retry_max",
    "_file_stream_retry_wait_min_seconds",
    "_file_stream_retry_wait_max_seconds",
    "_file_stream_timeout_seconds",
    "_file_uploader_retry_max",
    "_file_uploader_retry_wait_min_seconds",
    "_file_uploader_retry_wait_max_seconds",
    "_file_uploader_timeout_seconds",
    "_flow_control_custom",
    "_flow_control_disabled",
    "_graphql_retry_max",
    "_graphql_retry_wait_min_seconds",
    "_graphql_retry_wait_max_seconds",
    "_graphql_timeout_seconds",
    "_internal_check_process",
    "_internal_queue_timeout",
    "_ipython",
    "_jupyter",
    "_jupyter_name",
    "_jupyter_path",
    "_jupyter_root",
    "_kaggle",
    "_live_policy_rate_limit",
    "_live_policy_wait_time",
    "_log_level",
    "_network_buffer",
    "_noop",
    "_notebook",
    "_offline",
    "_sync",
    "_os",
    "_platform",
    "_python",
    "_runqueue_item_id",
    "_require_nexus",
    "_save_requirements",
    "_service_transport",
    "_service_wait",
    "_start_datetime",
    "_start_time",
    "_stats_pid",
    "_stats_sample_rate_seconds",
    "_stats_samples_to_average",
    "_stats_join_assets",
    "_stats_neuron_monitor_config_path",
    "_stats_open_metrics_endpoints",
    "_stats_open_metrics_filters",
    "_stats_disk_paths",
    "_tmp_code_dir",
    "_tracelog",
    "_unsaved_keys",
    "_windows",
    "allow_val_change",
    "anonymous",
    "api_key",
    "azure_account_url_to_access_key",
    "base_url",
    "code_dir",
    "config_paths",
    "console",
    "deployment",
    "disable_code",
    "disable_git",
    "disable_hints",
    "disable_job_creation",
    "disabled",
    "docker",
    "email",
    "entity",
    "files_dir",
    "force",
    "git_commit",
    "git_remote",
    "git_remote_url",
    "git_root",
    "heartbeat_seconds",
    "host",
    "ignore_globs",
    "init_timeout",
    "is_local",
    "job_name",
    "job_source",
    "label_disable",
    "launch",
    "launch_config_path",
    "log_dir",
    "log_internal",
    "log_symlink_internal",
    "log_symlink_user",
    "log_user",
    "login_timeout",
    "mode",
    "notebook_name",
    "problem",
    "program",
    "program_relpath",
    "project",
    "project_url",
    "quiet",
    "reinit",
    "relogin",
    "resume",
    "resume_fname",
    "resumed",
    "root_dir",
    "run_group",
    "run_id",
    "run_job_type",
    "run_mode",
    "run_name",
    "run_notes",
    "run_tags",
    "run_url",
    "sagemaker_disable",
    "save_code",
    "settings_system",
    "settings_workspace",
    "show_colors",
    "show_emoji",
    "show_errors",
    "show_info",
    "show_warnings",
    "silent",
    "start_method",
    "strict",
    "summary_errors",
    "summary_timeout",
    "summary_warnings",
    "sweep_id",
    "sweep_param_path",
    "sweep_url",
    "symlink",
    "sync_dir",
    "sync_file",
    "sync_symlink_latest",
    "system_sample",
    "system_sample_seconds",
    "table_raise_on_max_row_limit_exceeded",
    "timespec",
    "tmp_dir",
    "username",
    "wandb_dir",
]

SETTINGS_TOPOLOGICALLY_SORTED: Final[Tuple[_Setting, ...]] = (
    "_async_upload_concurrency_limit",
    "_service_wait",
    "_stats_sample_rate_seconds",
    "_stats_samples_to_average",
    "anonymous",
    "api_key",
    "base_url",
    "console",
    "job_source",
    "mode",
    "problem",
    "project",
    "run_id",
    "start_method",
    "_aws_lambda",
    "_colab",
    "_network_buffer",
    "_flow_control_disabled",
    "_flow_control_custom",
    "_ipython",
    "_jupyter",
    "_kaggle",
    "_noop",
    "_notebook",
    "disabled",
    "_offline",
    "_stats_neuron_monitor_config_path",
    "run_mode",
    "_start_datetime",
    "timespec",
    "root_dir",
    "wandb_dir",
    "tmp_dir",
    "_tmp_code_dir",
    "_windows",
    "is_local",
    "deployment",
    "files_dir",
    "log_dir",
    "log_internal",
    "log_symlink_internal",
    "log_symlink_user",
    "log_user",
    "project_url",
    "resume_fname",
    "run_url",
    "settings_system",
    "settings_workspace",
    "sweep_url",
    "sync_dir",
    "sync_file",
    "sync_symlink_latest",
)
