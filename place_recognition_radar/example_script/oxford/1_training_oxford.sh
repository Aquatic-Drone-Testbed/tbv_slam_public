
#Optional visualization
#dir=`rospack find place_recognition_radar`
#rviz_config="${dir}/rviz/train_coral_viz.rviz"
#killall -r rviz >/dev/null
#rosrun rviz rviz -d ${rviz_config}&

rosrun place_recognition_radar coral_training --dataset oxford --sequence 2019-01-10-11-46-21-radar-oxford-10k --visualize 0 #Set to 1 for visualization
