## Steps for Unity Setup and Installation of MLAgents Package

1. Clone the ml-agents package from GitHub.

`git clone --branch release_18 https://github.com/Unity-Technologies/ml-agents.git`


_the following steps occur in the Unity application._
1. Create a new project named `GnomansLand_v1`
2. Open the package manager inside Unity.
3. Install the dependencies

### You can add the local com.unity.ml-agents package (from the repository that you just cloned) to your project by:

1. Navigating to the menu Window -> Package Manager.
2. In the package manager window click on the + button on the top left of the packages list).
3. Select Add package from disk...
4. Navigate into the com.unity.ml-agents folder.
5. Select the package.json file.




Following the steps below, we will be creating our own customized environment for Neo Valley. This is where our agent population (the Gnomes) will live in the vanilla releases of the game. Later development will expand terretory to a tile-based auto-generated open world.

https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Create-New.md


### Food Collection Example from Unity
![foodcollection][foodCollector]

```sh
python -m pip install mlagents_envs==0.28.0
(GnomansLand) grahamwaters@iMac-3 ml-agents-unity % mlagents-learn config/gnome_config.yml --env=3DBall --inference
```

[foodCollector]:images/foodCollector.png