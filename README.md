# robosys_mypkg
これは2021年にロボットシステム学課題2で作成したROSパッケージです。

1から100で乱数を発生させ、1が出たら1Hzで「1」と「トゥース！！！！！！！！！！」を出力し、2から100が出たら50Hzで数字（「7」,「56」など）が出力されます。
***
# 動作環境
・Raspberry Pi 4

・python3

・ROS_VER : noetic

・OS : ubuntu 20.04 Server
***

# 使用方法
**・インストール**

以下のコマンドを実行してください。

```
$ git clone git@github.com:ryuseiiiii/robosys_mypkg.git

$ cd ~/robosys_mypkg/scripts/

$ chmod +x rannsuu.py

$ chmod +x rannsuu_rate.py
```
***
**・実行**

※デモ動画がこの下にあります。

端末1から順に以下のコマンドを実行してください。(Ctrl+Cで終了)

端末3と端末4は横に並べて見ると良いです。
***
**・端末1**
```
$ roscore &
```
***
**・端末2**
```
$ rosrun robosys_mypkg rannsuu.py
```
***
**・端末3**
```
$ rostopic echo /rand
```
***
**・端末4**
```
$ rosrun robosys_mypkg rannsuu_rate.py
```
***
# デモ動画　　変更途中
[[Raspberry Pi 4] デバイスドライバ](https://www.youtube.com/watch?v=oNSrJS55dIE)
***
# ライセンス
[BSD 3-Clause "New" or "Revised" License](https://github.com/ryuseiiiii/robosys_mypkg/blob/main/LICENSE)
***
# 参考
・以下のサイトを参考にしました。

[ROS インストール](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)

[python ファイル名](https://teratail.com/questions/173842)

[python 文字列の出力](https://qiita.com/Morio/items/4614b2f4483b1d8e5cc1#:~:text=%E7%94%BB%E9%9D%A2%E3%81%B8%E3%81%AE%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E5%87%BA%E5%8A%9B%E3%81%AF%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%81%AE%E5%9F%BA%E6%9C%AC%E4%B8%AD%E3%81%AE%E5%9F%BA%E6%9C%AC%E3%81%A7%E3%81%99%E3%80%82%20Python%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E7%94%BB%E9%9D%A2%E3%81%B8%E3%81%AE%E5%87%BA%E5%8A%9B%E3%81%AB%E3%81%AF%E3%80%8Cprint%E9%96%A2%E6%95%B0%E3%80%8D%E3%82%92%E4%BD%BF%E3%81%84%E3%81%BE%E3%81%99%E3%80%82,Python%E3%82%92%E4%BD%BF%E3%81%86%E4%B8%8A%E3%81%A7%E3%80%81print%E9%96%A2%E6%95%B0%E3%81%AF%E6%AC%A0%E3%81%8B%E3%81%99%E4%BA%8B%E3%81%8C%E5%87%BA%E6%9D%A5%E3%81%AA%E3%81%84%E3%82%82%E3%81%AE%E3%81%A7%E3%81%99%E3%80%82%20%E4%BB%8A%E5%9B%9E%E3%81%AFprint%E9%96%A2%E6%95%B0%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E8%AA%AC%E6%98%8E%E3%81%97%E3%81%BE%E3%81%99%E3%80%82%20print%E9%96%A2%E6%95%B0%E3%81%AF%E3%80%81%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E7%94%BB%E9%9D%A2%E3%81%AB%E5%87%BA%E5%8A%9B%E3%81%99%E3%82%8B%E9%96%A2%E6%95%B0%E3%81%A7%E3%81%99%E3%80%82)

[python random関数](https://techacademy.jp/magazine/15821)

[python インデント](https://www.sejuku.net/blog/71596)
***
# 自分のオリジナル　　変更途中
myled.c内の32行目から44行目は私のオリジナルです。目覚まし時計や小学生が良く持っている防犯ブザーをイメージして作成しました。
```
        else if(c == '2'){
                for(i=0;i<100;i++){
                        if(i%2 == 0){
                                gpio_base[7] = 1 << 25;
                                msleep(50);
                        }else if(1%2 != 0){
                                gpio_base[10] = 1 << 25;
                                msleep(50);
                        }
                }
                gpio_base[10] = 1 << 25;

        }
```
