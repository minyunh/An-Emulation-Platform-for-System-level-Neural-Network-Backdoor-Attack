
Install

https://carla.readthedocs.io/en/latest/build_linux/

https://hackmd.io/Xn8EqrPlTwy2TgUP7NWM2Q

- Software requirements
    
    ```
    sudo apt-get update &&
    sudo apt-get install wget software-properties-common &&
    sudo add-apt-repository ppa:ubuntu-toolchain-r/test &&
    wget -O - <https://apt.llvm.org/llvm-snapshot.gpg.key|sudo> apt-key add
    
    ```
    
    - Ubuntu 20.04.
        
        ```
        sudo apt-add-repository "deb <http://apt.llvm.org/focal/> llvm-toolchain-focal main"
        sudo apt-get update
        sudo apt-get install build-essential clang-10 lld-10 g++-7 cmake ninja-build libvulkan1 python python-dev python3-dev python3-pip libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev git
        sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-10/bin/clang++ 180 &&
        sudo update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-10/bin/clang 180
        
        ```
        
    - If you need to upgrade:
    `pip3 install --upgrade pip`
    - install the following Python dependencies:
        
        ```
        pip install --user setuptools &&
        pip3 install --user -Iv setuptools==47.3.1 &&
        pip install --user distro &&
        pip3 install --user distro &&
        pip install --user wheel &&
        pip3 install --user wheel auditwheel
        
        ```
        
    - Unreal Engine
    - Clone the content for CARLA's fork of Unreal Engine 4.26 to your local computer:
        
        ```
        git clone --depth 1 -b carla <https://github.com/CarlaUnreal/UnrealEngine.git> ~/UnrealEngine_4.26
        
        ```
        
    - token https://hackmd.io/@yillkid/ry_FvBmWY
    - pass by 20240610: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
        
        `cd ~/UnrealEngine_4.26`
        
    - Make the build. This may take an hour or two depending on your system.
        
        ```
        ./Setup.sh && ./GenerateProjectFiles.sh && make
        
        ```
        
    - Open the Editor to check that Unreal Engine has been installed properly.
        
        ```
        cd ~/UnrealEngine_4.26/Engine/Binaries/Linux && ./UE4Editor
        
        ```
        
    - Build CARLA
        
        ```
        git clone <https://github.com/carla-simulator/carla>
        
        ```
        
    - Get assets
        
        ```
        ./Update.sh
        
        ```
        
    - Open ~/.bashrc
        
        ```
        gedit ~/.bashrc
        
        ```
        
    - Add the following line to the bottom of the file:
        
        ```
        export UE4_ROOT=~/UnrealEngine_4.26
        
        ```
        
    - source ~/.bashrc
    - Builds the CARLA client.
    
    ```
    make PythonAPI
    
    ```
    
    - Launches CARLA server in Editor window
    
    ```
    make launch
    
    ```
    
    - cd PythonAPI/examples
    - python3 -m pip install -r requirements.txt
    - pip3 install shapely
    - pip3 isntall networkx
    - If the simulation is running at a very low FPS rate, go to Edit -> Editor preferences -> Performance in the Unreal Engine editor and disable Use less CPU when in background.
