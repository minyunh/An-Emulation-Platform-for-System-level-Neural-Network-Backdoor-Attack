# RoadRunner

## New

1. Open RoadRunner
2. Choose NewProject->Select save path -> Base+Add on(all of Asset)
3. New Scene

## Save


A. In roadrunner

1. File→ export → CARLA(.fbx, xodr, .rrdata.xml)
2. Choose file path, and save→ export.

→ get .fbx and .xodr file

B. plugin
1. download plugins: https://link.zhihu.com/?target=https%3A//www.mathworks.com/supportfiles/roadRunnerPlugins/RoadRunner_Plugins.zip
2. copy files (Unreal\Plugins) to Carla\unreal\carlaUE4\Plugins
3. make launch
4. Edit->plugins, check plugins installed

C. import 
1. Content/RoadRunne/Static (If not exisit, create)
2. right click static → Add/import content → import to / Game/RoadRunner/Static
3. Choose the file .fbx (step A-2)
4. New window (MathWorks RoadRunner Import Options) → choose Import
5. New window (FBX Scene Import Options) 
    1. Scene→ Hierarchy Type → choos Create one Blueprint
    2. Scene→ Texture → Invert Normal Maps
    3. Static Meshes → Normal Import Method → Import Normals
    
    And choose Import
    
6. right click FbxScene_XXX → choose Edit 
    1. new window up-left coner → choose  Components: DefaultSceneRoot
    2. Right side → Details → Transform → Mobility → Static
    3. Compile and Save
7. File->Save Current As...→Save XXX.umap in Content/RoadRunner/Maps
8. Copy  carla\Unreal\CarlaUE4\Content\Carla\Maps\OpenDrive\XXX.xodr to \CarlaUE4\Content\RoadRunner\Maps\OpenDrive (if not exisit, create OpenDrive)

→ Press button “Play” and run demo code !
