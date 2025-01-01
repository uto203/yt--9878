import time
import math
import pygame

# 初期化関数で受け取る変数をグローバル変数として扱う
def initialize(**kwargs):
    global screen, player_rect, player_bullets, last_circle_shot_time
    # 必要なオブジェクトや設定を受け取って使用可能にする
    screen = kwargs.get('screen')
    player_rect = kwargs.get('player_rect')
    player_bullets = kwargs.get('player_bullets')
    
    # 最後に弾を撃った時間を記録する変数（2秒ごとに撃つために使用）
    last_circle_shot_time = 0

# 弾丸を周囲に発射する関数
def on_fire(bullet):
    global last_circle_shot_time
    
    # 2秒ごとの発射
    current_time = time.time()
    if current_time - last_circle_shot_time >= 2:
        # プレイヤーの周囲に円形に弾を撃つ
        angle_step = 45  # 弾を撃つ角度の間隔
        speed = 5  # 弾の速度
        bullet_size = (10, 10)  # 弾のサイズ
        bullet_color = (0, 255, 0)  # 緑色の弾
        
        # 360度分、45度刻みで弾を生成
        for angle in range(0, 360, angle_step):
            radians = math.radians(angle)
            velocity = (speed * math.cos(radians), speed * math.sin(radians))
            
            # 新しい弾を生成し、プレイヤーの位置を中心に設定
            new_bullet = {
                'pos': list(player_rect.center),
                'velocity': velocity,
                'size': bullet_size,
                'color': bullet_color,
                'animation_index': 0,
                'last_anim_time': current_time
            }
            
            # player_bulletsリストに追加
            player_bullets.append(new_bullet)
        
        # 最後に弾を撃った時間を更新
        last_circle_shot_time = current_time

# 毎フレーム呼ばれる更新処理
def update():
    # 各弾丸の位置を更新
    for bullet in player_bullets:
        bullet['pos'][0] += bullet['velocity'][0]
        bullet['pos'][1] += bullet['velocity'][1]

# 描画関数
def draw(screen):
    for bullet in player_bullets:
        # 緑色のデフォルトの色を設定（色が指定されていない場合）
        color = bullet.get('color', (0, 255, 0))
        pygame.draw.circle(screen, color, (int(bullet['pos'][0]), int(bullet['pos'][1])), bullet['size'][0] // 2)
