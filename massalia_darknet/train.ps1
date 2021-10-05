Start-Process -FilePath "./darknet.exe" -ArgumentList "detector train data/obj.data cfg/yolo-obj.cfg yolov4.conv.137 -map" -NoNewWindow -Wait
pause