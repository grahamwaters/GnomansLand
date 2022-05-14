## Steps for Unity Setup and Installation of MLAgents Package

1. Download the mlagents package from GitHub.


_the following steps occur in the Unity application._
1. Create a new project named `GnomansLand_v1`
2. Open the package manager inside Unity.
3. Install the dependencies

Following the steps below, we will be creating our own customized environment for Neo Valley. This is where our agent population (the Gnomes) will live in the vanilla releases of the game. Later development will expand terretory to a tile-based auto-generated open world.

https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Create-New.md


### Food Collection Example from Unity
![foodcollection][foodCollector]

```sh
python -m pip install mlagents_envs==0.28.0
```

[foodCollector]:images/foodCollector.png