#include<unistd.h>
#include <libwandb_cpp.h>

int main() {
  auto wb = new wandb::Session();

  wandb::Config config = {
      {"param1", 4},
      {"param2", 4.2},
      {"param3", "smiles"},
  };
  auto run = wb->initRun({
      wandb::run::WithConfig(config),
      // wandb::run::WithRunID("runid"),
      // wandb::run::WithName("sample run name"),
  });

  for (int i = 0; i < 5; i++) {
    wandb::History history = {
        {"val", 3.14 + i},
        {"val2", 1.23 + i},
        {"val23", 1},
        {"cat", "dog"},
    };
    run.log(history);
  }

  run.finish();
  return 0;
}
