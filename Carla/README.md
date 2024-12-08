### 1. Compile the server

- `cd ~/carla`
- `make launch`

### 2. Start simulator(unreal engine)

- press the "play" button 
- should wait a minute
    

### 3. Compile client

- open another terminal
- `cd ~/carla/PythonAPI/examples`
- `python3 manual_control.py`
- `dynamic_weather.py` (if need)




- 讓車子生成在地圖中固定位置，走固定路徑:
-     spawn_point -> 生成點，可用 spawn_point.location.x = ? 去更改
-     destination -> 終點，可用 destination.x = ? 去更改
-     要注意不要選擇到地圖中不是道路的位置
-     也可以加參數 s=? ，讓每次一樣


- 車子的相機視角:
-     _camera_transforms = carla.Transform(carla.Location(x= , y=, z= ), carla.Rotation(pitch= , yaw= , rool= )), modeXXX)
-    x, y, z 跟車子的相對位置，車子中心是 （0, 0, z) z=0是地板，pitch,, yaw, roll 是相機角度
-    車子擋風玻璃視角: (carla.Transform(carla.Location(x=0.8, y=0, z=1.3), carla.Rotation(pitch=8.0)), attachment.Rigid)
-    車子: vehicle.lincoln.mkz_2020，不同車行視角需要微調，因為車身長度不一樣

去偵測路牌有三種方式:
1. 即時 (非常的卡不建議)
2. 將每一偵影像存下來，弄成影片，再去跑偵測 (還是會卡，但勉強可以)
   ```
   if save_img:
	else:
		vid_writer[i].write(im0)  #原本存影片frame
    path = str(Path(save_path).with_suffix("")) #設定存照片的路徑
		cv2.imwrite(path+str(seen)+".jpg", im0) #存照片
   ```
4. 利用螢幕錄影，再去跑偵測(順，但是依據使用的錄影方式，解析度可能跑掉)
   
