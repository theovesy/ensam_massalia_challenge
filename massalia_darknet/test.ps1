Start-Process -FilePath "./darknet.exe" -ArgumentList "detector test data/obj.data cfg/yolo-obj.cfg yolo-obj_final.weights -map" -NoNewWindow -Wait
pause