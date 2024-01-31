import os
os.system("pip uninstall -y mmcv-full")
os.system("mim install 'mmengine>=0.6.0'")
# os.system("pip install mmcv==2.0.1 -f https://download.openmmlab.com/mmcv/dist/cu118/torch2.0/index.html")
os.system("mim install 'mmcv-lite==2.0.1'")
os.system("mim install 'mmdet>=3.0.0,<4.0.0'")
os.system("mim install 'mmyolo'")
os.system("pip install -e .")
os.system("python tools/demo.py configs/pretrain/yolo_world_l_t2i_bn_2e-4_100e_4x8gpus_obj365v1_goldg_train_lvis_minival.py yolow-v8_l_clipv2_frozen_t2iv2_bn_o365_goldg_pretrain.pth")
