<link rel="stylesheet" type="text/css" media="all" href="style.css" />

# Game
by 王睿閎

![game](boom.gif)

## Introduction

一開始

介紹這款遊戲

玩家用{W,A,S,D}來移動，以{N,B}來射擊，玩家需要經由移動跟射擊來擊敗BOSS，敵人會攻擊玩家，把BOSS擊敗並且走到門後就能夠獲勝，如果生命值為0就會輸


---

## Implementation Details

我使用PYTHON跟PYCAT來做這款遊戲，在這個遊戲中我用到了這些程式語言list,class,inheritance。



---

## 遊戲創作

- 遇到的困難?
    在創作這款遊戲的過程中遇到了許多的困難
    
    1.讓玩家跳起來
    ```Python
    if w.is_key_down(KeyCode.W):#當W鍵按下時
        if self.is_touching_ground:#判斷是否碰到地板
            self.y_speed = 10
            self.is_touching_ground = False
    self.y += self.y_speed
    self.y_speed -= 0.5
        if self.y_speed < 0:
        while self.is_touching_any_sprite_with_tag('platform'):
            self.is_touching_ground = True
            self.y_speed = 0
            self.y += 0.5
    ```
---

## 程式碼

程式碼的連結 [code](https://github.com/HANKWRH/python-class-0/blob/main/L15/15-1.py)
