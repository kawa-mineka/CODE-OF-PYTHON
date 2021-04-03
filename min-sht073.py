#####################################
# -----    code of python     ----- #
#####################################
#     program mineka.kawakami       #
#           2020 06/28              #
#     language python 3.8(64bit)    #
#                                   # 
#       OS windows10(64bit)         #
#          Editer vs-code           #
#         Game Engine Pyxel         #
#                                   #
#        Development machine        #
#          CPU corei5-6500          #
#         base clock 3.2Ghz         #
#    turboboost clock 3.6Ghz        #
#           4Core 4thread           #
#        GPU GeForce GTX960         #
#            Memory 8GB             #
#####################################

#todo1 MOUNTAIN_REGION 地下洞窟＆地底湖の実装
#todo4 MOUNTAIN_REGION ブリザーディア(ボス)の実装(かなり難しい.......)
#todo10 MOUNTAIN_REGION 大気圏突入時のスタッフクレジット表示の実装

#todo12 MOUNTAIN_REGION 中ボスの実装
#todo13 ADVACE_BASE 中ボスの実装
#todo15 VOLCANIC_BELT スクロールシステムの構築(縦2画面フリースクロール＋横強制スクロール)+ラスタースクロールによる炎の演出+上下3キャララインほどの多ラインスクロール
#todo16 VOLCANIC_BELT メインスクロール面でのプロミネンスアニメーション(当たり判定アリ)
#todo17 VOLCANIC_BELT メインスクロール面に重ね合わせての岩盤(ＢＧ)の挟みこみアニメーション実装
#todo17A VOLCANIC_BELT 暗闇の中を突き進んでいくスポットライトエフェクトの実装

#todo18 ゲームプレイ中の実績解除ダイアログ表示（ボスキャラ戦闘中は表示せず破壊後か破壊できなかったらリスタート時に表示）
#todo19 汎用性のある中ボスの実装
#todo21 汎用母艦「アークウェスディ」からの自機射出演出
#todo23 狙い撃ちn-way弾を射出する関数で偶数弾の処理が微妙に奇数弾っぽくなってるのを治す(自機狙いの弾が出なくて奇数弾→偶数弾になってるポイ)
#todo29 敵の2回屈折サーチレーザーの実装
#todo30 敵のウェーブカッターの実装
#todo31 敵のリップルレーザーの実装
#todo32 敵のワインダーレーザーの実装
#todo33 敵のサークルレーザーの実装
#todo36 敵の反射レーザーの実装
#todo39 敵のスプレッドボムの実装
#todo40 敵のロックオンレーザーの実装（実際にロックオンされて当たる訳ではないので注意）

#todo50 NIGHT_SKYSCRAPER 夜間超高層ビル地帯の背景グラフイックとスクロールシステムの構築(縦2画面任意スクロール＋左右マップリピートによる3重スクロール)
#todo51 NIGHT_SKYSCRAPER 中ボスの実装
#todo52 NIGHT_SKYSCRAPER ボスの実装



#todo80 ネームエントリー(別に必要ないかも？ストーリー重視だから・・)
#todo81 第2の機体ElegantPerlの実装
#todo82 ElegantPerl専用のPerlCrawの実装
#todo83 機体選択シーンの実装
#todo84 機体選択シーンにおける各機体のタイポモーションロゴのアニメーション作成(難しそう)

#todo90 MagiForceとJusticePythonの合体演出
#todo91 美咲フォントを使用した日本語テキスト表示関数の実装


#todo703 画面上の任意の位置＆画面下の任意の位置から降下、上昇してくる敵編隊の実装
#todo705 子世代まで分裂する隕石の実装(結構硬い感じで)
#todo706 画面後ろから出てきて画面前方まで移動し、x軸合わせのサーチレーザーを撃ってくる敵（ちょっと硬め）の実装
#todo707 自機とx軸が一致したら上または下方向に発射されるロングロケットミサイル→ドット絵作成済み
#todo708 斜め前方にレーザー（少し長め）を等間隔で発射してくるレーザー固定砲台→ドット絵作成済み
#todo709 3way弾を撃ってくる固定砲台(近づくと反応してくる)→ドット絵作成済み
#todo710 自機とx軸が一致したら高速レーザーを発射する固定砲台→ドット作成済み
#todo711 前からゆっくりとやってきてある程度の距離まで進んだら下部に装備している高速ミサイルを発射して上方向か下方向に離脱していく中型機→ドット絵作成済み
#todo712 高速回転キリ揉み飛行で一撃離脱で大量の弾をばらまいていく高速機（最初自機のクローとして使おうとしてた物をドット絵として再利用する）→ドット絵作成済み

#todo800 メイン武器を高速で切り替えたときグラフイックパターンがおかしくなるバグ取り
#todo801 ボスを倒した瞬間,自機がほぼ同時にやられた場合、進行不可になるバグの処置
#todo801 自機が爆発中にボスが出現すると、進行不可になるバグの処置
#todo803 ウィンドウシステムを改良する（滅茶苦茶難しそう・・・今は同じようなコードを羅列してるだけなのでシンプルに行きたいところですが・・）
#todo804 難易度選択によるスタート時のクロー追加ボーナスでローリングクローだけ上手く複数追加されない(1個だけなら追加される)(おそらく2~4個追加時に全く同じ座標で回転し続けて1個だけで回っているように見える？のかも？)要バグ取り


#todo900 BGMの作成(無理そう.........)

#実装完了済み！
#todo2 MOUNTAIN_REGION 雲後面ラスタスクロール＋前面雲スクロールの実装 2021 02/06 実装完了
#todo3 BGマップチップデータ書き換えによるアニメーションの実装 2021 01/27 実装完了 2021 02/08 スクロール中面の山脈の小さな滝アニメも実装
#todo9 MOUNTAIN_REGION 大気圏突入時の自機との摩擦面の加熱エフェクトと火花の描画実装 2021 02/08 だいたい実装完了
#todo8 今まではイメージバンク0~2は背景オブジェクト,BGパターン,フォントがいろんな場所に散らばっていたのを、イメージバンク0は奇数面のBG,1は偶数面のBG,2はオブジェクトに分けて整理する 2021 02/06 処理完了
#todo14 メニューでのステージ&ループ数選択の実装 2021 02/14 実装完了
#todo11 MOUNTAIN_REGION リスタート時、宇宙での流れる星や成層圏のラスタースクロールが表示されなくなるバグ取り(変数を初期化できてないっぽい？) bg_cls_colorとbg_transparent_colorを__init__だけでなくstage_start_initでも初期化するようにした（ゲーム中のイベントで変化することもあるのでステージスタート時でも初期化した）2021 02/14 実装完了
#todo20 ボスの当たり判定を「弱点」と「自機のみにダメージを与える部分」に分ける（今までは「自機のみにダメージを与える部分」にもショットを当てるとダメージを与えていた）ボスのダメージ判定矩形を大きくするとレーザーで大ダメージを与えて弱くなるのでサイズの調整必要あり 2021 02/14 実装完了
#todo23 狙い撃ちn-way弾を射出する関数の実装 2021 02/20 実装完了
#todo24 敵の誘導弾の実装 2021 02/21 実装完了
#todo25 敵のホーミングレーザーの実装 2021 02/21 実装完了
#todo26 敵のサイン＆コサイン弾の実装 2021 02/22 実装完了
#todo27 敵のサーチレーザーの実装 2021 02/27 実装完了
#todo28 敵の回転弾の実装 2021 02/28 実装完了 2021 03/07 回転半径も変化させることが出来るようにした
#todo   敵の加速弾、減速弾の実装完了 2021 02/28 
#todo34 敵の落下弾の実装 2021 02/28 実装完了
#todo35 敵の分裂弾の実装 2021 02/28 実装完了 2021 03/06 複数回の分裂も可能にした
#todo37 敵のアップレーザーの実装 2021 03/08 実装完了→背景障害物との当たり判定が左端の8x8ドットでしか行われていないバグ
#todo38 敵のダウンレーザーの実装 2021 03/08 実装完了→背景障害物との当たり判定が左端の8x8ドットでしか行われていないバグ
#todo41 敵のベクトルレーザーの実装 2021 03/10 実装完了→レーザーの長さを一番上基準ではなく中央基準にする
#todo701 自機とx軸が一致したら上下から挟みこみ攻撃する敵の実装(クランパリオン) 2021 03/14 実装完了→上下挟み込み時も縦のイオンエンジン描画アニメをさせる
#todo702 画面内のあらかじめ決められた場所へスプライン曲線で移動しそこについたら狙い撃ち弾を出して画面外へ高速離脱する敵の実装(ロールブリッツ) 2021 03/14 実装完了
#todo41 難易度選択メニューの実装 2021 03/28 実装完了
#todo704 チョット大き目で耐久力のある広めの範囲から自機狙い＆ばらまき弾を撃ってくる重爆撃機みたいな敵の実装 2021 03/20 実装完了
#todo712 爆発パターンがその場で爆発していただけなので地上物はスクロールスピードに合わせて爆発パターンが移動するようにする 2021 03/20 実装完了

from random import randint
from random import random
import pyxel
#import pygame #MP3再生するためだけに使用する予定・・・予定は未定・・・
import math

#定数の定義関連##################################################################################################
WINDOW_W = 160     #ゲームウィンドウの横サイズ
WINDOW_H = 120     #ゲームウィンドウの縦サイズ
SHIP_H = 8         #自機の縦サイズ
SHIP_W = 8         #自機の横サイズ
MOVE_LIMIT = 20    #前方に進める限界距離


SHOT_EXP_MAXIMUM    = 71 #自機ショットの最大経験値（この数値を超えちゃダメだよ）
                         #例 self.j_python_shot_table_listのｙ軸の最大値がこの数と一致します
                         #これより大きい数値にしちゃうとindex erroerになっちゃうからね
MISSILE_EXP_MAXIMUM = 71 #自機ミサイルの最大経験値（この数値を超えちゃダメだよ）
                         #例 self.j_python_missile_table_listのｙ軸の最大値がこの数と一致します
                         #これより大きい数値にしちゃうとindex erroerになっちゃうからね

#!ゲームステータス関連の定数定義 game_statusに代入されます#######################################################################
SCENE_IPL                 =  0    #IPL(Initial Program Load)
SCENE_SPLASH_LOGO         =  1    #起動処理中（スプラッシュロゴ表示）

SCENE_TITLE_INIT          = 10    #タイトル表示に必要な初期化をする
SCENE_TITLE               = 11    #タイトル表示中
SCENE_TITLE_MENU_SELECT   = 12    #タイトルメニュー選択中
SCENE_CREDIT              = 13    #クレジットタイトル表示中

SCENE_CONFIG              = 20    #設定メニュー表示中

SCENE_DEBUG_CONGIG        = 30    #デバッグモード設定メニュー表示中

SCENE_TITLE_DEMO          = 40    #タイトルデモ表示中（ストーリーとかのビジュアルシーン）
SCENE_ADVERTISE_DEMO      = 41    #アドバタイズデモ（コンピュータによるゲームの宣伝の為のリプレイ再生）
SCENE_MIDDLE_DEMO         = 42    #中間デモ中

SCENE_GAME_START_INIT     = 50    #ゲーム開始前の初期化    スコアやシールド値、ショットレベルやミサイルレベルなどの初期化
SCENE_STAGE_START_INIT    = 51    #ステージ開始前の初期化   自機の座標や各リストの初期化、カウンター類の初期化
SCENE_START               = 52    #ゲーム開始(スタートダイアログを出したり、自機の出現アニメーションとか)
SCENE_PLAY                = 53    #ゲームプレイ中
SCENE_BOSS_APPEAR         = 54    #ボスキャラ現れる！
SCENE_BOSS_BATTLE         = 55    #ボスキャラと戦闘中
SCENE_BOSS_EXPLOSION      = 56    #ボスキャラ爆発中！
SCENE_PAUSE               = 57    #一時中断中
SCENE_EXPLOSION           = 58    #被弾して爆発中（ゲーム自体はまだ進行している）
SCENE_RESTORATION         = 59    #復活中(自機は点滅状態で無敵状態だよ)

SCENE_GAME_OVER           = 60 #ゲームオーバーメッセージ表示中（ゲームはまだ進行している）
SCENE_GAME_OVER_FADE_OUT  = 61 #ゲームオーバーメッセージ表示中（ゲーム自体は停止、画面をフェードアウトさせていく）
SCENE_GAME_OVER_SHADOW_IN = 62 #ゲームオーバーメッセージ表示中（ゲーム自体は停止、画面をシャドウインさせていく）
SCENE_GAME_OVER_STOP      = 63 #ゲームオーバーメッセージ表示中（ゲーム自体は停止している）
SCENE_RETURN_TITLE        = 64 #ゲームオーバーになりタイトルに戻るかどうかカーソルを出して選択待ち

SCENE_STAGE_CLEAR               = 70 #ステージクリア
SCENE_STAGE_CLEAR_MOVE_MY_SHIP  = 71 #ステージクリア後、自機がステージクリア画像左上まで自動に動いていくシーン
SCENE_STAGE_CLEAR_MY_SHIP_BOOST = 72 #ステージクリア後、自機がブーストして右へ過ぎ去っていくシーン
SCENE_STAGE_CLEAR_FADE_OUT      = 73 #ステージクリア後のフェードアウト

SCENE_CONTINUE    = 80   #コンティニューメッセージ表示中

SCENE_ENDING      = 90   #エンディング表示中

SCENE_STAFF_ROLL  = 99   #スタッフロール表示中

#自機のIDナンバー定義
J_PYTHON =          0    #Justice Python
PYTHON_FORCE =      1    #Python4.0(4th.force)
E_PERL =            2    #Elegant Perl(practical extraction and report language)
C_FORTRAN =         3    #Classical FORTRAN 1954
AI_LOVE_LISP =      4    #AI love LISP 1958
ECLIPSING_ALGOL =   5    #Eclipsing Binary ALGOL 1958
AUNT_COBOL =        6    #Aunt COBOL more better 1959
BEGINNING_ADA =     7    #Beginning programmer Ada 1815-1983
FIRST_BASIC =       8    #First Beginners All purpose Symbolic Instruction Code 1964
CUTTER_SHARP_2000 = 9    #Cutter # 2000
LEGEND_ASM        = 10   #Legend Assembler
LAST_RUST         = 11   #Last Rust
GAMBA_RUBY        = 12   #GAMBA Ruby New Generation IDOL
SHIFT_SWIFT       = 13   #SHIFT timer SWIFT space
MAGI_FORCE        = 14   #MAGI FORCE power is dream
LOOK_AT_LOGO      = 15   #LOOK AT THE TURTLE LOGO! 1967

#サブウェポン関連のIDナンバー定数定義
TAIL_SHOT        = 0 #テイルショットＩＤナンバー
PENETRATE_ROCKET = 1 #ペネトレートロケットＩＤナンバー
SEARCH_LASER     = 2 #サーチレーザーＩＤナンバー
HOMING_MISSILE   = 3 #ホーミングミサイルＩＤナンバー
SHOCK_BUMPER     = 4 #ショックバンパーＩＤナンバー

#難易度リストを参照するときに使用するインデックスナンバー定数定義
LIST_DIFFICULTY          = 0 #難易度(難しさ)
LIST_START_BONUS_SHOT    = 1 #ゲーム開始時のショットボーナス
LIST_START_BONUS_MISSILE = 2 #ゲーム開始時のミサイルボーナス
LIST_START_BONUS_SHIELD  = 3 #ゲーム開始時のシールドボーナス
LIST_START_CLAW          = 4 #ゲーム開始時のクローの数
LIST_REPAIR_SHIELD       = 5 #ステージクリア後に回復するシールド値
LIST_RETURN_BULLET       = 6 #撃ち返し弾の有無と有の時の種類
LIST_SCORE_MAGNIFICATION = 7 #スコア倍率
LIST_RANK_EXPONENTIAL    = 8 #ランク上昇指数
LIST_START_RANK          = 9 #ゲームスタート時のランク数
#難易度名の定数定義
GAME_VERY_EASY = 0
GAME_EASY      = 1
GAME_NORMAL    = 2
GAME_HARD      = 3
GAME_VERY_HARD = 4
GAME_INSAME    = 5 #狂ってる・・・・・

#ランクリストを参照するときに使用するインデックスナンバー定数定義
LIST_RANK                           = 0  #ランク数
LIST_RANK_E_SPEED_MAG               = 1  #敵スピード倍率
LIST_RANK_BULLET_SPEED_MAG          = 2  #敵狙い撃ち弾スピード倍率
LIST_RANK_RETURN_BULLET_PROBABILITY = 3  #敵撃ち返し弾発射確率
LIST_RANK_E_HP_MAG                  = 4  #敵耐久力倍率

#ゲーム開始時に追加されるクロー数の定数定義
NO_CLAW        = 0
ONE_CLAW       = 1
TWO_CLAW       = 2
THREE_CLAW     = 3
#ステージクリア時に回復するシールド値
REPAIR_SHIELD0 = 0
REPAIR_SHIELD1 = 1
REPAIR_SHIELD2 = 2
REPAIR_SHIELD3 = 3


#!ステージの名称関連の定数定義################################################################
STAGE_MOUNTAIN_REGION         = 1 #ステージ1 山岳地帯             Mountain Region
STAGE_ADVANCE_BASE            = 2 #ステージ2 前線基地             Advance Base
STAGE_VOLCANIC_BELT           = 3 #ステージ3 火山地帯             Volcanic Belt
STAGE_NIGHT_SKYSCRAPER        = 4 #ステージ4 夜間超高層ビル地帯    Night Skyscraper
STAGE_AMPHIBIOUS_ASSAULT_SHIP = 5 #ステージ5 強襲揚陸艦襲撃       Amphibious Assault Ship
STAGE_DEEP_SEA_TRENCH         = 6 #ステージ6 深海海溝             Deep Sea Trench
STAGE_INTERMEDIATE_FORTRESS   = 7 #ステージ7 中間要塞             Intermediate Fortress
STAGE_ESCAPE_FORTRESS         = 8 #ステージ8 要塞脱出             Escape Fortress
SATGE_BOSS_RUSH               = 9 #ステージ9 連続強敵襲来          Boss Rush

#クロー関連の定数定義（主にトレースクロー）
TRACE_CLAW_COUNT = 4        #トレースクローの数
TRACE_CLAW_INTERVAL = 60    #トレースクローの間隔
TRACE_CLAW_BUFFER_SIZE = 60 #トレースクローのバッファーサイズ   1フレームは60分の1秒 60フレームで1秒分となります
CLAW_RAPID_FIRE_NUMBER = 2  #クローの最大連射数

SHIP_EXPLOSION_TIMER_LIMIT = 180 #自機が爆発した後、まだどれだけゲームが進行し続けるかのタイマー限界数
GAME_OVER_TIMER_LIMIT = 180      #ゲームオーバーダイアログを表示した後まだどれだけゲームが進行し続けるのかのタイマー限界数

FADE_IN = 0                      #フェードインアウト用エフェクトスクリーン用の定数定義 0=in 1=out
FADE_OUT = 1

#イメージバンクの定数定義
IMG0 = 0 #イメージバンク0
IMG1 = 1 #イメージバンク1
IMG2 = 2 #イメージバンク2

#パーティクルの種類
PARTICLE_DOT = 0                 #パーティクルタイプ 1~2ドット描画タイプ(破壊後のエフェクト)
PARTICLE_CIRCLE = 1              #パーティクルタイプ 円形パーティクル   (破壊後のエフェクト)
PARTICLE_LINE = 2                #パーティクルタイプ ラインパーティクル (跳ね返りエフェクト)
PARTICLE_FIRE_SPARK = 3          #パーティクルタイプ 大気圏突入時の火花 (火花が飛び散るエフェクト)

PARTICLE_SHOT_DEBRIS = 4         #パーティクルタイプ 自機ショットの破片(デブリ)(障害物に当たったエフェクト)
PARTICLE_MISSILE_DEBRIS  = 5     #パーティクルタイプ 自機ミサイルの破片(デブリ)(障害物に当たったエフェクト)

PARTICLE_BOSS_DEBRIS1  = 6       #パーティクルタイプ ボスの破片1(破壊後のエフェクト)かなり大きい金属プレート
PARTICLE_BOSS_DEBRIS2  = 7       #パーティクルタイプ ボスの破片2(破壊後のエフェクト)回転するブロック状な物
PARTICLE_BOSS_DEBRIS3  = 8       #パーティクルタイプ ボスの破片3(破壊後のエフェクト)ホワイト系のスパーク 
PARTICLE_BOSS_DEBRIS4  = 9       #パーティクルタイプ ボスの破片4(破壊後のエフェクト)橙色系の落下する火花
PARTICLE_BOSS_DEBRIS5  = 10      #パーティクルタイプ ボスの破片5(破壊後のエフェクト)
PARTICLE_BOSS_DEBRIS6  = 11      #パーティクルタイプ ボスの破片6(破壊後のエフェクト)

#背景オブジェクトの種類
BG_OBJ_CLOUD1,BG_OBJ_CLOUD2,BG_OBJ_CLOUD3,BG_OBJ_CLOUD4,BG_OBJ_CLOUD5        = 0,1,2,3,4       #雲小1~5
BG_OBJ_CLOUD6,BG_OBJ_CLOUD7,BG_OBJ_CLOUD8,BG_OBJ_CLOUD9,BG_OBJ_CLOUD10       = 5,6,7,8,9       #雲小6~10

BG_OBJ_CLOUD11,BG_OBJ_CLOUD12,BG_OBJ_CLOUD13,BG_OBJ_CLOUD14,BG_OBJ_CLOUD15   = 10,11,12,13,14  #雲中11~15
BG_OBJ_CLOUD16,BG_OBJ_CLOUD17,BG_OBJ_CLOUD18                                 = 15,16,17        #雲中16~18

BG_OBJ_CLOUD19,BG_OBJ_CLOUD20,BG_OBJ_CLOUD21                                 = 18,19,20        #雲大19~21

BG_OBJ_CLOUD22                                                               = 21              #雲特大22

#爆発パターンの種類
EXPLOSION_NORMAL =   0  #標準サイズ(8x8サイズ)の敵を倒したときの爆発パターン
EXPLOSION_MIDDLE =   1  #スクランブルハッチや重爆撃機系の敵を倒したときの中くらいの爆発パターン 
EXPLOSION_MY_SHIP = 10  #自機の爆発パターン

#メッセージウィンドウ関連の定数定義 window_statusに代入されます
WINDOW_OPEN = 0                  #テキストウィンドウ開き進行中
WINDOW_WRITE_TITLE_BAR = 4       #テキストウィンドウのタイトルバー表示中
WINDOW_WRITE_MESSAGE = 5         #テキストメッセージの表示中
WINDOW_SELECT_YES_NO = 8         #「はい」「いいえ」の2択表示中
WINDOW_OPEN_COMPLETED = 9        #テキストウィンドウ開き完了！
WINDOW_CLOSE = 10                #テキストウィンドウ閉め進行中
WINDOW_CLOSE_COMPLETED = 11      #テキストウィンドウ閉め完了！ 

#メッセージの表示の仕方
DISP_OFF = 0                      #0=表示しない
DISP_ON = 1                       #1=表示する 
DISP_CENTER = 2                   #2=中央表示
DISP_LEFT_ALIGN = 3               #3=左揃え
DISP_RIGHT_ALIGN = 4              #4=右揃え

#火花エフェクトの表示の仕方(大気圏突入シーンなどのエフェクトで使用)
SPARK_OFF = 0                     #火花表示なし
SPARK_ON  = 1                     #火花表示あり

#パワーアップアイテム類のtype定数の定義 obtain_itemクラスのitem_typeに代入されます
ITEM_SHOT_POWER_UP     = 1        #ショットアイテム
ITEM_MISSILE_POWER_UP  = 2        #ミサイルアイテム
ITEM_SHIELD_POWER_UP   = 3        #シールドアイテム

ITEM_CLAW_POWER_UP     = 4        #クローアイテム
ITEM_TRIANGLE_POWER_UP = 5        #トライアングルアイテム（ショット、ミサイル、シールド）

ITEM_TAIL_SHOT_POWER_UP        = 10      #テイルショットアイテム
ITEM_PENETRATE_ROCKET_POWER_UP = 11      #ペネトレートロケットアイテム
ITEM_SEARCH_LASER_POWER_UP     = 12      #サーチレーザーアイテム
ITEM_HOMING_MISSILE_POWER_UP   = 13      #ホーミングミサイルアイテム
ITEM_SHOCK_BUMPER_POWER_UP     = 14      #ショックバンパーアイテム 

#!ステージのイベントリストで使う定数の定義
EVENT_ENEMY              = 0  #敵出現
EVENT_ADD_APPEAR_ENEMY   = 1  #敵出現（早回しによる敵の追加出現）
EVENT_FAST_FORWARD_NUM   = 2  #早回しに関する編隊群のパラメーターを設定するイベント

EVENT_SCROLL                      = 60 #スクロール制御
EVENT_DISPLAY_STAR                = 61 #星のスクロールのon/off
EVENT_CHANGE_BG_CLS_COLOR         = 62 #背景でまず最初に塗りつぶす色を指定する(初期状態は黒で塗り潰してます) CLSカラーの指定
EVENT_CHANGE_BG_TRANSPARENT_COLOR = 63 #背景マップを敷き詰める時の透明色を指定する(初期状態は黒)            TRANSPARENTカラーの指定
EVENT_CLOUD                       = 64 #背景雲の表示設定
EVENT_RASTER_SCROLL               = 65 #ラスタースクロールの制御
EVENT_BG_SCREEN_ON_OFF            = 66 #各BGスクリーンの表示のオンオフ
EVENT_ENTRY_SPARK_ON_OFF          = 67 #大気圏突入の火花エフェクト表示のオンオフ

EVENT_DISPLAY_CAUTION    = 70 #CAUTION.注意表示
EVENT_COMMANDER_MESSSAGE = 71 #司令からの通信メッセージ

EVENT_MIDDLE_BOSS        = 80 #中ボス出現
EVENT_WARNING            = 90 #WARNING.警告表示
EVENT_BOSS               = 100#ボスキャラ出現

#イベントリスト・スクロール制御関連の定数定義
SCROLL_NUM_SET               = 0  #スクロール関連のパラメーター設定
SCROLL_START                 = 1  #スクロール開始
SCROLL_STOP                  = 2  #スクロールストップ
SCROLL_SPEED_CHANGE          = 3  #スクロールスピードチェンジ
SCROLL_SPEED_CHANGE_VERTICAL = 4  #縦スクロールスピードチェンジ

SCROLL_SPEED                 = 5  #スクロールスピード直接指定
SCROLL_REVERSE               = 6  #逆スクロール開始
SCROLL_UP                    = 7  #上方向にスクロール開始
SCROLL_DOWN                  = 8  #下方向にスクロール開始

#イベントリスト・雲のスクロール制御関連の定数定義
CLOUD_NUM_SET                = 0  #雲のパラメータ設定
CLOUD_START                  = 1  #雲を流すのを開始する
CLOUD_STOP                   = 2  #雲を流すのを停止する

#イベントリスト BGスクロールオンオフの制御関連の定数定義
BG_BACK   = 0 #BGスクリーン奥
BG_MIDDLE = 1 #BGスクリーン真ん中
BG_FRONT  = 2 #BGスクリーン手前

#背景スクロールの種類
SCROLL_TYPE_TRIPLE_SCROLL_AND_STAR     = 0 #横3重スクロール+星スクロール
SCROLL_TYPE_8FREEWAY_SCROLL_AND_RASTER = 1 #8方向自由スクロール+ラスタースクロール

#背景の星のスクロールの有無
STAR_SCROLL_ON        = 1 #星スクロールあり
STAR_SCROLL_OFF       = 0 #           なし

#背景ラスタスクロールの有無
RASTER_SCROLL_ON      = 1 #ラスタースクロールあり
RASTER_SCROLL_OFF     = 0 #                なし

#背景ラスタスクロールの種類
RASTER_NORMAL         = 0 #奥と手前のラインごとのスクロールスピードの差で奥行き感を出すタイプ (流れるスピードはスクロールスピードに依存します)
RASTER_WAVE           = 1 #x軸にたいして波打つラスタースクロールタイプ(x座標オフセット値を加減算して波打つ感じを表現します)

#!敵キャラの名前(タイプナンバー)定数定義####################################
CIR_COIN           =  1  #無人編隊戦闘機 サーコイン（サークルコイン）
SAISEE_RO          =  2  #回転戦闘機サイシーロ(サインカーブを描く敵)
HOUDA_UNDER        =  3  #固定砲台ホウダ 下
HOUDA_UPPER        =  4  #固定砲台ホウダ 上
HOPPER_CHAN2       =  5  #はねるホッパーチャンmk2
MIST_M54           =  6  #謎の回転飛翔体M54
TWIN_ARROW_SIN     =  7  #真！(SIN)ツインアロー
TWIN_ARROW         =  8  #自機を追尾してくるツインアロー
ROLBOARD           =  9  #ロルボードＹ軸を合わせた後突っ込んで来る怖い
KURANBURU_UNDER    = 10  #クランブルアンダー(スクランブルハッチ)
KURANBURU_UPPER    = 11  #クランブルアッパー(スクランブルハッチ)
RAY_BLASTER        = 12  #レイブラスター 直進して画面前方のどこかで停止→レーザービーム射出→急いで後退するレーザー系
GREEN_LANCER       = 13  #3way弾を出してくるグリーンランサー・翠の硬い奴(ミサイルパワーアップアイテムを持っている！)
TEMI               = 14  #テミー(アイテムキャリアー)
MUU_ROBO           = 15  #ムーロボ 地面を左右に動きながらチョット進んできて弾を撃つ移動砲台
CLAMPARION         = 16  #2機一体で挟みこみ攻撃をしてくるクランパリオン
ROLL_BLITZ         = 17  #ロールブリッツ 画面内のあらかじめ決められた場所へスプライン曲線で移動,そこについたら狙い撃ち弾を出して画面外へ高速離脱
VOLDAR             = 18  #ボルダー 硬めの弾バラマキ重爆撃機
ROLL_BLITZ_POINTER = 19  #ロールブリッツポインター(最大5定点を滑らかに通過していくロールブリッツ)

#敵キャラの大きさの定数定義(この定数を見て敵を破壊した後に育成する爆発パターンの種類を決定しています)
E_SIZE_NORMAL         = 4  #敵サイズノーマル（8ドット）四方の当たり判定
E_SIZE_MIDDLE22       = 6  #敵サイズ2x2チップタイプ  中型16ドットx16ドットの当たり判定
E_SIZE_MIDDLE32       = 8  #敵サイズ3x2チップタイプ  中型24ドットx16ドットの当たり判定
E_SIZE_MIDDLE32_Y_REV = 9  #敵サイズ3x2チップタイプ  中型24ドットx16ドットの当たり判定(上下反転版)(天井に固定されてるハッチとかです)
E_SIZE_HI_MIDDLE53    =10  #敵サイズ5x3チップタイプ  準中型40ドットx24ドットの当たり判定（重爆撃機とか)
#敵キャラのIDナンバー定数定義
ID00,ID01,ID02,ID03,ID04,ID05,ID06,ID07,ID08,ID09,ID10 = 0,1,2,3,4,5,6,7,8,9,10
#敵キャラのステータス(状態)
ENEMY_STATUS_NORMAL    = 0 #通常 score_normal
ENEMY_STATUS_ATTACK    = 1 #攻撃 score_attack
ENEMY_STATUS_ESCAPE    = 2 #撤退 score_escape
ENEMY_STATUS_AWAITING  = 3 #待機 score_awaiting
ENEMY_STATUS_DEFENSE   = 4 #防御 score_defense
ENEMY_STATUS_BERSERK   = 5 #怒り score_berserk

ENEMY_STATUS_MOVE_COORDINATE_INIT    = 10 #移動用座標初期化
ENEMY_STATUS_MOVE_BEZIER_CURVE       = 11 #ベジェ曲線で移動

#敵の攻撃方法(enemyクラスのattack_methodに入る)の定数定義
ENEMY_ATTCK_ANY                 = 0     #任意攻撃(移動ルートで攻撃方法が変わるのではなく体力や自機の位置などによって攻撃方法が変化します)
ENEMY_ATTACK_NO_FIRE            = 1     #なにも攻撃しないよ
ENEMY_ATTACK_AIM_BULLET         = 2     #狙い撃ち弾
ENEMY_ATTACK_FRONT_5WAY         = 3     #前方に5way弾を撃ってきます
ENEMY_ATTACK_FRONT_GREEN_LASER  = 4     #前方に細いグリーンレーザーを撃ってきます
#ヒットポイント(耐久力)の定数定義
HP00,HP01,HP02,HP03,HP04,HP05,HP06,HP07,HP08,HP09 =  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
HP10,HP11,HP12,HP13,HP14,HP15,HP16,HP17,HP18,HP19 = 10,11,12,13,14,15,16,17,18,19
HP20,HP21,HP22,HP23,HP24,HP25,HP26,HP27,HP28,HP29 = 20,21,22,23,24,25,26,27,28,29
HP30,HP31,HP32,HP33,HP34,HP35,HP36,HP37,HP38,HP39 = 30,31,32,33,34,35,36,37,38,39
HP40,HP41,HP42,HP43,HP44,HP45,HP46,HP47,HP48,HP49 = 40,41,42,43,44,45,46,47,48,49
HP50,HP51,HP52,HP53,HP54,HP55,HP56,HP57,HP58,HP59 = 50,51,52,53,54,55,56,57,58,59
#得点の定数定義
PT01,PT02,PT03,PT04,PT05,PT06,PT07,PT08,PT09,PT10 =  1, 2, 3, 4, 5, 6, 7, 8, 9,10
PT11,PT12,PT13,PT14,PT15,PT16,PT17,PT18,PT19,PT20 = 11,12,13,14,15,16,17,18,19,20
PT21,PT22,PT23,PT24,PT25,PT26,PT27,PT28,PT29,PT30 = 21,22,23,24,25,26,27,28,29,30
PT31,PT32,PT33,PT34,PT35,PT36,PT37,PT38,PT39,PT40 = 31,32,33,34,35,36,37,38,39,40
PT41,PT42,PT43,PT44,PT45,PT46,PT47,PT48,PT49,PT50 = 41,42,43,44,45,46,47,48,49,50

PT1000 = 1000
#レベルの定数定義
LV00,LV01,LV02,LV03,LV04,LV05,LV06,LV07,LV08,LV09,LV10 = 0,1,2,3,4,5,6,7,8,9,10
#サイズ(大きさ)の定数定義 おもに画像表示用、当たり判定用としてwidthやheightに入ります
SIZE_1, SIZE_2, SIZE_3, SIZE_4, SIZE_5  =  1, 2, 3, 4, 5
SIZE_6, SIZE_7, SIZE_8, SIZE_9, SIZE_10 =  6, 7, 8, 9,10

SIZE_11,SIZE_12,SIZE_13,SIZE_14,SIZE_15 = 11,12,13,14,15
SIZE_16,SIZE_17,SIZE_18,SIZE_19,SIZE_20 = 16,17,18,19,20

SIZE_21,SIZE_22,SIZE_23,SIZE_24,SIZE_25 = 21,22,23,24,25
SIZE_26,SIZE_27,SIZE_28,SIZE_29,SIZE_30 = 26,27,28,29,30

SIZE_31,SIZE_32,SIZE_33,SIZE_34,SIZE_35 = 31,32,33,34,35
SIZE_36,SIZE_37,SIZE_38,SIZE_39,SIZE_40 = 36,37,38,39,40

SIZE_41,SIZE_42,SIZE_43,SIZE_44,SIZE_45 = 41,42,43,44,45
SIZE_46,SIZE_47,SIZE_48,SIZE_49,SIZE_50 = 46,47,48,49,50
#空中物か地上物かの判定用定数定義 enemyクラスのfloating_flagに入ります
AERIAL_OBJ = 0 #空中物(飛行物体)
GROUND_OBJ = 1 #地上物
MOVING_OBJ = 2 #地上を移動する物体(装甲車とか)

#!敵弾のタイプ定数定義
ENEMY_SHOT_NORMAL            =  0 #通常弾
ENEMY_SHOT_SIN               =  1 #サインカーブ弾
ENEMY_SHOT_COS               =  2 #コサインカーブ弾
ENEMY_SHOT_LASER             =  3 #レーザービーム
ENEMY_SHOT_GREEN_LASER       =  4 #ボスのグリーンレーザー
ENEMY_SHOT_RED_LASER         =  5 #ボスのレッドレーザー
ENEMY_SHOT_YELLOW_LASER      =  6 #ボスのイエローレーザー
ENEMY_SHOT_BLUE_LASER        =  7 #ボスのブルーレーザー
ENEMY_SHOT_RAINBOW_LASER     =  8 #ボスのレインボーレーザー
ENEMY_SHOT_HOMING_LASER      =  9 #ホーミングレーザー(レイフォースみたいなの)
ENEMY_SHOT_HOMING_LASER_TAIL = 10 #ホーミングレーザーの尻尾
ENEMY_SHOT_LOCKON_LASER      = 11 #ロックオンレーザー(レイフォースみたいなの)
ENEMY_SHOT_LOCKON_LASER_TAIL = 12 #ロックオンレーザーの尻尾
ENEMY_SHOT_SEARCH_LASER      = 13 #サーチレーザー(イメージファイトみたいなの)
ENEMY_SHOT_SEARCH_LASER_TAIL = 14 #サーチレーザーの尻尾
ENEMY_SHOT_WAVE              = 15 #ウェーブカッター(ダライアスみたいなの)
ENEMY_SHOT_RIPPLW_LASER      = 16 #リップルレーザー(グラディウスⅡみたいなの)
ENEMY_SHOT_WAINDER_LASER     = 17 #ワインダーレーザー(グラディウスみたいなの)
ENEMY_SHOT_CIRCLE_LASER      = 18 #サークルレーザー(イメージファイトみたいなの)
ENEMY_SHOT_2TURN_LASER       = 19 #2回屈折サーチレーザー(ダライアスバーストみたいなの)
ENEMY_SHOT_BOUND_LASER       = 20 #反射レーザー(R-TYPEみたいなの)
ENEMY_SHOT_DROP_BULLET       = 21 #落下弾
ENEMY_SHOT_CIRCLE_BULLET     = 22 #回転弾
ENEMY_SHOT_SPLIT_BULLET      = 21 #分裂弾
ENEMY_SHOT_HOMING_BULLET     = 23 #誘導弾
ENEMY_SHOT_UP_LASER          = 24 #アップレーザー
ENEMY_SHOT_DOWN_LASER        = 25 #ダウンレーザー
ENEMY_SHOT_SPREAD_BOMB       = 26 #スプレッドボム
ENEMY_SHOT_VECTOR_LASER      = 27 #ベクトルレーザー(グラ２みたいなの)
ENEMY_SHOT_GREEN_CUTTER      = 28 #「ブリザーディア」が尾翼部から射出するグリーンカッター

#!分裂弾の種類の定数定義
ENEMY_SHOT_DIVISION_3WAY     = 1 #3way分裂弾
ENEMY_SHOT_DIVISION_5WAY     = 2 #5way分裂弾
ENEMY_SHOT_DIVISION_7WAY     = 3 #7way分裂弾
ENEMY_SHOT_DIVISION_9WAY     = 4 #9way分裂弾

#育成する打ち返し弾の種類 Explosionクラスのreturn_bullet_typeに入る,難易度リスト(game_difficulty_list)でも使用してます
RETURN_BULLET_NONE      = 0 #撃ち返ししない
RETURN_BULLET_AIM       = 1 #自機狙い弾を1発撃ち返す
RETURN_BULLET_DELAY_AIM = 2 #自機狙い撃ち返し＆遅れて更に自機狙い弾を撃ち返す 2発
RETURN_BULLET_3WAY      = 3 #自機狙いの3way弾を撃ち返してくる


#敵弾クラスで使用する定数定義 主にcollision_typeやwidth,heightに入る
ESHOT_COL_MIN88 = 0 #最小の正方形8x8ドットでの当たり判定タイプ     collision_typeに入る
ESHOT_COL_BOX   = 1 #長方形での当たり判定タイプ                   collision_typeに入る 判定はwidth,heightを見て行います

ESHOT_SIZE1  =  1 #敵ショットのサイズ  1ドット width,heightに入ります
ESHOT_SIZE2  =  2 #敵ショットのサイズ  2ドット
ESHOT_SIZE3  =  3 #敵ショットのサイズ  3ドット
ESHOT_SIZE4  =  4 #敵ショットのサイズ  4ドット
ESHOT_SIZE5  =  5 #敵ショットのサイズ  5ドット
ESHOT_SIZE6  =  6 #敵ショットのサイズ  6ドット
ESHOT_SIZE7  =  7 #敵ショットのサイズ  7ドット
ESHOT_SIZE8  =  8 #敵ショットのサイズ  8ドット
ESHOT_SIZE9  =  9 #敵ショットのサイズ  9ドット
ESHOT_SIZE10 = 10 #敵ショットのサイズ 10ドット
ESHOT_SIZE11 = 11 #敵ショットのサイズ 11ドット
ESHOT_SIZE12 = 12 #敵ショットのサイズ 12ドット
ESHOT_SIZE13 = 13 #敵ショットのサイズ 13ドット
ESHOT_SIZE14 = 14 #敵ショットのサイズ 14ドット
ESHOT_SIZE15 = 15 #敵ショットのサイズ 15ドット
ESHOT_SIZE16 = 16 #敵ショットのサイズ 16ドット 

#敵や爆発関連の表示用のプライオリティレベルの定数定義
PRIORITY_SEND_TO_BACK         = 0  #最背面(スクロールしない背景が多いです)
PRIORITY_BACK                 = 1  #背面
PRIORITY_MIDDLE               = 2  #中面
PRIORITY_BOSS_BACK            = 3  #ボスキャラの真後ろ
PRIORITY_BOSS                 = 4  #ボスキャラと同面
PRIORITY_BOSS_FRONT           = 5  #ボスキャラの直ぐ手前
PRIORITY_FRONT_SCROLL         = 6  #前面スクロールのすぐ手前
PRIORITY_FRONT                = 7  #前面
PRIORITY_MORE_FRONT           = 8  #さらに前面
PRIORITY_TOP                  = 9  #最前面(すべてにおいて最後の描画されるため最前面となる！)

#ボスキャラのboss_type定数定義
BOSS_BREEZARDIA              = 0 #MOUNTAIN_REGIONのボス「ブリザーディア」
BOSS_FATTY_VALGUARD          = 1 #ADVANCED_BASEのボス  「ファッティバルガード」


#敵キャラが持っているアイテム類のID enemyクラスのitemに代入されます
E_NO_POW      = 0                #敵は何もパワーアップアイテムを持っていないです・・・涙
E_SHOT_POW    = 1                #敵が持っているショットアイテム定数定義
E_MISSILE_POW = 2                #敵が持っているミサイルアイテム定数定義
E_SHIELD_POW  = 3                #敵が持っているシールドアイテム定数定義

E_CLAW_POW        = 4            #敵が持っているクローアイテム定数定義

E_TRIANGLE_POW    = 5            #敵が持っている正三角形アイテム（ショット、ミサイル、シールド）アイテム定数定義

E_DESTRUCTION_POW = 6            #敵が持っている破壊アイテム定数定義（ザコ敵を殲滅させるアイテム）
E_SCORE_POW       = 7            #敵が持っている得点アップアイテムの定数定義
E_INVINCIBLE_POW  = 8            #敵が持っている無敵アイテムの定数定義

E_TAIL_SHOT_POW        = 10       #敵が持っているテイルショットアイテム定数定義
E_PENETRATE_ROCKET_POW = 11       #敵が持っているペネトレートロケットアイテム定数定義
E_SEARCH_LASER_POW     = 12       #敵が持っているサーチレーザーアイテム定数定義
E_HOMING_MISSILE_POW   = 13       #敵が持っているホーミングミサイルアイテム定数定義
E_SHOCK_BUMPER_POW     = 14       #敵が持っているショックバンパーアイテム定数定義 

#!bossクラスのstatusに入る定数定義   (状態遷移フラグとして使用します)
BOSS_STATUS_MOVE_COORDINATE_INIT    = 0   #ボス用のステータス定数定義 移動用座標初期化
BOSS_STATUS_MOVE_BEZIER_CURVE       = 10  #ボス用のステータス定数定義 ベジェ曲線で移動
BOSS_STATUS_MOVE_LEMNISCATE_CURVE   = 11  #ボス用のステータス定数定義 レムニスケート曲線で移動

BOSS_STATUS_EXPLOSION_START         = 80  #ボス撃破！爆発開始！
BOSS_STATUS_EXPLOSION               = 81  #ボス爆発中！
BOSS_STATUS_BLAST_SPLIT_START       = 82  #ボス爆破分裂開始
BOSS_STATUS_BLAST_SPLIT             = 83  #ボス爆破分裂中
BOSS_STATUS_DISAPPEARANCE           = 89  #ボス消滅・・・・・

#bossクラスのattack_methodに入る定数定義 (ボスの攻撃方法)
BOSS_ATTACK_NO_FIRE = 0               #なにも攻撃しないよ
BOSS_ATTACK_FRONT_5WAY = 1            #前方に5way弾を撃ってきます
BOSS_ATTACK_RIGHT_GREEN_LASER = 2     #後方に細いグリーンレーザーを撃ってきます
BOSS_ATTACK_FRONT_5WAY_AIM_BULLET = 3 #前方5way+狙い撃ち弾
BOSS_ATTACK_FRONT_5WAY_HOMING = 4     #前方5way+ホーミング弾

BOSS_HP_BAR_DISPLAY_TIME = 32         #ボスの耐久力バーを表示する時間(弾が当たるたびにこの数値がカウンターに入る)

#bossクラスのweapon_statusに入る定数定義(ボスの持つ武器の状態)
WEAPON_READY               = 0    #何もしていない準備万端な状態
WEAPON_ROCK_ON             = 1    #目標を定めた状態（予兆エフェクトを表示)
WEAPON_FIRE                = 2    #武器発射中

#!オブジェクトのクラス宣言エリア####################################################################################################
#そもそもクラスって何なのか今でも判らない・・・設計図（？）みたいなものらしいが・・・
#配列リストはこのように使いますよ～～～って言うのを記述した設計図？ってことなん？？？？？

class Shot:#自機弾のクラス設定
     def __init__(self):
          self.shot_type = 0
          self.posx = 0
          self.posy = 0
          self.vx = 0
          self.vy = 0
          self.width = 0
          self.height = 0
          self.offset_y = 0
          self.shot_power = 0
          self.shot_hp = 0
     def update(self,shot_type, x , y, vx, vy, width, height, offset_y, shot_power, shot_hp):
          self.shot_type = shot_type
          self.posx = x
          self.posy = y
          self.vx = vx
          self.vy = vy
          self.width = width
          self.height = height
          self.offset_y = offset_y
          self.shot_power = shot_power
          self.shot_hp = shot_hp
class Missile:#自機ミサイルのクラス設定
     def __init__(self):
          self.missile_type = 0 #0=右下ミサイル 1=右上ミサイル 2=左下ミサイル 3=左上ミサイル 4=テイルショット 5=ぺネトレートロケット 6=サーチレーザー 7=ホーミングミサイル
          self.posx = 0
          self.posy = 0
          self.vx = 0
          self.vy = 0
          self.missile_power = 0
          self.missile_hp = 0
          self.missile_flag1 = 0
          self.missile_flag2 = 0
          self.x_reverse = 0
          self.y_reverse = 0
          self.width = 0
          self.height = 0
          self.tx = 0
          self.ty = 0
          self.theta = 0
          self.speed = 0
     def update(self,missile_type, x , y, vx, vy, missile_power, missile_hp,missile_flag1,missile_flag2,x_reverse,y_reverse,width,height,tx,ty,theta,speed):
          self.missile_type = missile_type
          self.posx = x
          self.posy = y
          self.vx = vx
          self.vy = vy
          self.missile_power = missile_power
          self.missile_hp = missile_hp
          self.missile_flag1 = missile_flag1
          self.missile_flag2 = missile_flag2
          self.x_reverse = x_reverse
          self.y_reverse = y_reverse
          self.width = width
          self.height = height
          self.tx = tx
          self.ty = ty
          self.theta = theta
          self.speed = speed
class Claw:#クローのクラス設定
     def __init__(self):
         self.number = 0 #クローのIDナンバー 0~3まで
         self.claw_type = 0 #0=ローリングタイプ 1=トレースタイプ 2=フックスタイプ 3=リバースタイプ
         self.status = 0 #0=回転開始や固定開始の初期位置まで動いていく #1==回転中もしくは固定完了
         self.posx = 0#インスタンス育成時は自機のX座標が入る
         self.posy = 0#インスタンス育成時は自機のY座標が入る
         self.roll_vx = 0
         self.roll_vy = 0
         self.fix_vx = 0
         self.fix_vy = 0

         self.reverse_vx = 0
         self.reverse_vy = 0

         self.offset_x = 0#クローの現時点での座標オフセット値
         self.offset_y = 0
         self.offset_roll_x = 0        #ローリングクローの処理開始の座標（オフセット値）
         self.offset_roll_y = 0
         self.offset_fix_x = 0         #フックスクローの処理開始の間隔倍率を掛けた座標（オフセット値）実際に比較対象になるのはこっちのほう
         self.offset_fix_y = 0
         self.offset_fix_origin_x = 0  #フックスクローの処理開始の間隔倍率を掛ける前の元の座標（オフセット値）
         self.offset_fix_origin_y = 0
         self.offset_reverse_x = 0     #リバースクローの処理開始の座標（オフセット値）
         self.offset_reverse_y = 0
         self.intensity = 0
         self.timer = 0
         self.degree = 0 #回転角度 度数法（主にこちらを使用するのです！）
         self.radian = 0 #回転角度 弧度法
         self.speed = 0 #回転スピード(弧度法0~360度)
         self.radius = 0 #半径
         self.degree_interval = 0 #クローの個数に応じた回転間隔(1個=設定なし 2個=180度 3個=120度 4個=90度)
         self.angle_difference = 0 #ひとつ前のクローとの回転角度の差（この値がdegree_intarvalと同じ数値になるまで回転スピードを増減させていく）
         self.shot_type = 0
         self.shot_power = 0
         self.animation_number = 0
     def update(self,number,claw_type,status,x,y,roll_vx,roll_vy,fix_vx,fix_vy,reverse_vx,reverse_vy,offset_x,offset_y,offset_roll_x,offset_roll_y,offset_fix_x,offset_fix_y,offset_fix_origin_x,offset_fix_origin_y,offset_reverse_x,offset_reverse_y,intensity,timer,degree,radian,speed,radius,degree_interval,angle_difference,shot_type,shot_power,animation_number):
         self.number = number
         self.claw_type = claw_type
         self.status = status
         self.posx = x
         self.posy = y
         self.roll_vx = roll_vx
         self.roll_vy = roll_vy
         self.fix_vx = fix_vx
         self.fix_vy = fix_vy
         self.reverse_vx = reverse_vx
         self.reverse_vy = reverse_vy
         self.offset_x = offset_x
         self.offset_y = offset_y
         self.offset_roll_x = offset_roll_x
         self.offset_roll_y = offset_roll_y
         self.offset_fix_x = offset_fix_x
         self.offset_fix_y = offset_fix_y
         self.offset_fix_origin_x = offset_fix_origin_x
         self.offset_fix_origin_y = offset_fix_origin_y
         self.offset_reverse_x = offset_reverse_x
         self.offset_reverse_y = offset_reverse_y
         self.intensity = intensity
         self.timer = timer
         self.degree = degree
         self.radian = radian
         self.speed = speed
         self.radius = radius
         self.degree_interval = degree_interval
         self.angle_difference = angle_difference
         self.shot_type = shot_type
         self.shot_power = shot_power
         self.animation_number = animation_number
class Trace_coordinates:#トレースクロー（オプション）座標のクラス設定
     def __init__(self):
         self.posx = 0 #自機のx座標をオプションのx座標としてコピーして使用する
         self.posy = 0 #自機のy座標をオプションのy座標としてコピーして使用する
     def update(self, ox, oy):
         self.posx = ox
         self.posy = oy
class Claw_shot:#クローショット（クローの弾）のクラス設定
     def __init__(self):
          self.shot_type = 0
          self.posx = 0
          self.posy = 0
          self.vx = 0
          self.vy = 0
          self.width = 0
          self.height = 0
          self.offset_x = 0
          self.offset_y = 0
          self.shot_power = 0
          self.shot_hp = 0
     def update(self,shot_type, x , y, vx, vy, width, height, offset_x, offset_y, shot_power, shot_hp):
          self.shot_type = shot_type
          self.posx = x
          self.posy = y
          self.vx = vx
          self.vy = vy
          self.width = width
          self.height = height
          self.offseet_x = offset_x
          self.offset_y = offset_y
          self.shot_power = shot_power
          self.shot_hp = shot_hp
class Star:#背景の流れる星のクラス設定
     def __init__(self):
          self.posx = 0
          self.posy = 0
          self.speed = 0
     def update(self,x , y, speed):
          self.posx = x
          self.posy = y
          self.speed = speed
class Enemy:#敵キャラ達のクラス設定
     def __init__(self):
          self.enemy_type = 0    #敵のタイプ
          self.enemy_id = 0      #敵のIDナンバー
          self.status = 0        #敵の状態
          self.attack_method = 0 #敵の攻撃方法
          self.posx = 0 #敵の位置座標(x,y)
          self.posy = 0
          self.offset_x = 0 #座標オフセット値
          self.offset_y = 0
          self.offset_p1x = 0 #パーツ1のオフセット座標値(p1x,p1y)
          self.offset_p1y = 0
          self.offset_p2x = 0 #パーツ2のオフセット座標値(p2x,p2y)
          self.offset_p2y = 0
          self.offset_p3x = 0 #パーツ3のオフセット座標値(p3x,p3y)
          self.offset_p3y = 0
          self.offset_p4x = 0 #パーツ4のオフセット座標値(p4x,p4y)
          self.offset_p4y = 0

          self.ax = 0 #移動元の座標
          self.ay = 0
          self.bx = 0 #予約座標1
          self.by = 0
          self.cx = 0 #予約座標2
          self.cy = 0 
          self.dx = 0 #移動先の座標(destination_x,y)
          self.dy = 0
          self.qx = 0 #2次ベジェ曲線の制御点qとして使用
          self.qy = 0
          self.vx = 0 #敵の速度ベクトル(vx,vy)
          self.vy = 0
          

          self.o1x = 0 #移動元の座標1(origin1_x,y)(リストを使わずにインスタンス育成時に座標を指定してベジェ曲線移動するときに使うメンバ変数)とりあえず5点まで移動できるように変数を確保してます
          self.o1y = 0 
          self.d1x = 0 #移動先の座標1(destination1_x,y)
          self.d1y = 0
          self.q1x = 0 #2次ベジェ曲線の制御点q1として使用
          self.q1y = 0
          self.a1  = 0 #加速度(acceleration1)

          self.o2x = 0 #移動元の座標2(origin2_x,y)
          self.o2y = 0 
          self.d2x = 0 #移動先の座標2(destination2_x,y)
          self.d2y = 0
          self.q2x = 0 #2次ベジェ曲線の制御点q2として使用
          self.q2y = 0
          self.a2  = 0 #加速度(acceleration2)
          
          self.o3x = 0 #移動元の座標3(origin3_x,y)
          self.o3y = 0 
          self.d3x = 0 #移動先の座標3(destination3_x,y)
          self.d3y = 0
          self.q3x = 0 #2次ベジェ曲線の制御点q3として使用
          self.q3y = 0
          self.a3  = 0 #加速度(acceleration3)
          
          self.o4x = 0 #移動元の座標4(origin4_x,y)
          self.o4y = 0 
          self.d4x = 0 #移動先の座標4(destination4_x,y)
          self.d4y = 0
          self.q4x = 0 #2次ベジェ曲線の制御点q4として使用
          self.q4y = 0
          self.a4  = 0 #加速度(acceleration4)
          
          self.o5x = 0 #移動元の座標5(origin5_x,y)
          self.o5y = 0 
          self.d5x = 0 #移動先の座標5(destination5_x,y)
          self.d5y = 0
          self.q5x = 0 #2次ベジェ曲線の制御点q5として使用
          self.q5y = 0
          self.a5  = 0 #加速度(acceleration5)       

          self.width = 0  #敵の横幅
          self.height = 0 #敵の縦幅
          self.move_speed        = 0 #敵の全体的な移動スピード
          self.move_speed_offset = 0 #敵の全体的な移動スピード(オフセット値)move_speedとかけ合わせたり加減算したりしてスピードを変化とか出来そう
          self.direction = 0    #敵の移動方向
          self.enemy_hp = 0     #敵の耐久力
          self.enemy_flag1 = 0  #フラグ用その1
          self.enemy_flag2 = 0  #フラグ用その２
          self.enemy_size = 0   #敵の全体的な大きさ
          self.enemy_count1 = 0 #汎用カウンタその1
          self.enemy_count2 = 0 #汎用カウンタその2
          self.enemy_count3 = 0 #汎用カウンタその3
          self.parts1_flag = 0 #各部位用のフラグ
          self.parts2_flag = 0
          self.parts3_flag = 0
          self.parts4_flag = 0
          self.item = 0           #0=パワーアップアイテム未所持 1=ショットアイテム 2=ミサイルアイテム 3=シールドアイテム
                                  #これ以外の項目については敵キャラが持っているアイテム類のＩＤを参照してね
          self.formation_id = 0   #単独機の場合は0 1番最初に出現した編隊群は1 2番目に出現した編隊群2 3番目の編隊は3 みたいな感じで数値が代入される
          self.timer        = 0   #時間(三角関数系で使用)
          self.speed        = 0   #速度(三角関数系で使用)
          self.intensity    = 0   #振れ幅(三角関数系で使用)
          self.acceleration  = 0  #加速度
          self.move_index    = 0  #2次ベジェ曲線での移動用リストを参照するときに使用するインデックス値（リストの添え字に入る数値）
          self.obj_time      = 0  #2次ベジェ曲線での移動用のtime（現在のタイムフレーム番号が入る）(0~totaltimeまで変化する)ピエール・ベジェさんありがとう・・・
          self.obj_totaltime = 0  #2次ベジェ曲線での移動用のtotaltime（移動元から移動先までに掛けるトータルフレーム数が入る60なら1秒掛けて移動元から移動先まで移動するって事,120なら2秒かかる)
          self.color         = 0  #色
          self.floating_flag = 0  #地上物か空中物かどうかのフラグ 0=空中物 1=地上物 2=地上を移動する物体(装甲車とか)
          self.score_normal  = 0  #通常時の得点
          self.score_attack  = 0  #攻撃時の得点
          self.score_escape  = 0  #撤退時の得点
          self.score_awaiting = 0 #待機中の得点
          self.score_defense  = 0 #防御中の得点
          self.score_berserk  = 0 #怒り状態の得点
     def update(self,enemy_type,enemy_id,status,attack_method,
                x, y,
                offset_x,offset_y,
                offset_p1x,offset_p1y,
                offset_p2x,offset_p2y,
                offset_p3x,offset_p3y,
                offset_p4x,offset_p4y,
                ax,ay,bx,by,cx,cy,dx,dy,qx,qy,
                vx, vy,

                o1x,o1y,d1x,d1y,q1x,q1y,a1,
                o2x,o2y,d2x,d2y,q2x,q2y,a2,
                o3x,o3y,d3x,d3y,q3x,q3y,a3,
                o4x,o4y,d4x,d4y,q4x,q4y,a4,
                o5x,o5y,d5x,d5y,q5x,q5y,a5,
                
                width, height,
                move_speed,move_speed_offset,
                direction,
                enemy_hp,
                enemy_flag1, enemy_flag2,
                enemy_size,
                enemy_count1, enemy_count2, enemy_count3,
                parts1_flag,parts2_flag,parts3_flag,parts4_flag,

                item,formation_id,
                timer,speed,intensity,
                acceleration,
                move_index,obj_time,obj_totaltime,
                color,floating_flag,
                score_normal,score_attack,score_escape,score_awaiting,score_defense,score_berserk):
          self.enemy_type = enemy_type
          self.enemy_id = enemy_id
          self.status = status
          self.attack_method = attack_method
          self.posx = x
          self.posy = y
          self.offset_x = offset_x
          self.offset_y = offset_y
          self.offset_p1x = offset_p1x
          self.offset_p1y = offset_p1y
          self.offset_p2x = offset_p2x
          self.offset_p2y = offset_p2y
          self.offset_p3x = offset_p3x
          self.offset_p3y = offset_p3y
          self.offset_p4x = offset_p4x
          self.offset_p4y = offset_p4y
          self.ax = ax
          self.ay = ay
          self.bx = bx
          self.by = by
          self.cx = cx
          self.cy = cy          
          self.dx = dx
          self.dy = dy
          self.qx = qx
          self.qy = qy
          self.vx = vx
          self.vy = vy

          self.o1x = o1x
          self.o1y = o1y 
          self.d1x = d1x
          self.d1y = d1y
          self.q1x = q1x
          self.q1y = q1y
          self.a1  = a1
          
          self.o2x = o2x
          self.o2y = o2y 
          self.d2x = d2x
          self.d2y = d2y
          self.q2x = q2x
          self.q2y = q2y
          self.a2  = a2
          
          self.o3x = o3x
          self.o3y = o3y 
          self.d3x = d3x
          self.d3y = d3y
          self.q3x = q3x
          self.q3y = q3y
          self.a3  = a3

          self.o4x = o4x
          self.o4y = o4y 
          self.d4x = d4x
          self.d4y = d4y
          self.q4x = q4x
          self.q4y = q4y
          self.a4  = a4
          
          self.o5x = o5x
          self.o5y = o5y 
          self.d5x = d5x
          self.d5y = d5y
          self.q5x = q5x
          self.q5y = q5y
          self.a5  = a5
          
          self.width = width
          self.height = height
          self.move_speed = move_speed
          self.move_speed_offset = move_speed_offset
          self.direction = direction
          self.enemy_hp = enemy_hp
          self.enemy_flag1 = enemy_flag1
          self.enemy_flag2 = enemy_flag2
          self.enemy_size = enemy_size
          self.enemy_count1 = enemy_count1
          self.enemy_count2 = enemy_count2
          self.enemy_count3 = enemy_count3
          self.parts1_flag = parts1_flag
          self.parts2_flag = parts2_flag
          self.parts3_flag = parts3_flag
          self.parts4_flag = parts4_flag
          self.item = item
          self.formation_id = formation_id
          self.timer = timer
          self.speed = speed
          self.intensity = intensity
          self.acceleration  = acceleration
          self.move_index    = move_index
          self.obj_time      = obj_time
          self.obj_totaltime = obj_totaltime
          self.color = color
          self.floating_flag  = floating_flag
          self.score_normal   = score_normal
          self.score_attack   = score_attack
          self.score_escape   = score_escape
          self.score_awaiting = score_awaiting
          self.score_defense  = score_defense
          self.score_berserk  = score_berserk
class Boss:#ボスキャラのクラス設定
     def __init__(self):
          self.boss_id = 0
          self.boss_type = 0
          self.status = 0
          self.parts_number = 0 #破壊可能部位の数 0なら本体のみ 1なら破壊可能部位が1箇所あり 4なら4箇所あるという事です
          self.main_hp   = 0    #本体の耐久力
          self.parts1_hp = 0    #各部位の耐久力(1~4)
          self.parts2_hp = 0
          self.parts3_hp = 0
          self.parts4_hp = 0
          self.parts5_hp = 0
          self.parts6_hp = 0
          self.parts7_hp = 0
          self.parts8_hp = 0
          self.parts9_hp = 0
          self.parts1_score = 0 #各パーツを破壊した時の得点
          self.parts2_score = 0
          self.parts3_score = 0
          self.parts4_score = 0
          self.parts5_score = 0
          self.parts6_score = 0
          self.parts7_score = 0
          self.parts8_score = 0
          self.parts9_score = 0
          self.level = 0 #レベル
          self.weapon1_status,self.weapon1_interval,self.weapon1_rapid_num,self.weapon1_cool_down_time,self.weapon1_omen_count = 0,0,0,0,0 #武器1の状態,発射間隔,連射数,次に発射できるまでの時間(クールタイム),予兆エフェクトカウンター
          self.weapon2_status,self.weapon2_interval,self.weapon2_rapid_num,self.weapon2_cool_down_time,self.weapon2_omen_count = 0,0,0,0,0 #武器2の状態,発射間隔,連射数,次に発射できるまでの時間(クールタイム),予兆エフェクトカウンター
          self.weapon3_status,self.weapon3_interval,self.weapon3_rapid_num,self.weapon3_cool_down_time,self.weapon3_omen_count = 0,0,0,0,0 #武器3の状態,発射間隔,連射数,次に発射できるまでの時間(クールタイム),予兆エフェクトカウンター
          self.weapon4_status,self.weapon4_interval,self.weapon4_rapid_num,self.weapon4_cool_down_time,self.weapon4_omen_count = 0,0,0,0,0 #武器4の状態,発射間隔,連射数,次に発射できるまでの時間(クールタイム),予兆エフェクトカウンター
          self.weapon5_status,self.weapon5_interval,self.weapon5_rapid_num,self.weapon5_cool_down_time,self.weapon5_omen_count = 0,0,0,0,0 #武器5の状態,発射間隔,連射数,次に発射できるまでの時間(クールタイム),予兆エフェクトカウンター
          self.posy = 0
          self.offset_x = 0 #座標オフセット値
          self.offset_y = 0
          self.ax = 0 #移動元の座標
          self.ay = 0
          self.bx = 0
          self.by = 0
          self.cx = 0
          self.cy = 0 
          self.dx = 0 #移動先の座標(destination_x,y)
          self.dy = 0
          self.qx = 0 #2次ベジェ曲線の制御点qとして使用
          self.qy = 0
          self.vx = 0 #速度
          self.vy = 0
          self.width = 0  #画像の横の大きさ
          self.height = 0 #画像の縦の大きさ
          
          self.col_damage_point1_x,self.col_damage_point1_y = 0,0 #ボスの弱点位置1 始点x,y座標
          self.col_damage_point1_w,self.col_damage_point1_h = 0,0 #     弱点位置1 横の長さ,縦の長さ w=0の場合は当たり判定として使用しない
          
          self.col_damage_point2_x,self.col_damage_point2_y = 0,0 #ボスの弱点位置2 始点x,y座標
          self.col_damage_point2_w,self.col_damage_point2_h = 0,0 #     弱点位置2 横の長さ,縦の長さ w=0の場合は当たり判定として使用しない

          self.col_damage_point3_x,self.col_damage_point3_y = 0,0 #ボスの弱点位置3 始点x,y座標
          self.col_damage_point3_w,self.col_damage_point3_h = 0,0 #     弱点位置3 横の長さ,縦の長さ w=0の場合は当たり判定として使用しない

          self.col_damage_point4_x,self.col_damage_point4_y = 0,0 #ボスの弱点位置3 始点x,y座標
          self.col_damage_point4_w,self.col_damage_point4_h = 0,0 #     弱点位置3 横の長さ,縦の長さ w=0の場合は当たり判定として使用しない
          
          self.col_main1_x = 0 #本体1当たり判定の始点x
          self.col_main1_y = 0 #                始点y            
          self.col_main1_w = 0 #              横の長さ 横の長さが0の場合は当たり判定として使用しない
          self.col_main1_h = 0 #              縦の長さ

          self.col_main2_x = 0 #本体2当たり判定の始点x
          self.col_main2_y = 0 #                始点y            
          self.col_main2_w = 0 #              横の長さ 横の長さが0の場合は当たり判定として使用しない
          self.col_main2_h = 0 #              縦の長さ

          self.col_main3_x = 0 #本体3当たり判定の始点x
          self.col_main3_y = 0 #                始点y            
          self.col_main3_w = 0 #              横の長さ 横の長さが0の場合は当たり判定として使用しない
          self.col_main3_h = 0 #              縦の長さ

          self.col_main4_x = 0 #本体4当たり判定の始点x
          self.col_main4_y = 0 #                始点y            
          self.col_main4_w = 0 #              横の長さ 横の長さが0の場合は当たり判定として使用しない
          self.col_main4_h = 0 #              縦の長さ

          self.col_main5_x = 0 #本体5当たり判定の始点x
          self.col_main5_y = 0 #                始点y            
          self.col_main5_w = 0 #              横の長さ 横の長さが0の場合は当たり判定として使用しない
          self.col_main5_h = 0 #              縦の長さ

          self.col_main6_x = 0 #本体6当たり判定の始点x
          self.col_main6_y = 0 #                始点y            
          self.col_main6_w = 0 #              横の長さ 横の長さが0の場合は当たり判定として使用しない
          self.col_main6_h = 0 #              縦の長さ

          self.col_main7_x = 0 #本体7当たり判定の始点x
          self.col_main7_y = 0 #                始点y            
          self.col_main7_w = 0 #              横の長さ 横の長さが0の場合は当たり判定として使用しない
          self.col_main7_h = 0 #              縦の長さ

          self.col_main8_x = 0 #本体8当たり判定の始点x
          self.col_main8_y = 0 #                始点y            
          self.col_main8_w = 0 #              横の長さ 横の長さが0の場合は当たり判定として使用しない
          self.col_main8_h = 0 #              縦の長さ

          
          self.col_parts1_x = 0 #パーツ1当たり判定の始点x
          self.col_parts1_y = 0 #パーツ1当たり判定の始点y            
          self.col_parts1_w = 0 #パーツ1当たり判定(横の長さ）
          self.col_parts1_h = 0 #パーツ1当たり判定(縦の長さ)
          
          self.col_parts2_x = 0 #パーツ2当たり判定の始点x
          self.col_parts2_y = 0 #パーツ2当たり判定の始点y            
          self.col_parts2_w = 0 #パーツ2当たり判定(横の長さ）
          self.col_parts2_h = 0 #パーツ2当たり判定(縦の長さ)
          
          self.col_parts3_x = 0 #パーツ3当たり判定の始点x
          self.col_parts3_y = 0 #パーツ3当たり判定の始点y            
          self.col_parts3_w = 0 #パーツ3当たり判定(横の長さ）
          self.col_parts3_h = 0 #パーツ3当たり判定(縦の長さ)
          
          self.col_parts4_x = 0 #パーツ4当たり判定の始点x
          self.col_parts4_y = 0 #パーツ4当たり判定の始点y            
          self.col_parts4_w = 0 #パーツ4当たり判定(横の長さ）
          self.col_parts4_h = 0 #パーツ4当たり判定(縦の長さ)

          self.col_parts5_x = 0 #パーツ5当たり判定の始点x
          self.col_parts5_y = 0 #パーツ5当たり判定の始点y            
          self.col_parts5_w = 0 #パーツ5当たり判定(横の長さ）
          self.col_parts5_h = 0 #パーツ5当たり判定(縦の長さ)
          
          self.col_parts6_x = 0 #パーツ6当たり判定の始点x
          self.col_parts6_y = 0 #パーツ6当たり判定の始点y            
          self.col_parts6_w = 0 #パーツ6当たり判定(横の長さ）
          self.col_parts6_h = 0 #パーツ6当たり判定(縦の長さ)
          
          self.col_parts7_x = 0 #パーツ7当たり判定の始点x
          self.col_parts7_y = 0 #パーツ7当たり判定の始点y            
          self.col_parts7_w = 0 #パーツ7当たり判定(横の長さ）
          self.col_parts7_h = 0 #パーツ7当たり判定(縦の長さ)
          
          self.col_parts8_x = 0 #パーツ8当たり判定の始点x
          self.col_parts8_y = 0 #パーツ8当たり判定の始点y            
          self.col_parts8_w = 0 #パーツ8当たり判定(横の長さ）
          self.col_parts8_h = 0 #パーツ8当たり判定(縦の長さ)

          self.col_parts9_x = 0 #パーツ9当たり判定の始点x
          self.col_parts9_y = 0 #パーツ9当たり判定の始点y            
          self.col_parts9_w = 0 #パーツ9当たり判定(横の長さ）
          self.col_parts9_h = 0 #パーツ9当たり判定(縦の長さ)

          self.main_hp_bar_offset_x,  self.main_hp_bar_offset_y   = 0,0 #本体のHPバーを表示する座標のオフセット値

          self.parts1_hp_bar_offset_x,self.parts1_hp_bar_offset_y = 0,0 #パーツ1のHPバーを表示する座標のオフセット値
          self.parts2_hp_bar_offset_x,self.parts2_hp_bar_offset_y = 0,0 #パーツ2のHPバーを表示する座標のオフセット値
          self.parts3_hp_bar_offset_x,self.parts3_hp_bar_offset_y = 0,0 #パーツ3のHPバーを表示する座標のオフセット値
          self.parts4_hp_bar_offset_x,self.parts4_hp_bar_offset_y = 0,0 #パーツ4のHPバーを表示する座標のオフセット値
          self.parts5_hp_bar_offset_x,self.parts5_hp_bar_offset_y = 0,0 #パーツ5のHPバーを表示する座標のオフセット値
          self.parts6_hp_bar_offset_x,self.parts6_hp_bar_offset_y = 0,0 #パーツ6のHPバーを表示する座標のオフセット値
          self.parts7_hp_bar_offset_x,self.parts7_hp_bar_offset_y = 0,0 #パーツ7のHPバーを表示する座標のオフセット値
          self.parts8_hp_bar_offset_x,self.parts8_hp_bar_offset_y = 0,0 #パーツ8のHPバーを表示する座標のオフセット値
          self.parts9_hp_bar_offset_x,self.parts9_hp_bar_offset_y = 0,0 #パーツ9のHPバーを表示する座標のオフセット値
          
          self.size = 0          #大きさ
          self.priority = 0      #画像表示時の優先度
          self.attack_method = 0 #攻撃方法
          self.direction = 0     #方向
          self.acceleration = 0  #加速度
          self.timer = 0    #時間
          self.degree = 0   #回転角度 度数法（主にこちらを使用するのです！）
          self.radian = 0   #回転角度 弧度法
          self.speed = 0    #回転スピード(弧度法0~360度)
          self.radius = 0   #半径
          self.flag1 = 0    #フラグ類
          self.flag2 = 0
          self.flag3 = 0
          self.flag4 = 0
          self.count1 = 0   #カウンター類
          self.count2 = 0
          self.count3 = 0
          self.count4 = 0
          self.parts1_flag = 0 #各部位用のフラグ
          self.parts2_flag = 0
          self.parts3_flag = 0
          self.parts4_flag = 0
          self.parts5_flag = 0
          self.parts6_flag = 0
          self.parts7_flag = 0
          self.parts8_flag = 0
          self.parts9_flag = 0
          self.animation_number1 = 0 #アニメーションパターンナンバー用
          self.animation_number2 = 0
          self.animation_number3 = 0
          self.animation_number4 = 0
          self.move_index = 0     #移動用のインデックス（リストの添え字に入る数値）
          self.obj_time = 0       #2次ベジェ曲線での移動用のtime（現在のタイムフレーム番号が入る）(0~totaltimeまで変化する)ピエール・ベジェさんありがとう・・・
          self.obj_totaltime = 0  #2次ベジェ曲線での移動用のtotaltime（移動元から移動先までに掛けるトータルフレーム数が入る60なら1秒掛けて移動元から移動先まで移動するって事,120なら2秒かかる)
          self.invincible = 0     #無敵状態かどうかのフラグ(出現時は無敵にするとかで使うかも？)
          self.display_time_main_hp_bar   = 0 #耐久力ゲージをどれだけの時間表示させるかのカウント 1=60ミリ秒
          self.display_time_parts1_hp_bar = 0
          self.display_time_parts2_hp_bar = 0
          self.display_time_parts3_hp_bar = 0
          self.display_time_parts4_hp_bar = 0
          self.display_time_parts5_hp_bar = 0
          self.display_time_parts6_hp_bar = 0
          self.display_time_parts7_hp_bar = 0
          self.display_time_parts8_hp_bar = 0
          self.display_time_parts9_hp_bar = 0
     def update(self,boss_id,boss_type,status,parts_number,
                main_hp,
                parts1_hp,parts2_hp,parts3_hp,
                parts4_hp,parts5_hp,parts6_hp,
                parts7_hp,parts8_hp,parts9_hp,
                parts1_score,parts2_score,parts3_score,
                parts4_score,parts5_score,parts6_score,
                parts7_score,parts8_score,parts9_score,
                level,

                weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count,
                weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count,
                weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count,
                weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count,
                weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count,
                x,y,offset_x,offset_y,ax,ay,bx,by,cx,cy,dx,dy,qx,qy,vx,vy,
                width,height,
                
                col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h,
                col_damage_point2_x,col_damage_point2_y,col_damage_point2_w,col_damage_point2_h,
                col_damage_point3_x,col_damage_point3_y,col_damage_point3_w,col_damage_point3_h,
                col_damage_point4_x,col_damage_point4_y,col_damage_point4_w,col_damage_point4_h,
                
                col_main1_x ,col_main1_y ,col_main1_w ,col_main1_h,
                col_main2_x ,col_main2_y ,col_main2_w ,col_main2_h,
                col_main3_x ,col_main3_y ,col_main3_w ,col_main3_h,
                col_main4_x ,col_main4_y ,col_main4_w ,col_main4_h,
                col_main5_x ,col_main5_y ,col_main5_w ,col_main5_h,
                col_main6_x ,col_main6_y ,col_main6_w ,col_main6_h,
                col_main7_x ,col_main7_y ,col_main7_w ,col_main7_h,
                col_main8_x ,col_main8_y ,col_main8_w ,col_main8_h,

                col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h,
                col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h,
                col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h,
                col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h,
                col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h,
                col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h,
                col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h,
                col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h,
                col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h,

                main_hp_bar_offset_x,main_hp_bar_offset_y,

                parts1_hp_bar_offset_x,parts1_hp_bar_offset_y,
                parts2_hp_bar_offset_x,parts2_hp_bar_offset_y,
                parts3_hp_bar_offset_x,parts3_hp_bar_offset_y,
                parts4_hp_bar_offset_x,parts4_hp_bar_offset_y,
                parts5_hp_bar_offset_x,parts5_hp_bar_offset_y,
                parts6_hp_bar_offset_x,parts6_hp_bar_offset_y,
                parts7_hp_bar_offset_x,parts7_hp_bar_offset_y,
                parts8_hp_bar_offset_x,parts8_hp_bar_offset_y,
                parts9_hp_bar_offset_x,parts9_hp_bar_offset_y,

                size,priority,attack_method,direction,acceleration,timer,degree,radian,speed,radius,
                flag1,flag2,flag3,flag4,
                count1,count2,count3,count4,
                parts1_flag,parts2_flag,parts3_flag,
                parts4_flag,parts5_flag,parts6_flag,
                parts7_flag,parts8_flag,parts9_flag,
                animation_number1,animation_number2,animation_number3,animation_number4,
                move_index,
                obj_time,obj_totaltime,
                invincible,
                display_time_main_hp_bar,
                display_time_parts1_hp_bar,display_time_parts2_hp_bar,display_time_parts3_hp_bar,
                display_time_parts4_hp_bar,display_time_parts5_hp_bar,display_time_parts6_hp_bar,
                display_time_parts7_hp_bar,display_time_parts8_hp_bar,display_time_parts9_hp_bar,
                ):
          self.boss_id = boss_id
          self.boss_type = boss_type
          self.status = status
          self.parts_number = parts_number
          self.main_hp = main_hp
          self.parts1_hp = parts1_hp
          self.parts2_hp = parts2_hp
          self.parts3_hp = parts3_hp
          self.parts4_hp = parts4_hp
          self.parts5_hp = parts5_hp
          self.parts6_hp = parts6_hp
          self.parts7_hp = parts7_hp
          self.parts8_hp = parts8_hp
          self.parts9_hp = parts9_hp
          self.parts1_score = parts1_score
          self.parts2_score = parts2_score
          self.parts3_score = parts3_score
          self.parts4_score = parts4_score
          self.parts5_score = parts5_score
          self.parts6_score = parts6_score
          self.parts7_score = parts7_score
          self.parts8_score = parts8_score
          self.parts9_score = parts9_score
          self.level = level

          self.weapon1_status         = weapon1_status
          self.weapon1_interval       = weapon1_interval
          self.weapon1_rapid_num      = weapon1_rapid_num
          self.weapon1_cool_down_time = weapon1_cool_down_time
          self.weapon1_omen_count     = weapon1_omen_count  
          
          self.weapon2_status         = weapon2_status
          self.weapon2_interval       = weapon2_interval
          self.weapon2_rapid_num      = weapon2_rapid_num
          self.weapon2_cool_down_time = weapon2_cool_down_time
          self.weapon2_omen_count     = weapon2_omen_count  
          
          self.weapon3_status         = weapon3_status
          self.weapon3_interval       = weapon3_interval
          self.weapon3_rapid_num      = weapon3_rapid_num
          self.weapon3_cool_down_time = weapon3_cool_down_time
          self.weapon3_omen_count     = weapon3_omen_count  
          
          self.weapon4_status         = weapon4_status
          self.weapon4_interval       = weapon4_interval
          self.weapon4_rapid_num      = weapon4_rapid_num
          self.weapon4_cool_down_time = weapon4_cool_down_time
          self.weapon4_omen_count     = weapon4_omen_count  
          
          self.weapon5_status         = weapon5_status
          self.weapon5_interval       = weapon5_interval
          self.weapon5_rapid_num      = weapon5_rapid_num
          self.weapon5_cool_down_time = weapon5_cool_down_time
          self.weapon5_omen_count     = weapon5_omen_count  
          
          self.posx = x
          self.posy = y
          self.offset_x = offset_x
          self.offset_y = offset_y
          self.ax = ax
          self.ay = ay
          self.bx = bx
          self.by = by
          self.cx = cx
          self.cy = cy          
          self.dx = dx
          self.dy = dy
          self.qx = qx
          self.qy = qy
          self.vx = vx
          self.vy = vy
          self.width = width 
          self.height = height
          
          self.col_damage_point1_x = col_damage_point1_x
          self.col_damage_point1_y = col_damage_point1_y
          self.col_damage_point1_w = col_damage_point1_w
          self.col_damage_point1_h = col_damage_point1_h

          self.col_damage_point2_x = col_damage_point2_x
          self.col_damage_point2_y = col_damage_point2_y
          self.col_damage_point2_w = col_damage_point2_w
          self.col_damage_point2_h = col_damage_point2_h

          self.col_damage_point3_x = col_damage_point3_x
          self.col_damage_point3_y = col_damage_point3_y
          self.col_damage_point3_w = col_damage_point3_w
          self.col_damage_point3_h = col_damage_point3_h

          self.col_damage_point4_x = col_damage_point4_x
          self.col_damage_point4_y = col_damage_point4_y
          self.col_damage_point4_w = col_damage_point4_w
          self.col_damage_point4_h = col_damage_point4_h
          
          self.col_main1_x = col_main1_x
          self.col_main1_y = col_main1_y
          self.col_main1_w = col_main1_w
          self.col_main1_h = col_main1_h

          self.col_main2_x = col_main2_x
          self.col_main2_y = col_main2_y
          self.col_main2_w = col_main2_w
          self.col_main2_h = col_main2_h
          
          self.col_main3_x = col_main3_x
          self.col_main3_y = col_main3_y
          self.col_main3_w = col_main3_w
          self.col_main3_h = col_main3_h
          
          self.col_main4_x = col_main4_x
          self.col_main4_y = col_main4_y
          self.col_main4_w = col_main4_w
          self.col_main4_h = col_main4_h

          self.col_main5_x = col_main5_x
          self.col_main5_y = col_main5_y
          self.col_main5_w = col_main5_w
          self.col_main5_h = col_main5_h
          
          self.col_main6_x = col_main6_x
          self.col_main6_y = col_main6_y
          self.col_main6_w = col_main6_w
          self.col_main6_h = col_main6_h
          
          self.col_main7_x = col_main7_x
          self.col_main7_y = col_main7_y
          self.col_main7_w = col_main7_w
          self.col_main7_h = col_main7_h
          
          self.col_main8_x = col_main8_x
          self.col_main8_y = col_main8_y
          self.col_main8_w = col_main8_w
          self.col_main8_h = col_main8_h
          
          self.col_parts1_x = col_parts1_x
          self.col_parts1_y = col_parts1_y
          self.col_parts1_w = col_parts1_w
          self.col_parts1_h = col_parts1_h

          self.col_parts2_x = col_parts2_x
          self.col_parts2_y = col_parts2_y
          self.col_parts2_w = col_parts2_w
          self.col_parts2_h = col_parts2_h
          
          self.col_parts3_x = col_parts3_x
          self.col_parts3_y = col_parts3_y
          self.col_parts3_w = col_parts3_w
          self.col_parts3_h = col_parts3_h
          
          self.col_parts4_x = col_parts4_x
          self.col_parts4_y = col_parts4_y
          self.col_parts4_w = col_parts4_w
          self.col_parts4_h = col_parts4_h

          self.col_parts5_x = col_parts5_x
          self.col_parts5_y = col_parts5_y
          self.col_parts5_w = col_parts5_w
          self.col_parts5_h = col_parts5_h

          self.col_parts6_x = col_parts6_x
          self.col_parts6_y = col_parts6_y
          self.col_parts6_w = col_parts6_w
          self.col_parts6_h = col_parts6_h
          
          self.col_parts7_x = col_parts7_x
          self.col_parts7_y = col_parts7_y
          self.col_parts7_w = col_parts7_w
          self.col_parts7_h = col_parts7_h
          
          self.col_parts8_x = col_parts8_x
          self.col_parts8_y = col_parts8_y
          self.col_parts8_w = col_parts8_w
          self.col_parts8_h = col_parts8_h

          self.col_parts9_x = col_parts9_x
          self.col_parts9_y = col_parts9_y
          self.col_parts9_w = col_parts9_w
          self.col_parts9_h = col_parts9_h

          self.main_hp_bar_offset_x = main_hp_bar_offset_x  
          self.main_hp_bar_offset_y = main_hp_bar_offset_y

          self.parts1_hp_bar_offset_x = parts1_hp_bar_offset_x
          self.parts1_hp_bar_offset_y = parts1_hp_bar_offset_y

          self.parts2_hp_bar_offset_x = parts2_hp_bar_offset_x
          self.parts2_hp_bar_offset_y = parts2_hp_bar_offset_y
          
          self.parts3_hp_bar_offset_x = parts3_hp_bar_offset_x
          self.parts3_hp_bar_offset_y = parts3_hp_bar_offset_y
          
          self.parts4_hp_bar_offset_x = parts4_hp_bar_offset_x
          self.parts4_hp_bar_offset_y = parts4_hp_bar_offset_y

          self.parts5_hp_bar_offset_x = parts5_hp_bar_offset_x
          self.parts5_hp_bar_offset_y = parts5_hp_bar_offset_y

          self.parts6_hp_bar_offset_x = parts6_hp_bar_offset_x
          self.parts6_hp_bar_offset_y = parts6_hp_bar_offset_y
          
          self.parts7_hp_bar_offset_x = parts7_hp_bar_offset_x
          self.parts7_hp_bar_offset_y = parts7_hp_bar_offset_y
          
          self.parts8_hp_bar_offset_x = parts8_hp_bar_offset_x
          self.parts8_hp_bar_offset_y = parts8_hp_bar_offset_y

          self.parts9_hp_bar_offset_x = parts9_hp_bar_offset_x
          self.parts9_hp_bar_offset_y = parts9_hp_bar_offset_y

          self.size = size
          self.priority = priority
          self.attack_method = attack_method
          self.direction = direction
          self.acceleration = acceleration
          self.timer = timer
          self.degree = degree
          self.radian = radian
          self.speed = speed
          self.radius = radius
          self.flag1 = flag1
          self.flag2 = flag2
          self.flag3 = flag3
          self.flag4 = flag4
          self.count1 = count1
          self.count2 = count2
          self.count3 = count3
          self.count4 = count4
          self.parts1_flag = parts1_flag
          self.parts2_flag = parts2_flag
          self.parts3_flag = parts3_flag
          self.parts4_flag = parts4_flag
          self.parts5_flag = parts5_flag
          self.parts6_flag = parts6_flag
          self.parts7_flag = parts7_flag
          self.parts8_flag = parts8_flag
          self.parts9_flag = parts9_flag
          self.animation_number1 = animation_number1
          self.animation_number2 = animation_number2
          self.animation_number3 = animation_number3
          self.animation_number4 = animation_number4
          self.move_index = move_index
          self.obj_time = obj_time
          self.obj_totaltime = obj_totaltime
          self.invincible = invincible
          self.display_time_main_hp_bar = display_time_main_hp_bar
          self.display_time_parts1_hp_bar = display_time_parts1_hp_bar
          self.display_time_parts2_hp_bar = display_time_parts2_hp_bar
          self.display_time_parts3_hp_bar = display_time_parts3_hp_bar
          self.display_time_parts4_hp_bar = display_time_parts4_hp_bar
          self.display_time_parts5_hp_bar = display_time_parts5_hp_bar
          self.display_time_parts6_hp_bar = display_time_parts6_hp_bar
          self.display_time_parts7_hp_bar = display_time_parts7_hp_bar
          self.display_time_parts8_hp_bar = display_time_parts8_hp_bar
          self.display_time_parts9_hp_bar = display_time_parts9_hp_bar      
class Enemy_shot:#敵弾のクラス設定
     def __init__(self):
          self.enemy_shot_type = 0 #敵弾の種類
          self.enemy_shot_id   = 0 #敵弾に振られたIDナンバー
          self.posx = 0            #敵弾の座標x,y
          self.posy = 0
          self.collision_type = 0 #自機との当たり判定の種類 0=単純な小さな正方形で自機との距離を比べて当たったか判断 1=長方形でwidth,heightを見て自機と当たったかどうか判断する
          self.width  = 0 #弾の横幅
          self.height = 0 #弾の縦幅
          self.cx = 0     #回転弾で使用する回転の中心cx,cy
          self.cy = 0
          self.vx = 0     #速度ベクトルvx,vy
          self.vy = 0
          self.accel = 0     #加速度
          self.power = 0     #弾のパワー
          self.hp = 0        #弾のヒットポイント
          self.count1 = 0    #汎用カウンタ1
          self.count2 = 0    #汎用カウンタ2
          self.timer = 0     #時間(三角関数系で使用)
          self.speed = 0     #速度(三角関数系で使用)
          self.intensity = 0 #振れ幅(三角関数系で使用)
          self.aim = 0       #狙い撃つ方向
          self.disappearance_count = 0 #消滅するまでのカウントタイマー
          self.stop_count = 0          #その場に止まり続ける時に使用するカウンタ
          self.priority = 0            #描画優先度 0=1番最前面に表示 1=ボスより奥&敵より手前 2=ボスより奥&敵よりも奥
          self.turn_theta = 0          #誘導弾やホーミングミサイル,レーザーでの最大旋回可能角度(これ以上の角度では曲がることが出来ません)
          self.search_flag = 0                #サーチレーザーなどで自機の位置を調べて曲がる位置を確定させたかどうかのフラグ
          self.rotation_omega = 0             #回転弾などで使用する角度が入ります(現在値)
          self.rotation_omega_incremental = 0 #回転弾などで使用する,1フレームで増加する角度が入ります
          self.radius = 0        #回転弾などで使用する半径(現在値)
          self.radius_max = 0    #回転弾などで使用する半径(目標となる最大値)
          self.division_type = 0 #分裂弾かどうかのフラグとそのタイプ
                                 #0=分裂はしない 1=自機狙いの3way 2=自機狙いの5way 3=自機狙いの7way 4=16方向弾 5=誘導弾4個
                                 #6=誘導弾8個
          self.division_count = 0        #分裂するまでのカウント
          self.radius_incremental = 0    #回転弾などで使用する半径の増分
          self.division_count_origin = 0 #分裂するまでのカウント(元となる数値です変化はしません)
          self.division_num = 0          #分裂する回数(0なら1回だけ分裂して通常弾に戻る 1なら2分裂(孫分裂),2なら3分裂(ひ孫)後通常弾に戻ります)
          self.angle = 0                 #グラフイック表示時に使用する回転角の数値
          self.expansion = 0             #だんだんと広がっていくウェーブやレーザーの広がっていくドット数(毎フレーム)
          self.expansion_flag = 0        #ウェーブやレーザーが最大まで広がったら立てるフラグ
          self.width_max = 0             #拡大ウェーブや拡大レーザーリップルレーザーの横幅の最大値
          self.height_max = 0            #拡大ウェーブや拡大レーザーリップルレーザーの縦幅の最大値
          self.color = 0                 #色
          self.anime = 0                 #アニメーション用カウンター
     def update(self,enemy_shot_type,enemy_shot_id, x, y,collision_type,width,height, cx,cy, vx,vy,accel,power, hp, count1, count2, timer, speed, intensity, aim,disappearance_count,stop_count,priority,turn_theta,search_flag,rotation_omega,rotation_omega_incremental,radius,radius_max,division_type,division_count,radius_incremental,division_count_origin,division_num,angle,expansion,expansion_flag,width_max,height_max,color,anime):
          self.enemy_shot_type = enemy_shot_type
          self.enemy_shot_id   = enemy_shot_id
          self.posx = x
          self.posy = y
          self.collision_type = collision_type
          self.width = width
          self.height = height
          self.cx = cx
          self.cy = cy
          self.vx = vx
          self.vy = vy
          self.accel = accel
          self.power = power
          self.hp = hp
          self.count1 = count1
          self.count2 = count2
          self.timer = timer
          self.speed = speed
          self.intensity = intensity
          self.aim = aim
          self.disappearance_count = disappearance_count
          self.stop_count = stop_count
          self.priority = priority
          self.turn_theta = turn_theta
          self.search_flag = search_flag
          self.rotation_omega = rotation_omega
          self.rotation_omega_incremental = rotation_omega_incremental
          self.radius = radius
          self.radius_max = radius_max
          self.division_type = division_type
          self.division_count = division_count
          self.radius_incremental = radius_incremental
          self.division_count_origin = division_count_origin
          self.division_num = division_num
          self.angle = angle
          self.expansion = expansion
          self.expansion_flag = expansion_flag
          self.width_max = width_max
          self.height_max = height_max
          self.color = color
          self.anime = anime
class Explosion:#爆発のクラス設定
     def __init__(self):
          self.explosion_type = 0 #爆発の種類
          self.priority = 0       #描画優先度
          self.posx = 0 #x座標
          self.posy = 0 #y座標
          self.vx = 0   #速度(ベクトル)
          self.vy = 0
          self.explotion_count = 0 #アニメーションパターン数
          self.return_bullet_type = 0  #打ち返し弾の種類 0=打ち返しなし 1=自機狙い弾1個 2=自機狙い弾1個+数フレーム停止して自機を狙う弾1個
          self.return_buller_count = 0 #打ち返し弾を生み出すまでのカウントタイマー(0になったら打ち返し弾を育成する)
          self.x_reverse = 0           #x軸方向(横)反転フラグ1=通常表示 -1=横に反転する
          self.y_reverse = 0           #y軸方向(横)反転フラグ1=通常表示 -1=縦に反転する
     def update(self,explosion_type,priority,x,y,vx,vy,explosion_count,return_bullet_type,return_buller_count,x_reverse,y_reverse):
          self.explosion_type = explosion_type
          self.priority = priority
          self.posx = x
          self.posy = y
          self.vx = vx
          self.vy = vy
          self.explosion_count = explosion_count
          self.return_bullet_type = return_bullet_type
          self.return_buller_count = return_buller_count
          self.x_reverse = x_reverse
          self.y_reverse = y_reverse
class Particle:#パーティクル（粒子）クラスの設定
     def __init__(self):
          self.particle_type = 0 #パーティクルの種類
          self.posx = 0 #x座標
          self.posy = 0 #y座標
          self.size = 0 #大きさ
          self.vx = 0 #速度(ベクトル)
          self.vy = 0
          self.life = 0 #パーティクルの生存期間
          self.wait = 0 #ウェイト(どれだけその場所に停止し続けるのかのウェイトカウンター)
          self.color = 0 #パーティクルの色
     def update(self,particle_type,x,y,size,vx,vy,life,wait,color):
          self.particle_type = particle_type
          self.posx = x
          self.posy = y
          self.size = size
          self.vx = vx
          self.vy = vy
          self.life = life
          self.wait = wait
          self.color = color
class Background_object:#背景の物体(背景オブジェクト）クラスの設定 (雲や鳥や泡や木葉や背景を移動する艦隊とか当たり判定の無い大き目の物体)
     def __init__(self):
          self.background_object_type = 0 #背景オブジェクトの種類
          self.posx,self.posy = 0,0 #x,y座標
          self.size           = 0   #大きさ
          self.ax,self.ay     = 0,0 #加速度
          self.bx,self.by     = 0,0
          self.cx,self.cy     = 0,0
          self.dx,self.dy     = 0,0
          self.vx,self.vy     = 0,0 #速度(ベクトル)
          self.width          = 0   #横
          self.height         = 0   #縦
          self.life           = 0   #生存時間
          self.wait           = 0   #停止時間
          self.color          = 0   #色
          self.speed          = 0   #速度(倍率)
          self.direction      = 0   #方向
          self.flag1,self.flag2,self.flag3    = 0,0,0 #フラグ1~3
          self.count1,self.count2,self.count3 = 0,0,0 #カウント1~3
          self.animation_number1,self.animation_number2,self.animation_number3 = 0,0,0 #アニメーション番号1~3
     def update(self,background_object_type,
                posx,posy,
                size,
                ax,ay, bx,by, cx,cy, dx,dy, vx,vy,
                width,height,
                life,wait,color,speed,direction,
                flag1,flag2,flag3,
                count1,count2,count3,
                animation_number1,animation_number2,animation_number3
                ):
          self.background_object_type = background_object_type
          self.posx,self.posy = posx,posy
          self.size           = size
          self.ax,self.ay     = ax,ay
          self.bx,self.by     = bx,by
          self.cx,self.cy     = cx,cy
          self.dx,self.dy     = dx,dy
          self.vx,self.vy     = vx,vy
          self.width          = width
          self.height         = height
          self.life           = life
          self.wait           = wait
          self.color          = color
          self.speed          = speed
          self.direction      = direction
          self.flag1,self.flag2,self.flag3    = flag1,flag2,flag3
          self.count1,self.count2,self.count3 = count1,count2,count3
          self.animation_number1,self.animation_number2,self.animation_number3 = animation_number1,animation_number2,animation_number3
class Window: #メッセージ表示ウィンドウのクラスの設定
    def __init__(self):
        self.window_id = 0
        self.window_id_sub = 0
        self.window_type = 0
        self.window_status = 0
        self.window_title = ""
        self.window_title_flag = 0
        
        self.mes1 = ""
        self.mes1_flag = 0
        self.mes1_ox = 0
        self.mes1_color = 0

        self.mes2 = ""
        self.mes2_flag = 0
        self.mes2_ox = 0
        self.mes2_color = 0

        self.mes3 = ""
        self.mes3_flag = 0
        self.mes3_ox = 0
        self.mes3_color = 0

        self.mes4 = ""
        self.mes4_flag = 0
        self.mes4_ox = 0
        self.mes4_color = 0

        self.mes5 = ""
        self.mes5_flag = 0
        self.mes5_ox = 0
        self.mes5_color = 0

        self.mes6 = ""
        self.mes6_flag = 0
        self.mes6_ox = 0
        self.mes6_color = 0

        self.mes7 = ""
        self.mes7_flag = 0
        self.mes7_ox = 0
        self.mes7_color = 0
        
        self.posx = 0
        self.posy = 0
        self.width = 0
        self.height = 0
        self.open_width = 0
        self.open_height = 0
        self.vx = 0
        self.vy = 0
        self.open_speed = 0
        self.close_speed = 0
        self.open_delay = 0
        self.close_delay = 0
        self.marker = 0
        self.color = 0
    def update(self,window_id,window_id_sub,window_type,window_status,window_title,window_title_flag,\
         mes1,mes1_flag,mes1_ox,mes1_color,\
         mes2,mes2_flag,mes2_ox,mes2_color,\
         mes3,mes3_flag,mes3_ox,mes3_color,\
         mes4,mes4_flag,mes4_ox,mes4_color,\
         mes5,mes5_flag,mes5_ox,mes5_color,\
         mes6,mes6_flag,mes6_ox,mes6_color,\
         mes7,mes7_flag,mes7_ox,mes7_color,\
         x,y,width,height,open_width,open_height,vx,vy,open_speed,close_speed,open_delay,close_delay,marker,color):
        self.window_id = window_id
        self.window_id_sub = window_id_sub
        self.window_type = window_type
        self.window_status = window_status
        self.window_title = window_title
        self.window_title_flag = window_title_flag

        self.mes1 = mes1
        self.mes1_flag = mes1_flag
        self.mes1_ox = mes1_ox
        self.mes1_color = mes1_color
        
        self.mes2 = mes2
        self.mes2_flag = mes2_flag
        self.mes2_ox = mes2_ox
        self.mes2_color = mes2_color

        self.mes3 = mes3
        self.mes3_flag = mes3_flag
        self.mes3_ox = mes3_ox
        self.mes3_color = mes3_color

        self.mes4 = mes4
        self.mes4_flag = mes4_flag
        self.mes4_ox = mes4_ox
        self.mes4_color = mes4_color

        self.mes5 = mes5
        self.mes5_flag = mes5_flag
        self.mes5_ox = mes5_ox
        self.mes5_color = mes5_color

        self.mes6 = mes6
        self.mes6_flag = mes6_flag
        self.mes6_ox = mes6_ox
        self.mes6_color = mes6_color

        self.mes7 = mes7
        self.mes7_flag = mes7_flag
        self.mes7_ox = mes7_ox
        self.mes7_color = mes7_color



        self.posx = x
        self.posy = y
        self.width = width
        self.height = height
        self.open_width = open_width
        self.open_height = open_height
        self.vx = vx
        self.vy = vy
        self.open_speed = open_speed
        self.close_speed = close_speed
        self.open_delay = open_delay
        self.close_delay = close_delay
        self.marker = marker
        self.color = color
class Obtain_item:#手に入れるアイテム類（パワーアップ勲章とかコインアイテムとか）のクラス設定
    def __init__(self):
        self.item_type = 0                       #アイテムのタイプ 1=ショットパワーアップ 2=ミサイルパワーアップ 3=シールドパワーアップ
                                                 #                これ以外はパワーアップアイテム類のtype定数の定義を参照してください
        self.posx = 0                            #x座標
        self.posy = 0                            #y座標
        self.vx = 0                              #速度ベクトル
        self.vy = 0
        self.width = 0                           #横の大きさ
        self.height = 0                          #縦の大きさ
        self.color = 0                           #色
        self.intensity = 0                       #振れの度合い
        self.timer = 0                           #時間
        self.degree = 0                          #回転角度 度数法（主にこちらを使用するのです！）
        self.radian = 0                          #回転角度 弧度法
        self.speed = 0                           #回転スピード(弧度法0~360度)
        self.radius = 0                          #半径
        self.radius_max = 0                      #半径の最大値(回転半径が変化する物ではこの数値を最大値として設定することにします)
        self.animation_number = 0                #アニメーションパターンのオフセット指定番号用
        self.score = 0                           #得点
        self.shot = 0                            #ショットパワーの増加量
        self.missile = 0                         #ミサイルパワーの増加量
        self.shield = 0                          #シールドパワーの増加量
        self.flag1 = 0                           #フラグ用その１
        self.flag2 = 0                           #フラグ用その２
        self.flag3 = 0                           #フラグ用その３
        self.bounce = 0                          #画面左端で跳ね返って戻ってくる回数(バウンス回数)
        self.status = 0                          #状態遷移用（ステータス）
    def update(self,item_type,x,y,vx,vy,width,height,color,intensity,timer,degree,radian,speed,radius,radius_max,animation_number,score,shot,missile,shield,flag1,flag2,flag3,bounce,status):
        self.item_type = item_type
        self.posx = x
        self.posy = y
        self.vx = vx
        self.vy = vy
        self.width = width
        self.height = height
        self.color = color
        self.intensity = intensity
        self.timer = timer
        self.degree = degree
        self.radian = radian
        self.speed = speed
        self.radius = radius
        self.radius_max = radius_max
        self.animation_number = animation_number
        self.score = score
        self.shot = shot
        self.missile = missile
        self.shield = shield
        self.flag1 = flag1
        self.flag2 = flag2
        self.flag3 = flag3
        self.bounce = bounce
        self.status = status
class Enemy_formation: #敵の編隊数のリストのクラス設定
     def __init__(self):
          self.formation_id = 0               #それぞれの編隊に与えられたidナンバー(1~?)(0は単独機で使用してるので編隊では未使用です) 
          self.formation_number = 0           #何機編隊なのか編隊の総数が入ります
          self.on_screen_formation_number = 0 #画面上に存在する編隊数(撃墜されたり画面からいなくなったらだんだん数が減ってきます0になったらリストからインスタンス破棄します)
          self.shoot_down_number = 0          #撃墜するべき編隊総数 (7機編隊なら最初は7で1機撃墜すると1減らしていく、この値が0になったらパワーアップアイテム出現！って事ね)
     
     def update(self,formation_id,formation_number,on_screen_formation_number,shoot_down_number):
          self.formation_id               = formation_id
          self.formation_number           = formation_number
          self.on_screen_formation_number = on_screen_formation_number
          self.shoot_down_number          = shoot_down_number
class Event_append_request: #早回しなどの敵の追加や乱入中ボス,臨時のスクロールスピードや方向の調整などの追加リクエストが入るリストのクラス設定です
     def __init__(self):
          self.timer = 0      #イベントが開始されるカウントタイマー
          self.event_type = 0 #イベントのタイプ
          self.enemy_type = 0 #敵の種類
          self.posx = 0       #x座標
          self.posy = 0       #y座標
          self.number = 0     #敵の数
     def update(self,timer,event_type,enemy_type,x,y,number):
          self.timer = timer
          self.event_type = event_type
          self.enemy_type = enemy_type
          self.posx = x
          self.posy = y
          self.number = number
class Raster_scroll: #背景でラスタースクロールするときに使用する横ラインのデータ設定値のクラス
     def __init__(self):
          self.scroll_id = 0       #複数のラスタースクロールを動作させる時に使用するidナンバー
          self.raster_type = 0     #ラスタースクロールの種類
          self.priority  = 0       #描画時の優先度
          self.display = 0         #描画するかどうかの判定用 (0=描画しない 1=描画する)
          self.scroll_line_no = 0  #ラスタースクロール時に使用するそれぞれの横ラインの割り当てられた番号(上方向から0~任意の数値)
          self.total_line_num = 0  #どこまでラスタスクロールさせるかの縦軸総ライン数 (scroll_line_noに入る最大値(任意の数値)が入る)
          self.posx = 0            #x座標
          self.posy = 0            #y座標
          self.offset_x = 0        #現在のx座標値に対してのオフセット値
          self.offset_y = 0        #現在の垂直スクロールカウント数に対してのy軸オフセット値
          self.img_bank = 0        #グラフイックパターンのあるイメージバンクの数値
          self.posu = 0            #グラフイックパターンが記録されている横座標(pyxelのblt命令のuの値)
          self.posv = 0            #グラフイックパターンが記録されている縦座標(pyxelのblt命令のvの値)
          self.width = 0           #各ラインを描画するときの横幅の数値(単位はドット)
          self.height = 0          #縦幅(通常は1だけど上下スクロールするときに1ドットだと隙間が出来る可能性があるので2ドットでもいいかも？)
          self.speed = 0           #スクロールスピード
          self.transparent_color=0 #透明色の指定
          self.wave_timer = 0      #ウェーブラスタースクロール用のタイマー
          self.wave_speed = 0      #ウェーブラスタースクロール用のスピード
          self.wave_intensity = 0 #ウェーブラスタースクロール用の振れ幅
     def update(self,scroll_id,raster_type,priority,display,scroll_line_no,total_line_num,
                x,y,offset_x,offset_y,img_bank,u,v,width,height,speed,transparent_color,
                wave_timer,wave_speed,wave_intensity):
          self.scroll_id = scroll_id
          self.raster_type = raster_type
          self.priority = priority
          self.display = display
          self.scroll_line_no = scroll_line_no
          self.total_line_num = total_line_num
          self.posx = x
          self.posy = y
          self.offsrt_x = offset_y
          self.offset_y = offset_y
          self.img_bank = img_bank
          self.posu = u
          self.posv = v
          self.width = width
          self.height = height
          self.speed = speed
          self.transparent_color = transparent_color
          self.wave_timer = wave_timer
          self.wave_speed = wave_speed
          self.wave_intensity = wave_intensity

class App:
     ##########################################################################################################################################
     #関数を定義沢山定義するところだよ############################################################################################################
     #なんかpythonではこのあたり（Appクラスの __init__関数定義が終わったあたり）で定義しないとエラーが出るらしい
     #確かに関数定義をしないで関数呼び出したらエラーになるよなぁ・・・最初は関数定義はどこでも定義できると思って最後の方で定義してエラー出て悩んでたよ
     
     def __init__(self):
          pyxel.init(WINDOW_W,WINDOW_H,caption="mineka shooting game",fps=60) #ゲームウィンドウのタイトルバーの表示とfpsの設定(60fpsにした)
          pyxel.load("min-sht2.pyxres") #画像リソースファイルを読み込み
          pyxel.mouse(False) #マウスカーソルを非表示にする

          self.bg_cls_color = 0            #BGをCLS(クリアスクリーン)するときの色の指定(通常は0=黒色です)
          self.bg_transparent_color = 0    #BGタイルマップを敷き詰めるときに指定する透明色です
          
          #ゲーム中で絶対に変化することのないリスト群はここで作成します#######################################
          #サブウェポンセレクターカーソルなどで使用する点滅用カラーリスト群(pyxelのカラーナンバーだよ)
          self.blinking_color         = [0,1,5,12, 6,7,6,12,5,1]
          self.red_flash_color        = [0,1,5, 4, 2,8,2, 4,5,1]
          self.green_flash_color      = [0,1,5, 3,11,11,3,5,1,0]
          self.yellow_flash_color     = [0,2,4,9,9,10,9,9,4,2,0]
          self.monochrome_flash_color = [0,0,1,5,12,13,15,7,7,15,13,12,5,1,0]
          self.rainbow_flash_color    = [3,4,5,6,7,8,9,10,11,12,13,14,15,1,2]

          #サブウェポンアイテムの外を回っている四角形描画で使用するための「おっきくなったり、ちいさくなったりするオフセット数値」のリスト群(単位はドット)
          self.expansion_shrink_number = [1,1,1,2,2,2,3,3,3,4,   4,5,5,6,6,7,8,9,10,9,   8,7,6,6,5,5,4,4,3,3,   3,2,2,2,1,1,1,1,1,1,1,1]

          #敵１のアニメーションパターンのキャラチップ番号定義
          self.anime_enemy001 = [0,0,   8,8,   16,16,     24,   16,16,   8,8,   0,0,  0,0]
          #敵２のアニメーションパターンのキャラチップ番号定義
          self.anime_enemy002 = [40,40,40,40,40,
                                 48,48,48,48,48,
                                 56,56,56,56,56,
                                 64,64,64,64,64,
                                 72,72,72,72,72,
                                 80,80,80,80,80,
                                 88,88,88,88,88,
                                 96,96,96,96,96]
          #敵３のアニメーションパターンのキャラチップ番号定義
          self.anime_enemy003 = [32,32,32,
                                 40,40,40,
                                 48,48,48,
                                 40,40,40,
                                 32,32,32]
          #敵５のアニメーションパターンのキャラチップ番号定義
          self.anime_enemy005 = [104,104,104,104,104,
                                 112,112,112,112,112,
                                 120,120,120,120,120,
                                 128,128,128,128,128,
                                 136,136,136,136,136,
                                 144,144,144,144,144,
                                 152,152,152,152,152,
                                 160,160,160,160,160]
          #敵９のアニメーションパターンのキャラチップ番号定義
          self.anime_enemy009 = [  0, 0, 0, 0, 0,
                                   8, 8, 8, 8, 8,
                                  16,16,16,16,16,
                                  24,24,24,24,24,
                                  32,32,32,32,32,
                                  40,40,40,40,40,
                                  48,48,48,48,48,
                                  56,56,56,56,56]
          
          #敵の移動データリスト
          #[移動元座標ax,ay, 移動先座標dx,dy,2次ベジェ曲線向けの制御点qx,qy, 現在のフレーム番号を移動に使う総フレーム数で割ったもの=t,移動速度,加速度,攻撃方法]
          #axが9999の時はエンドコードとみなし最初に戻る
          
          #ダミー用
          self.enemy_move_data_dummy = [
               [ 0,   0,   0,  0,     0, 0,    0,   0,0,   ENEMY_ATTACK_NO_FIRE],
               [9999],]
          #敵17用
          self.enemy_move_data17 = [
               [ 160, 10,    160,  120,     20,  60,    240,   1.0,1.01,   ENEMY_ATTACK_NO_FIRE],
              
                  
               [9999],]

          #敵の移動データリスト(タイプナンバーの並びで各リストへ渡すテーブルリストとなっています)(意味不明な日本語・・・自分でも言ってる意味が分からない）
          self.enemy_move_data_list = [[ 0,self.enemy_move_data_dummy],[ 1,self.enemy_move_data_dummy],[ 2,self.enemy_move_data_dummy],
                                       [ 3,self.enemy_move_data_dummy],[ 4,self.enemy_move_data_dummy],[ 5,self.enemy_move_data_dummy],
                                       [ 6,self.enemy_move_data_dummy],[ 7,self.enemy_move_data_dummy],[ 8,self.enemy_move_data_dummy],
                                       [ 9,self.enemy_move_data_dummy],[10,self.enemy_move_data_dummy],[11,self.enemy_move_data_dummy],
                                       [12,self.enemy_move_data_dummy],[13,self.enemy_move_data_dummy],[14,self.enemy_move_data_dummy],
                                       [15,self.enemy_move_data_dummy],[16,self.enemy_move_data_dummy],[17,self.enemy_move_data17    ],
                                       [18,self.enemy_move_data_dummy],[19,self.enemy_move_data_dummy],[20,self.enemy_move_data_dummy],
                                       [21,self.enemy_move_data_dummy],[22,self.enemy_move_data_dummy],[23,self.enemy_move_data_dummy],
                                       [24,self.enemy_move_data_dummy],[25,self.enemy_move_data_dummy],[26,self.enemy_move_data_dummy],
                                    ]          
          #ボス１の移動データリスト
          #[移動元座標ax,ay, 移動先座標dx,dy,2次ベジェ曲線向けの制御点qx,qy, 現在のフレーム番号を移動に使う総フレーム数で割ったもの=t,移動速度,加速度,攻撃方法]
          #axが9999の時はエンドコードとみなし最初に戻る
          self.boss_move_data1 = [
               [-40,  0,   120,  0,     80, 240,    240,   1.1,0.995,   BOSS_ATTACK_FRONT_5WAY],
               [120,  0,   120,120,     0,   60,    240,   1.2,0.999,   BOSS_ATTACK_FRONT_5WAY_AIM_BULLET],
               [120,120,   -40,120,     80, -240,   240,   1.1,0.995,   BOSS_ATTACK_FRONT_5WAY_HOMING],
               [-40,120,   -40,  0,     160, 60,    240,   0.7,0.999,   BOSS_ATTACK_RIGHT_GREEN_LASER],      
               [9999],]
          
          self.boss_move_data2 = [
               [-40,  0,   120,  0,     80, 240,    240,   1.1,0.995,   BOSS_ATTACK_FRONT_5WAY],
               [120,  0,   120,120,     0,   60,    240,   1.2,0.999,   BOSS_ATTACK_FRONT_5WAY_AIM_BULLET],
               [120,120,   -40,120,     80, -240,   240,   1.1,0.995,   BOSS_ATTACK_FRONT_5WAY_HOMING],
               [-40,120,   -40,  0,     160, 60,    240,   0.7,0.999,   BOSS_ATTACK_RIGHT_GREEN_LASER],      
               [9999],]
          
          #ステージデータリスト
          #各ステージで使用する設定データのリストです
          #[
          # ステージ名,
          # 障害物とみなす背景画像(BG)のY座標位置(例88だとキャラチップのＹ座標が88以上のマップチップは障害物とみなされます),
          # BG(背景スクロール)で使用するタイルマップの番号,
          # 背景スクロールの種類,星スクロールのon/off,ラスタスクロールのon/off,
          # BG背景(手前)を表示するかどうかのフラグ,BG背景(中央)を表示するかどうかのフラグ,BG背景(奥)を表示するかどうかのフラグ
          # 大気圏突入時の火花を表示するかどうかのフラグ
          # ]
          self.stage_data_list = [
               [STAGE_MOUNTAIN_REGION,256,IMG1,
               SCROLL_TYPE_8FREEWAY_SCROLL_AND_RASTER ,STAR_SCROLL_ON,
               RASTER_SCROLL_ON,
               DISP_ON,DISP_ON,DISP_ON,
               SPARK_ON],

               [STAGE_ADVANCE_BASE,   88 ,IMG0,
               SCROLL_TYPE_TRIPLE_SCROLL_AND_STAR     ,STAR_SCROLL_ON,
               RASTER_SCROLL_OFF,
               DISP_ON,DISP_ON,DISP_ON,
               SPARK_OFF],
               ]
          
          #難易度ごとの各種設定数値のリスト
          #フォーマット
          #[
          # [難易度名,開始時のショットボーナス,開始時のミサイルボーナス,開始時のシールドボーナス,クロー初期値,ステージクリア後に回復するシールド値,撃ち返し弾の有無,        スコア倍率, ランク上昇指数, スタートランク数]
          #]
          self.game_difficulty_list = [
              [GAME_VERY_EASY,6,6,6,                                                      THREE_CLAW, REPAIR_SHIELD3,                  RETURN_BULLET_NONE,     1.0,        1.0,           0],
              [GAME_EASY     ,3,3,3,                                                      ONE_CLAW,   REPAIR_SHIELD2,                  RETURN_BULLET_NONE,     1.0,        1.0,           0],
              [GAME_NORMAL   ,0,0,0,                                                      NO_CLAW,    REPAIR_SHIELD2,                  RETURN_BULLET_AIM,      1.0,        1.0,           0],
              [GAME_HARD     ,0,0,0,                                                      NO_CLAW,    REPAIR_SHIELD1,                  RETURN_BULLET_AIM,      1.0,        1.5,           5],
              [GAME_VERY_HARD,0,0,0,                                                      NO_CLAW,    REPAIR_SHIELD0,                  RETURN_BULLET_DELAY_AIM,2.0,       1.75,          10],
              [GAME_INSAME   ,0,0,0,                                                      NO_CLAW,    REPAIR_SHIELD0,                  RETURN_BULLET_DELAY_AIM,3.0,        2.0,          15],
              ]
          #ランク値による各種設定数値のリスト
          #フォーマット
          #[
          #    [ランク,  敵スピード倍率, 敵弾弾スピード倍率,    撃ち返し弾確率%,  敵耐久力倍率]敵のスピード倍率は3.9までにしておいてください、追尾戦闘機のスピードが速すぎると一瞬で画面外に飛んでいくみたいで・・
          #]
          self.game_rank_data_list = [
               [ 0,     1.0,           1.0,                  0,              1.0],
               [ 1,     1.0,           1.0,                  0,              1.0],
               [ 2,     1.1,           1.0,                  1,              1.0],
               [ 3,     1.1,           1.0,                  1,              1.0],
               [ 4,     1.2,           1.0,                  1,              1.0],
               [ 5,     1.2,           1.1,                  1,              1.0],
               [ 6,     1.2,           1.1,                  2,              1.0],
               [ 7,     1.2,           1.1,                  2,              1.0],
               [ 8,     1.2,           1.1,                  2,              1.0],
               [ 9,     1.2,           1.1,                  2,              1.0],
               [10,     1.3,           1.1,                  3,              1.1],
               [11,     1.3,           1.1,                  3,              1.1],
               [12,     1.3,           1.2,                  3,              1.1],
               [13,     1.3,           1.2,                  4,              1.1],
               [14,     1.3,           1.2,                  4,              1.1],
               [15,     1.4,           1.3,                  4,              1.1],
               [16,     1.4,           1.3,                  5,              1.1],
               [17,     1.4,           1.3,                  5,              1.1],
               [18,     1.4,           1.3,                  5,              1.1],
               [19,     1.4,           1.3,                  5,              1.1],
               [20,     1.4,           1.4,                  6,              1.2],
               [21,     1.4,           1.4,                  6,              1.2],
               [22,     1.4,           1.4,                  6,              1.2],
               [23,     1.4,           1.4,                  6,              1.2],
               [24,     1.4,           1.4,                  6,              1.2],
               [25,     1.4,           1.5,                  6,              1.3],
               [26,     1.4,           1.5,                  6,              1.3],
               [27,     1.4,           1.5,                  7,              1.3],
               [28,     1.4,           1.5,                  7,              1.3],
               [29,     1.4,           1.5,                  7,              1.4],
               [30,     1.4,           1.5,                  7,              1.4],
               [31,     1.5,           1.5,                  7,              1.4],
               [32,     1.5,           1.5,                  7,              1.4],
               [33,     1.5,           1.5,                  7,              1.4],
               [34,     1.5,           1.5,                  8,              1.4],
               [35,     1.5,           1.6,                  8,              1.4],
               [36,     1.5,           1.6,                  8,              1.4],
               [37,     1.5,           1.6,                  8,              1.4],
               [38,     1.5,           1.6,                  8,              1.5],
               [39,     1.5,           1.6,                  8,              1.5],
               [40,     1.6,           1.6,                  8,              1.5],
               [41,     1.6,           1.7,                  8,              1.5],
               [42,     1.6,           1.7,                  8,              1.5],
               [43,     1.6,           1.7,                  9,              1.5],
               [44,     1.6,           1.7,                  9,              1.5],
               [45,     1.6,           1.7,                  9,              1.5],
               [46,     1.6,           1.7,                  9,              1.5],
               [47,     1.6,           1.7,                  9,              1.5],
               [48,     1.6,           1.7,                  9,              1.5],
               [49,     1.6,           1.7,                  9,              1.6],
               [50,     1.6,           1.7,                 10,              1.6],
               ]
          #ショットパワーアップテーブルのフォーマット
          #
          #x軸 [ショットレベル,ショットスピード(倍率),バルカンショットの連射数,ショットの攻撃力(倍率)]
          #y軸 self.shot_exp(通常はショットパワーアップアイテムを取るとshot_expが3増える、特殊機体で成長度が遅い2とか1しか増えない機体もあります)
          #だいたい8個取って8*3の24exp入手で次の武装にレベルアップする感じ
          # 8個入手(24exp)で初期シングルショットバルカンからレーザー
          #更に8個入手(合計16個)(48exp)でレーザーからウェーブカッター
          #更に8個入手(合計24個)(72exp)でウェーブカッターLv4になる感じなのです

          #Justice Pythonのショット・パワーアップテーブル表
          self.j_python_shot_table_list = [
                [0,  1,1, 1],[0,  1,2, 1],[0,1.1,2, 1],
                [0,1.2,2, 1],[0,1.2,3, 1],[0,1.2,4, 1],
                [1,1.2,2, 1],[1,1.2,3, 1],[1,1.2,3, 1],
                [1,1.3,3, 1],[1,1.3,3, 1],[1,1.3,3, 1],
                [2,1.3,3, 1],[2,1.3,3, 1],[2,1.3,3, 1],
                [2,1.3,3, 1],[2,1.3,3, 1],[2,1.3,3, 1],
                [3,1.3,3, 1],[3,1.3,3, 1],[3,1.4,3, 1],
                [3,1.4,3, 1],[3,1.4,3, 1],[3,1.5,3, 1],

                [4,1.5,3, 1],[4,1.5,3, 1],[4,1.5,3, 1],
                [4,1.5,3, 1],[4,1.5,3, 1],[4,1.5,3, 1],
                [4,1.5,3, 1],[4,1.5,3, 1],[4,1.5,3, 1],
                [4,1.5,3, 1],[4,1.5,3, 1],[4,1.5,3, 1],
                [5,1.5,3, 1],[5,1.5,3, 1],[5,1.5,3, 1],
                [5,1.5,3, 1],[5,1.5,3, 1],[5,1.5,3, 1],
                [5,1.5,3, 1],[6,1.5,3, 1],[6,1.5,3, 1],
                [6,1.5,3, 1],[6,1.5,3, 1],[6,1.5,3, 1],

                [ 7,1.2,3, 1],[ 7,1.2,3, 1],[ 7,1.2,3, 1],
                [ 7,1.3,3, 1],[ 7,1.3,3, 1],[ 7,1.3,3, 1],
                [ 8,1.3,2, 1],[ 8,1.3,3, 1],[ 8,1.3,2, 1],
                [ 8,1.3,2, 1],[ 8,1.3,2, 1],[ 8,1.3,2, 1],
                [ 9,1.4,2, 1],[ 9,1.4,2, 1],[ 9,1.4,2, 1],
                [ 9,1.4,2, 1],[ 9,1.4,2, 1],[ 9,1.4,2, 1],
                [10,1.4,2, 1],[10,1.4,2, 1],[10,1.5,2, 1],
                [10,1.5,2, 1],[10,1.5,2, 1],[10,1.5,3, 1],
                [99999],]

          #ミサイルパワーアップテーブルのフォーマット
          #
          #x軸 [ミサイルレベル,ミサイルスピード(倍率),ミサイルの連射数,ミサイルの攻撃力(倍率)]
          #y軸 self.missile_exp(通常はショットパワーアップアイテムを取るとmissile_expが3増える、特殊機体で成長度が遅い2とか1しか増えない機体もあります)
          #だいたい8個取って8*3の24exp入手で次のミサイルにレベルアップする感じ
          # 8個入手(24exp)でノーマルミサイルからツインミサイル
          #更に8個入手(合計16個)(48exp)でツインミサイルからからマルチミサイルになる感じ・・・・かもです！
          
          #Justice Pythonのミサイル・パワーアップテーブル表
          self.j_python_missile_table_list = [
                [0,  1,1, 1],[0,  1,1, 1],[0,1.2,1, 1],
                [0,1.2,1, 1],[0,1.2,1, 1],[0,1.3,1, 1],
                [0,1.3,2, 1],[0,1.3,2, 1],[0,1.4,2, 1],
                [0,1.4,2, 1],[0,1.4,2, 1],[0,1.5,2, 1],
                [0,1.5,2, 1],[0,1.6,2, 1],[0,1.7,2, 1],
                [0,1.8,2, 1],[0,1.9,2, 1],[0,2.0,2, 1],
                [0,2.1,2, 1],[0,2.2,2, 1],[0,2.3,2, 1],
                [0,2.4,3, 1],[0,2.6,3, 1],[0,2.7,3, 1],

                [1,1.9,2, 1],[1,1.9,2, 1],[1,1.9,2, 1],
                [1,2.0,2, 1],[1,2.0,2, 1],[1,2.1,2, 1],
                [1,2.1,2, 1],[1,2.2,2, 1],[1,2.2,2, 1],
                [1,2.3,2, 1],[1,2.4,2, 1],[1,2.4,2, 1],
                [1,2.4,2, 1],[1,2.4,2, 1],[1,2.5,2, 1],
                [1,2.5,2, 1],[1,2.5,2, 1],[1,2.5,2, 1],
                [1,2.5,2, 1],[1,2.6,2, 1],[1,2.7,2, 1],
                [1,2.7,2, 1],[1,2.8,3, 1],[1,2.9,3, 1],

                [2,2.1,2, 1],[2,2.2,2, 1],[2,2.2,2, 1],
                [2,2.3,2, 1],[2,2.4,2, 1],[2,2.5,2, 1],
                [2,2.6,2, 1],[2,2.6,2, 1],[2,2.6,2, 1],
                [2,2.7,3, 1],[2,2.7,3, 1],[2,2.8,3, 1],
                [2,2.9,3, 1],[2,2.9,3, 1],[2,2.9,3, 1],
                [2,2.9,3, 1],[2,2.9,3, 1],[2,2.9,3, 1],
                [2,3.0,3, 1],[2,3.1,3, 1],[2,3.2,4, 1],
                [2,3.3,4, 1],[2,3.4,4, 1],[2,3.5,4, 1],
                [99999],]
          #スコアランキングの初期データ [順位,名前,得点,クリアステージ,選択機体]
          self.score_ranking_very_easy_init = [
               [ 1,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 2,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 3,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 4,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 5,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 6,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 7,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 8,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 9,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [10,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
          ]
          self.score_ranking_easy_init = [
               [ 1,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 2,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 3,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 4,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 5,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 6,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 7,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 8,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 9,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [10,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
          ]
          self.score_ranking_normal_init = [
               [ 1,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 2,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 3,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 4,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 5,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 6,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 7,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 8,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 9,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [10,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
          ]
          self.score_ranking_hard_init = [
               [ 1,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 2,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 3,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 4,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 5,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 6,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 7,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 8,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 9,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [10,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
          ]
          self.score_ranking_very_hard_init = [
               [ 1,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 2,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 3,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 4,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 5,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 6,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 7,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 8,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 9,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [10,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
          ]
          self.score_ranking_insame_init = [
               [ 1,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 2,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 3,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 4,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 5,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 6,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 7,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 8,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [ 9,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
               [10,"mineka",76500,SATGE_BOSS_RUSH,J_PYTHON],
          ]       
          #IPLメッセージデータその1
          self.ipl_mes1 = [
               ["INITIAL PROGRAM LOADING",7],
               [".",7],
               ["..",7],
               ["...",7],
               ["....",7],
               ['LOADING PROGRAM "CODE OF PYTHON"',7],
               ["POWERD BY PYXEL",6],
               ["POWERD BY PYGAME",5],
               ["FILE CHECK OK",7],
               ["BOOTING PROGRAM",7],
               ["2021 PROJECT MINE",6],
               ["SINCE 2020",7],
               ["...",7],
               ["....",7],
               ["MAIN SYSYTEM OK",7],
               ["SUB SYSYTEM OK",6],
               ["L'S SYSTEM OK",5],
               ["DISPLAY OK",5],
               ["DIALOG SYSYTEM OK",8],
               
               [".",7],
               ["..",7],
               ["...",7],
               ["....",7],
               ["EXECUTE OPERETING SYSTEM",8],
               ["GOOD LUCK!",8],
               
               
               
               ]

          
          self.game_status = SCENE_IPL               #ゲームステータスを「IPL表示」にする
          #self.game_status = SCENE_GAME_START_INIT   #ゲームの状況ステータスを表してます（ゲームそのもの自体の状態遷移フラグとして使用します）
                                                     #まず最初はゲームステータスは「ゲームスタート時の初期化」にします
                                                     #将来的には「起動処理中」とか「タイトル表示中」にする予定
          
          #再スタートで初期化してはいけない変数はここ(appクラスの__init__関数)で定義します###################################
          self.hi_score =  100                      #ハイスコア
          self.total_game_playtime_seconds = 0      #トータルゲームプレイ時間 (秒)

          #####IPL関連の変数を初期化#####################################################################################
          self.display_ipl_time = 200              #IPLメッセージを表示する時間 200
          self.text_console_scroll_counter = 0     #テキストコンソールでスクロールして画面上に消えて行った行数
          self.ipl_mes_write_line_num = 0          #スクリーンに表示したIPLメッセージデータの行数
          self.text_screen = []                    #テキストスクリーン用のリストを初期化して使えるようにします

          self.scroll_type = 0                      #スクロールの種類が入る変数を初期化
          self.game_playing_flag = 0                #ゲーム中なのか？それ以外の状態なのか？を示すフラグです 0=プレイ以外 1=プレイ中
          self.star_scroll_flag  = 0                #背景のスクロールする星々を表示するかのフラグを初期化
          self.raster_scroll_flag = 0               #背景ラスタスクロールを表示するかのフラグを初期化
          self.reference_tilemap  = 0               #BGタイルマップを調べたり書き換えたりする時、どのタイルマップナンバーを使用するのかの変数の初期化です
          

          #デバッグモード＆ゴッドモード用のフラグやパラメーターの初期化とか宣言はこちらで行うようにします########################
          self.debug_menu_status                = 0 #デバッグパラメータの表示ステータス
                                                    #0=表示しない 1=フル表示タイプ 2=簡易表示タイプ
          
          self.boss_collision_rect_display_flag = 0 #ボス用の当たり判定確認の為の矩形表示フラグ(デバッグ時に1にします)
          self.bg_collision_Judgment_flag       = 1 #背景の障害物との衝突判定を行うかどうかのフラグ
                                                    #0=背景の障害物との当たり判定をしない 1=行う

          self.boss_test_mode                   = 0 #ボス戦闘のみのテストモード 
                                                    #0=オフ 1=オン scroll_countを増やさない→マップスクロールしないので敵が発生しません
                                                    #イベントリストもボス専用の物が読み込まれます
          self.no_enemy_mode                    = 0 #マップチップによる敵の発生を行わないモードのフラグですです(地上の敵が出ない！)2021 03/07現在機能してない模様
                                                    #0=マップスクロールによって敵が発生します
                                                    #1=                         発生しません          
          
          #毎フレームごとにupdateとdrawを呼び出す
          pyxel.run(self.update,self.draw) #この命令でこれ以降は１フレームごとに自動でupdate関数とdraw関数が交互に実行されることとなります
                                           #近年のゲームエンジンはみんなこんな感じらしい？？？unityやUEもこんな感じなのかな？？使ったことないけど
     #自機との距離を求める関数定義
     def to_my_ship_distance(self,x,y):
          dx = x - self.my_x
          dy = y - self.my_y
          distance = math.sqrt(dx * dx + dy * dy)
          return(distance)   #最初この行を return(self,distance)って記述しててエラーが出て、どうやったら良いのかわかんなかった・・・この場合はタプルになるらしい！？(良く判るって無いｗ)
     
     #狙い撃ち弾を射出する関数定義 
     def enemy_aim_bullet(self,ex,ey,div_type,div_count,div_num,stop_count,accel):
         if len(self.enemy_shot) < 800:
              #目標までの距離を求めdに代入します
              d = math.sqrt((self.my_x - ex) * (self.my_x - ex) + (self.my_y - ey) * (self.my_y - ey))
              #速さが一定値speedになる様に速度(vx,vy)を求める
              #目標までの距離dが0の時は何もせずに戻る
              if d == 0:
                   return
              else:
                   #敵と自機との距離dとx,y座標との差からvx,vyの増分を計算する
                   vx = ((self.my_x - ex) / (d * 1))
                   vy = ((self.my_y - ey) / (d * 1))
                       
                   new_enemy_shot = Enemy_shot()
                   new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,vx,vy, accel,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count,0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                   self.enemy_shot.append(new_enemy_shot)#敵弾リストに新しい弾の情報を書き込む

     #狙い撃ち弾(ゲームランクに依存）を射出する関数定義 
     def enemy_aim_bullet_rank(self,ex,ey,div_type,div_count,div_num,stop_count,accel):
         if randint(0,self.run_away_bullet_probability) != 0:
              return
         else:
              self.enemy_aim_bullet(ex,ey,div_type,div_count,div_num,stop_count,accel)
         
     #前方3way弾を射出する関数定義 
     def enemy_forward_3way_bullet(self,ex,ey):
         if len(self.enemy_shot) < 800:
             new_enemy_shot = Enemy_shot()
             new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1,0,              1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
             self.enemy_shot.append(new_enemy_shot)
             
             new_enemy_shot = Enemy_shot()
             new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.8,-0.5*0.8,   1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
             self.enemy_shot.append(new_enemy_shot)
             
             new_enemy_shot = Enemy_shot()
             new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.8,0.5*0.8,    1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
             self.enemy_shot.append(new_enemy_shot)  
     
     #前方5way弾を射出する関数定義 
     def enemy_forward_5way_bullet(self,ex,ey):
         if len(self.enemy_shot) < 800:
              self.enemy_forward_3way_bullet(ex,ey) #まずは前方3way弾を射出

              new_enemy_shot = Enemy_shot()
              new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.9,0.2,     1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
              self.enemy_shot.append(new_enemy_shot)
             
              new_enemy_shot = Enemy_shot()
              new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,-1*0.9,-0.2,    1,1,1,1,0,0,1,0,0,0,0,PRIORITY_FRONT,0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
              self.enemy_shot.append(new_enemy_shot)
             
     #狙い撃ちn-way弾を射出する関数定義
     def enemy_aim_bullet_nway(self,ex,ey,theta,n,div_type,div_count,div_num,stop_count):#ex,ey=敵の座標(弾を出す座標),theta=弾と弾の角度,n=弾の総数,div_type=育成する弾は通常弾なのか分裂弾なのかのフラグとそのタイプ,div_count=分裂するまでのカウント(div_count_originにも同じ数値が入ります),div_num=分裂する回数,stop_count=その場に止まるカウント数
         if len(self.enemy_shot) < 800:
              #1度 = (1 × 3.14) ÷ 180 = 0.017453292519943295ラジアン
              #1度は約0.0174ラジアンと設定する
              
              #目標までの距離を求める dに距離が入る
              d = math.sqrt((self.my_x - ex) * (self.my_x - ex) + (self.my_y - ey) * (self.my_y - ey))
              
              #速さが一定値speedになる様に速度(vx,vy)を求める
              if d == 0:
                   return #目標までの距離dが0の時は何もせずに戻る
              else:
                   #敵と自機との距離とx座標、y座標との差から中心の基本速度ベクトル(cvx,cvx)を計算するcentralvx,centralvy
                   cvx = ((self.my_x - ex) / (d * 1))
                   cvy = ((self.my_y - ey) / (d * 1))

                   if n % 2 == 1:
                        #奇数弾の処理#######3way弾とか5way弾とか7way弾とか##################################
                        #まず最初に中央の弾を発射する
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,cvx,cvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)#敵弾リストに中央狙い弾の情報を書き込む

                        for i in range((n+1) // 2):
                             #時計回り方向に i*(theta*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                             rvx = cvx * math.cos(theta*i*0.0174) - cvy * math.sin(theta*i*0.0174)
                             rvy = cvx * math.sin(theta*i*0.0174) + cvy * math.cos(theta*i*0.0174)
                             new_enemy_shot = Enemy_shot()
                             new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                             self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む


                             #反時計回り方向に -i*(theta*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                             rvx = cvx * math.cos(-(theta*i*0.0174)) - cvy * math.sin(-(theta*i*0.0174))
                             rvy = cvx * math.sin(-(theta*i*0.0174)) + cvy * math.cos(-(theta*i*0.0174))
                             new_enemy_shot = Enemy_shot()
                             new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                             self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む
                   else:
                        #偶数弾の処理#######2way弾とか4ay弾とか6way弾とか##################################
                        for i in range(n // 2):
                             #時計回り方向に i*(theta//2*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                             rvx = cvx * math.cos(theta / 2*(i+1)*0.0174) - cvy * math.sin(theta / 2*(i+1)*0.0174)
                             rvy = cvx * math.sin(theta / 2*(i+1)*0.0174) + cvy * math.cos(theta / 2*(i+1)*0.0174)
                             new_enemy_shot = Enemy_shot()
                             new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,  1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                             self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む


                             #反時計回り方向に -i*(theta//2*n)度 回転させたベクトルを計算してRotatevx,Rotatevyに代入する
                             rvx = cvx * math.cos(-(theta // 2 * (i+1) * 0.0174)) - cvy * math.sin(-(theta // 2*(i+1)*0.0174))
                             rvy = cvx * math.sin(-(theta // 2 * (i+1) * 0.0174)) + cvy * math.cos(-(theta // 2*(i+1)*0.0174))
                             new_enemy_shot = Enemy_shot()
                             new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,rvx,rvy,   1,1,1,1,1,0,1,0,0,0,stop_count,PRIORITY_FRONT,0,0,0,0,0,0, div_type,div_count, 0, div_count,div_num, 0, 0,0, 0,0,   0,0)
                             self.enemy_shot.append(new_enemy_shot)#敵弾リストに時計回りに回転させた弾の情報を書き込む
          
     #レーザービームを発射する関数定義
     def enemy_laser(self,ex,ey,length,speed):
          if len(self.enemy_shot) < 800: 
                         for number in range(length):
                             new_enemy_shot = Enemy_shot()
                             new_enemy_shot.update(ENEMY_SHOT_LASER,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -(speed),0,     1,1,1,   0,0,0,    speed,0,0,  0, number * 2 ,PRIORITY_BOSS_FRONT, 0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                             self.enemy_shot.append(new_enemy_shot)
          return()
     
     #サイン弾を射出する関数定義 
     def enemy_sin_bullet(self,ex,ey,timer,speed,intensity):
         if len(self.enemy_shot) < 800:
              new_enemy_shot = Enemy_shot()
              new_enemy_shot.update(ENEMY_SHOT_SIN,ID00,ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0, 0,0,  1,1,1, 1,1,   timer,speed,intensity,  0, 0,   0,PRIORITY_FRONT, 0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
              self.enemy_shot.append(new_enemy_shot)#敵弾リストに新しい弾の情報を書き込む
     
     #ボス用のレッドレーザービームを発射する関数定義
     def enemy_red_laser(self,ex,ey,length,speed):
          if len(self.enemy_shot) < 800: 
                         for number in range(length):
                             new_enemy_shot = Enemy_shot()
                             new_enemy_shot.update(ENEMY_SHOT_RED_LASER,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,  -(speed),0,   1,1,1,   0,0,0,    speed,0,0,  0,number * 2 ,PRIORITY_BOSS_BACK,   0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0, 0,0,0,   0,0)
                             self.enemy_shot.append(new_enemy_shot)
          return()

     #ボス用のグリーンレーザービームを発射する関数定義
     def enemy_green_laser(self,ex,ey,length,speed):
          if len(self.enemy_shot) < 800: 
                         for number in range(length):
                             new_enemy_shot = Enemy_shot()
                             new_enemy_shot.update(ENEMY_SHOT_GREEN_LASER,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,0,0,  -(speed),0,   1,1,1,   0,0,0,    speed,0,0,  0,number * 2 ,PRIORITY_BOSS_BACK,  0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0, 0,0,0,   0,0)
                             self.enemy_shot.append(new_enemy_shot)
          return()
     
     #ミサイルリスト内から同じタイプのミサイルが何発存在するのか数をカウントする関数定義
     def count_missile_type(self,missile_type1,missile_type2,missile_type3,missile_type4):
         quantity = 0
         self.type_check_quantity = 0
         missile_count = len(self.missile)#ミサイルリストの総数を数える
         for i in range (missile_count):
             if      self.missile[i].missile_type == missile_type1 or self.missile[i].missile_type == missile_type2\
                  or self.missile[i].missile_type == missile_type3 or self.missile[i].missile_type == missile_type4:
                 quantity += 1#変数（個数）を１増やして勘定していく
         
                 self.type_check_quantity = quantity
         return (self,quantity)

     #与えられたcx,cy座標を元に敵の全x,y座標を調べてx座標が一致した敵が存在するか調べる関数（サーチレーザー向け）
     def search_laser_enemy_cordinate(self,cx,cy):
          self.search_laser_flag = 0        #x軸が一致した敵を発見したかどうかのフラグ
          self.search_laser_y_direction = 0 #上下どちらかに曲げるかの反転値 -1=上方向 1=下方向
          enemy_count = len(self.enemy)
          for i in range (enemy_count):
               if -2 <= self.enemy[i].posx - cx <= 2:#敵の中でx座標がほぼ一致したものを発見したのなら
                    if self.enemy[i].posy >= cy:#レーザーのy座標より敵のy座標が大きいのなら発見フラグを立てy軸の向きを加算(下方向)にする
                         self.search_laser_flag = 1
                         self.search_laser_y_direction = 1
                    else:#レーザーのy座標より敵のy座標が小さいのなら発見フラグを立てy軸の向きを減算(上方向)にする
                         self.search_laser_flag = 1
                         self.search_laser_y_direction = -1
          return()
     
     #与えられたcx,cy座標を元に敵の全x,y座標から距離を求め一番近い敵の座標を調べる関数（ホーミングミサイル向け）
     def search_homing_missile_enemy_cordinate(self,cx,cy):
          self.search_homing_missile_flag = 0 #狙い撃つ敵を発見したかどうかのフラグ 0=未発見 1=発見
          self.search_homing_missile_tx = 200 #狙い撃つ敵のx座標が入る TargetX
          self.search_homing_missile_ty =  60 #狙い撃つ敵のy座標が入る TargetY
          self.min_distance = 200             #現時点での計算して求めた敵までの距離の最小値が入る
          enemy_count = len(self.enemy)
          for i in range (enemy_count):
               #目標までの距離を求める dに距離が入る
               d = abs(math.sqrt((self.enemy[i].posx - cx) * (self.enemy[i].posx - cx) + (self.enemy[i].posy - cy) * (self.enemy[i].posy - cy)))
               if self.min_distance > d:
                    self.min_distance = d#敵までの距離の最小値を更新したので記録する
                    self.search_homing_missile_tx = self.enemy[i].posx#狙い撃つ敵の座標をtx,tyに代入する
                    self.search_homing_missile_ty = self.enemy[i].posy

                    self.search_homing_missile_flag = 1 #狙い撃つ敵を発見したのでフラグを立てる
               
          return()

     #背景（ＢＧタイルマップのキャラチップ）を取得する
     def get_bg_chip(self,x,y,bg_chip):
         self.bgx = (((self.scroll_count // 8) -256) // 2) + x // 8
         #x座標を8で割った切り捨て値がBGマップでのx座標となる
         #(self.scroll_count // 8) -256) // 2)       この数値がスクロールした分x座標オフセット値となる

         self.bgy = (y // 8)
         #Y座標を8で割った切り捨て数値がBGマップでのy座標となる
         #bgxがMAPの外に存在するときは強制的にbgxを0にしちゃう(マイナスの値や256以上だとエラーになるため)
         if  0 > self.bgx:
             self.bgx = 0
         if self.bgx > 255:
             self.bgx = 0
         #bgyがMAPの外に存在するときは強制的にbgyを一番上の座標か一番下の座標にしちゃう(マイナスの値や15より大きいと（まぁ他の面のマップデータにアクセスするのでエラーにはなりませんが・・・）だとエラーになるため)
         if self.bgy < 0:
             self.bgy = 0
         if self.bgy > 15:
             self.bgy = 15
         
         if self.stage_loop == 2:
              self.bgy += 16
         elif self.stage_loop == 3:
              self.bgy += 32
         self.bg_chip = pyxel.tilemap(self.reference_tilemap).get(self.bgx,self.bgy)
         return(self,x,y,bg_chip)
     #背景（ＢＧタイルマップのキャラチップ）を取得し、更に障害物かどうかを判別する
     def check_bg_collision(self,x,y,bg_chip,collision_flag):
         self.collision_flag = 0#コリジョンフラグ（障害物と接触したかどうかのフラグ）を初期化 (0=当たってない 1=接触しちゃった！)
         
         self.bgy = y // 8#bgy座標はy座標を8で割った切り捨て値としてその位置にあるＢＧ（バックグラウンド（背景チップ））をチェックする
         self.bgx = (((self.scroll_count // 8) -256) // 2) + x // 8
         #(self.scroll_count // 8) -256) // 2)=x=0       現在表示されている画面のＸ座標値0がＢＧマップのこの値と同じになる
         #bgxがMAPの外に存在するときは強制的にbgxを0にしちゃう(マイナスの値や256以上だとエラーになるため)
         if  0 > self.bgx:
                self.bgx = 0
         if self.bgx > 255:
                self.bgx = 0
         
         #bgyがMAPの外に存在するときは強制的にbgyを一番上の座標か一番下の座標にしちゃう(マイナスの値や15より大きいと（まぁ他の面のマップデータにアクセスするのでエラーにはなりませんが・・・）だとエラーになるため)
         if  0 > self.bgy:
                self.bgy = 0
         if self.bgy > 15:
                self.bgy = 15
         
         if self.stage_loop == 2:
              self.bgy += 16
         elif self.stage_loop == 3:
              self.bgy += 32
         
         self.bg_chip = pyxel.tilemap(0).get(self.bgx,self.bgy)
         #bgx,bgyの座標のキャラチップナンバーをゲット！

         if (self.bg_chip // 4) >= self.bg_obstacle_y: #(bg_chip // 4)でキャラチップのＹ座標になるんです
                self.collision_flag = 1                #y座標がbg_obstacle_yより大きかったら障害物に当たったとみなす
         return(self,x,y,bg_chip,collision_flag)
     #背景マップチップを消去する(0を書き込む) x,yはキャラ単位 x=(0~255) y=(0~15)
     def delete_map_chip(self,x,y):
         pyxel.tilemap(self.reference_tilemap).set(x,y + (self.stage_loop - 1)* 16,0)#マップチップを消去する（0=何もない空白）を書き込む
     
     #背景（ＢＧタイルマップのキャラチップ）を取得する (8方向フリースクロール専用)
     def get_bg_chip_free_scroll(self,x,y,bg_chip):
         #x座標を8で割った切り捨て値がBGマップでのx座標となる
         self.bgx = int(self.scroll_count           // 8 % (256 -20)) + x // 8
         
         #Y座標を8で割った切り捨て値がBGマップでのy座標となる
         self.bgy = int(self.vertical_scroll_count  // 8 % 256) + y // 8
         
         #bgx,bgyのクリッピング処理
         #bgxがMAPの外に存在するときは強制的にbgxを0または255にしちゃう(マイナスの値や256以上だとエラーになるため)
         if  self.bgx < 0:
             self.bgx = 0
         if self.bgx > 255:
             self.bgx = 255
         #bgyがMAPの外に存在するときは強制的にbgyを0または255にしちゃう(マイナスの値や256以上だとエラーになるため)
         if self.bgy < 0:
             self.bgy = 0
         if self.bgy > 255:
             self.bgy = 255
         
         self.bg_chip = pyxel.tilemap(self.reference_tilemap).get(self.bgx,self.bgy)
         return(self,x,y,bg_chip)
     
     #背景マップチップに書き込む関数 （8方向フリースクロール専用） x,yはキャラ単位 x=(0~255) y=(0~255) n=(0~255)マップチップナンバー
     def write_map_chip_free_scroll(self,x,y,n):
         pyxel.tilemap(self.reference_tilemap).set(x,y,n)#マップチップナンバーnを座標x,yに書き込む
     
     #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数
     def level_up_my_shot(self):
          if self.shot_exp > SHOT_EXP_MAXIMUM:  #自機ショットの経験値は最大経験値を超えないように補正してやります
               self.shot_exp = SHOT_EXP_MAXIMUM
          if self.shot_exp < 0:                 #自機ショットの経験値は0より小さくならないよう補正します
               self.shot_exp = 0                #経験値がマイナスになることは無いと思うけどエナジードレインする敵攻撃とかあったらそうなりそう
          
          self.shot_level               = self.shot_table_list[self.shot_exp][0] #テーブルリストを参照して経験値に対応したショットレベルを代入する
          self.shot_speed_magnification = self.shot_table_list[self.shot_exp][1] #テーブルリストを参照して経験値に対応したショットスピード倍率を代入する
          self.shot_rapid_of_fire       = self.shot_table_list[self.shot_exp][2] #テーブルリストを参照して経験値に対応したショット連射数を代入する
          
     #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数
     def level_up_my_missile(self):
          if self.missile_exp > MISSILE_EXP_MAXIMUM:  #自機ミサイルの経験値は最大経験値を超えないように補正してやります
               self.missile_exp = MISSILE_EXP_MAXIMUM
          if self.missile_exp < 0:                 #自機ミサイルの経験値は0より小さくならないよう補正します
               self.missile_exp = 0                #経験値がマイナスになることは無いと思うけどエナジードレインする敵攻撃とかあったらそうなりそう
          
          self.missile_level               = self.missile_table_list[self.missile_exp][0] #テーブルリストを参照して経験値に対応したミサイルレベルを代入する
          self.missile_speed_magnification = self.missile_table_list[self.missile_exp][1] #テーブルリストを参照して経験値に対応したミサイルスピード倍率を代入する
          self.missile_rapid_of_fire       = self.missile_table_list[self.missile_exp][2] #テーブルリストを参照して経験値に対応したミサイル連射数を代入する
          
     #敵編隊出現時、現在の編隊IDナンバーとIDナンバーに対応した編隊数、そして現在の生存編隊数をenemy_formationクラスに登録する関数
     def record_enemy_formation(self,num):
          #編隊なので編隊のＩＤナンバーと編隊の総数、現在の編隊生存数をEnemy_formationリストに登録します
          new_enemy_formation = Enemy_formation()
          new_enemy_formation.update(self.current_formation_id,num,num,num)
          self.enemy_formation.append(new_enemy_formation)
          self.current_formation_id += 1                #編隊IDを1増加させ次の編隊IDにするのです

     #敵破壊時、編隊ＩＤをみて編隊リストに登録されていた撃墜するべき総数を減少させ、全滅させたらフラグを立てて戻ってくる関数
     def check_enemy_formation_shoot_down_number(self,id):
          enemy_formation_count = len(self.enemy_formation)
          for i in reversed(range(enemy_formation_count)): #インスタンスを消去するのでreversedで昇順ではなく降順で調べていきます
               if id == self.enemy_formation[i].formation_id: #調べるidとリストに登録されているidが同じだったら
                    self.enemy_formation[i].shoot_down_number -= 1          #撃墜するべき編隊総数を1減らす
                    self.enemy_formation[i].on_screen_formation_number -= 1 #それと同時に撃墜されたことで画面上に存在する編隊も1機減るのでこちらも1減らす
                    if self.enemy_formation[i].shoot_down_number == 0: #もし編隊をすべて撃墜したのなら
                         self.enemy_extermination_flag = 1 #殲滅フラグを建てる
                         del self.enemy_formation[i]      #該当した編隊リストは必要ないのでインスタンスを消去する
                         break                            #もうこれ以上リストを調べ上げる必要はないのでbreakしてループから抜け出す
     
     #敵が画面から消える時、編隊ＩＤをみて編隊リストに登録されていた「画面上に存在する編隊数」を減少させ0になったらインスタンスを破棄する関数です
     #まぁ所属する編隊idナンバーを見て編隊がもう存在しなかったリストからインスタンスを破棄するって事ですわん
     def check_enemy_formation_exists(self,id):
          enemy_formation_count = len(self.enemy_formation)
          for i in reversed(range(enemy_formation_count)): #インスタンスを消去するのでreversedで昇順ではなく降順で調べていきます
               if id == self.enemy_formation[i].formation_id: #調べるidとリストに登録されているidが同じだったら
                    self.enemy_formation[i].on_screen_formation_number -= 1 #画面上に存在する編隊数を1機減らす
                    if self.enemy_formation[i].on_screen_formation_number == 0: #もし編隊がすべて画面に存在しないのなら
                         del self.enemy_formation[i]      #該当した編隊リストは必要ないのでインスタンスを消去する
                         break                            #もうこれ以上リストを調べ上げる必要はないのでbreakしてループから抜け出す

     #敵を破壊した後の処理
     def enemy_destruction(self,e):
         # 引数のeは敵リストenemyのインデックス値となります 例enemy[e]
         #ここから敵機破壊処理となります###################################################
         #自機ショットや自機ミサイル、クローショットが敵に当たり敵の耐久力が0以下になったらその座標に爆発を生成する
         if   self.enemy[e].enemy_size == E_SIZE_NORMAL:         #標準的な大きさの敵8x8ドットの敵を倒したとき
              new_explosion = Explosion()
              new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.enemy[e].posx,self.enemy[e].posy,0,0,10,RETURN_BULLET_NONE,0,  1,1)
              self.explosions.append(new_explosion)       
         elif self.enemy[e].enemy_size == E_SIZE_MIDDLE32:       #スクランブルハッチを倒したとき
              new_explosion = Explosion()
              new_explosion.update(EXPLOSION_MIDDLE,PRIORITY_MORE_FRONT,self.enemy[e].posx + 4,self.enemy[e].posy,0,0,10*2,RETURN_BULLET_NONE,0,  1,1)
              self.explosions.append(new_explosion)
         elif self.enemy[e].enemy_size == E_SIZE_MIDDLE32_Y_REV: #天井のスクランブルハッチを倒したとき
              new_explosion = Explosion()
              new_explosion.update(EXPLOSION_MIDDLE,PRIORITY_MORE_FRONT,self.enemy[e].posx + 4,self.enemy[e].posy,0,0,10*2,RETURN_BULLET_NONE,0,  1,-1)
              self.explosions.append(new_explosion)
         elif self.enemy[e].enemy_size == E_SIZE_HI_MIDDLE53:    #重爆撃機タイプを倒したとき 大型爆発パターン2個育成
              new_explosion = Explosion()
              new_explosion.update(EXPLOSION_MIDDLE,PRIORITY_MORE_FRONT,self.enemy[e].posx + 4 ,self.enemy[e].posy + 4,0,0,10*2,RETURN_BULLET_NONE,0,  1,1)
              self.explosions.append(new_explosion)
              new_explosion = Explosion()
              new_explosion.update(EXPLOSION_MIDDLE,PRIORITY_MORE_FRONT,self.enemy[e].posx + 28,self.enemy[e].posy + 4,0,0,10*2,RETURN_BULLET_NONE,0,  1,1)
              self.explosions.append(new_explosion)
         
         #敵編隊殲滅フラグを強制的に初期化する
         self.enemy_extermination_flag = 0
         #編隊機の場合は撃墜するべき総数に達したのかどうかを調べ上げる（編隊全部殲滅した？）
         if self.enemy[e].formation_id != 0:#編隊機の場合は以下の処理をする
             self.check_enemy_formation_shoot_down_number(self.enemy[e].formation_id) 
         #早回しの条件チェック
         if self.enemy_extermination_flag == 1 and self.fast_forward_destruction_num !=0: #もし編隊殲滅フラグON,「敵編隊殲滅必要数」が0以外ならば
              self.fast_forward_destruction_num -= 1                                      #1編隊を殲滅させたので「敵編隊殲滅必要数」を1減少さる
              for i in range(self.fast_forward_destruction_num):
                   #次に出現する敵のタイマーをfast_forward_destruction_num分先まで早回し時のパラメーター分減少させる(全体的に編隊群が速く出現する感じ)
                   #ただし減少させたタイマー値が現在のタイマー値であるstage_countより小さくなってしまうとこれ以降のイベントが実行されなくなるので
                   #早回し処理は行わずそのままの値にしておく
                   if self.stage_count < self.event_list[self.event_index + i][0] - self.fast_forward_destruction_count:
                        self.event_list[self.event_index + i][0] -= self.fast_forward_destruction_count
              
              if self.fast_forward_destruction_num == 0: #「敵編隊殲滅必要数」が0になったら・・・・
                   self.add_appear_flag = 1 #「早回し敵発生フラグ」をonにする

         
         
         #アイテム育成############################################################
         if (self.enemy[e].formation_id   == 0 and self.enemy[e].item == E_SHOT_POW) or (self.enemy_extermination_flag == 1 and self.enemy[e].item == E_SHOT_POW):
             #ショットパワーアップアイテムを持っているのならアイテムを育成する
             new_obtain_item = Obtain_item()
             new_obtain_item.update(ITEM_SHOT_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   1,0,0,  0,0,0, self.pow_item_bounce_num,0)
             self.obtain_item.append(new_obtain_item)
         elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_MISSILE_POW) or (self.enemy_extermination_flag == 1 and self.enemy[e].item == E_MISSILE_POW):
             #ミサイルパワーアップアイテムを持っているのならアイテムを育成する
             new_obtain_item = Obtain_item()
             new_obtain_item.update(ITEM_MISSILE_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,1,0,  0,0,0, self.pow_item_bounce_num,0)
             self.obtain_item.append(new_obtain_item)
         elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_SHIELD_POW) or (self.enemy_extermination_flag == 1 and self.enemy[e].item == E_SHIELD_POW):
             #シールドパワーアップアイテムを持っているのならアイテムを育成する
             new_obtain_item = Obtain_item()
             new_obtain_item.update(ITEM_SHIELD_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,0,1,  0,0,0, self.pow_item_bounce_num,0)
             self.obtain_item.append(new_obtain_item)
         
         
         elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_CLAW_POW) or (self.enemy_extermination_flag == 1 and self.enemy[e].item == E_CLAW_POW):
             #クローアイテムを持っているのならアイテムを育成する
             new_obtain_item = Obtain_item()
             new_obtain_item.update(ITEM_CLAW_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
             self.obtain_item.append(new_obtain_item)
         
         elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_TRIANGLE_POW) or (self.enemy_extermination_flag == 1 and self.enemy[e].item == E_TRIANGLE_POW):
             #トライアングルアイテムを持っているのならアイテムを育成する
             new_obtain_item = Obtain_item()
             new_obtain_item.update(ITEM_TRIANGLE_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.3,0,   8,8,   1,   0.9,  0.3,   0,0,  0.5,0,15, 0,0,   1,1,1,  0,0,2 * 60, self.pow_item_bounce_num,0)
             self.obtain_item.append(new_obtain_item)
         
         
         elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_TAIL_SHOT_POW) or (self.enemy_extermination_flag == 1 and self.enemy[e].item == E_TAIL_SHOT_POW):
             #テイルショットアイテムを持っているのならアイテムを育成する
             new_obtain_item = Obtain_item()
             new_obtain_item.update(ITEM_TAIL_SHOT_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,10,10,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
             self.obtain_item.append(new_obtain_item)
         
         elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_PENETRATE_ROCKET_POW) or (self.enemy_extermination_flag == 1 and self.enemy[e].item == E_PENETRATE_ROCKET_POW):
             #ペネトレートロケットアイテムを持っているのならアイテムを育成する
             new_obtain_item = Obtain_item()
             new_obtain_item.update(ITEM_PENETRATE_ROCKET_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,10,10,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
             self.obtain_item.append(new_obtain_item)
         
         elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_SEARCH_LASER_POW) or (self.enemy_extermination_flag == 1 and self.enemy[e].item == E_SEARCH_LASER_POW):
             #サーチレーザーアイテムを持っているのならアイテムを育成する
             new_obtain_item = Obtain_item()
             new_obtain_item.update(ITEM_SEARCH_LASER_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,10,10,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
             self.obtain_item.append(new_obtain_item)
         
         elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_HOMING_MISSILE_POW) or (self.enemy_extermination_flag == 1 and self.enemy[e].item == E_HOMING_MISSILE_POW):
             #ホーミングミサイルアイテムを持っているのならアイテムを育成する
             new_obtain_item = Obtain_item()
             new_obtain_item.update(ITEM_HOMING_MISSILE_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,10,10,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
             self.obtain_item.append(new_obtain_item)
         
         elif (self.enemy[e].formation_id == 0 and self.enemy[e].item == E_SHOCK_BUMPER_POW) or (self.enemy_extermination_flag == 1 and self.enemy[e].item == E_SHOCK_BUMPER_POW):
             #ショックバンパーアイテムを持っているのならアイテムを育成する
             new_obtain_item = Obtain_item()
             new_obtain_item.update(ITEM_SHOCK_BUMPER_POWER_UP,self.enemy[e].posx,self.enemy[e].posy, 0.5,0,   8,8,   1,   0.9,  0.3,   0,0,  0.05,10,10,0,0,   0,0,0,  0,0,0, self.pow_item_bounce_num,0)
             self.obtain_item.append(new_obtain_item)
     
     #敵をベジェ曲線で移動させるために必要な座標をリストから取得する関数
     def enemy_get_bezier_curve_coordinate(self,enemy_type,i): #enemy_type=敵のタイプナンバー,i=インデックスナンバ値           
         self.enemy_move_data = self.enemy_move_data_list[enemy_type][1]
         self.enemy[i].ax             = self.enemy_move_data[self.enemy[i].move_index][0]#リストから新たな移動元座標を登録する
         self.enemy[i].ay             = self.enemy_move_data[self.enemy[i].move_index][1]
         self.enemy[i].dx             = self.enemy_move_data[self.enemy[i].move_index][2]#リストから新たな移動先座標を登録する
         self.enemy[i].dy             = self.enemy_move_data[self.enemy[i].move_index][3]
         self.enemy[i].qx             = self.enemy_move_data[self.enemy[i].move_index][4]#リストから2次ベジェ曲線用の制御点座標を登録する
         self.enemy[i].qy             = self.enemy_move_data[self.enemy[i].move_index][5]

         self.enemy[i].obj_totaltime  = self.enemy_move_data[self.enemy[i].move_index][6]#リストから移動に掛けるトータルタイムを取得し登録する

         self.enemy[i].move_speed     = self.enemy_move_data[self.enemy[i].move_index][7]#リストから移動スピードを取得し登録する
         self.enemy[i].acceleration   = self.enemy_move_data[self.enemy[i].move_index][8]#リストから加速度を取得し登録する

         self.enemy[i].attack_method  = self.enemy_move_data[self.enemy[i].move_index][9]#リストから攻撃方法を取得し登録する

     #敵17をベジェ曲線で移動させるために必要な座標をリストから取得する関数
     def enemy17_get_bezier_curve_coordinate(self,i):                         
          self.enemy[i].ax             = self.enemy_move_data17[self.enemy[i].move_index][0]#リストから新たな移動元座標を登録する
          self.enemy[i].ay             = self.enemy_move_data17[self.enemy[i].move_index][1]
          self.enemy[i].dx             = self.enemy_move_data17[self.enemy[i].move_index][2]#リストから新たな移動先座標を登録する
          self.enemy[i].dy             = self.enemy_move_data17[self.enemy[i].move_index][3]
          self.enemy[i].qx             = self.enemy_move_data17[self.enemy[i].move_index][4]#リストから2次ベジェ曲線用の制御点座標を登録する
          self.enemy[i].qy             = self.enemy_move_data17[self.enemy[i].move_index][5]

          self.enemy[i].obj_totaltime  = self.enemy_move_data17[self.enemy[i].move_index][6]#リストから移動に掛けるトータルタイムを取得し登録する

          self.enemy[i].move_speed     = self.enemy_move_data17[self.enemy[i].move_index][7]#リストから移動スピードを取得し登録する
          self.enemy[i].acceleration   = self.enemy_move_data17[self.enemy[i].move_index][8]#リストから加速度を取得し登録する

          self.enemy[i].attack_method  = self.enemy_move_data17[self.enemy[i].move_index][9]#リストから攻撃方法を取得し登録する
     
     #ボスにショットを当てた後の処理(ドットパーティクル育成、背景の星をオマケで追加,ボス本体のHPが0以下になった時の処理などなど)
     def boss_processing_after_hitting(self,h,e):
         #ドットパーティクル生成
         for _number in range(10):
             self.update_append_particle(PARTICLE_DOT,self.shots[h].posx,self.shots[h].posy,self.shots[h].vx / 2,self.shots[h].vy / 2, 0,0,0)
         
         #オマケで背景の星も追加するぞ～～☆彡
         if len(self.stars) < 600:
              new_stars = Star()
              new_stars.update(WINDOW_W - 1,randint(0,WINDOW_H),randint(1,50))
              self.stars.append(new_stars)

         if self.boss[e].main_hp <= 0:#ボス本体のHPが0以下になったのなら
             for _number in range(60):#爆発パターンを60個育成
                 new_explosion = Explosion()
                 new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[e].posx + self.boss[e].width / 2 + randint(0,50) -25,self.boss[e].posy + self.boss[e].height / 2 + randint(0,50) -25,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                 self.explosions.append(new_explosion)
             
             #ゲームステータス(状態遷移)を「SCENE_BOSS_EXPLOSION」ボスキャラ爆発中！にする
             self.game_status = SCENE_BOSS_EXPLOSION             
             #ボスの状態遷移フラグステータスを「BOSS_STATUS_EXPLOSION_START」ボス撃破！爆発開始！にしてやる
             self.boss[e].status = BOSS_STATUS_EXPLOSION_START
             #もうボスは爆発開始しちゃうので当たり判定は無くなり無敵状態となる！（爆発して無敵状態になるとは・・・矛盾しておる・・・）
             self.boss[e].invincible = 1
             #スコア加算（あとあといろんなスコアシステム実装する予定だよ）
             self.score += 1
                              
         self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させるため
         pyxel.play(0,2)#変な爆発音を出すのだ～～～☆彡
     
     #各面のボスをBossクラスに定義して出現させる
     def born_boss(self):
          #col_main1_x, col_main1_y, col_main1_w, col_main1_h  = 1*8,1*8,5*8,2*8
          if        self.stage_number == STAGE_MOUNTAIN_REGION:
               new_boss = Boss()
               boss_id = 0
               boss_type = BOSS_BREEZARDIA
               boss_status = BOSS_STATUS_MOVE_LEMNISCATE_CURVE
               parts_number = 0
               main_hp = 150
               parts1_hp,parts2_hp,parts3_hp,parts4_hp = 50,50,50,50
               parts5_hp,parts6_hp,parts7_hp,parts8_hp =   0,  0,  0,  0
               parts9_hp = 0
               parts1_score,parts2_score,parts3_score = 1,1,1
               parts4_score,parts5_score,parts6_score = 1,1,1
               parts7_score,parts8_score,parts9_score = 1,1,1 
               level = LV00
               weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count = WEAPON_READY,4,0,0,0  #上部メイン主砲
               weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count = WEAPON_READY,30,0,0,0 #前部グリーンレーザー砲
               weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count = WEAPON_READY,0,0,0,0
               weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count = WEAPON_READY,0,0,0,0
               weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count = WEAPON_READY,0,0,0,0
               posx,posy = -64,50
               offset_x,offset_y = 0,0
               ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy = 0,0, 0,0, 0,0, 0,0, 0,0, 0,0
               width,height = 14*8,6*8

               col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h =  5 ,3*8,1*8,1*8
               col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h = 7*8,2*8,1*8,1*8
               col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h = 0,0,0,0
               col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h = 0,0,0,0

               col_main1_x, col_main1_y, col_main1_w, col_main1_h  = 1*8  ,1*8+5,     6*8-2,2*8
               col_main2_x, col_main2_y, col_main2_w, col_main2_h  = 2*8  ,4*8  ,     6*8,2*8-2
               col_main3_x, col_main3_y, col_main3_w, col_main3_h  = 7*8  ,3*8  ,   4*8  ,1*8 
               col_main4_x, col_main4_y, col_main4_w, col_main4_h  =   0  ,     0,    0,    0
               col_main5_x, col_main5_y, col_main5_w, col_main5_h  =   0  ,     0,    0,    0
               col_main6_x, col_main6_y, col_main6_w, col_main6_h  =   0  ,     0,    0,    0
               col_main7_x, col_main7_y, col_main7_w, col_main7_h  =   0  ,     0,    0,    0
               col_main8_x, col_main8_y, col_main8_w, col_main8_h  =   0  ,     0,    0,    0

               col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h =10*8 ,5*8,  8,  8
               col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h =9*8-4,5*8,  8,  8
               col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h =5*8-3,  2,  8,  8
               col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h =2*8  ,1*8-6,8,  8
               col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h =    0,  0,  0,  0
               col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h =    0,  0,  0,  0
               col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h =    0,  0,  0,  0
               col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h =    0,  0,  0,  0
               col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h =    0,  0,  0,  0



               main_hp_bar_offset_x,main_hp_bar_offset_y     = 8,-3

               parts1_hp_bar_offset_x,parts1_hp_bar_offset_y = 10*8  ,5*8+10
               parts2_hp_bar_offset_x,parts2_hp_bar_offset_y =  9*8-4,5*8+10
               parts3_hp_bar_offset_x,parts3_hp_bar_offset_y =  5*8-3, -2
               parts4_hp_bar_offset_x,parts4_hp_bar_offset_y =  2*8  ,  0
               parts5_hp_bar_offset_x,parts5_hp_bar_offset_y =      0,  0
               parts6_hp_bar_offset_x,parts6_hp_bar_offset_y =      0,  0
               parts7_hp_bar_offset_x,parts7_hp_bar_offset_y =      0,  0
               parts8_hp_bar_offset_x,parts8_hp_bar_offset_y =      0,  0
               parts9_hp_bar_offset_x,parts9_hp_bar_offset_y =      0,  0

               size = 0
               priority = 0
               attack_method = BOSS_ATTACK_FRONT_5WAY
               direction = 0
               acceleration = 0
               timer = 0
               degree = 0
               radian = 0
               speed = 0
               radius = 0
               flag1,flag2,flag3,flag4 = 0,0,0,0
               count1,count2,count3,count4 = 0,0,0,0
               parts1_flag,parts2_flag,parts3_flag,parts4_flag = 1,1,1,1
               parts5_flag,parts6_flag,parts7_flag,parts8_flag = 0,0,0,0
               parts9_flag = 0
               animation_number1,animation_number2,animation_number3,animation_number4 = 0,0,0,0
               move_index = 0
               obj_time = 0
               obj_totaltime = 0
               invincible = 0
               display_time_main_hp_bar = 0
               display_time_parts1_hp_bar,display_time_parts2_hp_bar = 0,0
               display_time_parts3_hp_bar,display_time_parts4_hp_bar = 0,0
               display_time_parts5_hp_bar,display_time_parts6_hp_bar = 0,0
               display_time_parts7_hp_bar,display_time_parts8_hp_bar = 0,0
               display_time_parts9_hp_bar = 0

               new_boss.update(boss_id,boss_type,boss_status,
                  parts_number,
                  main_hp,
                  parts1_hp,parts2_hp,parts3_hp,parts4_hp,
                  parts5_hp,parts6_hp,parts7_hp,parts8_hp,
                  parts9_hp,
                  parts1_score,parts2_score,parts3_score,
                  parts4_score,parts5_score,parts6_score,
                  parts7_score,parts8_score,parts9_score,
                  level,

                  weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count,
                  weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count,
                  weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count,
                  weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count,
                  weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count,
                  
                  posx,posy,offset_x,offset_y,
                  ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy,
                  width,height,
                  col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h,
                  col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h,
                  col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h,
                  col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h,
                  col_main1_x,  col_main1_y,  col_main1_w,  col_main1_h,
                  col_main2_x,  col_main2_y,  col_main2_w,  col_main2_h,
                  col_main3_x,  col_main3_y,  col_main3_w,  col_main3_h,
                  col_main4_x,  col_main4_y,  col_main4_w,  col_main4_h,
                  col_main5_x,  col_main5_y,  col_main5_w,  col_main5_h,
                  col_main6_x,  col_main6_y,  col_main6_w,  col_main6_h,
                  col_main7_x,  col_main7_y,  col_main7_w,  col_main7_h,
                  col_main8_x,  col_main8_y,  col_main8_w,  col_main8_h,
                  
                  col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h,
                  col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h,
                  col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h,
                  col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h,
                  col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h,
                  col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h,
                  col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h,
                  col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h,
                  col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h,

                  main_hp_bar_offset_x,main_hp_bar_offset_y,
                  parts1_hp_bar_offset_x,parts1_hp_bar_offset_y,
                  parts2_hp_bar_offset_x,parts2_hp_bar_offset_y,
                  parts3_hp_bar_offset_x,parts3_hp_bar_offset_y,
                  parts4_hp_bar_offset_x,parts4_hp_bar_offset_y,
                  parts5_hp_bar_offset_x,parts5_hp_bar_offset_y,
                  parts6_hp_bar_offset_x,parts6_hp_bar_offset_y,
                  parts7_hp_bar_offset_x,parts7_hp_bar_offset_y,
                  parts8_hp_bar_offset_x,parts8_hp_bar_offset_y,
                  parts9_hp_bar_offset_x,parts9_hp_bar_offset_y,

                  size,priority,attack_method,direction,acceleration,timer,degree,radian,speed,radius,
                  flag1,flag2,flag3,flag4,
                  count1,count2,count3,count4,
                  parts1_flag,parts2_flag,parts3_flag,
                  parts4_flag,parts5_flag,parts6_flag,
                  parts7_flag,parts8_flag,parts9_flag,
                  animation_number1,animation_number2,animation_number3,animation_number4,
                  move_index,
                  obj_time,obj_totaltime,
                  invincible,
                  display_time_main_hp_bar,
                  display_time_parts1_hp_bar,display_time_parts2_hp_bar,display_time_parts3_hp_bar,
                  display_time_parts4_hp_bar,display_time_parts5_hp_bar,display_time_parts6_hp_bar,
                  display_time_parts7_hp_bar,display_time_parts8_hp_bar,display_time_parts9_hp_bar
                  )
               self.boss.append(new_boss)       
          
          elif      self.stage_number == STAGE_ADVANCE_BASE:
               new_boss = Boss()
               boss_id = 0
               boss_type = BOSS_FATTY_VALGUARD
               boss_status = BOSS_STATUS_MOVE_COORDINATE_INIT
               parts_number = 0
               main_hp = 400
               parts1_hp,parts2_hp,parts3_hp,parts4_hp = 70,70,70,70
               parts5_hp,parts6_hp,parts7_hp,parts8_hp =   0,  0,  0,  0
               parts9_hp = 0
               parts1_score,parts2_score,parts3_score = 1,1,1
               parts4_score,parts5_score,parts6_score = 1,1,1
               parts7_score,parts8_score,parts9_score = 1,1,1 
               level = LV00
               
               weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count = WEAPON_READY,0,0,0,0
               weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count = WEAPON_READY,0,0,0,0
               weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count = WEAPON_READY,0,0,0,0
               weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count = WEAPON_READY,0,0,0,0
               weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count = WEAPON_READY,0,0,0,0
               
               posx,posy = -64,50
               offset_x,offset_y = 0,0
               ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy = 0,0, 0,0, 0,0, 0,0, 0,0, 0,0
               width,height = 8*8,5*8

               col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h = 1*8,1*8,5*8,2*8
               col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h = 6*8,2*8,1*8,1*8
               col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h = 3*8,3*8,3*8,1*8
               col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h = 2*8,  6,  8,  6

               col_main1_x, col_main1_y, col_main1_w, col_main1_h  = 1*8+4,1*8,5*8-4,2*8
               col_main2_x, col_main2_y, col_main2_w, col_main2_h  = 6*8+4,2*8,1*8-4,1*8
               col_main3_x, col_main3_y, col_main3_w, col_main3_h  = 3*8+4,3*8,3*8-4,1*8 
               col_main4_x, col_main4_y, col_main4_w, col_main4_h  = 2*8+4,  6,  8-4,  6 
               col_main5_x, col_main5_y, col_main5_w, col_main5_h  =   8,  8,  0,  0 
               col_main6_x, col_main6_y, col_main6_w, col_main6_h  =   8,  8,  0,  0
               col_main7_x, col_main7_y, col_main7_w, col_main7_h  =   8,  8,  0,  0 
               col_main8_x, col_main8_y, col_main8_w, col_main8_h  =   8,  8,  0,  0 

               col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h =   0,2*8,2*8,  8
               col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h = 1*8,  0,2*8,  8
               col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h = 1*8,3*8,  8,  8
               col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h = 6*8,2*8,  8,  8
               col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h =   0,  0,  0,  0
               col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h =   0,  0,  0,  0
               col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h =   0,  0,  0,  0
               col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h =   0,  0,  0,  0
               col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h =   0,  0,  0,  0


               main_hp_bar_offset_x  ,main_hp_bar_offset_y   = 8,-2

               parts1_hp_bar_offset_x,parts1_hp_bar_offset_y = 0,24
               parts2_hp_bar_offset_x,parts2_hp_bar_offset_y = 0,4
               parts3_hp_bar_offset_x,parts3_hp_bar_offset_y = 8,32
               parts4_hp_bar_offset_x,parts4_hp_bar_offset_y = 0,0
               parts5_hp_bar_offset_x,parts5_hp_bar_offset_y = 0,0
               parts6_hp_bar_offset_x,parts6_hp_bar_offset_y = 0,0
               parts7_hp_bar_offset_x,parts7_hp_bar_offset_y = 0,0
               parts8_hp_bar_offset_x,parts8_hp_bar_offset_y = 0,0
               parts9_hp_bar_offset_x,parts9_hp_bar_offset_y = 0,0

               size = 0
               priority = 0
               attack_method = 0
               direction = 0
               acceleration = 0
               timer = 0
               degree = 0
               radian = 0
               speed = 0
               radius = 0
               flag1,flag2,flag3,flag4 = 0,0,0,0
               count1,count2,count3,count4 = 0,0,0,0
               parts1_flag,parts2_flag,parts3_flag,parts4_flag = 1,1,1,1
               parts5_flag,parts6_flag,parts7_flag,parts8_flag = 0,0,0,0
               parts9_flag = 0
               animation_number1,animation_number2,animation_number3,animation_number4 = 0,0,0,0
               move_index = 0
               obj_time = 0
               obj_totaltime = 0
               invincible = 0
               display_time_main_hp_bar = 0
               display_time_parts1_hp_bar,display_time_parts2_hp_bar = 0,0
               display_time_parts3_hp_bar,display_time_parts4_hp_bar = 0,0
               display_time_parts5_hp_bar,display_time_parts6_hp_bar = 0,0
               display_time_parts7_hp_bar,display_time_parts8_hp_bar = 0,0
               display_time_parts9_hp_bar = 0
               
               new_boss.update(boss_id,boss_type,boss_status,
                  parts_number,
                  main_hp,
                  parts1_hp,parts2_hp,parts3_hp,
                  parts4_hp,parts5_hp,parts6_hp,
                  parts7_hp,parts8_hp,parts9_hp,
                  parts1_score,parts2_score,parts3_score,
                  parts4_score,parts5_score,parts6_score,
                  parts7_score,parts8_score,parts9_score,
                  level,

                  weapon1_status,weapon1_interval,weapon1_rapid_num,weapon1_cool_down_time,weapon1_omen_count,
                  weapon2_status,weapon2_interval,weapon2_rapid_num,weapon2_cool_down_time,weapon2_omen_count,
                  weapon3_status,weapon3_interval,weapon3_rapid_num,weapon3_cool_down_time,weapon3_omen_count,
                  weapon4_status,weapon4_interval,weapon4_rapid_num,weapon4_cool_down_time,weapon4_omen_count,
                  weapon5_status,weapon5_interval,weapon5_rapid_num,weapon5_cool_down_time,weapon5_omen_count,
                  
                  posx,posy,offset_x,offset_y,
                  ax,ay, bx,by, cx,cy, dx,dy, qx,qy, vx,vy,
                  width,height,
                  col_damage_point1_x,col_damage_point1_y,col_damage_point1_w,col_damage_point1_h,
                  col_damage_point2_x,col_damage_point2_y,co2_damage_point2_w,col_damage_point2_h,
                  col_damage_point3_x,col_damage_point3_y,co3_damage_point3_w,col_damage_point3_h,
                  col_damage_point4_x,col_damage_point4_y,co4_damage_point4_w,col_damage_point4_h,
                  col_main1_x,  col_main1_y,  col_main1_w,  col_main1_h,
                  col_main2_x,  col_main2_y,  col_main2_w,  col_main2_h,
                  col_main3_x,  col_main3_y,  col_main3_w,  col_main3_h,
                  col_main4_x,  col_main4_y,  col_main4_w,  col_main4_h,
                  col_main5_x,  col_main5_y,  col_main5_w,  col_main5_h,
                  col_main6_x,  col_main6_y,  col_main6_w,  col_main6_h,
                  col_main7_x,  col_main7_y,  col_main7_w,  col_main7_h,
                  col_main8_x,  col_main8_y,  col_main8_w,  col_main8_h,
                  col_parts1_x,col_parts1_y,col_parts1_w,col_parts1_h,
                  col_parts2_x,col_parts2_y,col_parts2_w,col_parts2_h,
                  col_parts3_x,col_parts3_y,col_parts3_w,col_parts3_h,
                  col_parts4_x,col_parts4_y,col_parts4_w,col_parts4_h,
                  col_parts5_x,col_parts5_y,col_parts5_w,col_parts5_h,
                  col_parts6_x,col_parts6_y,col_parts6_w,col_parts6_h,
                  col_parts7_x,col_parts7_y,col_parts7_w,col_parts7_h,
                  col_parts8_x,col_parts8_y,col_parts8_w,col_parts8_h,
                  col_parts9_x,col_parts9_y,col_parts9_w,col_parts9_h,
                  
                  main_hp_bar_offset_x,main_hp_bar_offset_y,
                  parts1_hp_bar_offset_x,parts1_hp_bar_offset_y,
                  parts2_hp_bar_offset_x,parts2_hp_bar_offset_y,
                  parts3_hp_bar_offset_x,parts3_hp_bar_offset_y,
                  parts4_hp_bar_offset_x,parts4_hp_bar_offset_y,
                  parts5_hp_bar_offset_x,parts5_hp_bar_offset_y,
                  parts6_hp_bar_offset_x,parts6_hp_bar_offset_y,
                  parts7_hp_bar_offset_x,parts7_hp_bar_offset_y,
                  parts8_hp_bar_offset_x,parts8_hp_bar_offset_y,
                  parts9_hp_bar_offset_x,parts9_hp_bar_offset_y,

                  size,priority,attack_method,direction,acceleration,timer,degree,radian,speed,radius,
                  flag1,flag2,flag3,flag4,
                  count1,count2,count3,count4,
                  parts1_flag,parts2_flag,parts3_flag,
                  parts4_flag,parts5_flag,parts6_flag,
                  parts7_flag,parts8_flag,parts9_flag,
                  animation_number1,animation_number2,animation_number3,animation_number4,
                  move_index,
                  obj_time,obj_totaltime,
                  invincible,
                  display_time_main_hp_bar,
                  display_time_parts1_hp_bar,display_time_parts2_hp_bar,display_time_parts3_hp_bar,
                  display_time_parts4_hp_bar,display_time_parts5_hp_bar,display_time_parts6_hp_bar,
                  display_time_parts7_hp_bar,display_time_parts8_hp_bar,display_time_parts9_hp_bar
                  )
               self.boss.append(new_boss)
                    
     #ボスをベジェ曲線で移動させるために必要な座標をリストから取得する関数
     def boss_get_bezier_curve_coordinate(self,i):                         
          self.boss[i].ax             = self.boss_move_data1[self.boss[i].move_index][0]#リストから新たな移動元座標を登録する
          self.boss[i].ay             = self.boss_move_data1[self.boss[i].move_index][1]
          self.boss[i].dx             = self.boss_move_data1[self.boss[i].move_index][2]#リストから新たな移動先座標を登録する
          self.boss[i].dy             = self.boss_move_data1[self.boss[i].move_index][3]
          self.boss[i].qx             = self.boss_move_data1[self.boss[i].move_index][4]#リストから2次ベジェ曲線用の制御点座標を登録する
          self.boss[i].qy             = self.boss_move_data1[self.boss[i].move_index][5]

          self.boss[i].obj_totaltime  = self.boss_move_data1[self.boss[i].move_index][6]#リストから移動に掛けるトータルタイムを取得し登録する

          self.boss[i].speed          = self.boss_move_data1[self.boss[i].move_index][7]#リストから移動スピードを取得し登録する
          self.boss[i].acceleration   = self.boss_move_data1[self.boss[i].move_index][8]#リストから加速度を取得し登録する

          self.boss[i].attack_method  = self.boss_move_data1[self.boss[i].move_index][9]#リストから攻撃方法を取得し登録する

     #ボスの耐久力バーの表示（ボスの付近にＨＰバーを描画する）
     def display_boss_hp_bar(self,x,y,hp):
          pyxel.rectb(x-1,y-1, 32+2,3, self.blinking_color[pyxel.frame_count // 8 % 10]) #点滅四角線描画
          pyxel.line(x,y, x + hp,y, 8) #赤色の耐久力バーの表示
     
     #ボスの各部位耐久力バーの表示（破壊可能部位の付近にＨＰバーを描画する）短いタイプ横16ドット
     def display_boss_hp_short_bar(self,x,y,hp):
          pyxel.line(x,y + 1, x + 12,y + 1, self.red_flash_color[pyxel.frame_count // 8 % 10]) #点滅線描画
          pyxel.line(x,y    , x + hp,y    ,8) #赤色の耐久力バーの表示

     #ボスの各部位耐久力バーの表示（破壊可能部位の付近にＨＰバーを描画する）更に短いタイプ横8ドット
     def display_boss_hp_short2_bar(self,x,y,hp):
          pyxel.line(x,y + 1, x + 4,y + 1, self.red_flash_color[pyxel.frame_count // 8 % 10]) #点滅線描画
          pyxel.line(x,y    , x + hp,y    ,8) #赤色の耐久力バーの表示
     
     #スコア加算処理
     def add_score(self,point):
          self.score += int(point * self.score_magnification) #スコアをpoint*スコア倍率分加算する(整数値で)

     #ラスタースクロール用のデータの初期化＆生成
     def create_raster_scroll_data(self):
          #1面STAGE_MOUNTAIN_REGIONのラスタースクロール用の設定値の初期化
          new_raster_scroll = Raster_scroll()
          for i in range(24-1):
               new_raster_scroll = Raster_scroll()
               new_raster_scroll.update(0,RASTER_NORMAL,1,RASTER_SCROLL_ON,  i,23,   0,0,    0,0,    IMG1,    96,112+i,   160,1,    -0.1 -(0.03 * i) ,15,   0,0,0)
               self.raster_scroll.append(new_raster_scroll)  #湖面のラスタースクロール用の横ライン（縦24ライン分）を育成する
         
          for i in range(24-1):
               new_raster_scroll = Raster_scroll()
               new_raster_scroll.update(1,RASTER_NORMAL,1,RASTER_SCROLL_ON,  i,23,  0,0,  0,-80,  IMG1,   96,112+i,   160,1,    -0.05 -(0.01 * i) ,15,    0,0,0)
               self.raster_scroll.append(new_raster_scroll)  #成層圏と大気圏の境目のラスタースクロール用の横ライン（縦24ライン分）を育成する（湖面と同じグラフイックだけど・・）

          for i in range(40-1):
               new_raster_scroll = Raster_scroll()
               new_raster_scroll.update(2,RASTER_WAVE,0,RASTER_SCROLL_ON,    i,39,  0,0,   0,-38,  IMG1,   144,72+i,   14*8,1,    -0.35,13,    0,0.02,(i-20)*0.4)
               self.raster_scroll.append(new_raster_scroll)  #雲ウェーブラスタースクロール用の横ライン(縦40ライン分)を育成する

     #ラスタースクロールの表示のon/off(search_id,flag)
     def disp_control_raster_scroll(self,id,flag):
          raster_scroll_count = len(self.raster_scroll)
          for i in range(raster_scroll_count): #ラスタースクロールクラスに登録されたインスタンスのdisplayを調べていきます
               if self.raster_scroll[i].scroll_id == id: #scroll_idと調べるidが一致したのなら
                    self.raster_scroll[i].display = flag #flag(0=表示しない 1=表示する)を書き込む
     
     ################################################################ボツ関数群・・・・・・(涙)##########################################################
     #外積を計算する関数 self.cpに結果が入る(バグありなので使えないっぽい・・・この関数)
     def cross_product_calc_function(self,ax,ay,bx,by,cx,cy):
          self.cp = (ax - cx) * (by - cy) - (bx - cx) * (ay - cy)
          return()
     #三角形と点の当たり判定を行う関数(ax,ay)(bx,by)(cx,cy)=三角形の各頂点の座標,px,py=三角形の中か外にあるかどうかを判定するポイント用座標)
     #(バグあるので使えないっいぽい。。。この関数・・・ボツダナ)
     def point_in_triangle(self,px,py,ax,ay,bx,by,cx,cy):
         #
         #
         #C++だとこんな感じ
         #
         #外積を計算して符号だけ返す
         #float sign (fPoint a, fPoint b, fPoint c)
         #{
         #    return (a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y);
         #}
         #3辺のベクトルと判定ポイントと頂点結んだベクトルの外積を求め全ての符号が同じならbool値でtrue,違っていたらfalseを返す 
         #bool PointInTriangle (fPoint p, fPoint a, fPoint b, fPoint c)
         #{
         #    float d1,d2,d3
         #    bool has_negative, has_positive;
         # 
         #    d1 = sign(p, a, b);
         #    d2 = sign(p, b, c);
         #    d3 = sign(p, c, a);
         #    has_negative = (d1 < 0) || (d2 < 0) || (d3 < 0);
         #    has_positive = (d1 > 0) || (d2 > 0) || (d3 > 0);
         # 
         #    return !(has_negative && has_positive);
         #}
          
          self.cp = 0                         #外積計算用変数を初期化
          self.point_inside_triangle_flag = 0 #判別用のフラグを初期化 
          
          self.cross_product_calc_function(px,py,ax,ay,bx,by)
          d1 = self.cp
          self.cross_product_calc_function(px,py,bx,by,cx,cy)
          d2 = self.cp
          self.cross_product_calc_function(px,py,cx,cy,ax,ay)
          d3 = self.cp
          if (d1 < 0 and d2 < 0 and d3 < 0) or (d1 > 0 and d2 > 0 and d3 > 0):#d1~d3が全てマイナスの数値 または d1~d3が全てプラスの数値だったら

               self.point_inside_triangle_flag = 1 #三角形の内側に点があった！のでフラグをon
          else:
               self.point_inside_triangle_flag = 0 #三角形の外側だった・・・・のでフラグをoff   
     #自機を追尾してくる敵キャラ用のvx,vyの増分とdir（方向）を求める関数   まだ未完成
     
     #!###############################################################################################################################
     #!###############################################################################################################################
     #!update関数から呼び出される関数群 ################################################################################################
     #!###############################################################################################################################
     #!###############################################################################################################################
     #IPLの更新#######################################
     def update_ipl(self):
          self.display_ipl_time -= 1     #IPLメッセージを表示する時間カウンターを1減らす
          if self.display_ipl_time <= 0: #カウンターが0以下になったら・・・
               self.game_status = SCENE_TITLE_INIT #ゲームステータスを「SCENE_TITLE_INIT(タイトル表示に必要な変数を初期化)」にする

          if (pyxel.frame_count % 10) == 0:
               if len(self.ipl_mes1) > self.ipl_mes_write_line_num: #まだ書き込むべき文字列があるのなら・・・
                    text_mes = str(self.ipl_mes1[self.ipl_mes_write_line_num][0])
                    text_col =     self.ipl_mes1[self.ipl_mes_write_line_num][1]
                    self.text_screen.append([text_mes,text_col]) #文字列群をテキストスクリーンのリストに追加する
                    self.ipl_mes_write_line_num +=1  #スクリーンに表示したIPLメッセージデータの行数カウンタを1インクリメント
     
     #タイトル表示に必要な変数を設定＆初期化する##############
     def update_title_init(self):
          #タイトル関連の変数を初期化
          
          # self.display_title_time = 204            #タイトルを表示する時間
          # self.title_oscillation_count = 200       #タイトルグラフイックの振れ幅カウンター
          # self.title_slash_in_count =    100       #タイトルグラフイックが下から切り込んで競りあがってくる時に使うカウンター
          
          self.display_title_time        = 10       #タイトルを表示する時間
          self.title_oscillation_count = 10         #タイトルグラフイックの振れ幅カウンター
          self.title_slash_in_count =    10         #タイトルグラフイックが下から切り込んで競りあがってくる時に使うカウンター
          
          self.stars = []                           #タイトル表示時も背景の星を流したいのでリストをここで初期化してやります
          self.star_scroll_speed = 1                #背景の流れる星のスクロールスピード 1=通常スピード 0.5なら半分のスピードとなります
          self.window = []                          #タイトル表示時もメッセージウィンドウを使いたいのでリストをここで初期化してあげます

          self.bg_cls_color = 0           #BGをCLS(クリアスクリーン)するときの色の指定(通常は0=黒色です)ゲーム時に初期値から変更されることがあるのでここで初期化する

          # セレクトカーソル関連の変数宣言   タイトル画面でセレクトカーソルを使いたいのでここで変数などを宣言＆初期化します
          self.cursor_show = False          #セレクトカーソルを表示するかしないかのフラグ用
          self.cursor_x = 0                 #セレクトカーソルのx座標
          self.cursor_y = 0                 #セレクトカーソルのy座標
          self.cursor_item = 0              #いま指し示しているアイテムナンバー
          self.cursor_page = 0              #いま指し示しているページナンバー
          self.cursor_color = 0             #セレクトカーソルの色
          self.cursor_decision_item = -1    #ボタンが押されて「決定」されたアイテムのナンバー -1は未決定 ここをチェックしてどのアイテムが選択されたのか判断する
          self.cursor_max_item = 0          #最大項目数 5の場合(0~4)の5項目分カーソルが移動することになります 3だったら(0~2)って感じで
          self.cursor_menu_layer = 0        #現在選択中のメニューの階層の数値が入ります
          self.cursor_pre_decision_item = 0 #前の階層で選択したアイテムのナンバーを入れます
                                            #選択してcursor_decision_itemに入ったアイテムナンバーをcursor_pre_decision_itemに入れて次の階層に潜るって手法かな？
          
          self.stage_number = STAGE_MOUNTAIN_REGION  #最初に出撃するステージ   タイトルメニューでステージを選択して変化させるのでここで初期化します
          self.stage_loop   = 1                      #ループ数(ステージ周回数) タイトルメニューで周回数を選択して変化させるのでここで初期化します
          self.game_difficulty = GAME_NORMAL         #難易度                  タイトルメニューで難易度を選択して変化させるのでここで初期化します
          self.game_status = SCENE_TITLE             #ゲームステータスを「SCENE_TITLE」にしてタイトル表示を開始する
     
     #タイトルの更新#######################################
     def update_title(self):
          self.display_title_time -= 1          #タイトルを表示する時間カウンターを1減らす
          if self.display_title_time <= 0:      #カウンターが0以下になったら・・・
               self.display_title_time = 0      #強制的に0の状態にする

          self.title_oscillation_count -= 1     #タイトルグラフイックの振れ幅カウンターを1減らす
          if self.title_oscillation_count < 0:  #カウンターが0以下になったら・・・
               self.title_oscillation_count = 0 #強制的に0の状態にする

          self.title_slash_in_count -= 1        #タイトルグラフイックが下から切り込んで競りあがってくる時に使うカウンターを1減らす
          if self.title_slash_in_count < 0:     #カウンターが0以下になったら・・・
               self.title_slash_in_count = 0    #強制的に0の状態にする
          
          #全てのカウンター類が0になったらゲームメニューウィンドウを育成する
          if self.title_oscillation_count == 0 and self.title_slash_in_count == 0 and self.display_title_time == 0:
               new_window = Window()
               new_window.update(0,0,2,WINDOW_OPEN,\
               "MENU",DISP_CENTER,\
               "GAME START",DISP_CENTER,0,7,\
               "SELECT STAGE",DISP_CENTER,0,3,\
               "LOOP NUMBER",DISP_CENTER,0,3,\
               "BOSS MODE",DISP_CENTER,0,7,\
               "HITBOX",DISP_CENTER,0,7,\
               "DIFFICULTY",DISP_CENTER,0,7,\
               "",DISP_CENTER,0,7,\
               44,52,   0,0,  8*8,7*8,   2,1, 1,1,   0,0,    0,0)
               self.window.append(new_window)                           #「SELECT MENU」を育成する
               self.cursor_show = True                                  #選択カーソル表示をonにする
               self.cursor_x = 46                                       #セレクトカーソルの座標を設定します
               self.cursor_y = 64
               self.cursor_item = 0                                     #いま指示しているアイテムナンバーは0の「YES」
               self.cursor_decision_item = -1                           #まだボタンも押されておらず未決定状態なのでdecision_itemは-1
               self.cursor_max_item = 5                                 #最大項目数は「GAME START」「SELECT STAGE」「SELECT LOOP NUMBER」「BOSS MODE」「HITBOX」「DIFFICULTY」の6項目なので 6-1=5を代入
               self.cursor_menu_layer = 0                               #メニューの階層は最初は0にします
               self.game_status = SCENE_TITLE_MENU_SELECT #ゲームステータスを「TITLE_MENU_SELECT」(タイトルでメニューを選択中)」にする
                    
     #タイトルメニューの選択中の更新#####################################
     def update_title_menu_select(self):
          if self.cursor_menu_layer == 0: #メニューが0階層目の選択分岐
               if   self.cursor_decision_item == 0:               #GAME STARTが押されたら
                    self.cursor_show = False                      #セレクトカーソルの表示をoffにする
                    self.game_status = SCENE_GAME_START_INIT      #ゲームステータスを「GAME_START_INIT」にしてゲーム全体を初期化＆リスタートする
               
               elif self.cursor_decision_item == 1:               #SELECT STAGEが押されたら
                    self.cursor_pre_x = self.cursor_x                         #新しいウィンドウを開く前に現在のカーソル関連の変数を記憶しておきます
                    self.cursor_pre_y = self.cursor_y                         #
                    self.cursor_pre_item = self.cursor_item                   #
                    self.cursor_pre_decision_item = self.cursor_decision_item #
                    self.cursor_pre_max_item = self.cursor_max_item           # 


                    new_window = Window()
                    new_window.update(0,0,1,WINDOW_OPEN,\
                    "",DISP_CENTER,\
                    "1",DISP_CENTER,0,7,\
                    "2",DISP_CENTER,0,7,\
                    "3",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    90,60,   0,0,  2*8,5*8,   2,2, 1,1,   0,0,    0,0)
                    self.window.append(new_window)                           #「STAGE」を育成する
                    self.cursor_show = True                                  #選択カーソル表示をonにする
                    self.cursor_x = 90                                       #セレクトカーソルの座標を設定します
                    self.cursor_y = 72
                    self.cursor_item = 0                                     #いま指示しているアイテムナンバーは0の「1」
                    self.cursor_decision_item = -1                           #まだボタンも押されておらず未決定状態なのでdecision_itemは-1
                    self.cursor_max_item = 2                                 #最大項目数は3項目なので 3-1=2を代入
                    
                    self.cursor_menu_layer = 1                               #メニューの階層が増えたので0から1にします
               elif self.cursor_decision_item == 2:               #SELECT LOOP NUMBERが押されたら
                    self.cursor_pre_x = self.cursor_x                         #新しいウィンドウを開く前に現在のカーソル関連の変数を記憶しておきます
                    self.cursor_pre_y = self.cursor_y                         #
                    self.cursor_pre_item = self.cursor_item                   #
                    self.cursor_pre_decision_item = self.cursor_decision_item #
                    self.cursor_pre_max_item = self.cursor_max_item           # 


                    new_window = Window()
                    new_window.update(0,0,0,WINDOW_OPEN,\
                    "",DISP_CENTER,\
                    "1",DISP_CENTER,0,7,\
                    "2",DISP_CENTER,0,7,\
                    "3",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    90+22,60+6,   0,0,  2*8,5*8,   2,2, 1,1,   0,0,    0,0)
                    self.window.append(new_window)                           #「LOOP NUMBER」を育成する
                    self.cursor_show = True                                  #選択カーソル表示をonにする
                    self.cursor_x = 90+22                                       #セレクトカーソルの座標を設定します
                    self.cursor_y = 72+6
                    self.cursor_item = 0                                     #いま指示しているアイテムナンバーは0の「1」
                    self.cursor_decision_item = -1                           #まだボタンも押されておらず未決定状態なのでdecision_itemは-1
                    self.cursor_max_item = 2                                 #最大項目数は3項目なので 3-1=2を代入
                    
                    self.cursor_menu_layer = 1                               #メニューの階層が増えたので0から1にします
               elif self.cursor_decision_item == 3:               #BOSS MODEが押されたら
                    self.cursor_pre_x = self.cursor_x                         #新しいウィンドウを開く前に現在のカーソル関連の変数を記憶しておきます
                    self.cursor_pre_y = self.cursor_y                         #
                    self.cursor_pre_item = self.cursor_item                   #
                    self.cursor_pre_decision_item = self.cursor_decision_item #
                    self.cursor_pre_max_item = self.cursor_max_item           # 


                    new_window = Window()
                    new_window.update(0,0,0,WINDOW_OPEN,\
                    "ON",DISP_CENTER,\
                    "OFF",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    96+2,60,   0,0,  2*8+6,2*8,   2,1, 1,1,   0,0,    0,0)
                    self.window.append(new_window)                           #「BOSS MODE ON/OFF」を育成する
                    self.cursor_show = True                                  #選択カーソル表示をonにする
                    self.cursor_x = 96+2                                       #セレクトカーソルの座標を設定します
                    self.cursor_y = 72-8
                    self.cursor_item = 0                                     #いま指示しているアイテムナンバーは0の「1」
                    self.cursor_decision_item = -1                           #まだボタンも押されておらず未決定状態なのでdecision_itemは-1
                    self.cursor_max_item = 1                                 #最大項目数は2項目なので 2-1=1を代入
                    
                    self.cursor_menu_layer = 1                               #メニューの階層が増えたので0から1にします
               elif self.cursor_decision_item == 4:               #HITBOXが押されたら
                    self.cursor_pre_x = self.cursor_x                         #新しいウィンドウを開く前に現在のカーソル関連の変数を記憶しておきます
                    self.cursor_pre_y = self.cursor_y                         #
                    self.cursor_pre_item = self.cursor_item                   #
                    self.cursor_pre_decision_item = self.cursor_decision_item #
                    self.cursor_pre_max_item = self.cursor_max_item           # 


                    new_window = Window()
                    new_window.update(0,0,0,WINDOW_OPEN,\
                    "ON",DISP_CENTER,\
                    "OFF",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    96+2,60,   0,0,  2*8+6,2*8,   2,1, 1,1,   0,0,    0,0)
                    self.window.append(new_window)                           #「HITBOX ON/OFF」を育成する
                    self.cursor_show = True                                  #選択カーソル表示をonにする
                    self.cursor_x = 96+2                                       #セレクトカーソルの座標を設定します
                    self.cursor_y = 72-8
                    self.cursor_item = 0                                     #いま指示しているアイテムナンバーは0の「1」
                    self.cursor_decision_item = -1                           #まだボタンも押されておらず未決定状態なのでdecision_itemは-1
                    self.cursor_max_item = 1                                 #最大項目数は2項目なので 2-1=1を代入
                    
                    self.cursor_menu_layer = 1                               #メニューの階層が増えたので0から1にします
               elif self.cursor_decision_item == 5:               #DIFFICULTYが押されたら
                    self.cursor_pre_x = self.cursor_x                         #新しいウィンドウを開く前に現在のカーソル関連の変数を記憶しておきます
                    self.cursor_pre_y = self.cursor_y                         #
                    self.cursor_pre_item = self.cursor_item                   #
                    self.cursor_pre_decision_item = self.cursor_decision_item #
                    self.cursor_pre_max_item = self.cursor_max_item           # 


                    new_window = Window()
                    new_window.update(0,0,1,WINDOW_OPEN,\
                    "VERY EASY",DISP_LEFT_ALIGN,\
                    "EASY",DISP_LEFT_ALIGN,0,7,\
                    "NORMAL",DISP_LEFT_ALIGN,0,7,\
                    "HARD",DISP_LEFT_ALIGN,0,7,\
                    "VERY HARD",DISP_LEFT_ALIGN,0,7,\
                    "INSAME",DISP_LEFT_ALIGN,0,7,\
                    "",DISP_LEFT_ALIGN,0,7,\
                    "",DISP_LEFT_ALIGN,0,7,\
                    93,52,   0,0,  6*8,6*8,   3,3, 1,1,   0,0,    0,0)
                    self.window.append(new_window)                           #「DIFFICULTY」を育成する
                    self.cursor_show = True                                  #選択カーソル表示をonにする
                    self.cursor_x = 96                                       #セレクトカーソルの座標を設定します
                    self.cursor_y = 72
                    self.cursor_item = 2                                     #いま指示しているアイテムナンバーは2の「NORMAL」
                    self.cursor_decision_item = -1                           #まだボタンも押されておらず未決定状態なのでdecision_itemは-1
                    self.cursor_max_item = 5                                 #最大項目数は6項目なので 6-1=5を代入
                    
                    self.cursor_menu_layer = 1                               #メニューの階層が増えたので0から1にします
           
          
          elif self.cursor_menu_layer == 1: #メニューが1階層目の選択分岐
               if self.cursor_pre_decision_item == 1 and self.cursor_decision_item == 0:
                    #「SELECT STAGE」→「1」
                    self.stage_number   = 1  #ステージナンバー1
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0       #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 1 and self.cursor_decision_item == 1:
                    #「SELECT STAGE」→「2」
                    self.stage_number   = 2  #ステージナンバー2
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0   #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 1 and self.cursor_decision_item == 2:
                    #「SELECT STAGE」→「3」
                    self.stage_number   = 3  #ステージナンバー3
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0   #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               

               elif self.cursor_pre_decision_item == 2 and self.cursor_decision_item == 0:
                    #「SELECT LOOP NUMBER」→「1」
                    self.stage_loop = 1  #ループ数に1週目を代入
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0       #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 2 and self.cursor_decision_item == 1:
                    #「SELECT LOOP NUMBER」→「2」
                    self.stage_loop = 2  #ループ数に2週目を代入
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0       #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 2 and self.cursor_decision_item == 2:
                    #「SELECT LOOP NUMBER」→「3」
                    self.stage_loop = 3  #ループ数に3週目を代入
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0       #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               
               elif self.cursor_pre_decision_item == 3 and self.cursor_decision_item == 0:
                    #「BOSS MODE」→「ON」
                    self.boss_test_mode = 1  #ボステストモードをon
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0       #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 3 and self.cursor_decision_item == 1:
                    #「BOSS MODE」→「OFF」
                    self.boss_test_mode = 0  #ボステストモードをoff
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0       #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 4 and self.cursor_decision_item == 0:
                    #「HITBOX」→「ON」
                    self.boss_collision_rect_display_flag = 1  #ボス当たり判定表示をon
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0       #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 4 and self.cursor_decision_item == 1:
                    #「HITBOX」→「OFF」
                    self.boss_collision_rect_display_flag = 0  #ボス当たり判定表示をoff
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0       #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               
               elif self.cursor_pre_decision_item == 5 and self.cursor_decision_item == 0:
                    #「DIFFICULTY」→「VERY_EASY」
                    self.game_difficulty = GAME_VERY_EASY
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0       #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 5 and self.cursor_decision_item == 1:
                    #「DIFFICULTY」→「EASY」
                    self.game_difficulty = GAME_EASY
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0   #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 5 and self.cursor_decision_item == 2:
                    #「DIFFICULTY」→「NORMAL」
                    self.game_difficulty = GAME_NORMAL
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0   #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 5 and self.cursor_decision_item == 3:
                    #「DIFFICULTY」→「HARD」
                    self.game_difficulty = GAME_HARD
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0   #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 5 and self.cursor_decision_item == 4:
                    #「DIFFICULTY」→「VERY_HARD」
                    self.game_difficulty = GAME_VERY_HARD
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0   #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
               elif self.cursor_pre_decision_item == 5 and self.cursor_decision_item == 5:
                    #「DIFFICULTY」→「INSAME」
                    self.game_difficulty = GAME_INSAME
                    window_count = len(self.window)
                    del self.window[window_count - 1] #最後に開かれたウィンドウを消去する(現在のウィンドウ消去）
                    self.cursor_menu_layer =  0   #階層を0にする
                    self.cursor_x = self.cursor_pre_x                         #カーソルの変数を前回の物に戻してやります
                    self.cursor_y = self.cursor_pre_y                         #
                    self.cursor_item = self.cursor_pre_item                   #
                    self.cursor_max_item = self.cursor_pre_max_item           #
                    self.cursor_decision_item = -1
                    self.cursor_pre_decision_item = -1
     #!ゲームスタート時の初期化#########################################
     def update_game_start_init(self):
         self.score = 0                 #スコア
         self.my_shield = 5            #自機のシールド耐久値
         self.my_speed = 1              #自機の初期スピード
         
         self.my_x = 24    #自機のx座標の初期値
         self.my_y = 50    #自機のy座標の初期値
         self.my_vx = 1    #自機のx方向の移動量
         self.my_vy = 0    #自機のy方向の移動量
         
         self.run_away_bullet_probability = 10 #敵が過ぎ去っていくときに弾を出す確率

     
         self.game_playing_flag = 1      #ゲームプレイフラグを「ゲームプレイ中」にする
         
         self.select_shot_id = 0         #現在使用しているショットのIDナンバー(ナンバーの詳細はshot_levelを参照するのです！)
         
         self.shot_exp = 0               #自機ショットの経験値 パワーアップアイテムを取ることにより経験値がたまりショットのレベルが上がっていく
         self.shot_level = 0             #自機ショットのレベル  0~3バルカンショット  4=レーザー 5=ツインレーザー 6=3WAYレーザー
                                         #7=ウェーブカッターLv1  8=ウェーブカッターLv2  9=ウェーブカッターLv3   10=ウェーブカッターLv4
         self.shot_speed_magnification=1 #自機ショットのスピードに掛ける倍率(vxに掛け合わせる)  
         self.shot_rapid_of_fire = 1     #自機ショットの連射数  初期値は1連射
         
         self.missile_exp = 0               #自機ミサイルの経験値 パワーアップアイテムを取ることにより経験値が溜まりミサイルのレベルが上がっていく
         self.missile_level = 0             #自機ミサイルのレベル  0~2 0=右下のみ  1=右下左上前方2方向  2=右下右上  左下左上4方向
         self.missile_speed_magnification=1 #自機ミサイルのスピードに掛ける倍率(vxに掛け合わせる)
         self.missile_rapid_of_fire = 1     #自機ミサイルの連射数  初期値は1連射
         
         self.select_sub_weapon_id = -1       #現在使用しているサブウェポンのIDナンバー -1だと何も所有していない状態
         self.sub_weapon_list = [0,0,0,0,0]   #どのサブウェポンを所持しているかのリスト(インデックスオフセット値)
                                              #0=テイルショット 1=ペネトレートロケット 2=サーチレーザー 3=ホーミングミサイル 4=ショックバンバー
         self.star_scroll_speed = 1           #背景の流れる星のスクロールスピード 1=通常スピード 0.5なら半分のスピードとなります
         self.pow_item_bounce_num = 6         #パワーアップアイテムが画面の左端で跳ね返って戻ってくる回数
                                              #初期値は6でアップグレードすると増えていくです

         self.playtime_frame_counter    = 0 #プレイ時間(フレームのカウンター) 60フレームで＝1秒         
         self.one_game_playtime_seconds = 0 #1プレイでのゲームプレイ時間(秒単位)
         
         self.game_play_count = 0 #ゲーム開始から経過したフレームカウント数(1フレームは60分の1秒)1面～今プレイしている面までのトータルフレームカウント数です

         self.claw_type = 0               # クローのタイプ 
                                          # 0=ローリングクロー 1=トレースクロー 2=フィックスクロー 3=リバースクロー
         self.claw_number = 0             # クローの装備数 0=装備無し 1=1機 2=2機 3=3機 4=4機
         self.claw_difference = 360       # クロ―同士の角度間隔 1機=360 2機=180度 3機=120度 4機=90度
         self.trace_claw_index = 0        #トレースクロー（オプション）時のトレース用配列のインデックス値
         self.trace_claw_distance = 12    #トレースクロー同士の間隔
         self.fix_claw_magnification = 1  #フイックスクロー同士の間隔の倍率 0.5~2まで0.1刻み
         self.reverse_claw_svx = 1        #リバースクロー用の攻撃方向ベクトル(x軸)
         self.reverse_claw_svy = 0        #リバースクロー用の攻撃方向ベクトル(y軸)
         self.claw_shot_speed = 2         #クローショットのスピード（初期値は移動量２ドット）
         
         self.ls_shield_hp = 0            #L'sシールドの耐久力 0=シールド装備していない 1以上はシールド耐久値を示す

         self.claw = []                   #クローのリスト クローのリストはステージスタート時に初期化してしまうと次のステージに進んだときクローが消滅してしまうのでgame_start_initで初期化します
         #難易度に応じた数値をリストから取得する
         self.start_bonus_shot    = self.game_difficulty_list[self.game_difficulty][LIST_START_BONUS_SHOT]    #初期ショットボーナスをリストを参照し難易度に合わせて取得、変数に代入する
         self.start_bonus_missile = self.game_difficulty_list[self.game_difficulty][LIST_START_BONUS_MISSILE] #初期ミサイルボーナスをリストを参照し難易度に合わせて取得、変数に代入する
         self.start_bonus_shield  = self.game_difficulty_list[self.game_difficulty][LIST_START_BONUS_SHIELD]  #初期シールドボーナスをリストを参照し難易度に合わせて取得、変数に代入する
         self.start_claw          = self.game_difficulty_list[self.game_difficulty][LIST_START_CLAW]          #初期クローボーナスをリストを参照し難易度に合わせて取得、変数に代入する
         self.repair_shield       = self.game_difficulty_list[self.game_difficulty][LIST_REPAIR_SHIELD]       #ステージクリア後に回復するシールド値をリストを参照し難易度に合わせて取得、変数に代入する
         self.return_bullet       = self.game_difficulty_list[self.game_difficulty][LIST_RETURN_BULLET]       #撃ち返し弾の有無とありの時の種類をリストを参照し難易度に合わせて取得、変数に代入する
         self.score_magnification = self.game_difficulty_list[self.game_difficulty][LIST_SCORE_MAGNIFICATION] #スコア倍率をリストを参照し難易度に合わせて取得、変数に代入する
         self.rank_exponential    = self.game_difficulty_list[self.game_difficulty][LIST_RANK_EXPONENTIAL]    #ランク上昇指数をリストを参照し難易度に合わせて取得、変数に代入する
         self.rank                = self.game_difficulty_list[self.game_difficulty][LIST_START_RANK]          #ゲームスタート時のランク数をリストを参照し難易度に合わせて取得、変数に代入する
         
         #ランクに応じた数値をリストから取得する
         self.enemy_speed_mag           = self.game_rank_data_list[self.rank][LIST_RANK_E_SPEED_MAG]               #敵スピード倍率をリストを参照してランク数で取得、変数に代入する
         self.enemy_bullet_speed_mag    = self.game_rank_data_list[self.rank][LIST_RANK_BULLET_SPEED_MAG]          #敵狙い撃ち弾スピード倍率をリストを参照してランク数で取得、変数に代入する
         self.return_bullet_probability = self.game_rank_data_list[self.rank][LIST_RANK_RETURN_BULLET_PROBABILITY] #敵撃ち返し弾発射確率をリストを参照してランク数で取得、変数に代入する
         self.enemy_hp_mag              = self.game_rank_data_list[self.rank][LIST_RANK_E_HP_MAG]                  #敵耐久力倍率をリストを参照してランク数で取得、変数に代入する
         
         
         self.shot_table_list = self.j_python_shot_table_list       #とりあえずショットテーブルリストは初期機体のj_pythonのものをコピーして使用します
                                                                    #将来的には選択した機体で色々な機体のリストがコピーされるはず
         self.missile_table_list = self.j_python_missile_table_list #とりあえずミサイルテーブルリストは初期機体のj_pythonのものをコピーして使用します
                                                                    #将来的には選択した機体で色々な機体のリストがコピーされるはず・・・ほんとかなぁ？
     
         #ゲームスタート時のいろいろなボーナスの処理
         self.shot_exp  += self.start_bonus_shot
         self.missile_exp += self.start_bonus_missile
         self.my_shield += self.start_bonus_shield
         self.level_up_my_shot()      #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
         self.level_up_my_missile()   #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
         if self.start_claw == ONE_CLAW: #ゲーム開始時クローの数が1の時は
             self.update_append_claw() #クロー追加ボーナスの数値の回数分、追加関数を呼び出す
         elif self.start_claw == TWO_CLAW: #ゲーム開始時クローの数が2の時は
             self.update_append_claw() #2回呼び出し
             self.update_append_claw()
         elif self.start_claw == THREE_CLAW: #ゲーム開始時クローの数が3の時は
             self.update_append_claw() #3回呼び出し
             self.update_append_claw()
             self.update_append_claw()

     #!ステージスタート時の初期化#######################################
     def update_stage_start_init(self):
         #画像リソースファイルを読み込みます
         pyxel.load("min-sht2.pyxres")
         self.my_x = 24    #自機のx座標の初期値
         self.my_y = 50    #自機のy座標の初期値
         self.my_vx = 1    #自機のx方向の移動量
         self.my_vy = 0    #自機のy方向の移動量
         
         self.bg_obstacle_y                = self.stage_data_list[self.stage_number - 1][1] #BG障害物とみなすＹ座標位置をリストを参照して取得、変数に代入する
         self.reference_tilemap            = self.stage_data_list[self.stage_number - 1][2] #BGにアクセスするときどのタイルマップを使用するかの数値をリストを参照して取得、変数に代入する
         self.scroll_type                  = self.stage_data_list[self.stage_number - 1][3] #スクロールの種類をリストを参照して取得、変数に代入する
         self.star_scroll_flag             = self.stage_data_list[self.stage_number - 1][4] #背景のスクロールする星々を表示するかのフラグをリストを参照して取得、変数に代入する
         self.raster_scroll_flag           = self.stage_data_list[self.stage_number - 1][5] #背景のラスタースクロールを表示するかのフラグをリストを参照して取得、変数に代入する
         self.disp_flag_bg_front           = self.stage_data_list[self.stage_number - 1][6] #BG背景(手前)を表示するかどうかのフラグをリストを参照して取得、変数に代入する
         self.disp_flag_bg_middle          = self.stage_data_list[self.stage_number - 1][7] #BG背景(中間)を表示するかどうかのフラグをリストを参照して取得、変数に代入する
         self.disp_flag_bg_back            = self.stage_data_list[self.stage_number - 1][8] #BG背景(奥)を表示するかどうかのフラグをリストを参照して取得、変数に代入する
         self.atmospheric_entry_spark_flag = self.stage_data_list[self.stage_number - 1][9] #大気圏突入時の火花を発生させるかどうかのフラグをリストを参照して取得、変数に代入する
         
         self.present_repair_item_flag = 0 #ボス破壊後の爆発シーンでリペアアイテムを出すときに使用するフラグ 0=まだアイテム出してない 1=アイテム放出したよ～
         
         self.bg_cls_color = 0            #BGをCLS(クリアスクリーン)するときの色の指定(通常は0=黒色です) ゲーム中のイベントで変化することもあるのでステージスタート時でも初期化する
         self.bg_transparent_color = 0    #BGタイルマップを敷き詰めるときに指定する透明色です            ゲーム中のイベントで変化することもあるのでステージスタート時でも初期化する
         
         self.my_boost_injection_count = 0 #ステージクリア後のブースト噴射用のカウンター

         self.timer_flare_flag = 0             #タイマーフレア（触れると物質の時間経過が遅くなるフレア）を放出するかどうかのフラグ
          
         self.auto_move_mode = 0                           #自動移動モードのフラグ
                                                           #0 = パッドやキーボード入力によって移動 
                                                           #1 = イベントによる自動移動モードとなり設定された位置まで自動で移動して行きます
         self.auto_move_mode_x,self.auto_move_mode_y = 0,0 #自動移動モードがonの時はこの座標に向かって毎フレームごと自動で移動して行きます
         self.auto_move_mode_complete = 0                  #自動移動モードで目標座標まで移動したらこのフラグを立てます

         self.add_appear_flag = 0      #敵を追加発生させる時に立てるフラグです
         
         self.record_games_status = 0  #ポーズを掛けたときに直前のゲームステータスを記録しておく変数
         
         self.scroll_count = 0           #ステージ開始からスクロールした背景のドット数カウンタ
                                         #(スクロールスピードが小数になったときはこのカウントも少数になるので注意！)
         self.vertical_scroll_count = 0  #ステージ開始から縦スクロールした背景のドット数カウンタ 主に縦スクロールするステージで使用します
                                         #(スクロールスピードが小数になったときはこのカウントも小数になるので注意！)

         self.stage_count = 0            #ステージ開始から経過したフレームカウント数(1フレームは60分の1秒)常に整数だよ
         
         self.side_scroll_speed               =1  #横スクロールするスピードの現在値が入ります 1フレームで1ドットスクロール(実数ですのん)
         self.side_scroll_speed_set_value     =1  #横スクロールスピードの設定値(変化量の分だけ1フレームごと増加減させ、この設定値までもって行く)
         self.side_scroll_speed_variation     =0  #横スクロールスピードを変化させる時の差分(変化量)

         self.vertical_scroll_speed           =0  #縦スクロールするスピードの現在値が入ります 1フレームで1ドットスクロール(実数ですのん)
         self.vertical_scroll_speed_set_value =0  #縦スクロールスピードの設定値(変化量の分だけ1フレームごと増加減させ、この設定値までもって行く)
         self.vertical_scroll_speed_variation =0  #縦スクロールスピードを変化させる時の差分(変化量)
         
         self.display_cloud_flag     = 0    #背景の流れる雲を表示するかどうかのフラグ(0=表示しない 1=表示する)

         self.cloud_append_interval  = 6    #雲を追加させる間隔
         self.cloud_quantity         = 0    #雲の量
         self.cloud_how_flow         = 0    #雲の流れ方
         self.cloud_flow_speed       = 0    #雲の流れるスピード
         
         self.warning_dialog_flag          = 0 #WARINIGダイアログを表示するかどうかのフラグ
         self.warning_dialog_display_time  = 0 #WARINIGダイアログの表示時間(フレーム単位)
         self.warning_dialog_logo_time     = 0 #WARNINGグラフイックロゴの表示に掛ける時間(フレーム単位)
         self.warning_dialog_text_time     = 0 #WARNINGテキスト表示に掛ける時間(フレーム単位)

         self.stage_clear_dialog_flag          = 0 #STAGE CLEARダイアログを表示するかどうかのフラグ
         self.stage_clear_dialog_display_time  = 0 #STAGE CLEARダイアログの表示時間(フレーム単位)
         self.stage_clear_dialog_logo_time1    = 0 #STAGE CLEARグラフイックロゴの表示に掛ける時間その１(フレーム単位)
         self.stage_clear_dialog_logo_time2    = 0 #STAGE CLEARグラフイックロゴの表示に掛ける時間その２(フレーム単位)
         self.stage_clear_dialog_text_time     = 0 #STAGE CLEARテキスト表示に掛ける時間(フレーム単位)
         
         self.event_index = 0             #イベントリストのインデックス値（イベントリストが現在どの位置にあるのかを示す値です）
         self.type_check_quantity = 0     #特定のショットタイプがリストにどれだけあるのかチェックして数えた数がここに入る
         self.my_ship_explosion_timer = 0 #自機が爆発した後、まだどれだけゲームが進行するかのタイマーカウント
         self.game_over_timer = 0         #ゲームオーバーダイアログを表示した後まだどれだけゲームが進行するかのタイマーカウント
         self.fade_in_out_counter = 0     #フェードイン＆フェードアウト用エフェクトスクリーン用のカウンタ（基本的にx軸(キャラクター単位）の値です)
                                          #0~19 で 19になった状態が一番右端を描画したという事になります
                                          #19になった時点で完了となります
         self.fade_complete_flag = 0      #フェードイン＆フェードアウトが完了したかのフラグが入る所(0=まだ終わっていない 1=完了！)
         self.shadow_in_out_counter = 0            #シャドウイン＆シャドウアウト用エフェクトスクリーン用のカウンタ
         self.shadow_in_out_complete_flag = 0      #シャドウイン＆シャドウアウトが完了したかのフラグが入る所(0=まだ終わっていない 1=完了！)
         
         self.current_formation_id = 1   #現在の敵編隊のＩＤナンバー（0は単独機で編隊群は1からの数字が割り当てられます）
                                         #編隊が1編隊出現するごとにこの数字が1増えていく
                                         #例 1→2→3→4→5→6→7→8→9→10みたいな感じで増えていく
         self.fast_forward_destruction_num = 0        #早回しの条件を満たすのに必要な「破壊するべき編隊の総数」が入ります
         self.fast_forward_destruction_count = 0      #破壊するべき編隊の総数」が1以上ならば編隊を破壊すると次の編隊の出現カウントがこの数値だけ少なくなり出現が早まります
         self.add_appear_flag = 0                     #早回しの条件をすべて満たしたときに建つフラグです、このフラグが立った時、イベントリストに「EVENT_ADD_APPEAR_ENEMY」があったらそこで敵編隊を追加発生させます

         self.my_rolling_flag = 0 #0=通常の向き  1=下方向に移動中のキャラチップ使用  2=上方向に移動中のキャラチップ使用
         self.my_moved_flag = 0   #自機が移動したかどうかのフラグ（トレースクローの時、自機のＸＹ座標を履歴リストに記録するのか？しないのか？で使う）
                                  #0=自機は止まっているので座標履歴リストに記録はしない 
                                  #1=自機は移動したので座標履歴リストに記録する
         
         self.invincible_counter = 0 #無敵時間(単位はフレーム)のカウンタ 0の時以外は無敵状態です
         self.invincible_time = 30   #ダメージを受けた後の無敵時間の初期値

         self.enemy_bound_collision_flag = 0 #ホッパー君が地面に接触してバウンドしたかどうかのフラグ(デバッグ用に使います)
         self.mountain_x = 0                 #8wayフリースクロール＋ラスタースクロール時の背景に表示される山のBGX座標用の変数です（デバッグ様に使用します）
         self.cp = 0                         #外積計算用の変数(何故か判らないけど関数内で宣言せずに使うとintじゃなくてtupleになってしまうので・・・何故？)
         self.point_inside_triangle_flag = 0 #三角形の中に点が存在するかを判別する関数用のフラグを初期化

         #リスト群の初期化#############################################################################
         #新しいクラスを作った時はここで必ず初期化するコードを記述する事！！！！！！
         #リストは初期化しないと使えないっポイ！？ぞ・・・っと・・・・・・
         #############################################################################################
         self.shots = []                #自機弾のリスト
         self.missile = []              #ミサイルのリスト
         self.claw_shot = []            #クローの弾のリスト
         self.enemy = []               #敵のリスト
         self.enemy_shot = []           #敵の弾のリスト
         self.obtain_item = []          #取得アイテム類のリスト(パワーアップカプセルなど)
         self.stars = []                #背景の流れる星々のリスト           当たり判定はありません
         self.explosions = []           #爆発パターン群のリスト             当たり判定はありません
         self.particle = []             #パーティクル（火花の粒子）のリスト  当たり判定はありません
         self.background_object = []    #背景オブジェクトのリスト           当たり判定はありません
         self.window = []               #メッセージウィンドウのリスト        当たり判定はありません
         self.claw_coordinates = []     #自機クロー（トレースモード）のxy座標リスト まぁオプションのxy座標が入るリストです
         self.enemy_formation = []      #敵の編隊数のＩＤと出現時の総数と現在の生存数が入るリストです
         self.event_append_request = [] #イベント追加リクエストが入るリストです(敵などの臨時追加発注発生）
         self.boss = []                 #ボスのリスト
         self.raster_scroll = []        #ラスタースクロール用のリスト
         
         #各ステージのイベントリストだよ
         #イベントリストは早回しで「イベントが実行されるステージカウント数タイマー」が書き換えられるので関数「update_stage_start_init」内でリスタートごとに再読み込みする
         #
         #データリスト形式
         #[イベントが実行されるステージカウント数タイマー,イベントの内容,敵キャラのIDナンバー,x座標,y座標,編隊の場合は編隊数,通常or早回し発生の判別,編隊殲滅後カウントを減少させる数,実際に減らすカウント数]
         #スクロールカウント数が99999999の場合は実質エンドコードみたいな～☆彡
         #
         #各イベントのフォーマット
         #EVENT_FAST_FORWARD_NUM   早回しする編隊群数と時間の設定[この時点から早回しする編隊群の数(例 3だとこのイベントからあと3イベント早回しが発生します),早回しするタイマー数(例 30だとこれ以降カウントタイマーが編隊を全滅させる事で30早まります)]
         #EVENT_ENEMY              敵の出現                    [敵キャラのＩＤナンバー,出現x座標,出現y座標,編隊群の場合は編隊数の指定]
         #EVENT_WARNING            ワーニングダイアログ表示      [警告表示時間,グラフイックロゴ表示に掛ける時間,テキスト表示に掛ける時間](単位は全てフレームです)
         #EVENT_BOSS               各ステージに対応したボスを出現させる
         #EVENT_ADD_APPEAR_ENEMY   早回しの条件が成立したとき敵を出現させる [敵キャラのＩＤナンバー,出現x座標,出現y座標,編隊数]
         #EVENT_SCROLL             スクロール制御
         #   SCROLL_NUM_SET          スクロール関連のパラメーター設定 [横スクロールスピード設定値,横スクロールスピードの変化量,縦スクロールスピード設定値,縦スクロールスピードの変化量]
         #   SCROLL_START            スクロールの開始（横スクロールでスピードは通常の1)
         #   SCROLL_STOP             スクロールの停止
         #   SCROLL_SPEED_CHANGE     スクロールスピードを変化させる[スクロールスピードの設定値(-ならバックスクロール),スクロールスピードの変化量(-なら減速,+なら加速)]
         #   VERTICAL_SCROLL_START   縦スクロールの開始
         #   VERTICAL_SCROLL_STOP    縦スクロールのスタート
         #EVENT_DISPLAY_STAR       背景星スクロールのon/off [0=off/1=on]
         #EVENT_CHANGE_BG_CLS_COLOR 背景でまず最初に塗りつぶす色の指定 0~15 pyxelのカラーコード
         #EVENT_CHANGE_BG_TRANSPARENT_COLOR 背景マップチップを敷き詰める時に使用する透明色の指定 0~15 pyxelのカラーコード
         #EVENT_CLOUD              背景の雲の制御
         #   CLOUD_NUM_SET            雲のパラメータ設定[発生させる間隔(単位はフレーム),
         #                                             雲の量(0=比較的小さい雲だけ,1=小中サイズの雲を流す,2=小中大すべての種類の雲を流す),
         #                                             流れ方(0=そのまま左に素直に流れていく-0.25=上方向に流されていく0.25=下方向に流されていく),
         #                                             流れるスピード(倍率となります,通常は1,少数も使用可です)
         #                                             ]              
         #   CLOUD_START              雲を流すのを開始する
         #   CLOUS_STOP               雲を流すのを停止する
         #EVENT_RASTER_SCROLL         ラスタースクロールの制御
         #   RASTER_SCROLL_OFF           ラスタースクロールの表示をoffにする[表示オフにするラスタスクロールのid]
         #   RASTER_SCROLL_ON            ラスタースクロールの表示をonにする [表示オンにするラスタスクロールのid]
         #EVENT_BG_SCREEN_ON_OFF    背景ＢＧの表示のon/off
         #   BG_BACK or BG_MIDDLE or BG_FRONT  BGの種類を選択
         #   DISP_OFF or DISP_ON               表示オフ/表示オン
         #EVENT_ENTRY_SPARK_ON_OFF  大気圏突入の火花表示のon/off
         #   SPARK_OFF or SPARK_ON             火花表示on/off
     
         #ボステストモード専用のボスだけを出現させるイベントリスト
         self.event_list_boss_test_mode = [
               [   50,EVENT_WARNING,500,120,240],
               [  100,EVENT_BOSS],
               [99999999],]
         
         self.event_list_no_enemy_mode = [
               [200000,EVENT_WARNING,500,120,240],
               [200200,EVENT_BOSS],
               [99999999],]
         
         self.event_list_stage_mountain_region_l1= [
               [ 100,EVENT_BG_SCREEN_ON_OFF,BG_BACK,DISP_OFF],
               [ 110,EVENT_ENTRY_SPARK_ON_OFF,SPARK_OFF],
               
               [ 200,EVENT_ENEMY,CIR_COIN     ,160, 40   ,6],
               [ 300,EVENT_SCROLL,SCROLL_NUM_SET,    2,0.5,         0.5,0.01],
               [ 303,EVENT_ENTRY_SPARK_ON_OFF,SPARK_ON],
               [ 350,EVENT_SCROLL,SCROLL_NUM_SET,  2.5,0.5,         0.5,0.01],
               [ 400,EVENT_SCROLL,SCROLL_NUM_SET,    3,0.5,         0.5,0.01],
               [ 403,EVENT_ENEMY,CIR_COIN     ,160, 70   ,6],
               [ 450,EVENT_SCROLL,SCROLL_NUM_SET,  3.5,0.5,         0.5,0.01],
               [ 500,EVENT_SCROLL,SCROLL_NUM_SET,    4,0.5,         0.5,0.01],
               [ 550,EVENT_ENEMY,CIR_COIN     ,160, 40   ,6],
               [ 600,EVENT_SCROLL,SCROLL_NUM_SET,    5,0.5,         0.5,0.01],
               [ 690,EVENT_ENEMY,CIR_COIN     ,160, 70   ,6],
               [ 700,EVENT_SCROLL,SCROLL_NUM_SET,    6,0.5,         0.5,0.01],
               [ 800,EVENT_SCROLL,SCROLL_NUM_SET,    7,0.5,         0.5,0.01],
               [ 891,EVENT_ENEMY,SAISEE_RO,170, 50-10],
               [ 892,EVENT_ENEMY,SAISEE_RO,169, 50   ],
               [ 893,EVENT_ENEMY,SAISEE_RO,168, 50+10],
               [ 900,EVENT_SCROLL,SCROLL_NUM_SET,    8,0.5,         0.5,0.01],

               [ 910,EVENT_BG_SCREEN_ON_OFF,BG_BACK,DISP_ON],

               [ 951,EVENT_ENEMY,SAISEE_RO,170, 50-20],
               [ 952,EVENT_ENEMY,SAISEE_RO,169, 50   ],
               [ 953,EVENT_ENEMY,SAISEE_RO,168, 50+20],
               
               [1000,EVENT_CLOUD,CLOUD_NUM_SET,6,1,-0.25,1],
               [1010,EVENT_CLOUD,CLOUD_START],

               [1051,EVENT_ENEMY,SAISEE_RO,170, 50-30],
               [1052,EVENT_ENEMY,SAISEE_RO,169, 50-20],
               [1053,EVENT_ENEMY,SAISEE_RO,168, 50   ],
               [1054,EVENT_ENEMY,SAISEE_RO,167, 50+20],
               [1055,EVENT_ENEMY,SAISEE_RO,166, 50+30],

               [1100,EVENT_ENEMY,SAISEE_RO,170, 30   ],
               [1110,EVENT_ENEMY,SAISEE_RO,170, 30   ],
               [1120,EVENT_ENEMY,SAISEE_RO,170, 30   ],
               [1130,EVENT_ENEMY,SAISEE_RO,170, 30   ],
               [1140,EVENT_ENEMY,SAISEE_RO,170, 30   ],
               [1150,EVENT_ENEMY,SAISEE_RO,170, 30   ],
               [1160,EVENT_ENEMY,SAISEE_RO,170, 30   ],
               [1170,EVENT_ENEMY,SAISEE_RO,170, 30   ],
               [1180,EVENT_ENEMY,SAISEE_RO,170, 30   ],

               [1300,EVENT_ENEMY,SAISEE_RO,170, 70   ],
               [1310,EVENT_ENEMY,SAISEE_RO,170, 70   ],
               [1320,EVENT_ENEMY,SAISEE_RO,170, 70   ],
               [1330,EVENT_ENEMY,SAISEE_RO,170, 70   ],
               [1340,EVENT_ENEMY,SAISEE_RO,170, 70   ],
               [1350,EVENT_ENEMY,SAISEE_RO,170, 70   ],
               [1360,EVENT_ENEMY,SAISEE_RO,170, 70   ],
               [1370,EVENT_ENEMY,SAISEE_RO,170, 70   ],
               [1380,EVENT_ENEMY,SAISEE_RO,170, 70   ],

               [1451,EVENT_ENEMY,SAISEE_RO,170, 10   ],
               [1452,EVENT_ENEMY,SAISEE_RO,169, 20   ],
               [1453,EVENT_ENEMY,SAISEE_RO,168, 30   ],
               [1454,EVENT_ENEMY,SAISEE_RO,167, 40   ],
               [1455,EVENT_ENEMY,SAISEE_RO,166, 50   ],
               [1456,EVENT_ENEMY,SAISEE_RO,165, 60   ],
               [1457,EVENT_ENEMY,SAISEE_RO,164, 70   ],
               [1458,EVENT_ENEMY,SAISEE_RO,163, 80   ],
               [1459,EVENT_ENEMY,SAISEE_RO,162, 90   ],
               
               [1500,EVENT_DISPLAY_STAR,             DISP_OFF],
               [1510,EVENT_CHANGE_BG_CLS_COLOR,          12],
               [1560,EVENT_CHANGE_BG_TRANSPARENT_COLOR,  12],

               [1561,EVENT_ENEMY,SAISEE_RO,170, 10   ],
               [1562,EVENT_ENEMY,SAISEE_RO,169, 20   ],
               [1563,EVENT_ENEMY,SAISEE_RO,168, 30   ],
               [1564,EVENT_ENEMY,SAISEE_RO,167, 40   ],
               [1565,EVENT_ENEMY,SAISEE_RO,166, 50   ],
               [1566,EVENT_ENEMY,SAISEE_RO,165, 60   ],
               [1567,EVENT_ENEMY,SAISEE_RO,164, 70   ],
               [1568,EVENT_ENEMY,SAISEE_RO,163, 80   ],
               [1569,EVENT_ENEMY,SAISEE_RO,162, 90   ],

               [1600,EVENT_CLOUD,CLOUD_NUM_SET,6,2,-0.4,1],
               
               [1610,EVENT_ENEMY,VOLDAR,168, 0],

               
               [1710,EVENT_ENEMY,RAY_BLASTER,168, 40-20],
               [1720,EVENT_ENEMY,RAY_BLASTER,168, 40   ],
               [1730,EVENT_ENEMY,RAY_BLASTER,168, 40+20],

               [1810,EVENT_ENEMY,RAY_BLASTER,168, 60-20],
               [1850,EVENT_ENEMY,RAY_BLASTER,168, 60   ],
               [1890,EVENT_ENEMY,RAY_BLASTER,168, 60+20],
               
               

               [2300,EVENT_SCROLL,SCROLL_SPEED_CHANGE,0.5,-0.01],
               
               [2310,EVENT_RASTER_SCROLL,RASTER_SCROLL_OFF,1],

               [2340,EVENT_ENEMY,TWIN_ARROW,160,  20],
               [2341,EVENT_ENEMY,TWIN_ARROW,160,  60],
               [2342,EVENT_ENEMY,TWIN_ARROW,160, 100],

               [2600,EVENT_ENEMY,TWIN_ARROW,160, 60   ],
               [2601,EVENT_ENEMY,TWIN_ARROW,160, 60+10],
               [2602,EVENT_ENEMY,TWIN_ARROW,160, 60-10],
               [2603,EVENT_ENEMY,TWIN_ARROW,160, 60+20],
               [2604,EVENT_ENEMY,TWIN_ARROW,160, 60-20],

               [2740,EVENT_ENEMY,TWIN_ARROW,120,  -8],
               [2741,EVENT_ENEMY,TWIN_ARROW,160, 60],
               [2742,EVENT_ENEMY,TWIN_ARROW,120,  130],

               [2840,EVENT_ENEMY,TWIN_ARROW,120,  -8],
               [2841,EVENT_ENEMY,TWIN_ARROW,80,  -8],
               [2842,EVENT_ENEMY,TWIN_ARROW,160, 60],
               [2843,EVENT_ENEMY,TWIN_ARROW,80,  130],
               [2844,EVENT_ENEMY,TWIN_ARROW,120,  130],

               [3000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0,-0.004],
               [3100,EVENT_CLOUD,CLOUD_STOP],
               [3110,EVENT_ENTRY_SPARK_ON_OFF,SPARK_OFF],


               
               [3200,EVENT_SCROLL,SCROLL_SPEED_CHANGE,3.0,0.0001],
               [3210,EVENT_WARNING,500,120,240],
               [3300,EVENT_BOSS],
               


               
               [99999999],]
         
         self.event_list_stage_mountain_region_l2= [
               
               [ 300,EVENT_SCROLL,SCROLL_NUM_SET,    2,0.5,         0.5,0.01],
               [ 350,EVENT_SCROLL,SCROLL_NUM_SET,  2.5,0.5,         0.5,0.01],
               [ 400,EVENT_SCROLL,SCROLL_NUM_SET,    3,0.5,         0.5,0.01],
               [ 450,EVENT_SCROLL,SCROLL_NUM_SET,  3.5,0.5,         0.5,0.01],
               [ 500,EVENT_SCROLL,SCROLL_NUM_SET,    4,0.5,         0.5,0.01],
               [ 600,EVENT_SCROLL,SCROLL_NUM_SET,    5,0.5,         0.5,0.01],
               [ 700,EVENT_SCROLL,SCROLL_NUM_SET,    6,0.5,         0.5,0.01],
               [ 800,EVENT_SCROLL,SCROLL_NUM_SET,    7,0.5,         0.5,0.01],
               [ 900,EVENT_SCROLL,SCROLL_NUM_SET,    8,0.5,         0.5,0.01],
               
               [1000,EVENT_CLOUD,CLOUD_NUM_SET,6,1,-0.25,1],

               [1010,EVENT_CLOUD,CLOUD_START],
               
               [1500,EVENT_DISPLAY_STAR,             0],
               [1510,EVENT_CHANGE_BG_CLS_COLOR,          12],
               [1560,EVENT_CHANGE_BG_TRANSPARENT_COLOR,  12],
               

               [1600,EVENT_CLOUD,CLOUD_NUM_SET,6,2,-0.4,1],
               
               [2300,EVENT_SCROLL,SCROLL_SPEED_CHANGE,0.5,-0.01],
               
               [2310,EVENT_RASTER_SCROLL,RASTER_SCROLL_OFF,1],

               [3000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0,-0.004],
               [3100,EVENT_CLOUD,CLOUD_STOP],
               [3200,EVENT_SCROLL,SCROLL_SPEED_CHANGE,3.0,0.0001],
               [4000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0.05,0.01],
               [5000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,-0.05,-0.01],
               [6000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0.05,0.01],
               [7000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,-0.05,-0.01],
               [8000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0.05,0.01],
               [9000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,-0.05,-0.01],
               [11000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,0.05,0.01],
               [14000,EVENT_SCROLL,SCROLL_SPEED_CHANGE_VERTICAL,-0.05,-0.01],


               
               [99999999],]
         
         self.event_list_stage_mountain_region_dummy= [
               [99999999],]
               
         self.event_list_stage_advance_base_l1= [
               
               [  10,EVENT_FAST_FORWARD_NUM,4,30],
               [ 200,EVENT_ENEMY,CIR_COIN     ,160, 10   ,6],
               [ 500,EVENT_ENEMY,CIR_COIN     ,160, 90   ,6],
               [ 700,EVENT_ENEMY,CIR_COIN     ,160, 20   ,6],
               [ 900,EVENT_ENEMY,CIR_COIN     ,160, 80   ,6],

               [950,EVENT_ADD_APPEAR_ENEMY,CIR_COIN,160, 60,10],
               
               [1050,EVENT_ENEMY,SAISEE_RO,160, 60-24],
               [1051,EVENT_ENEMY,SAISEE_RO,160, 60   ],
               [1052,EVENT_ENEMY,SAISEE_RO,160, 60+24],

               [1080,EVENT_ENEMY,SAISEE_RO,160, 40-24],
               [1081,EVENT_ENEMY,SAISEE_RO,160, 40,  ],
               [1082,EVENT_ENEMY,SAISEE_RO,160, 40+24],
               
               [1095,EVENT_ENEMY,GREEN_LANCER,180,10],

               [1100,EVENT_ENEMY,CIR_COIN,    160,20    ,7],
               [1300,EVENT_ENEMY,CIR_COIN,    160,80    ,7],

               [1400,EVENT_ENEMY,TWIN_ARROW,160, 40],
               [1401,EVENT_ENEMY,TWIN_ARROW,160, 60],
               [1402,EVENT_ENEMY,TWIN_ARROW,160, 80],

               [1500,EVENT_ENEMY,TWIN_ARROW,160,  20],
               [1501,EVENT_ENEMY,TWIN_ARROW,160,  60],
               [1502,EVENT_ENEMY,TWIN_ARROW,160, 100],
               
               [1600,EVENT_ENEMY,TWIN_ARROW,160, 60   ],
               [1601,EVENT_ENEMY,TWIN_ARROW,160, 60+10],
               [1602,EVENT_ENEMY,TWIN_ARROW,160, 60-10],
               [1603,EVENT_ENEMY,TWIN_ARROW,160, 60+20],
               [1604,EVENT_ENEMY,TWIN_ARROW,160, 60-20],

               [3000,EVENT_SCROLL,SCROLL_SPEED_CHANGE,-4,-0.001],
               [4800,EVENT_SCROLL,SCROLL_STOP],
               [5010,EVENT_SCROLL,SCROLL_SPEED_CHANGE,1, 0.002],
               [6000,EVENT_SCROLL,SCROLL_SPEED_CHANGE,5, 0.002],

               [7000,EVENT_WARNING,500,120,240],
               [7300,EVENT_BOSS],
               [99999999],]

         self.event_list_stage_advance_base_l2= [
               [  10,EVENT_FAST_FORWARD_NUM,4,30],
               [ 200,EVENT_ENEMY,CIR_COIN     ,160, 10   ,6],
               [ 500,EVENT_ENEMY,CIR_COIN     ,160, 90   ,6],
               [ 700,EVENT_ENEMY,CIR_COIN     ,160, 20   ,6],
               [ 900,EVENT_ENEMY,CIR_COIN     ,160, 80   ,6],

               [950,EVENT_ADD_APPEAR_ENEMY,CIR_COIN,160, 60,10],
               
               [1050,EVENT_ENEMY,SAISEE_RO,160, 60-24],
               [1051,EVENT_ENEMY,SAISEE_RO,160, 60   ],
               [1052,EVENT_ENEMY,SAISEE_RO,160, 60+24],

               [1080,EVENT_ENEMY,SAISEE_RO,160, 40-24],
               [1081,EVENT_ENEMY,SAISEE_RO,160, 40,  ],
               [1082,EVENT_ENEMY,SAISEE_RO,160, 40+24],
               
               [1095,EVENT_ENEMY,GREEN_LANCER,180,10],

               [6000,EVENT_WARNING,500,120,240],
               [6300,EVENT_BOSS],
               [99999999],]
         
         self.event_list_stage_advance_base_l3= [    
               [  10,EVENT_FAST_FORWARD_NUM,4,30],
               [ 200,EVENT_ENEMY,CIR_COIN     ,160, 10   ,6],
               [ 500,EVENT_ENEMY,CIR_COIN     ,160, 90   ,6],
               [ 700,EVENT_ENEMY,CIR_COIN     ,160, 20   ,6],
               [ 900,EVENT_ENEMY,CIR_COIN     ,160, 80   ,6],

               [950,EVENT_ADD_APPEAR_ENEMY,CIR_COIN,160, 60,10],
               
               [1050,EVENT_ENEMY,SAISEE_RO,160, 60-24],
               [1051,EVENT_ENEMY,SAISEE_RO,160, 60   ],
               [1052,EVENT_ENEMY,SAISEE_RO,160, 60+24],

               [1080,EVENT_ENEMY,SAISEE_RO,160, 40-24],
               [1081,EVENT_ENEMY,SAISEE_RO,160, 40,  ],
               [1082,EVENT_ENEMY,SAISEE_RO,160, 40+24],
               
               [1095,EVENT_ENEMY,GREEN_LANCER,180,10],

               [1100,EVENT_ENEMY,CIR_COIN,    160,20    ,7],
               [1300,EVENT_ENEMY,CIR_COIN,    160,80    ,7],

               [1400,EVENT_ENEMY,TWIN_ARROW,160, 40],
               [1401,EVENT_ENEMY,TWIN_ARROW,160, 60],
               [1402,EVENT_ENEMY,TWIN_ARROW,160, 80],

               [1500,EVENT_ENEMY,TWIN_ARROW,160,  20],
               [1501,EVENT_ENEMY,TWIN_ARROW,160,  60],
               [1502,EVENT_ENEMY,TWIN_ARROW,160, 100],
               
               [1600,EVENT_ENEMY,TWIN_ARROW,160, 60   ],
               [1601,EVENT_ENEMY,TWIN_ARROW,160, 60+10],
               [1602,EVENT_ENEMY,TWIN_ARROW,160, 60-10],
               [1603,EVENT_ENEMY,TWIN_ARROW,160, 60+20],
               [1604,EVENT_ENEMY,TWIN_ARROW,160, 60-20],
               
               [6000,EVENT_WARNING,500,120,240],
               [6300,EVENT_BOSS],
               [99999999],] 
         
         #ゲーム全体のイベントリスト(ステージ、ループ数も考慮されてます)
         #フォーマット(このリストの書き方）は
         # game_event_list[
         #[ステージ1周回1、ステージ1周回2、ステージ1周回3],
         #[ステージ2周回1、ステージ2周回2、ステージ2周回3],
         #[ステージ3周回1、ステージ3周回2、ステージ3周回3],
         #[ステージ4周回1、ステージ4周回2、ステージ4周回3],
         #[ステージ5周回1、ステージ5周回2、ステージ5周回3],
         #[ステージ6周回1、ステージ6周回2、ステージ6周回3]
         #]
         #みたいな感じで書きます
         
         self.game_event_list = [
                                 [self.event_list_stage_mountain_region_l1,
                                  self.event_list_stage_mountain_region_l1,
                                  self.event_list_stage_mountain_region_l1],
                                 
                                 [self.event_list_stage_advance_base_l1   ,
                                  self.event_list_stage_advance_base_l2   ,
                                  self.event_list_stage_advance_base_l3]
                                 ]
         
         #self.game_event_list = [self.event_list_no_enemy_mode,  self.event_list_no_enemy_mode,  self.event_list_no_enemy_mode]
         
         #各ステージのＢＧ書き換えによるアニメーションの為のデータリスト群
         #フォーマットの説明
         #[アニメーションさせたいマップチップのx座標(0~255(8の倍数にしてね)),
         #                                  y座標(0~255(8の倍数にしてね)),
         #                                 アニメスピード(1なら1フレーム毎 2だと2フレーム毎って感じ),
         #                                 アニメ枚数(横一列に並べてください)]
         self.bg_animation_list_mountain_region = [
                                 [192,192,6,8],                                
                                 [144, 64,6,8],
                                 ]
    
         if self.boss_test_mode == 1:
              self.event_list = self.event_list_boss_test_mode #ボステストモードが1の時はボスだけが出現するイベントリストを登録します
         else:
              self.event_list = self.game_event_list[self.stage_number - 1][self.stage_loop - 1] 
                                                                             #self.event_list_stage_advance_base_l1          
                                                                             #とりあえずイベントリストはadvance_baseステージのものをコピーして使用します
                                                                             #将来的にはステージやループ回数を反映する・・・はず

         self.bg_animation_list = self.bg_animation_list_mountain_region     #とりあえずBGアニメーションパターンリストはmountain_regionのものをコピーして使用します

         #自機のXY座標をトレースクローのXY座標としてコピーし、初期化を行う(とりあえず60要素埋め尽くす)(60要素=60フレーム分=1秒過去分まで記録される)
         for _i in range(TRACE_CLAW_BUFFER_SIZE):
             new_traceclaw = Trace_coordinates()
             new_traceclaw.update(self.my_x,self.my_y)
             self.claw_coordinates.append(new_traceclaw)
         
         self.create_raster_scroll_data() #ラスタースクロール用のデータの初期化＆育成

     # キーボードとゲームパッド、または移動座標先を指定しての自動モードによる自機の移動処理を行う関数です
     def update_my_ship(self):
          self.my_rolling_flag = 0  #自機ローリングフラグ(旋回フラグ）を0に初期化する
          self.my_moved_flag = 0    #自機が動いたかどうかのフラグを0に初期化する
          
          if self.game_status == SCENE_STAGE_CLEAR_MY_SHIP_BOOST: #ゲームステータスが「ステージクリア後、自機がブースト加速して右に過ぎ去っていく」なら
               self.my_x += self.my_vx
               self.my_vx += 0.025 #速度0.01で加速していく
               self.my_boost_injection_count += 1 #ステージクリア後のブースト噴射用のカウンターを1増やしていく
               self.my_moved_flag = 1            #トレースクローも動かしたいので自機移動フラグOnにする

          elif self.auto_move_mode == 0: #手動移動モードの処理
               self.my_vx,self.my_vy = 0,0 #自機の自機の移動量(vx,vy)を0に初期化する

               # 左入力されたら  ｘ座標を  my_speedの数値だけ減らす
               if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT) or pyxel.btn(pyxel.GAMEPAD_2_LEFT):
                    self.my_moved_flag = 1#自機移動フラグOn
                    self.my_vx = -1
               # 右入力されたら  ｘ座標を  my_speedの数値だけ増やす
               if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT) or pyxel.btn(pyxel.GAMEPAD_2_RIGHT):
                    self.my_moved_flag = 1#自機移動フラグOn
                    self.my_vx = 1
               # 上入力されたら  y座標を  my_speedの数値だけ減らす
               if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD_1_UP) or pyxel.btn(pyxel.GAMEPAD_2_UP):
                    self.my_rolling_flag = 2
                    self.my_moved_flag = 1#自機移動フラグOn
                    self.my_vy = -1
               # 下入力されたら  y座標を  my_speedの数値だけ増やす
               if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD_1_DOWN) or pyxel.btn(pyxel.GAMEPAD_2_DOWN):
                    self.my_rolling_flag = 1
                    self.my_moved_flag = 1#自機移動フラグOn
                    self.my_vy = 1
          
               self.my_x += self.my_vx * self.my_speed #自機の移動量(vx,vy)と自機の速度(speed)を使って自機の座標を更新する（移動！）
               self.my_y += self.my_vy * self.my_speed
          
          elif self.auto_move_mode == 1 and self.auto_move_mode_complete == 0: #自動移動モード＆まだ移動完了フラグが建っていなかったら・・・
               self.my_vx,self.my_vy = 0,0 #自機の自機の移動量(vx,vy)を0に初期化する

               #左に自動移動
               if self.my_x > self.auto_move_mode_x:
                    self.my_moved_flag = 1#自機移動フラグOn
                    self.my_vx = -0.5
               #右に自動移動
               if self.my_x < self.auto_move_mode_x:
                    self.my_moved_flag = 1#自機移動フラグOn
                    self.my_vx = 0.5
               #上に自動移動
               if self.my_y > self.auto_move_mode_y:
                    self.my_rolling_flag = 2
                    self.my_moved_flag = 1#自機移動フラグOn
                    self.my_vy = -0.5
               #下に自動移動
               if self.my_y < self.auto_move_mode_y:
                    self.my_rolling_flag = 1
                    self.my_moved_flag = 1#自機移動フラグOn
                    self.my_vy = 0.5
               
               self.my_x += self.my_vx #自機の移動量(vx,vy)を使って自機の座標を更新する（移動！）
               self.my_y += self.my_vy

               if -1 <= self.my_x - self.auto_move_mode_x <= 1 and -1 <= self.my_y - self.auto_move_mode_y <= 1: #自機座標(x,y)と移動目的先の座標の差が誤差+-1以内ならば
                    self.auto_move_mode_complete = 1   #自動移動完了フラグをonにする
                    if self.game_status == SCENE_PLAY: #ゲームステータスが「PLAY」の時だけ
                         self.auto_move_mode = 0       #自動移動モードを解除し手動移動モードに移行します
                    elif self.game_status == SCENE_STAGE_CLEAR_MOVE_MY_SHIP: #ゲームステータスが「ステージクリア後の自機自動移動」だったら
                         self.game_status = SCENE_STAGE_CLEAR_MY_SHIP_BOOST  #ゲームステータスを「ステージクリア後、自機がブーストして右へ過ぎ去っていくシーン」にする
                         self.my_vx = -1.3 #ブースト開始の初期スピードは左へ1ドット毎フレーム（ちょっと左に戻ってから加速し、右へ飛んでいく）
                         self.my_boost_injection_count = 1 #ステージクリア後のブースト噴射用のカウンターの数値を初期化
                         self.my_moved_flag = 1            #トレースクローも動かしたいので自機移動フラグOnにする
                         pyxel.playm(3)  #ブーストサウンド？再生

     #自機の座標を過去履歴リストに書き込んでいく関数（トレースクローの座標として使用します）
     def update_my_ship_record_coordinate(self):
         if self.my_moved_flag == 1:#自機が移動したフラグがonならＸＹ座標を過去履歴リストに書き込み一番古い物を削除する
               new_traceclaw = Trace_coordinates()#new_traceclawにTrace_coordinatesクラスの型を登録
               new_traceclaw.update(self.my_x,self.my_y)#クラス登録された（クラス設計された？）new_traceclawに自機のＸＹ座標データを入れてインスタンスを作成する
               self.claw_coordinates.append(new_traceclaw)#1フレームごとに自機のXY座標の入ったインスタンスをclaw_coordinatesリストに追加していく(append)

               del self.claw_coordinates[0]#一番古いXY座標データをdelする(一番古いXY座標のインデックス値は0)

               #自機が移動したフラグがonならリバースクロー用のショット方向ベクトルも書き込む
               self.reverse_claw_svx = -(self.my_vx)#リバースクロー用のショット方向ベクトルは自機移動ベクトルを反転したものとなります
               self.reverse_claw_svy = -(self.my_vy)
     
     #キーボードの1が推されたらショット経験値を増やしていく                                     KEY 1
     def update_powerup_shot(self):
          if pyxel.btnp(pyxel.KEY_1):
               self.shot_exp += 1  #ショット経験値を１増やして武器をアップグレードさせていく
               self.level_up_my_shot() #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
               if self.shot_level > 10:
                    self.shot_level = 0
     
     #キーボードの2が推されたらミサイル経験値を増やしていく                                     KEY 2
     def update_powerup_missile(self):
          if pyxel.btnp(pyxel.KEY_2):
               self.missile_exp += 1#ミサイル経験値を１増やしてミサイルをアップグレードさせていく
               self.level_up_my_missile() #自機ミサイルの経験値を調べ可能な場合はレベルアップさせる関数を呼び出す
               if self.missile_level > 2:
                    self.missile_level = 0
     
     #キーボードの3かゲームパッドの「SELECT」ボタンが入力されたらが押されたらスピード変化させる    KEY 3  GAMEPAD SELECT
     def update_change_speed(self):
          if pyxel.btnp(pyxel.KEY_3) or pyxel.btnp(pyxel.GAMEPAD_1_SELECT) or pyxel.btnp(pyxel.GAMEPAD_2_SELECT):
               if self.my_speed == 1:
                    self.my_speed = 1.5
               elif self.my_speed == 1.5:
                    self.my_speed = 1.75
               else:
                    self.my_speed = 1
     
     #スペースキーかゲームバットＡが押されたらショットを発射する
     def update_fire_shot(self):
          if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD_1_A) or pyxel.btn(pyxel.GAMEPAD_2_A):     
              if self.shot_level == 7:#ウェーブカッターLv1発射
                   if len(self.shots) < self.shot_rapid_of_fire:
                   #if self.shot_type_count(self.shot_level) < 3: 
                        if (pyxel.frame_count % 8) == 0:
                             pyxel.play(2,5)
                             new_shot = Shot()
                             new_shot.update(self.shot_level,self.my_x + 5,self.my_y -4,       3,0,  8,16,  0,   2,1)
                             
                             self.shots.append(new_shot)

              if self.shot_level == 8:#ウェーブカッターLv2発射
                   if len(self.shots) < self.shot_rapid_of_fire:
                        if (pyxel.frame_count % 8) == 0:
                             pyxel.play(2,5)
                             new_shot = Shot()
                             new_shot.update(self.shot_level,self.my_x + 5,self.my_y -8,       3,0,  8,24,  0,   2,1)
                             self.shots.append(new_shot)
              
              if self.shot_level == 9:#ウェーブカッターLv3発射
                   if len(self.shots) < self.shot_rapid_of_fire:
                        if (pyxel.frame_count % 8) == 0:
                             pyxel.play(2,5)
                             new_shot = Shot()
                             new_shot.update(self.shot_level,self.my_x + 5,self.my_y -12,       3,0,  8,32,  0,   2,1)
                             self.shots.append(new_shot)
               
              if self.shot_level == 10:#ウェーブカッターLv4発射
                   if len(self.shots) < self.shot_rapid_of_fire:
                        if (pyxel.frame_count % 6) == 0:
                             pyxel.play(2,5)
                             new_shot = Shot()
                             new_shot.update(self.shot_level,self.my_x + 5,self.my_y -12,       4,0,  8,32,  0,   2,1)
                             self.shots.append(new_shot)

              if self.shot_level == 4:#レーザー発射
                   if len(self.shots) < 20:
                        if (pyxel.frame_count % 2) == 0:
                             pyxel.play(2,4)
                             new_shot = Shot()
                             new_shot.update(self.shot_level,self.my_x + 5,self.my_y,           3,1,  8,8,  0,   0.3,1)
                             self.shots.append(new_shot)

              if self.shot_level == 5:#ツインレーザー発射
                   if len(self.shots) < 40:
                        if (pyxel.frame_count % 2) == 0:
                             pyxel.play(2,4)
                             new_shot = Shot()
                             new_shot.update(self.shot_level,self.my_x + 5,self.my_y - 3,      3,1,  8,8,  -3,  0.3,1)
                             self.shots.append(new_shot)

                             new_shot = Shot()
                             new_shot.update(self.shot_level,self.my_x + 5,self.my_y + 3,      3,1,  8,8,    3, 0.3,1)
                             self.shots.append(new_shot)

              if self.shot_level == 6:#３ＷＡＹレーザー発射
                   if len(self.shots) < 80:
                        if (pyxel.frame_count % 2) == 0:
                             pyxel.play(2,4)
                             new_shot = Shot()
                             new_shot.update(self.shot_level,self.my_x + 1,self.my_y  -1,    1,-1.08,   8,8,   -1,  0.2,1)
                             self.shots.append(new_shot)

                             new_shot = Shot()
                             new_shot.update(self.shot_level,self.my_x + 6,self.my_y,        3,1,       8,8,    0,  0.3,1)
                             self.shots.append(new_shot)

                             pyxel.play(2,4)
                             new_shot = Shot()
                             new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 1,    2, 1.07,   8,8,    1,  0.2,1)
                             self.shots.append(new_shot)
              
              
              
              self.count_missile_type(5,5,5,5) #ミサイルタイプ5(ペネトレートロケット）がいくつ存在するのか調べる
              if self.type_check_quantity == 0 and self.select_sub_weapon_id == PENETRATE_ROCKET:#もしペネトレートロケットが全く存在しないのなら発射する！！！
                  new_missile = Missile()
                  new_missile.update(5,self.my_x + 4,self.my_y,   -0.8,-0.7,   6,    1   ,0,0,   0,1,   8,8, 0,0,  0,0) #ペネトレートロケット
                  self.missile.append(new_missile)#ペネトレートロケット育成

                  new_missile = Missile()
                  new_missile.update(5,self.my_x + 4,self.my_y,   -0.8,-0.7,   6,    1   ,0,0,   0,-1,  8,8, 0,0,  0,0) #ペネトレートロケット
                  self.missile.append(new_missile)#ペネトレートロケット育成

                  new_missile = Missile()
                  new_missile.update(5,self.my_x + 4,self.my_y,   -1,-0.8,   6,    1   ,0,0,   0,1,     8,8, 0,0,  0,0) #ペネトレートロケット
                  self.missile.append(new_missile)#ペネトレートロケット育成

                  new_missile = Missile()
                  new_missile.update(5,self.my_x + 4,self.my_y,   -1,-0.8,   6,    1   ,0,0,   0,-1,    8,8, 0,0,  0,0) #ペネトレートロケット
                  self.missile.append(new_missile)#ペネトレートロケット育成
                  
              
              self.count_missile_type(4,4,4,4) #ミサイルタイプ4(テイルショット）がいくつ存在するのか調べる
              if self.type_check_quantity == 0 and self.select_sub_weapon_id == TAIL_SHOT:#もしテイルショットが全く存在しないのなら発射する！！！
                  new_missile = Missile()
                  new_missile.update(4,self.my_x - 4,self.my_y,   -2,0,   3,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                  self.missile.append(new_missile)#テイルショット育成

              self.count_missile_type(6,6,6,6) #ミサイルタイプ6(サーチレーザー）がいくつ存在するのか調べる
              if self.type_check_quantity <= 1 and self.select_sub_weapon_id == SEARCH_LASER and pyxel.frame_count % 32 == 0: #サーチレーザーが全く存在しないのなら発射する！！！
                  new_missile = Missile()
                  new_missile.update(6,self.my_x + 14,self.my_y,   2,0,   1,1,   0,1,   0,0,   16,8,  0,0,  0,0) #サーチレーザー(flag2=1なのでちょっとｘ軸前方向に対して索敵する)
                  self.missile.append(new_missile)#サーチレーザー育成

                  new_missile = Missile()
                  new_missile.update(6,self.my_x     ,self.my_y,   2,0,   1,1,   0,0,   0,0,   16,8,  0,0,  0,0) #サーチレーザー
                  self.missile.append(new_missile)#サーチレーザー育成

              self.count_missile_type(7,7,7,7) #ミサイルタイプ7(ホーミングミサイル）がいくつ存在するのか調べる
              if self.type_check_quantity <= (self.sub_weapon_list[HOMING_MISSILE] * 4) - 4 and self.select_sub_weapon_id == HOMING_MISSILE and pyxel.frame_count % 8 == 0: #ホーミングミサイルの個数が1以下なら発射する！！！
                  new_missile = Missile()
                  new_missile.update(7,self.my_x - 4,self.my_y,   -2,1,   0.5,1,   0,0,   0,0,   8,8,      200,60,   2,1)
                  self.missile.append(new_missile)#ホーミングミサイル育成

                  new_missile = Missile()
                  new_missile.update(7,self.my_x - 4,self.my_y,   -2,-1,   0.5,1,   0,0,   0,0,   8,8,      200,60,   2,1)
                  self.missile.append(new_missile)#ホーミングミサイル育成


                  new_missile = Missile()
                  new_missile.update(7,self.my_x + 4,self.my_y + 2,   0,2,   0.5,1,   0,0,   0,0,   8,8,      200,60,   2,1)
                  self.missile.append(new_missile)#ホーミングミサイル育成

                  new_missile = Missile()
                  new_missile.update(7,self.my_x + 4,self.my_y - 2,   0,-2,   0.5,1,   0,0,   0,0,   8,8,      200,60,   2,1)
                  self.missile.append(new_missile)#ホーミングミサイル育成

              if len(self.shots) < (self.shot_rapid_of_fire + (self.shot_level) * 2):#バルカンショットの発射
               if (pyxel.frame_count % 6) == 0:    
                    if self.shot_level == 0:#初期ショット バルカンショット1連装
                              pyxel.play(2,1)
                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 4,self.my_y    ,4,0,  8,8,     0, 1,1)
                              self.shots.append(new_shot)
                    if self.shot_level == 1:#ツインバルカンショット 2連装
                              pyxel.play(2,1)
                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 2,4,0,  8,8,     0,  1,1)
                              self.shots.append(new_shot)

                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 2,4,0,  8,8,      0,  1,1)
                              self.shots.append(new_shot)
                    if self.shot_level == 2:#３ＷＡＹバルカンショット
                              pyxel.play(2,1)
                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 2  ,5,-0.3,  8,8,     0,  1,1)
                              self.shots.append(new_shot)

                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 6,self.my_y      ,5,0,     8,8,     0,  1,1)
                              self.shots.append(new_shot)

                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 2  ,5,0.3,   8,8,     0,  1,1)
                              self.shots.append(new_shot)
                    if self.shot_level == 3:#５ＷＡＹバルカンショット
                              pyxel.play(2,1)
                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 2,    5,-1,     8,8,     0,  1,1)
                              self.shots.append(new_shot)

                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 1,    5,-0.3,   8,8,     0,  1,1)
                              self.shots.append(new_shot)

                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 6,self.my_y,        5,0,      8,8,     0,  1,1)
                              self.shots.append(new_shot)

                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 1,    5,0.3,    8,8,     0,  1,1)
                              self.shots.append(new_shot)

                              new_shot = Shot()
                              new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 2,    5,1,      8,8,     0,  1,1)
                              self.shots.append(new_shot)

     #スペースキーかゲームバットＢボタンが押されたらミサイルを発射する
     def update_fire_missile(self): 
          if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD_1_B) or pyxel.btn(pyxel.GAMEPAD_2_B):
              if (pyxel.frame_count % 10) == 0:
                   self.count_missile_type(0,1,2,3)#ミサイルタイプ0,1,2,3の合計数を数える
                   if self.type_check_quantity < (self.missile_level + 1) * self.missile_rapid_of_fire:  #初期段階では２発以上は出せないようにする
                        if self.missile_level == 0:
                             pyxel.play(2,1)

                             new_missile = Missile()
                             new_missile.update(0,self.my_x + 4,self.my_y,   0.7,0.7,   3,    1   ,0,0,    1,1,  8,8  ,0,0,   0,0) #前方右下に落ちていくミサイル
                             self.missile.append(new_missile)#ミサイル育成

                        elif self.missile_level == 1:
                             pyxel.play(2,1)
                        
                             new_missile = Missile()
                             new_missile.update(0,self.my_x + 2,self.my_y +2,   0.7,0.7,   3,    1   ,0,0,    1,1,  8,8,  0,0,   0,0) #前方右下に落ちていくミサイル
                             self.missile.append(new_missile)#ミサイル育成
                      
                             new_missile = Missile()
                             new_missile.update(1,self.my_x + 2,self.my_y -2,   0.7,0.7,   3,     1   ,0,0    ,1,-1,  8,8,  0,0,  0,0) #前方右上に飛んでいくミサイル
                             self.missile.append(new_missile)#ミサイル育成

                        elif self.missile_level == 2:
                             pyxel.play(2,1)
                        
                             new_missile = Missile()
                             new_missile.update(0,self.my_x +2,self.my_y +2,   0.7,0.7,    3,    1   ,0,0,    1,1,   8,8,  0,0,  0,0) #前方右下に落ちていくミサイル
                             self.missile.append(new_missile)#ミサイル育成

                             new_missile = Missile()
                             new_missile.update(1,self.my_x +2,self.my_y -2,   0.7,0.7,    3,     1   ,0,0    ,1,-1,   8,8,  0,0,  0,0) #前方右上に飛んでいくミサイル
                             self.missile.append(new_missile)#ミサイル育成

                             new_missile = Missile()
                             new_missile.update(2,self.my_x -2,self.my_y +2,   -0.7,0.7,   3,    1   ,0,0,    -1,1,    8,8,  0,0,   0,0) #後方左下に落ちていくミサイル
                             self.missile.append(new_missile)#ミサイル育成

                             new_missile = Missile()
                             new_missile.update(3,self.my_x -2,self.my_y -2,   -0.7,0.7,   3,     1   ,0,0    ,-1,-1,   8,8,  0,0,   0,0) #後方左上に飛んでいくミサイル
                             self.missile.append(new_missile)#ミサイル育成
     
     #自機をはみ出さないようにする
     def update_clip_my_ship(self):
          if     self.game_status == SCENE_STAGE_CLEAR_MY_SHIP_BOOST\
              or self.game_status == SCENE_STAGE_CLEAR_FADE_OUT: #ステータスが「ブースト加速して去る」「ステージクリアフェードアウト」なら
               if self.my_x < 0:
                    self.my_x = 0
               if self.my_x >= WINDOW_W + 80:
                    self.my_x = WINDOW_W + 80
               return  #x軸はある程度まではみ出してok
          else:
               if self.my_x < 0:
                    self.my_x = 0
               if self.my_x >= WINDOW_W - MOVE_LIMIT:
                    self.my_x = WINDOW_W - MOVE_LIMIT - 1
    
          
          if self.my_y < 0:
               self.my_y = 0
          if self.my_y >= WINDOW_H - SHIP_H:
               self.my_y = WINDOW_H - SHIP_H - 1
     
     #################################自機弾関連の処理関数###############################################
     #自機弾の更新
     def update_my_shot(self):
          shot_count = len(self.shots)#弾の数を数える
          for i in reversed(range (shot_count)):
                    #弾の位置を更新！
                    if 0 <= self.shots[i].shot_type <= 3:#ショットタイプがバルカンショットの場合
                         self.shots[i].posx += self.shots[i].vx * self.shot_speed_magnification #弾のX座標をVX*speed_magnification(倍率)分加減算して更新
                         self.shots[i].posy += self.shots[i].vy                                 #弾のY座標をVY分加減算して更新

                    elif 4 <= self.shots[i].shot_type <= 6:#ショットタイプがレーザーの場合
                         self.shots[i].posx += self.shots[i].vx#弾のX座標をVX分加減算して更新
                         self.shots[i].offset_y = self.shots[i].offset_y * self.shots[i].vy#Ｙ軸オフセット値 vyの倍率ごと乗算して行って上下にずらしていく
                         self.shots[i].posy = self.my_y + self.shots[i].offset_y#自機のｙ座標+Ｙ軸オフセット値をレーザーのＹ座標としてコピーする（ワインダー処理）
                         self.shots[i].shot_hp = 1#レーザーなのでHPは減らず強制的にＨＰ＝１にする（ゾンビ化～みたいな）
                    

                    elif 7 <= self.shots[i].shot_type <= 10:#ショットタイプがウェーブカッターの場合
                         self.shots[i].posx += self.shots[i].vx * self.shot_speed_magnification #弾のX座標をVX*speed_magnification(倍率)分加減算して更新
                         self.shots[i].posy += self.shots[i].vy                                 #弾のY座標をVY分加減算して更新
                         self.shots[i].shot_hp = 1#ウェーブカッターはHPは減らず強制的にＨＰ＝１にする（ゾンビ化～みたいな）
                    


                    if self.shots[i].shot_hp == 0:
                       del self.shots[i]#自機弾のHPがゼロだったらインスタンスを破棄する（弾消滅） 

     #自機弾のはみだしチェック（はみ出て画面外に出てしまったら消去する)
     def update_clip_my_shot(self):
          shot_count = len(self.shots)#弾の数を数える
          for i in reversed(range (shot_count)):
               if (-16 < self.shots[i].posx < WINDOW_W + 16 ) and (-16 <self.shots[i].posy < WINDOW_H + 16):
                    continue
               else:
                    del self.shots[i]

     #自機弾と敵の当たり判定
     def update_collision_my_shot_enemy(self):
          shot_hit = len(self.shots)
          for h in reversed(range (shot_hit)):
              enemy_hit = len(self.enemy)
              for e in reversed(range (enemy_hit)):#ウェーブカッターの分も含めてＹ軸方向の幅の大きさも考えた当たり判定にする、Ｘ軸方向の当たり判定は普通に8ドット単位で行う
                  if     self.enemy[e].posx                        <= self.shots[h].posx + 4 <= self.enemy[e].posx + self.enemy[e].width\
                     and self.enemy[e].posy - self.shots[h].height <= self.shots[h].posy + 4 <= self.enemy[e].posy + self.enemy[e].height:

                      self.enemy[e].enemy_hp -= self.shots[h].shot_power #敵の耐久力をShot_powerの分だけ減らす
                      if self.enemy[e].enemy_hp <= 0:
                          self.enemy_destruction(e) #敵破壊処理関数呼び出し！
                          #パーティクル生成
                          for _number in range(5):
                               self.update_append_particle(PARTICLE_DOT,self.enemy[e].posx + 4,self.enemy[e].posy + 4,self.shots[h].vx / 2,self.shots[h].vy / 2, 0,0,0)
                      
                          #スコア加算
                          if self.enemy[e].status == ENEMY_STATUS_NORMAL:   #ステータスが「通常」ならscore_normalをpointとしてスコアを加算する
                               point = self.enemy[e].score_normal
                          elif self.enemy[e].status == ENEMY_STATUS_ATTACK: #ステータスが「攻撃中」ならscore_attackをpointとしてスコアを加算する
                               point = self.enemy[e].score_attack
                          elif self.enemy[e].status == ENEMY_STATUS_ESCAPE: #ステータスが「撤退中」ならscore_escapeをpointとしてスコアを加算する
                               point = self.enemy[e].score_escape
                          elif self.enemy[e].status == ENEMY_STATUS_AWAITING: #ステータスが「待機中」ならscore_awaitingをpointとしてスコアを加算する
                               point = self.enemy[e].score_awaiting
                          elif self.enemy[e].status == ENEMY_STATUS_DEFENSE: #ステータスが「防御中」ならscore_defenseをpointとしてスコアを加算する
                               point = self.enemy[e].score_defense
                          elif self.enemy[e].status == ENEMY_STATUS_BERSERK: #ステータスが「怒り状態」ならscore_berserkをpointとしてスコアを加算する
                               point = self.enemy[e].score_berserk
                          else:                                              #ステータスが以上に当てはまらないときはscore_normalとする
                               point = self.enemy[e].score_normal

                          self.add_score(point) #スコアを加算する関数の呼び出し
                          del self.enemy[e] #敵リストから破壊した敵をdel消去破壊するっ！
                    
                      self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させるため
                      pyxel.play(0,2)#変な爆発音を出すのだ～～～☆彡
              else:
                  continue
     
     #自機弾とボスとの当たり判定
     def update_collision_my_shot_boss(self):
          shot_hit = len(self.shots)
          for h in reversed(range (shot_hit)):
              boss_hit = len(self.boss)
              for e in reversed(range (boss_hit)):#ウェーブカッターの分も含めてＹ軸方向の幅の大きさも考えた当たり判定にする、Ｘ軸方向の当たり判定は普通に8ドット単位で行う
                  if self.boss[e].invincible != 1: #もしボスが無敵状態で無いのならば
                       #ボス本体の当たり判定1(弾を消滅させる)との判定
                       if         self.boss[e].posx                       + self.boss[e].col_main1_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main1_x + self.boss[e].col_main1_w\
                            and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main1_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main1_y + self.boss[e].col_main1_h\
                            and self.boss[e].col_main1_w != 0:
  
                              self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                              self.shots[h].shot_hp = 0#自機弾のＨＰをゼロして自機弾移動時にチェックしリストから消去させる
                              continue #これ以下の処理はせず次のループへと移行する
                       #ボス本体の当たり判定2(弾を消滅させる)との判定
                       if         self.boss[e].posx                       + self.boss[e].col_main2_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main2_x + self.boss[e].col_main2_w\
                            and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main2_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main2_y + self.boss[e].col_main2_h\
                            and self.boss[e].col_main2_w != 0:
  
                              self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                              self.shots[h].shot_hp = 0#自機弾のＨＰをゼロして自機弾移動時にチェックしリストから消去させる
                              continue #これ以下の処理はせず次のループへと移行する
                       #ボス本体の当たり判定3(弾を消滅させる)との判定
                       if         self.boss[e].posx                       + self.boss[e].col_main3_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main3_x + self.boss[e].col_main3_w\
                            and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main3_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main3_y + self.boss[e].col_main3_h\
                            and self.boss[e].col_main3_w != 0:
  
                              self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                              self.shots[h].shot_hp = 0#自機弾のＨＰをゼロして自機弾移動時にチェックしリストから消去させる
                              continue #これ以下の処理はせず次のループへと移行する
                       #ボス本体の当たり判定4(弾を消滅させる)との判定
                       if         self.boss[e].posx                       + self.boss[e].col_main4_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main4_x + self.boss[e].col_main4_w\
                            and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main4_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main4_y + self.boss[e].col_main4_h\
                            and self.boss[e].col_main4_w != 0:
  
                              self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                              self.shots[h].shot_hp = 0#自機弾のＨＰをゼロして自機弾移動時にチェックしリストから消去させる
                              continue #これ以下の処理はせず次のループへと移行する
                       #ボス本体の当たり判定5(弾を消滅させる)との判定
                       if         self.boss[e].posx                       + self.boss[e].col_main5_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main5_x + self.boss[e].col_main5_w\
                            and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main5_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main5_y + self.boss[e].col_main5_h\
                            and self.boss[e].col_main5_w != 0:
  
                              self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                              self.shots[h].shot_hp = 0#自機弾のＨＰをゼロして自機弾移動時にチェックしリストから消去させる
                              continue #これ以下の処理はせず次のループへと移行する
                       #ボス本体の当たり判定6(弾を消滅させる)との判定
                       if         self.boss[e].posx                       + self.boss[e].col_main6_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main6_x + self.boss[e].col_main6_w\
                            and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main6_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main6_y + self.boss[e].col_main6_h\
                            and self.boss[e].col_main6_w != 0:
  
                              self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                              self.shots[h].shot_hp = 0#自機弾のＨＰをゼロして自機弾移動時にチェックしリストから消去させる
                              continue #これ以下の処理はせず次のループへと移行する
                       #ボス本体の当たり判定7(弾を消滅させる)との判定
                       if         self.boss[e].posx                       + self.boss[e].col_main7_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main7_x + self.boss[e].col_main7_w\
                            and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main7_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main7_y + self.boss[e].col_main7_h\
                            and self.boss[e].col_main7_w != 0:
  
                              self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                              self.shots[h].shot_hp = 0#自機弾のＨＰをゼロして自機弾移動時にチェックしリストから消去させる
                              continue #これ以下の処理はせず次のループへと移行する
                       #ボス本体の当たり判定8(弾を消滅させる)との判定
                       if         self.boss[e].posx                       + self.boss[e].col_main8_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main8_x + self.boss[e].col_main8_w\
                            and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main8_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main8_y + self.boss[e].col_main8_h\
                            and self.boss[e].col_main8_w != 0:
  
                              self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                              self.shots[h].shot_hp = 0#自機弾のＨＰをゼロして自機弾移動時にチェックしリストから消去させる
                              continue #これ以下の処理はせず次のループへと移行する
                       
                       
                       #パーツ１との当たり判定
                       if         self.boss[e].posx + self.boss[e].col_parts1_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts1_x + self.boss[e].col_parts1_w\
                              and self.boss[e].posy + self.boss[e].col_parts1_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts1_y + self.boss[e].col_parts1_h\
                              and self.boss[e].parts1_flag == 1:
                              
                              self.boss[e].parts1_hp -= self.shots[h].shot_power #パーツ1の耐久力をShot_powerの分だけ減らす
                              if self.boss[e].parts1_hp <= 0: #パーツ1の耐久力が0以下になったのなら
                                  self.boss[e].parts1_flag = 0 #パーツ1の生存フラグを0にして破壊したことにする

                              self.boss[e].display_time_parts1_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ1耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                              self.boss_processing_after_hitting(h,e) #ボスにショットを当てた後の処理の関数を呼び出す！
                              continue #これ以下の処理はせず次のループへと移行する   
                       #パーツ2との当たり判定
                       if         self.boss[e].posx + self.boss[e].col_parts2_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts2_x + self.boss[e].col_parts2_w\
                              and self.boss[e].posy + self.boss[e].col_parts2_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts2_y + self.boss[e].col_parts2_h\
                              and self.boss[e].parts2_flag == 1:
                              
                              self.boss[e].parts2_hp -= self.shots[h].shot_power #パーツ2の耐久力をShot_powerの分だけ減らす
                              if self.boss[e].parts2_hp <= 0: #パーツ2の耐久力が0以下になったのなら
                                  self.boss[e].parts2_flag = 0 #パーツ2の生存フラグを0にして破壊したことにする

                              self.boss[e].display_time_parts2_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ2耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                              self.boss_processing_after_hitting(h,e) #ボスにショットを当てた後の処理の関数を呼び出す！ 
                              continue #これ以下の処理はせず次のループへと移行する                         
                       #パーツ3との当たり判定
                       if         self.boss[e].posx + self.boss[e].col_parts3_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts3_x + self.boss[e].col_parts3_w\
                              and self.boss[e].posy + self.boss[e].col_parts3_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts3_y + self.boss[e].col_parts3_h\
                              and self.boss[e].parts3_flag == 1:
                              
                              self.boss[e].parts3_hp -= self.shots[h].shot_power #パーツ3の耐久力をShot_powerの分だけ減らす
                              if self.boss[e].parts3_hp <= 0: #パーツ3の耐久力が0以下になったのなら
                                  self.boss[e].parts3_flag = 0 #パーツ3の生存フラグを0にして破壊したことにする

                              self.boss[e].display_time_parts3_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ3耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                              self.boss_processing_after_hitting(h,e) #ボスにショットを当てた後の処理の関数を呼び出す！
                              continue #これ以下の処理はせず次のループへと移行する                      
                       #パーツ4との当たり判定
                       if         self.boss[e].posx + self.boss[e].col_parts4_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts4_x + self.boss[e].col_parts4_w\
                              and self.boss[e].posy + self.boss[e].col_parts4_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts4_y + self.boss[e].col_parts4_h\
                              and self.boss[e].parts4_flag == 1:
                              
                              self.boss[e].parts4_hp -= self.shots[h].shot_power #パーツ4の耐久力をShot_powerの分だけ減らす
                              if self.boss[e].parts4_hp <= 0: #パーツ4の耐久力が0以下になったのなら
                                  self.boss[e].parts4_flag = 0 #パーツ4の生存フラグを0にして破壊したことにする

                              self.boss[e].display_time_parts4_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ4耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                              self.boss_processing_after_hitting(h,e) #ボスにショットを当てた後の処理の関数を呼び出す！
                              continue #これ以下の処理はせず次のループへと移行する                      
                      
                       #ダメージポイント1との判定
                       if         self.boss[e].posx                      + self.boss[e].col_damage_point1_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point1_x + self.boss[e].col_damage_point1_w\
                            and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_damage_point1_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point1_y + self.boss[e].col_damage_point1_h\
                            and self.boss[e].col_damage_point1_w != 0:
  
                              self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                              self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                              self.boss_processing_after_hitting(h,e) #ボスにショットを当てた後の処理の関数を呼び出す！
                              continue #これ以下の処理はせず次のループへと移行する
                       #ダメージポイント2との判定
                       if         self.boss[e].posx                      + self.boss[e].col_damage_point2_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point2_x + self.boss[e].col_damage_point2_w\
                            and self.boss[e].posy - self.shots[h].height + self.boss[e].col_damage_point2_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point2_y + self.boss[e].col_damage_point2_h\
                            and self.boss[e].col_damage_point2_w != 0:
  
                              self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                              self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                              self.boss_processing_after_hitting(h,e) #ボスにショットを当てた後の処理の関数を呼び出す！
                              continue #これ以下の処理はせず次のループへと移行する
                       #ダメージポイント3との判定
                       if         self.boss[e].posx                      + self.boss[e].col_damage_point3_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point3_x + self.boss[e].col_damage_point3_w\
                            and self.boss[e].posy - self.shots[h].height + self.boss[e].col_damage_point3_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point3_y + self.boss[e].col_damage_point3_h\
                            and self.boss[e].col_damage_point3_w != 0:
  
                              self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                              self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                              self.boss_processing_after_hitting(h,e) #ボスにショットを当てた後の処理の関数を呼び出す！
                              continue #これ以下の処理はせず次のループへと移行する
                       #ダメージポイント4との判定
                       if         self.boss[e].posx                      + self.boss[e].col_damage_point4_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point4_x + self.boss[e].col_damage_point4_w\
                            and self.boss[e].posy - self.shots[h].height + self.boss[e].col_damage_point4_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point4_y + self.boss[e].col_damage_point4_h\
                            and self.boss[e].col_damage_point4_w != 0:
  
                              self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                              self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                              self.boss_processing_after_hitting(h,e) #ボスにショットを当てた後の処理の関数を呼び出す！ 
                              continue #これ以下の処理はせず次のループへと移行する     
     
     #自機弾と背景障害物の当たり判定
     def update_collision_my_shot_bg(self):
          if  0 <= self.shot_level <= 6:#ウェーブカッターの場合は背景は貫通する
              shot_count = len(self.shots)
              for i in reversed(range(shot_count)):
                   self.check_bg_collision(self.shots[i].posx,self.shots[i].posy + 4,0,0)
                   if self.collision_flag == 1:
                        self.update_append_particle(PARTICLE_LINE,self.shots[i].posx,self.shots[i].posy,0,0, 0,0,0)
                        del self.shots[i]     
     
     #################################自機ミサイル関連の処理関数##########################################
     #自機ミサイルのはみだしチェック（はみ出て画面外に出てしまったら消去する）
     def update_clip_my_missile(self):
          missile_count = len(self.missile)#ミサイルリストの総数を数える
          for i in reversed(range (missile_count)):
               if (-24 < self.missile[i].posx < WINDOW_W + 18 ) and (-18 <self.missile[i].posy < WINDOW_H + 18):
                    continue
               else:
                    del self.missile[i]

     #自機ミサイルと敵の当たり判定
     def update_collision_missile_enemy(self):
          missile_hit = len(self.missile)
          for h in reversed(range (missile_hit)):
              enemy_hit = len(self.enemy)
              for e in reversed(range (enemy_hit)):
                  if      self.enemy[e].posx <= self.missile[h].posx + 4 <= self.enemy[e].posx +   self.enemy[e].width  + self.missile[h].width  / 2\
                      and self.enemy[e].posy <= self.missile[h].posy + 4 <= self.enemy[e].posy +   self.enemy[e].height + self.missile[h].height / 2:

                      self.enemy[e].enemy_hp -= self.missile[h].missile_power #敵の耐久力をミサイルパワーの分だけ減らす
                      if self.enemy[e].enemy_hp <= 0:
                          self.enemy_destruction(e) #敵破壊処理関数呼び出し！
                          #パーティクル生成
                          for _number in range(5):
                               self.update_append_particle(PARTICLE_DOT,self.enemy[e].posx + 4,self.enemy[e].posy + 4,self.missile[h].vx / 2,self.missile[h].vy / 2,   0,0,0)    
                      
                          del self.enemy[e]#敵リストから破壊した敵をＤＥＬ消去破壊！
                          self.score += 1#スコア加算（あとあといろんなスコアシステム実装する予定だよ）
                    
                      self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロにしてミサイル移動時にチェックしリストから消去させるため
                      pyxel.play(0,2)#ミサイルが敵を破壊した音！
              else:
                  continue

     #自機ミサイルの更新（背景障害物との当たり判定も行っています）
     def update_my_missile(self):
          missile_count = len(self.missile)#ミサイルの総数を数える
          for i in reversed(range (missile_count)):
              if 0 <= self.missile[i].missile_type <= 3:#通常ミサイルの処理
                    self.missile[i].vy = self.missile[i].y_reverse * 0.7#ミサイルの落下スピードを標準の0.7にしておく（ｙ軸反転を掛けて反転もさせる）
                    #ミサイルの真下（もしくは真上）が地形かどうか？チェック
                    self.check_bg_collision(self.missile[i].posx,(((self.missile[i].posy ) // 8) * 8) + self.missile[i].y_reverse + 8,  0,0)#これで上手くいった・・なんでや・・どうしてや？
                    
                    if self.collision_flag == 1:#障害物に当たった時の処理
                         self.missile[i].missile_flag1 = 1#もしミサイルの真下(y_reverseが-1なら真上）が障害物ならmissile_flag1を１にして
                         self.missile[i].vy = 0#縦方向の移動量vyを0にして横方向だけに進むようにする
                         if  2 <= self.missile[i].missile_type <= 3:
                              self.missile[i].vx = -1

                    #ミサイルの進行先が地形かどうか？チェック
                    self.check_bg_collision(self.missile[i].posx + (self.missile[i].x_reverse * 8),self.missile[i].posy + 4,0,0)
                    
                    if self.missile[i].missile_hp == 0:
                         del self.missile[i]#ミサイルのＨＰが0だったらインスタンスを破棄する（ミサイル消滅）
                                       
                    elif self.collision_flag == 1:
                         self.update_append_particle(PARTICLE_MISSILE_DEBRIS,self.missile[i].posx + (self.missile[i].missile_type // 2) * 2 - 8,self.missile[i].posy,0,0, 7,0,0)
                         #(self.missile[i].missile_type // 2) * 2 - 8の計算結果は
                         #ミサイルタイプが0右下ミサイルの場合は 0 // 2 * 2 - 8で -8
                         #ミサイルタイプが1右上ミサイルの場合は 1 // 2 * 2 - 8で -8
                         #ミサイルタイプが2左下ミサイルの場合は 2 // 2 * 2 - 8で +8
                         #ミサイルタイプが3左上ミサイルの場合は 3 // 2 * 2 - 8で +8となる よって補正値は右向きのミサイルの場合は-8 左向きのミサイルは+8となる
                         #
                         #う～ん、後方のミサイルは別にx+8の補正を入れなくても良いかもしれない・・・
                         #スクロールスピードの関係でミサイルデブリを表示した瞬間にスクロールして表示位置ずれるし
                         del self.missile[i]#ミサイルの右側が障害物だったらインスタンスを破棄する（ミサイル消滅）
                    else:
                        #進行先が地形ではなく尚且つミサイルのＨＰがまだ残っていたのなら、ミサイルの位置を更新！
                        if self.missile[i].vy == 0: #地面に設置して横方向動くときだけ倍率補正値を掛け合わせたvxとする
                            self.missile[i].posx += self.missile[i].vx * self.missile_speed_magnification #ミサイルのX座標を(VX*倍率補正)分加減算して更新
                        else:
                            self.missile[i].posx += self.missile[i].vx #上下に落ちていくときはミサイルのX座標をVXだけ加減算して更新
                        
                        self.missile[i].posy += self.missile[i].vy                                    #ミサイルのY座標をVY分加減算して更新                            
              elif    self.missile[i].missile_type == 4:#テイルショットの処理         
                  #テイルショットの位置が地形かどうか？チェック
                  self.check_bg_collision(self.missile[i].posx,self.missile[i].posy,0,0)
                  if self.collision_flag == 1 or self.missile[i].missile_hp == 0:
                       del self.missile[i]#テイルショットの位置が障害物かもしくはテイルショットのＨＰが0だったらインスタンスを破棄する（テイルショット消滅） 
                  else:
                        #進行先が地形ではなく尚且つテイルショットのＨＰがまだ残っていたのなら位置を更新！
                        self.missile[i].posx += self.missile[i].vx#テイルショットのX座標をVX分加減算して更新
                        self.missile[i].posy += self.missile[i].vy#テイルショットのY座標をVY分加減算して更新                     
              elif    self.missile[i].missile_type == 5:#ペネトレートロケットの処理
                  #進行先が地形ではなく尚且つペネトレートロケットのＨＰがまだ残っていたのなら位置を更新！
                  self.missile[i].vx += 0.02 #vxをだんだんと増加させていく
                  self.missile[i].posx += self.missile[i].vx #ペネトレートロケットのx座標をvxと足し合わせて更新
                  
                  self.missile[i].vy += 0.01 #vyをだんだんと増加させていく
                  self.missile[i].posy += self.missile[i].vy * self.missile[i].y_reverse #ペネトレートロケットのx,y座標をvx,vyと足し合わせて更新(y_reverseが-1ならy軸の補正が逆となる)             
              elif    self.missile[i].missile_type == 6:#サーチレーザーの処理         
                  #サーチレーザーの位置が地形かどうか？チェック
                  self.check_bg_collision(self.missile[i].posx,self.missile[i].posy,0,0)
                  if self.collision_flag == 1 or self.missile[i].missile_hp == 0:
                       del self.missile[i]#サーチレーザーの位置が障害物かもしくはサーチレーザーのＨＰが0だったらインスタンスを破棄する（サーチレーザー消滅） 
                  else:
                       self.missile[i].posx += self.missile[i].vx            #サーチレーザーのX座標をVX分加減算して更新
                       
                       if self.missile[i].missile_flag1 == 0:#状態遷移が(敵索敵中=0)なら
                            if self.missile[i].posx > self.my_x + 16:#サーチレーザーは自機より前方16ドット進んでから索敵を始める
                                 #索敵用関数の呼び出し(missile_flag2*16のぶんだけｘ方向の先で敵とのＸ座標を比較する)
                                 self.search_laser_enemy_cordinate(self.missile[i].posx + self.missile[i].missile_flag2 * 8,self.missile[i].posy)
                                 if self.search_laser_flag == 1:#敵機索敵ＯＫ！のフラグが立っていたのなら
                                      self.missile[i].missile_flag1 = 1 #状態遷移を(屈折中=1)にする                      
                                      self.missile[i].y_reverse = self.search_laser_y_direction #Y軸加算用の反転フラグ(-1=上方向 1=下方向)もそのまま代入
                                      
                                 
                       
                       elif self.missile[i].missile_flag1 == 1:#状態遷移が（屈折中=1)なら
                            self.missile[i].vx = 0 #x軸（横）に移動はさせないようvxに0を強制代入
                            self.missile[i].missile_flag1 = 2 #状態遷移を（縦に進行中=2)にする

                            self.missile[i].width  = 8   #レーザーは縦長になるので当たり判定は16x16に変化する(本当は8x16何だけど甘めに16x16にしちゃう)
                            self.missile[i].height = 16

                       elif self.missile[i].missile_flag1 == 2:#状態遷移が（縦に進行中=2)なら
                            self.missile[i].vx = 0 #x軸（横）に移動はさせないようvxに0を強制代入
                            #self.missile[i].posx += self.missile[i].vx            #サーチレーザーのX座標をVX分加減算して更新
                            self.missile[i].posy += self.missile[i].y_reverse * 2#サーチレーザーのY座標をy_reverse分加減算して更新     
              elif    self.missile[i].missile_type == 7:#ホーミングミサイルの処理         
                  if self.missile[i].missile_hp == 0:
                       del self.missile[i]#ホーミングミサイルのＨＰが0だったらインスタンスを破棄する（ホーミングミサイル消滅） 
                  else:
                      self.search_homing_missile_enemy_cordinate(self.missile[i].posx,self.missile[i].posy)#ホーミングミサイルのposx.posyを元に一番近距離の敵の座標を見つけ出す
                      if self.search_homing_missile_flag == 1:#もし狙い撃つ敵を見つけたのなら
                           self.missile[i].tx = self.search_homing_missile_tx #ターゲットとなる敵の座標をミサイルリストのTargetX,TargetYに代入する
                           self.missile[i].ty = self.search_homing_missile_ty
                
                      #ホーミングミサイルを目標位置まで追尾させる
                      vx0 = self.missile[i].vx
                      vy0 = self.missile[i].vy #ホーミングミサイルの速度(vx,vy)を(vx0,vy0)に退避する

                      #目標までの距離を求める dに距離が入る
                      #狙うターゲットとなる座標(tx,ty)
                      self.d = math.sqrt((self.missile[i].tx - self.missile[i].posx) * (self.missile[i].tx - self.missile[i].posx) + (self.missile[i].ty - self.missile[i].posy) * (self.missile[i].ty - self.missile[i].posy))
                
                      #ホーミングミサイルの速度 vx,vyを求める
                      #速さが一定値speedになるようにする
                      #目標までの距離dが0の時は速度を左方向にする
                      #theta(Θ)は旋回できる角度の上限
                      #ターゲット方向の速度ベクトル(vx1,vy1)を求める
                      if self.d == 0:#目標（ターゲット）までの距離は0だった？（重なっていた？）
                          vx1= 0
                          vy1 = self.missile[i].speed #目標までの距離dが0の時は速度を左方向にする
                      else:
                          #ホーミングミサイルとターゲットとの距離とＸ座標、Ｙ座標との差からＶＸ，ＶＹの増分を計算する
                         
                          vx1 = ((self.missile[i].tx - self.missile[i].posx) / (self.d * self.missile[i].speed))
                          vy1 = ((self.missile[i].ty - self.missile[i].posy) / (self.d * self.missile[i].speed))
                          #右回り旋回角度上限の速度ベクトル(vx2,vy2)を求める
                          #math.piはπ（円周率3.141592......)
                          #ううううぅ・・・難しい・・・・数学赤点の私には難しい・・・・
                          self.rad = 3.14 / 180 * self.missile[i].theta #rad = 角度degree（theta）をラジアンradianに変換
                          
                          self.missile[i].theta += 0.2 #旋回できる角度を増やしていく
                          if self.missile[i].theta > 360:
                              self.missile[i].theta = 360 #旋回可能角度は360度を超えないようにする
                
                          vx2 = math.cos(self.rad) * vx0 - math.sin(self.rad) * vy0
                          vy2 = math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0

                      #ターゲット方向に曲がるのか？ それとも旋回角度上限一杯（面舵一杯！とか取り舵一杯！とかそういう表現）で曲がるのか判別する
                      if vx0 * vx1 + vy0 * vy1 >= vx0 * vx2 + vy0 * vy2:
                          #ターゲット方向が旋回可能範囲内の場合の処理
                          #ターゲット方向に曲がるようにする
                          self.missile[i].vx = vx1
                          self.missile[i].vy = vy1
                      else:
                          #ターゲットが旋回可能範囲を超えている場合（ハンドルをいっぱいまで切ってもターゲットに追いつけないよ～）ハンドル一杯まで切る！
                          #左回り（取り舵方向）の旋回角度上限の速度ベクトルvx3,vy3を求める
                          vx3 =  math.cos(self.rad) * vx0 + math.sin(self.rad) * vy0
                          vy3 = -math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0

                          #ホーミングミサイルからターゲットへの相対ベクトル(px,py)を求める
                          px = self.missile[i].tx - self.missile[i].posx
                          py = self.missile[i].ty - self.missile[i].posy

                          #右回りか左回りを決める
                          #右回りの速度ベクトルの内積(p,v2)と左回りの速度ベクトルの内積(p,v3)の比較で右回りか左回りか判断する
                          #旋回角度が小さいほうが内積が大きくなるのでそちらの方に曲がるようにする
                          #
                          if px * vx2 + py * vy2 >= px * vx3 + py * vy3:
                              #右回り（面舵方向）の場合
                              self.missile[i].vx = vx2
                              self.missile[i].vy = vy2
                          else:
                              #左回り（取り舵方向）の場合
                              self.missile[i].vx = vx3
                              self.missile[i].vy = vy3
                        
                        
                        
                      #ホーミングミサイルの座標(posx,posy)を増分(vx,vy)を加減算更新して敵を移動させる(座標更新！)
                      self.missile[i].posx += self.missile[i].vx#ホーミングミサイルのX座標をVX分加減算して更新
                      self.missile[i].posy += self.missile[i].vy#ホーミングミサイルのY座標をVY分加減算して更新     
              
     #################################クロー関連の処理関数################################################
     #クローの更新
     def update_claw(self):
          if   self.claw_type == 0:#ローリングクローの時のみ実行
              #ひとつ前を回るクローとの回転角度の差の計算処理
              if self.claw_number == 4:#クロー4機の時の処理
                   self.claw[0].angle_difference = self.claw[1].degree - self.claw[0].degree
                   self.claw[1].angle_difference = self.claw[2].degree - self.claw[1].degree
                   self.claw[2].angle_difference = self.claw[3].degree - self.claw[2].degree
                   self.claw[3].angle_difference = self.claw[0].degree - self.claw[3].degree
              elif self.claw_number == 3:#クロー3機の時の処理
                   self.claw[0].angle_difference = self.claw[1].degree - self.claw[0].degree
                   self.claw[1].angle_difference = self.claw[2].degree - self.claw[1].degree
                   self.claw[2].angle_difference = self.claw[0].degree - self.claw[2].degree
              elif self.claw_number == 2:#クロー2機の時の処理
                   self.claw[0].angle_difference = self.claw[1].degree - self.claw[0].degree
                   self.claw[1].angle_difference = self.claw[0].degree - self.claw[1].degree
                   #クローが1機と0機の時は角度計算しないのです
              
              #クローの回転処理
              claw_count = len(self.claw)#クローの数を数える
              for i in range(claw_count):
                  if self.claw[i].status == 0:#ステータスが(0)の場合は回転開始の初期位置まで動いていく（自機の真上）
                     #self.claw[i].offset_x += self.claw[i].roll_vx
                     #self.claw[i].offset_y += self.claw[i].roll_vy#現在のオフセット座標値をroll_vx,roll_vyの分だけ加減算させていく
                     #
                     #self.claw[i].posx = self.my_x + self.claw[i].offset_x
                     #self.claw[i].posy = self.my_y + self.claw[i].offset_y#クローのX,Y座標をオフセット分だけ加減算させていって回転開始位置まで移動させてやる
                     #if  self.claw[i].offset_x == self.claw[i].offset_roll_x and self.claw[i].offset_y == self.claw[i].offset_roll_y:
                     #       self.claw[i].status = 1#回転開始初期位置のオフセット値まで行ったのならステータスを回転開始(1)にする
                      if self.claw[i].offset_x < self.claw[i].offset_roll_x:#offset_xとyをoffset_fix_xとyに+1ドット単位で増減させて同じ値に近づけていく
                              self.claw[i].offset_x += 1
                      elif self.claw[i].offset_x > self.claw[i].offset_roll_x:
                              self.claw[i].offset_x -= 1
                         
                      if self.claw[i].offset_y < self.claw[i].offset_roll_y:
                              self.claw[i].offset_y += 1
                      elif self.claw[i].offset_y > self.claw[i].offset_roll_y:
                              self.claw[i].offset_y -= 1

                      self.claw[i].posx = self.my_x + self.claw[i].offset_x
                      self.claw[i].posy = self.my_y + self.claw[i].offset_y#クローのX,Y座標をオフセット分だけ加減算させていって回転開始位置まで移動させてやる
                         
                      if  int(self.claw[i].offset_x) == int(self.claw[i].offset_roll_x) and int(self.claw[i].offset_y) == int(self.claw[i].offset_roll_y):
                             self.claw[i].status = 1#ローリングクロー回転開始初期位置のオフセット値まで行ったのならステータスを回転開始！！(1)にする 比較するときはint()を使って切り捨てた整数値で比較する
                                     
                  
                  
                  elif  self.claw[i].status == 1:#ステータスが(1)の場合は回転開始！
                      if self.claw[i].angle_difference == self.claw_difference:
                            self.claw[i].degree -= self.claw[i].speed#クローの個数に応じた回転間隔
                      elif self.claw[i].angle_difference > self.claw_difference:
                            self.claw[i].degree -= self.claw[i].speed - 1
                      else:
                            self.claw[i].degree -= self.claw[i].speed + 1


                      self.claw[i].degree = self.claw[i].degree % 360#角度は３６０で割った余りとする(0~359)
                      #極座標(r,θ)から直交座標(x,y)への変換は
                      #      x = r cos θ
                      #      y = r sin θ
                      self.claw[i].offset_x = self.claw[i].radius *   math.cos(math.radians(self.claw[i].degree))
                      self.claw[i].offset_y = self.claw[i].radius *  -math.sin(math.radians(self.claw[i].degree))

                      
                      #クローの座標を自機の座標を中心としオフセット値を足した物とする
                      #線形補間値0.2で線形補間してやる（ピッタリ自機に付いてくる）
                      self.claw[i].posx = self.claw[i].posx + 0.2 * ((self.my_x + self.claw[i].offset_x) - self.claw[i].posx)
                      self.claw[i].posy = self.claw[i].posy + 0.2 * ((self.my_y + self.claw[i].offset_y) - self.claw[i].posy)
          elif self.claw_type == 1:#トレースクローの時のみ実行
               for i in range(self.claw_number):#iの値は0からクローの数まで増えてイクです  ハイ！
                  self.claw[i].status = 1#トレースクローは出現と同時に移動開始のステータスにする
                  self.claw[i].posx = self.claw_coordinates[self.trace_claw_index + (TRACE_CLAW_BUFFER_SIZE - self.trace_claw_distance) - self.trace_claw_distance * i].posx#クローの座標をオフセット値のＸＹ座標とする
                  self.claw[i].posy = self.claw_coordinates[self.trace_claw_index + (TRACE_CLAW_BUFFER_SIZE - self.trace_claw_distance) - self.trace_claw_distance * i].posy
          elif self.claw_type == 2:#フィックスクローの時のみ実行
               claw_count = len(self.claw)#クローの数を数える
               for i in range(claw_count):
                    if self.claw[i].status == 0:#ステータスが(0)の場合はフイックスクローの初期位置まで動いていく（自機の上か下）
                         if self.claw[i].offset_x < self.claw[i].offset_fix_x:#offset_xとyをoffset_fix_xとyに0.5単位で増減させて同じ値に近づけていく
                              self.claw[i].offset_x += 0.5
                         elif self.claw[i].offset_x > self.claw[i].offset_fix_x:
                              self.claw[i].offset_x -= 0.5
                         
                         if self.claw[i].offset_y < self.claw[i].offset_fix_y:
                              self.claw[i].offset_y += 0.5
                         elif self.claw[i].offset_y > self.claw[i].offset_fix_y:
                              self.claw[i].offset_y -= 0.5

                         self.claw[i].posx = self.my_x + self.claw[i].offset_x
                         self.claw[i].posy = self.my_y + self.claw[i].offset_y#クローのX,Y座標をオフセット分だけ加減算させていってクロ―固定位置まで移動させてやる
                         
                         if  -0.5 <= self.claw[i].offset_x - self.claw[i].offset_fix_x <= 0.5 and -0.5 <= self.claw[i].offset_y - self.claw[i].offset_fix_y <= 0.5:
                             self.claw[i].status = 1#クロー固定位置のオフセット値付近(+-0.5)まで行ったのならステータスをクロー固定完了！！(1)にする
                    
                    elif self.claw[i].status == 1:#ステータスが(1)の場合はフイックスクローの固定は完了したので弾を発射とかしちゃう
                         if i <=1:
                              #クローの座標を自機の座標を中心としオフセット値を足した物とする
                              #クローナンバー0と1（内側のクロー）は線形補間値0.2で線形補間してやる（ピッタリ自機に付いてくる）
                              self.claw[i].posx = self.claw[i].posx + 0.2 * (self.my_x + self.claw[i].offset_x - self.claw[i].posx)
                              self.claw[i].posy = self.claw[i].posy + 0.2 * (self.my_y + (self.claw[i].offset_y * self.fix_claw_magnification) - self.claw[i].posy)
                         else:
                              #クローの座標を自機の座標を中心としオフセット値を足した物とする
                              #クローナンバー2と3（外側のクロー）は線形補間値0.1で線形補間してやる（ちょっと遅れて自機に引っ付いてくる）
                              self.claw[i].posx = self.claw[i].posx + 0.1 * (self.my_x + self.claw[i].offset_x - self.claw[i].posx)
                              self.claw[i].posy = self.claw[i].posy + 0.1 * (self.my_y + (self.claw[i].offset_y * self.fix_claw_magnification) - self.claw[i].posy)
          elif self.claw_type == 3:#リバースクローの時のみ実行
               claw_count = len(self.claw)#クローの数を数える
               for i in range(claw_count):
                    if self.claw[i].status == 0:#ステータスが(0)の場合はリバースクローの初期位置まで動いていく（自機の上か下）
                         if self.claw[i].offset_x < self.claw[i].offset_reverse_x:#offset_xとyをoffset_reverse_xとyに0.5単位で増減させて同じ値に近づけていく
                              self.claw[i].offset_x += 0.5
                         elif self.claw[i].offset_x > self.claw[i].offset_reverse_x:
                              self.claw[i].offset_x -= 0.5
                         
                         if self.claw[i].offset_y < self.claw[i].offset_reverse_y:
                              self.claw[i].offset_y += 0.5
                         elif self.claw[i].offset_y > self.claw[i].offset_reverse_y:
                              self.claw[i].offset_y -= 0.5

                         self.claw[i].posx = self.my_x + self.claw[i].offset_x
                         self.claw[i].posy = self.my_y + self.claw[i].offset_y#クローのX,Y座標をオフセット分だけ加減算させていってクロ―固定位置まで移動させてやる
                         
                         if  -0.5 <= self.claw[i].offset_x - self.claw[i].offset_reverse_x <= 0.5 and -0.5 <= self.claw[i].offset_y - self.claw[i].offset_reverse_y <= 0.5:
                             self.claw[i].status = 1#リバースクローの開始のオフセット値付近(+-0.5)まで行ったのならステータスをクロー固定完了！！(1)にする
                    
                    elif self.claw[i].status == 1:#ステータスが(1)の場合はリバースクローの固定は完了したので弾を発射とかしちゃう
                         if i == 1 or i == 2:
                              #クローの座標を自機の座標を中心としオフセット値を足した物とする
                              #クローナンバー1と2（上下のクロー）は線形補間値0.3で線形補間してやる（ピッタリ自機に付いてくる）
                              self.claw[i].posx = self.claw[i].posx + 0.3 * (self.my_x + self.claw[i].offset_x - self.claw[i].posx)
                              self.claw[i].posy = self.claw[i].posy + 0.3 * (self.my_y + self.claw[i].offset_y - self.claw[i].posy)
                         else:
                              #クローの座標を自機の座標を中心としオフセット値を足した物とする
                              #クローナンバー0と3（後部についてくるクロー）は線形補間値0.2で線形補間してやる（ちょっと遅れて自機に引っ付いてくる）
                              self.claw[i].posx = self.claw[i].posx + 0.2 * (self.my_x + self.claw[i].offset_x - self.claw[i].posx)
                              if self.claw_number == 4:#クローが4機の場合は定着させるＹ座標をそれぞれ変化させる
                                   self.claw[i].posy = self.claw[i].posy + 0.2 * (self.my_y + self.claw[i].offset_y + ((i * 3) - 4) - self.claw[i].posy)
                                   #クローナンバーi=0の時は(i*3)-4=0*3-4=-4で Y軸の補正値が-4になる
                                   #クローナンバーi=3の時は(i*3)-4=3*3-4=+5で Y軸の補正値が+5になる
                              else:#クローが１～３機のときは固定位置は変化させない
                                   self.claw[i].posy = self.claw[i].posy + 0.2 * (self.my_y + self.claw[i].offset_y - self.claw[i].posy)
 
     #クローが弾を発射する処理
     def update_fire_claw_shot(self):
          if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD_1_A) or pyxel.btn(pyxel.GAMEPAD_2_A):
              if (pyxel.frame_count % 16) == 0:#発射ボタンが押され尚且つ8フレーム毎だったら クローショットを育成する
                  if len(self.claw_shot) < CLAW_RAPID_FIRE_NUMBER * (self.claw_number):#クローショットの要素数がクローの数x２以下なら弾を発射する
                      #ここからクローが弾を発射する実処理
                      claw_count = len(self.claw)#クローの数を数える
                      for i in range(claw_count):
                          if self.claw[i].status != 0:#ステータスが0の時は初期回転位置や初期固定位置に移動中なので弾は発射しない
                             new_claw_shot = Shot()
                             if self.claw_type == 3:#クロータイプがリバースクローの時はクローショットの方向をreverse_claw_svx,reverse_claw_svyにして8方向弾にする
                                  new_claw_shot.update(0,self.claw[i].posx,self.claw[i].posy,     self.reverse_claw_svx,self.reverse_claw_svy,   8,8,   0,  1,1)
                                  self.claw_shot.append(new_claw_shot)
                             else:#リバースクロー以外のクローは全て前方に弾を撃つ
                                  new_claw_shot.update(0,self.claw[i].posx,self.claw[i].posy,    3,0,   8,8,   0,  1,1)
                                  self.claw_shot.append(new_claw_shot)

     #クローショットの更新
     def update_claw_shot(self):
          claw_shot_count = len(self.claw_shot)#クローの弾の数を数える
          for i in reversed(range (claw_shot_count)):
                    #クローの弾の位置を更新！
                    self.claw_shot[i].posx += self.claw_shot[i].vx * self.claw_shot_speed #弾のX座標をVX*claw_shot_speed分加減算して更新
                    self.claw_shot[i].posy += self.claw_shot[i].vy * self.claw_shot_speed #弾のY座標をVY*claw_shot_speed分加減算して更新
                    
                    if self.claw_shot[i].shot_hp != 0:
                       if (-16 < self.claw_shot[i].posx < WINDOW_W + 16 ) and (-16 <self.claw_shot[i].posy < WINDOW_H + 16):
                             continue
                       else:
                           del self.claw_shot[i]#クローショットが画面外まで飛んで行ってはみ出ていたのならインスタンス破棄（クローショット消滅）
                    else:
                        del self.claw_shot[i]#クローショットのHPがゼロだったらインスタンスを破棄する（クローショット消滅）
     
     #クローショットと敵の当たり判定
     def update_collision_claw_shot_enemy(self):
          claw_shot_hit = len(self.claw_shot)#クローの弾の数を数える
          for h in reversed(range (claw_shot_hit)):
              enemy_hit = len(self.enemy)
              for e in reversed(range (enemy_hit)):
                  if      self.enemy[e].posx <= self.claw_shot[h].posx + 4 <= self.enemy[e].posx + self.enemy[e].width\
                      and self.enemy[e].posy <= self.claw_shot[h].posy + 4 <= self.enemy[e].posy + self.enemy[e].height:

                      self.enemy[e].enemy_hp -= self.claw_shot[h].shot_power #敵の耐久力をクローショットパワーの分だけ減らす
                      if self.enemy[e].enemy_hp <= 0:
                          self.enemy_destruction(e) #敵破壊処理関数呼び出し！
                          #パーティクル生成
                          for _number in range(5):
                               self.update_append_particle(PARTICLE_DOT,self.enemy[e].posx + 4,self.enemy[e].posy + 4,self.claw_shot[h].vx / 2,self.claw_shot[h].vy / 2,    0,0,0)
                          
                          del self.enemy[e]#敵リストから破壊した敵をＤＥＬ消去破壊！
                          self.score += 1#スコア加算（あとあといろんなスコアシステム実装する予定だよ）
                    
                      self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにしてクローショット移動時にチェックしリストから消去させるため
                      pyxel.play(0,2)#ミサイルが敵を破壊した音！
              else:
                  continue
     
     #クローショットと背景との当たり判定
     def update_collision_claw_shot_bg(self):
          claw_shot_count = len(self.claw_shot)
          for i in reversed(range(claw_shot_count)):
              self.check_bg_collision(self.claw_shot[i].posx,(self.claw_shot[i].posy) + 4,0,0)
              if self.collision_flag == 1:#背景と衝突したのならクローショットを消滅させる
                  del self.claw_shot[i]          

     #################################敵弾関連の処理関数##################################################
     #敵の弾の更新&自機と敵弾の衝突判定
     def update_enemy_shot(self):
          enemy_shot_count = len(self.enemy_shot)#敵の弾数を数える
          for i in reversed(range (enemy_shot_count)):
               #敵の弾の位置を更新する！
               #サインカーブ弾の場合
               if self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_SIN:
                    self.enemy_shot[i].posx += self.enemy_shot[i].vx       #敵の弾のx座標をvx分加減算して更新
                    self.enemy_shot[i].timer += self.enemy_shot[i].speed
                    self.enemy_shot[i].posy += self.enemy_shot[i].intensity * math.sin(self.enemy_shot[i].timer + 3.14 / 4)
               #コサインカーブ弾の場合
               elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_COS:
                    self.enemy_shot[i].posx += self.enemy_shot[i].vx        #敵の弾のx座標をvx分加減算して更新
                    self.enemy_shot[i].timer += self.enemy_shot[i].speed
                    self.enemy_shot[i].posy += self.enemy_shot[i].intensity * math.cos(self.enemy_shot[i].timer + 3.14/2 + 3.14/4)
               #誘導弾orホーミングレーザーの場合
               elif    self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_HOMING_BULLET\
                    or self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_HOMING_LASER:
                    #誘導弾orホーミングレーザーを自機に追尾させる
                    vx0 = self.enemy_shot[i].vx
                    vy0 = self.enemy_shot[i].vy #誘導弾の速度ベクトル(vx,vy)を(vx0,vy0)に退避しておきます

                    #自機までの距離を求めdに距離として代入します
                    d = math.sqrt((self.my_x - self.enemy_shot[i].posx) * (self.my_x - self.enemy_shot[i].posx) + (self.my_y - self.enemy_shot[i].posy) * (self.my_y - self.enemy_shot[i].posy))
                
                    #誘導弾orホーミングレーザーの速度 vx,vyを求める
                    #速さはenemy_shot_speedで一定になるようにしています
                    #目標までの距離dが0の時は速度ベクトルを左方向にします
                    #turn_theta(Θシータ)は旋回できる角度の上限です

                    #enemy_shot_count1をホーミング性能が落ちていくカウンタの変数として使用します(1フレームごとに加算されていきます)
                    #enemy_shot_count2に入っている数値とenemy_shot_count1が同じ数値になった時に旋回できる角度の上限を1減らします

                    #自機方向の速度ベクトル(vx1,vy1)を求める
                    if d == 0:#自機までの距離は0だった？（重なっていた？）
                         vx1= 0
                         vy1 = self.enemy_shot[i].speed #自機までの距離dが0の時は速度を左方向にする
                    else:
                         #誘導弾orホーミングレーザーと自機との距離dとx,y座標との差からvx,vyの増分を計算する
                         
                         vx1 = ((self.my_x - self.enemy_shot[i].posx) / (d * self.enemy_shot[i].speed))
                         vy1 = ((self.my_y - self.enemy_shot[i].posy) / (d * self.enemy_shot[i].speed))
                    #右回り旋回角度上限の速度ベクトル(vx2,vy2)を求める
                    #math.piはπ（円周率3.141592......)
                    self.rad = 3.14 / 180 * self.enemy_shot[i].turn_theta #rad = 角度degree（theta）をラジアンradianに変換
                
                    vx2 = math.cos(self.rad) * vx0 - math.sin(self.rad) * vy0
                    vy2 = math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0

                    #自機方向に曲がるのか？ それとも旋回角度上限一杯（面舵一杯！とか取り舵一杯！とかそういう表現）で曲がるのか判別する
                    if vx0 * vx1 + vy0 * vy1 >= vx0 * vx2 + vy0 * vy2:
                         #自機方向が旋回可能範囲内の場合の処理
                         #自機方向に曲がるようにする
                         self.enemy_shot[i].vx = vx1
                         self.enemy_shot[i].vy = vy1
                    else:
                         #自機が旋回可能範囲を超えている場合（ハンドルをいっぱいまで切っても自機に追いつけないよ～）ハンドル一杯まで切る！
                         #左回り（取り舵方向）の旋回角度上限の速度ベクトルvx3,vy3を求める
                         vx3 =  math.cos(self.rad) * vx0 + math.sin(self.rad) * vy0
                         vy3 = -math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0

                         #誘導弾orホーミングレーザーから自機への相対ベクトル(px,py)を求める
                         px = self.my_x - self.enemy_shot[i].posx
                         py = self.my_y - self.enemy_shot[i].posy

                         #右回りか左回りを決める
                         #右回りの速度ベクトルの内積(p,v2)と左回りの速度ベクトルの内積(p,v3)の比較で右回りか左回りか判断する
                         #旋回角度が小さいほうが内積が大きくなるのでそちらの方に曲がるようにする
                         #
                         if px * vx2 + py * vy2 >= px * vx3 + py * vy3:
                              #右回り（面舵方向）の場合
                              self.enemy_shot[i].vx = vx2
                              self.enemy_shot[i].vy = vy2
                         else:
                              #左回り（取り舵方向）の場合
                              self.enemy_shot[i].vx = vx3
                              self.enemy_shot[i].vy = vy3
                    
                    #誘導弾orホーミングレーザーの座標(posx,posy)に速度ベクトル(vx,vy)を加減算して移動させる(座標を更新！)
                    self.enemy_shot[i].posx += self.enemy_shot[i].vx
                    self.enemy_shot[i].posy += self.enemy_shot[i].vy
                    #誘導性能を落していく処理
                    self.enemy_shot[i].count1 +=1 #誘導性能を落として行くカウンタ数をインクリメント
                    if self.enemy_shot[i].count1 >= self.enemy_shot[i].count2: #カウント上限(count2)を超えたのなら・・・
                         self.enemy_shot[i].turn_theta -= 1 #旋回上限角度を1度減らす
                         if self.enemy_shot[i].turn_theta < 0:
                              self.enemy_shot[i].turn_theta = 0 #turn_thetaはマイナスにならないようにする
                         self.enemy_shot[i].count1 = 0 #誘導性能を落として行くカウンタ数を初期化
                    
                    if self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_HOMING_LASER: #ホーミングレーザーの場合は
                         #ホーミングレーザーの尻尾部分を育成する
                         if (pyxel.frame_count % 3) == 0:
                              new_enemy_shot = Enemy_shot()
                              new_enemy_shot.update(ENEMY_SHOT_HOMING_LASER_TAIL,ID00,self.enemy_shot[i].posx,self.enemy_shot[i].posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,  0,0, 0,0,   0,  1,1, 0,0,  0,0,0, 0, 60,0,PRIORITY_FRONT, 0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                              self.enemy_shot.append(new_enemy_shot)      
               #ホーミングレーザーの尻尾の場合
               elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_HOMING_LASER_TAIL:
                    self.enemy_shot[i].disappearance_count -= 1 #消滅カウンターを1減少させる
                    if self.enemy_shot[i].disappearance_count <= 0:#消滅カウンターが0以下になったのなら
                         del self.enemy_shot[i]     #インスタンスを消滅させる 古い尻尾から消えていく・・・
                         continue                   #これ以下の処理はせずにループを続けていく
               #サーチレーザーの場合
               elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_SEARCH_LASER:
                    if self.enemy_shot[i].search_flag == 0: #サーチフラグがまだだっていないのなら自機とのx座標の比較を以下行っていく
                         if -2 <= self.my_x - self.enemy_shot[i].posx <= 2: #自機のx座標とサーチレーザーのx座標の差が+-2以内なら
                              self.enemy_shot[i].search_flag = 1 #サーチ完了フラグを立てる
                              self.enemy_shot[i].vx = 0 #サーチ完了したのでx軸方向の移動は今後させないようにvx=0にする
                              if self.my_y >= self.enemy_shot[i].posy:#サーチレーザーのy軸移動方向を決めていく
                                   self.enemy_shot[i].vy = 1 #自機がサーチレーザーより下方向にあるのでvy=1にして下方向に曲がらせる
                              else:
                                   self.enemy_shot[i].vy = -1 #自機がサーチレーザーより上方向にあるのでvy=-1にして上方向に曲がらせる
                         
                    self.enemy_shot[i].posx += self.enemy_shot[i].vx#敵の弾のx座標をvx分加減算して更新
                    self.enemy_shot[i].posy += self.enemy_shot[i].vy#敵の弾のy座標をvy分加減算して更新
                    #サーチレーザーの尻尾部分を育成する
                    if (pyxel.frame_count % 4) == 0:
                         new_enemy_shot = Enemy_shot()
                         new_enemy_shot.update(ENEMY_SHOT_SEARCH_LASER_TAIL,ID00,self.enemy_shot[i].posx,self.enemy_shot[i].posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,  0,0, 0,self.enemy_shot[i].vy, 0,  1,1, 0,0,  0,0,0, 0, 60,0,PRIORITY_FRONT,0,self.enemy_shot[i].search_flag,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0) #search_flagとvyはdraw時に使用するのでそのままコピーします
                         self.enemy_shot.append(new_enemy_shot)             
               #サーチレーザーの尻尾の場合
               elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_SEARCH_LASER_TAIL:
                    self.enemy_shot[i].disappearance_count -= 1 #消滅カウンターを1減少させる
                    if self.enemy_shot[i].disappearance_count <= 0:#消滅カウンターが0以下になったのなら
                         del self.enemy_shot[i]     #インスタンスを消滅させる 古い尻尾から消えていく・・・
                         continue                   #これ以下の処理はせずにループを続けていく
               #回転弾の場合
               elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_CIRCLE_BULLET:
                    self.enemy_shot[i].rotation_omega += self.enemy_shot[i].rotation_omega_incremental #rotation_omega_incrementalの分だけ角度を増加させていく(回転していく)
                    self.enemy_shot[i].rotation_omega = self.enemy_shot[i].rotation_omega % 360 #角度は３６０で割った余りとする(0~359)

                    self.enemy_shot[i].cx += self.enemy_shot[i].vx #回転の中心を速度ベクトルvx,vyを加算して位置を更新する
                    self.enemy_shot[i].cy += self.enemy_shot[i].vy
                    
                    #現在の半径radiusを目標となる半径radius_maxに近づけていく
                    if not -1 <= self.enemy_shot[i].radius_max - self.enemy_shot[i].radius <= 1: #radiusとradius_maxの差が+-1以内でない時は・・・
                         if self.enemy_shot[i].radius >= self.enemy_shot[i].radius_max:
                              self.enemy_shot[i].radius -= self.enemy_shot[i].radius_incremental
                         else:
                              self.enemy_shot[i].radius += self.enemy_shot[i].radius_incremental
                    
                    #中心cx,cy半径radius回転角度rotation_omegaから現在の敵弾の座標(posx.posy)を求める
                    self.enemy_shot[i].posx = self.enemy_shot[i].cx+ self.enemy_shot[i].radius * math.cos(math.radians(self.enemy_shot[i].rotation_omega))
                    self.enemy_shot[i].posy = self.enemy_shot[i].cy+ self.enemy_shot[i].radius * math.sin(math.radians(self.enemy_shot[i].rotation_omega))
               #落下弾の場合
               elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_DROP_BULLET:
                    #速度ベクトルを加速度で掛け合わせて加速もしくは減速させる x軸の速度ベクトルは変化させない
                    self.enemy_shot[i].vy += self.enemy_shot[i].accel #y軸の速度ベクトルに加速度を足し合わせて加速もしくは減速させる
                    self.enemy_shot[i].posx += self.enemy_shot[i].vx#敵の弾のx座標をvx分加減算して更新
                    self.enemy_shot[i].posy += self.enemy_shot[i].vy#敵の弾のy座標をvy分加減算して更新
               #アップレーザー,ダウンレーザーの場合
               elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_UP_LASER or self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_DOWN_LASER:
                    if self.enemy_shot[i].stop_count == 0:#もしストップカウントが0で動き出しても良いのなら・・・
                         self.enemy_shot[i].vx = self.enemy_shot[i].vx * self.enemy_shot[i].accel #速度ベクトルを加速度で掛け合わせて加速もしくは減速させる
                         self.enemy_shot[i].vy = self.enemy_shot[i].vy * self.enemy_shot[i].accel
                         self.enemy_shot[i].posx += self.enemy_shot[i].vx#敵の弾のx座標をvx分加減算して更新
                         self.enemy_shot[i].posy += self.enemy_shot[i].vy#敵の弾のy座標をvy分加減算して更新
                         self.enemy_shot[i].width += self.enemy_shot[i].expansion #毎フレームごとexpansion分だけ横幅を拡大させていく
                         if self.enemy_shot[i].width >= self.enemy_shot[i].width_max: #widthはwidth_maxを超えないようにします
                              self.enemy_shot[i].width = self.enemy_shot[i].width_max #幅は最大値とする
                              self.enemy_shot[i].vx = 0                               #最大幅まで広くなったのでもう横方向の移動は無し

                    else:
                         self.enemy_shot[i].stop_count -= 1#ストップカウントがまだ残っていたら１減らし、座標の更新は行わずそのままの位置で留まる
               #ベクトルレーザーの場合
               elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_VECTOR_LASER:
                    if self.enemy_shot[i].stop_count == 0:#もしストップカウントが0で動き出しても良いのなら・・・
                         self.enemy_shot[i].vx = self.enemy_shot[i].vx * self.enemy_shot[i].accel #速度ベクトルを加速度で掛け合わせて加速もしくは減速させる
                         self.enemy_shot[i].vy = self.enemy_shot[i].vy * self.enemy_shot[i].accel
                         self.enemy_shot[i].posx += self.enemy_shot[i].vx#敵の弾のx座標をvx分加減算して更新
                         self.enemy_shot[i].posy += self.enemy_shot[i].vy#敵の弾のy座標をvy分加減算して更新
                         self.enemy_shot[i].height += self.enemy_shot[i].expansion #毎フレームごとexpansion分だけ縦幅を拡大させていく
                         if self.enemy_shot[i].height >= self.enemy_shot[i].height_max: #heightはheight_maxを超えないようにします
                              self.enemy_shot[i].height = self.enemy_shot[i].height_max #幅は最大値とする
                              self.enemy_shot[i].vy = 0                               #最大幅まで広くなったのでもう縦方向の移動は無し

                    else:
                         self.enemy_shot[i].stop_count -= 1#ストップカウントがまだ残っていたら１減らし、座標の更新は行わずそのままの位置で留まる
               #その他の敵弾の場合
               else: 
                    if self.enemy_shot[i].stop_count == 0:#もしストップカウントが0で動き出しても良いのなら・・・
                         self.enemy_shot[i].vx = self.enemy_shot[i].vx * self.enemy_shot[i].accel #速度ベクトルを加速度で掛け合わせて加速もしくは減速させる
                         self.enemy_shot[i].vy = self.enemy_shot[i].vy * self.enemy_shot[i].accel
                         self.enemy_shot[i].posx += self.enemy_shot[i].vx#敵の弾のx座標をvx分加減算して更新
                         self.enemy_shot[i].posy += self.enemy_shot[i].vy#敵の弾のy座標をvy分加減算して更新
                         if   self.enemy_shot[i].division_type == ENEMY_SHOT_DIVISION_3WAY: #3way分裂弾を生み出す
                              self.enemy_shot[i].division_count -= 1 #分裂までのカウントをデクリメント
                              if self.enemy_shot[i].division_count == 0: #分裂カウントが0になったのなら・・・
                                   ex,ey = self.enemy_shot[i].posx,self.enemy_shot[i].posy
                                   theta = 20 #発射角度は20度
                                   n = 3 #3way弾
                                   if self.enemy_shot[i].division_num <= 0: #分裂回数がもう0ならもう分裂しない
                                        div_type = 0 #分裂無しタイプにする
                                   else:
                                        self.enemy_shot[i].division_num -= 1 #分裂回数を1減らす
                                        div_type = ENEMY_SHOT_DIVISION_3WAY #3way弾
                                   
                                   div_num = self.enemy_shot[i].division_num
                                   div_count = self.enemy_shot[i].division_count_origin
                                   stop_count = 0
                                   self.enemy_aim_bullet_nway(ex,ey,theta,n,div_type,div_count,div_num,stop_count) #自機狙い3way分裂弾育成
                                   del self.enemy_shot[i] #元の弾のインスタンスは消去する
                                   continue #ループはそのまま続けるのでcontinue
                         elif self.enemy_shot[i].division_type == ENEMY_SHOT_DIVISION_5WAY: #5way分裂弾を生み出す
                              self.enemy_shot[i].division_count -= 1 #分裂までのカウントをデクリメント
                              if self.enemy_shot[i].division_count == 0: #分裂カウントが0になったのなら・・・
                                   ex,ey = self.enemy_shot[i].posx,self.enemy_shot[i].posy
                                   theta = 40 #発射角度は40度
                                   n = 5 #3way弾
                                   if self.enemy_shot[i].division_num <= 0: #分裂回数がもう0ならもう分裂しない
                                        div_type = 0 #分裂無しタイプにする
                                   else:
                                        self.enemy_shot[i].division_num -= 1 #分裂回数を1減らす
                                        div_type = ENEMY_SHOT_DIVISION_5WAY #5way弾
                                   
                                   div_num = self.enemy_shot[i].division_num
                                   div_count = self.enemy_shot[i].division_count_origin
                                   stop_count = 0
                                   self.enemy_aim_bullet_nway(ex,ey,theta,n,div_type,div_count,div_num,stop_count) #自機狙い5way分裂弾育成
                                   del self.enemy_shot[i] #元の弾のインスタンスは消去する
                                   continue #ループはそのまま続けるのでcontinue
                         elif self.enemy_shot[i].division_type == ENEMY_SHOT_DIVISION_7WAY: #7way分裂弾を生み出す
                              self.enemy_shot[i].division_count -= 1 #分裂までのカウントをデクリメント
                              if self.enemy_shot[i].division_count == 0: #分裂カウントが0になったのなら・・・
                                   ex,ey = self.enemy_shot[i].posx,self.enemy_shot[i].posy
                                   theta = 100 #発射角度は100度
                                   n = 7 #7way弾
                                   if self.enemy_shot[i].division_num <= 0: #分裂回数がもう0ならもう分裂しない
                                        div_type = 0 #分裂無しタイプにする
                                   else:
                                        self.enemy_shot[i].division_num -= 1 #分裂回数を1減らす
                                        div_type = ENEMY_SHOT_DIVISION_7WAY #7way弾
                                   
                                   div_num = self.enemy_shot[i].division_num
                                   div_count = self.enemy_shot[i].division_count_origin
                                   stop_count = 0
                                   self.enemy_aim_bullet_nway(ex,ey,theta,n,div_type,div_count,div_num,stop_count) #自機狙い7way分裂弾育成
                                   del self.enemy_shot[i] #元の弾のインスタンスは消去する
                                   continue #ループはそのまま続けるのでcontinue
                         elif self.enemy_shot[i].division_type == ENEMY_SHOT_DIVISION_9WAY: #9way分裂弾を生み出す
                              self.enemy_shot[i].division_count -= 1 #分裂までのカウントをデクリメント
                              if self.enemy_shot[i].division_count == 0: #分裂カウントが0になったのなら・・・
                                   ex,ey = self.enemy_shot[i].posx,self.enemy_shot[i].posy
                                   theta = 160 #発射角度は160度
                                   n = 9 #9way弾
                                   if self.enemy_shot[i].division_num <= 0: #分裂回数がもう0ならもう分裂しない
                                        div_type = 0 #分裂無しタイプにする
                                   else:
                                        self.enemy_shot[i].division_num -= 1 #分裂回数を1減らす
                                        div_type = ENEMY_SHOT_DIVISION_9WAY #9way弾
                                   
                                   div_num = self.enemy_shot[i].division_num
                                   div_count = self.enemy_shot[i].division_count_origin
                                   stop_count = 0
                                   self.enemy_aim_bullet_nway(ex,ey,theta,n,div_type,div_count,div_num,stop_count) #自機狙い9way分裂弾育成
                                   del self.enemy_shot[i] #元の弾のインスタンスは消去する
                                   continue #ループはそのまま続けるのでcontinue
                    else:
                         self.enemy_shot[i].stop_count -= 1#ストップカウントがまだ残っていたら１減らし、座標の更新は行わずそのままの位置で留まる
               
               #敵のレーザー兵器がＬ’ｓシールドシステムに当たっているか判別###################################
               if self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_LASER and self.ls_shield_hp > 0:#敵のショットがレーザーの時かつシールドエナジーが残っているときのみ処理する
                    if   0 <= self.enemy_shot[i].posx - (self.my_x + 8) <= 4 and 0 <= self.enemy_shot[i].posy - (self.my_y - 12) < 26:#シールドと敵レーザーが接触したのなら
                         self.ls_shield_hp -= 1#シールドエナジーを1減らす
                         del self.enemy_shot[i]
                         continue
               
               #敵の弾が自機に当たっているか判別###########################################################
               if self.invincible_counter > 0: #無敵時間が残っていた場合は・・・
                    continue                   #衝突判定はせずループだけ続ける(continue)・・・無敵っていいよね・・・うん、うん.....
               if self.enemy_shot[i].collision_type == ESHOT_COL_MIN88: #最小の正方形8x8ドットでの当たり判定の場合
                    #敵の弾と自機の位置の2点間の距離を求める
                    self.dx = (self.enemy_shot[i].posx + 4) - (self.my_x + 4)
                    self.dy = (self.enemy_shot[i].posy + 4) - (self.my_y + 4)
                    self.distance = math.sqrt(self.dx * self.dx + self.dy * self.dy)
                    if self.distance < 3:
                         self.update_my_ship_damage(1) #敵弾と自機の位置の距離が3以下なら衝突したと判定し自機のシールド値を１減らす
               elif self.enemy_shot[i].collision_type == ESHOT_COL_BOX: #長方形での当たり判定の場合
                    if       0 <= (self.my_x+4) - (self.enemy_shot[i].posx+4) <= self.enemy_shot[i].width\
                         and 0 <= (self.my_y+4) - (self.enemy_shot[i].posy+4) <= self.enemy_shot[i].height:
                         self.update_my_ship_damage(1) #自機が敵弾の長方形の当たり判定の中に居たのなら衝突したと判定し自機のシールド値を１減らす
     
     #敵の弾のはみだしチェック（はみ出していたら消去する）
     def update_clip_enemy_shot(self):
          enemy_shot_count = len(self.enemy_shot)#敵の弾数を数える
          for i in reversed(range (enemy_shot_count)):
               if self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_CIRCLE_BULLET or self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_CIRCLE_LASER:
                    #回転系の弾の座標はcx,cyを基準としてはみだし判定する(結構大きくはみ出しても消えない感じで判定します)
                    if  (-40 < self.enemy_shot[i].cx < WINDOW_W + 40 ) and ( -40 < self.enemy_shot[i].cy < WINDOW_H + 40 ):
                         continue
                    else:
                         del self.enemy_shot[i]
               else:#それ以外の弾の座標はposx,posyを基準としてはみだし判定する
                    if  (-8 < self.enemy_shot[i].posx < WINDOW_W + 8) and ( -8 < self.enemy_shot[i].posy < WINDOW_H + 8 ):
                         continue
                    else:
                         del self.enemy_shot[i]               
     
     #敵の弾と背景障害物の当たり判定
     def update_collision_enemy_shot_bg(self):
          enemy_shot_count = len(self.enemy_shot)#敵の弾数を数える
          for i in reversed(range(enemy_shot_count)):
               if    self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_WAVE\
                  or self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_VECTOR_LASER:    #ウェーブ、ベクトルレーザーは当たり判定無し
                    continue #当たり判定はしないで次のループ回へ突入！
               elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_LASER: #レーザービームの場合は障害物にギリギリまで当たり食い込みたいのでx座標を右に1ブロック分(8ドット)だけ補正を入れてやる
                   self.check_bg_collision(self.enemy_shot[i].posx + 6 + 8,self.enemy_shot[i].posy + 4,0,0)
               else:
                   self.check_bg_collision(self.enemy_shot[i].posx + 6   ,self.enemy_shot[i].posy + 4,0,0)
               
               if self.collision_flag == 1: #衝突フラグが立っていたらを敵弾を消滅させる
                   del self.enemy_shot[i]          

     #背景の星の追加（発生＆育成）
     def update_append_star(self):
          if (pyxel.frame_count % 3) == 0:
               if len(self.stars) < 600:
                    new_stars = Star()
                    new_stars.update(WINDOW_W + 1,randint(0,WINDOW_H),randint(1,50))
                    self.stars.append(new_stars)

     #背景の星の更新（移動）
     def update_star(self):
          stars_count = len(self.stars)
          for i in reversed(range (stars_count)):
               if 0 < self.stars[i].posx and self.stars[i].posx < WINDOW_W + 2:#背景の星が画面内に存在するのか判定

               #背景の星の位置を更新する
                    self.stars[i].posx -= (self.stars[i].speed) / 12 * self.star_scroll_speed #左方向にspeedを１２で割った切り捨てドット分（star_scroll_speedは倍率です）星が左に流れます
               else:
                    del self.stars[i]#背景の星が画面外に存在するときはインスタンスを破棄する （流れ星消滅）

     #デバッグモードの更新（キーボードによる表示タイプや表示非表示の切り替え） KEY CONTROL
     def update_debug_status(self):
         if pyxel.btnp(pyxel.KEY_CONTROL):
             if self.debug_menu_status == 0:
                 self.debug_menu_status = 1
             elif self.debug_menu_status == 1:
                 self.debug_menu_status = 2
             else:
                 self.debug_menu_status = 0
     
     #デバッグモードによるキーボードやパッドでの敵や敵弾の強制追加発生
     def update_debug_mode_enemy_append(self):
          #敵タイプ1サーコインの発生  直進して斜め後退→勢いよく後退していく10機編隊       KEY 4 +++++++
          if (pyxel.frame_count % 8) == 0:
               if pyxel.btn(pyxel.KEY_4) or pyxel.btn(pyxel.GAMEPAD_1_LEFT_SHOULDER) or pyxel.btn(pyxel.GAMEPAD_2_LEFT_SHOULDER):
                    if len(self.enemy) < 400:

                         self.posy = randint(0,WINDOW_H - 8)
                         for number in range(10):
                              new_enemy = Enemy()
                              new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.posy,0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   -1,1,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1,0,    0, HP01,  0,0, E_SIZE_NORMAL,   30,0,0 ,    0,0,0,0,   E_SHOT_POW,self.current_formation_id ,0,0,0,    0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                              self.enemy.append(new_enemy)
                         
                         #編隊なので編隊のＩＤナンバーと編隊の総数、現在の編隊生存数をEnemy_formationリストに登録します
                         self.record_enemy_formation(10)
          #敵タイプ2サイシーロの発生  サインカーブを描く3機編隊                          KEY 5 ++++++
          if (pyxel.frame_count % 8) == 0:
               if pyxel.btn(pyxel.KEY_5):
                    if len(self.enemy) < 400:

                         self.posy = randint(0,WINDOW_H)
                         for number in range(3):
                              new_enemy = Enemy()
                              new_enemy.update(SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W + 10,((self.posy)-36) + (number * 12),0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   0,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1,0,   0,  HP01,   0,0,  E_SIZE_NORMAL,0.5,0.05,0,     0,0,0,0,   E_NO_POW,ID00 ,0,0,0    ,0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                              self.enemy.append(new_enemy)         
          #敵タイプ6の発生（謎の飛翔体Ｍ54）                                           KEY 6 ++++++
          if (pyxel.frame_count % 3) == 0:
               if pyxel.btn(pyxel.KEY_6):
                    if len(self.enemy) < 400:
                         self.posy = randint(0,WINDOW_H)
                         new_enemy = Enemy()
                         new_enemy.update(6,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,self.posy,0,0,    0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0, 0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1,0,   0,  HP01,   0,0,  E_SIZE_NORMAL,   0.5,0.05,0,     0,0,0,0,    E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)         
          #敵タイプ8ツインアローの発生 追尾戦闘機                                      KEY Z ++++++
          if (pyxel.frame_count % 3) == 0:
               if pyxel.btn(pyxel.KEY_Z):
                    if len(self.enemy) < 400:
                         self.posy = randint(0,WINDOW_H)
                         new_enemy = Enemy()
                         new_enemy.update(TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,self.posy,0,0,      0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0, 0,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1.5,0,  0,    HP01,     0,0,   E_SIZE_NORMAL,  0,  0, 1.3,    0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
          #敵タイプ9の発生 縦軸合わせ突進タイプ                                        KEY X ++++++
          if (pyxel.frame_count % 16) == 0:
               if pyxel.btn(pyxel.KEY_X):
                    if len(self.enemy) < 400:
                         new_enemy = Enemy()
                         new_enemy.update(9,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    80,40,0,0,      0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,  0,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.5,0,   0,    HP01,     0,0,   E_SIZE_NORMAL,  0,  0, 0,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
          #敵タイプ10の発生 地面のスクランブルハッチ                                    KEY C +++++
          if (pyxel.frame_count % 64) == 0:
               if pyxel.btn(pyxel.KEY_C):
                    if len(self.enemy) < 400:
                         #enemy_count1を出現してから突進タイプの敵を出すまでの時間のカウンタで使用します（射出開始カウンタ）
                         #enemy_count2を射出する敵の総数です（敵総数カウンタ）
                         new_enemy = Enemy()
                         new_enemy.update(10,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    170,96,0,0,     0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,   0,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_24,SIZE_26,   0.5,0,   0,    HP10,     0,0,   E_SIZE_MIDDLE32,  (randint(0,130) + 10),  6, 20,     0,0,0,0,       E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
          #敵タイプ12の発生 レイブラスター  レーザービームを出して高速で逃げていく敵      KEY D ++++++
          if (pyxel.frame_count % 8) == 0:
               if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT_SHOULDER) or pyxel.btn(pyxel.GAMEPAD_2_RIGHT_SHOULDER):
                    if len(self.enemy) < 400:
                         new_enemy = Enemy()
                         new_enemy.update(RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W + 8,randint(0,WINDOW_H),0,0,    0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   -2,(randint(0,1)-0.5),        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.98,0,    0,    HP01,  0,0,    E_SIZE_NORMAL,   80 + randint(0,40),0,0,      0,0,0,0,       E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
          #敵タイプ16の発生 2機一体で挟みこみ攻撃をしてくるクランパリオン                KEY T ++++++++
          if (pyxel.frame_count % 24) == 0:
               if pyxel.btn(pyxel.KEY_T):
                    if len(self.enemy) < 400:
                         new_enemy = Enemy()
                         new_enemy.update(CLAMPARION,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,     WINDOW_W,0,0,0,        0,0,0,0,0,0,0,0,          0,0,0,0,0,0,0,0,0,0,  -1.1,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.997,0,    0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,      0,0,0,0,     E_NO_POW,   ID00     ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)

                         new_enemy = Enemy()
                         new_enemy.update(CLAMPARION,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,     WINDOW_W,WINDOW_H-8,0,0,      0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,  -1.1,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.997,0,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,     0,0,0,0,     E_NO_POW,   ID00     ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
          #敵タイプ17の発生 ロールブリッツ あらかじめ決められた場所へスプライン曲線移動   KEY Y ++++++++
          if (pyxel.frame_count % 24) == 0:
               if pyxel.btn(pyxel.KEY_Y):
                    if len(self.enemy) < 400:
                         new_enemy = Enemy()
                         new_enemy.update(ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    0,0,0,0,      0,0,0,0,0,0,0,0,           0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   0,1,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,     0,0,0,0,       E_NO_POW,   ID00     ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)

                         new_enemy = Enemy()
                         new_enemy.update(ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    0,0,0,8,      0,0,0,0,0,0,0,0,         0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   0,1.05,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,     0,0,0,0,    E_NO_POW,   ID00     ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
                         
                         new_enemy = Enemy()
                         new_enemy.update(ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    0,0,0,16,     0,0,0,0,0,0,0,0,          0,0,0,0,0,0,0,0,0,0,  0,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0,0.95,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,    E_NO_POW,   ID00     ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
          #敵タイプ18の発生 ボルダー 硬めの弾バラマキ重爆撃機                           KEY R ++++++++
          if (pyxel.frame_count % 24) == 0:
               if pyxel.btn(pyxel.KEY_R):
                    if len(self.enemy) < 400:
                         new_enemy = Enemy()
                         new_enemy.update(VOLDAR,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   170,10,0,0,        0,0,0,0,0,0,0,0,         0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_40,SIZE_24,   -0.07,1,   0,    HP30,  0,0,    E_SIZE_HI_MIDDLE53,   0,0,0,    0,0,0,0,    E_NO_POW,   ID00     ,1,0.007,0.6,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
                    
          #敵弾1(前方加速弾&落下弾&サインコサイン弾&グリーンカッター)の発生             KEY A ----------------
          if(pyxel.frame_count % 3) == 0:
               if pyxel.btn(pyxel.KEY_A):
                    if len(self.enemy_shot) < 800:
                         #前方加速弾
                         new_enemy_shot = Enemy_shot()
                         new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -1,0,      1.01,      1,1,    1,0, 0,1,0,                    0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                         self.enemy_shot.append(new_enemy_shot)
                         #落下弾
                         new_enemy_shot = Enemy_shot()
                         new_enemy_shot.update(ENEMY_SHOT_DROP_BULLET,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -0.3,-1.1,      0.02,      1,1,    1,0, 0,1,0,          0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                         self.enemy_shot.append(new_enemy_shot)

                         #サイン弾
                         new_enemy_shot = Enemy_shot()
                         new_enemy_shot.update(ENEMY_SHOT_SIN,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,    0,0, -1,0,        1,    1,1,    1,0,  0.06,0.06,0.6,              0,   0,0,PRIORITY_FRONT,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                         self.enemy_shot.append(new_enemy_shot)
                         #コサイン弾
                         new_enemy_shot = Enemy_shot()
                         new_enemy_shot.update(ENEMY_SHOT_COS,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,    0,0,  -1,0,       1,    1,1,    1,0,  0.06,0.06,0.6,              0,   0,0,PRIORITY_FRONT,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                         self.enemy_shot.append(new_enemy_shot)

                         #グリーンカッター
                         new_enemy_shot = Enemy_shot()
                         new_enemy_shot.update(ENEMY_SHOT_GREEN_CUTTER,ID00,140,60,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE12,    0,0,  -0.3,0,       1.01,    1,1,    0,0,  0,0,0,              0,   0,0,PRIORITY_FRONT,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                         self.enemy_shot.append(new_enemy_shot)
          #敵弾2(自機狙い6way弾)の発生                               KEY B ----------------
          if(pyxel.frame_count % 3) == 0:
               if pyxel.btn(pyxel.KEY_B):
                    if len(self.enemy_shot) < 800:
                        new_enemy_shot = Enemy_shot()
                        ex = 80
                        ey = 60
                        theta = 30
                        n = 6
                        division_type = 0
                        division_count = 0
                        division_num = 0
                        stop_count = 0
                        self.enemy_aim_bullet_nway(ex,ey,theta,n,division_type,division_count,division_num,stop_count)    
          #敵弾3(前方レーザービーム)の発生                            KEY S ----------------
          if(pyxel.frame_count % 1) == 0:
               if pyxel.btn(pyxel.KEY_S):
                    if len(self.enemy_shot) < 800:
                         posy = randint(0,WINDOW_H)
                         for number in range(6):
                             new_enemy_shot = Enemy_shot()
                             new_enemy_shot.update(ENEMY_SHOT_LASER,ID00, WINDOW_W,posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0,  -2,0,   1,  1,1,   0,0,0,    1,0,0,  0,number * 2,PRIORITY_FRONT,  0,0,  0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                             self.enemy_shot.append(new_enemy_shot)
          #敵弾4(ホーミングレーザー)の発生                            KEY F -----------------
          if(pyxel.frame_count % 100) == 0:
               if pyxel.btn(pyxel.KEY_F):
                    if len(self.enemy_shot) < 800:
                        posy = 60
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_HOMING_LASER,ID00, WINDOW_W,posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0,   0.5,0.5,   1,     1,1,   0,20,0,    1,0,0,  0,0,PRIORITY_MORE_FRONT, 8,0,  0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)
          #敵弾5(サーチレーザー)の発生                                KEY G ------------------
          if(pyxel.frame_count % 100) == 0:
               if pyxel.btn(pyxel.KEY_G):
                    if len(self.enemy_shot) < 800:
                        posx = 100
                        posy = 60
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_SEARCH_LASER,ID00, posx,posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0,   -0.75,0,   1,    1,1,   0,0, 0,    1,0,0,  0,0,PRIORITY_MORE_FRONT, 0,0,  0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)
          #敵弾6(回転弾)の発生                                       KEY H ------------------
          if(pyxel.frame_count % 3) == 0:
               if pyxel.btn(pyxel.KEY_H):
                    if len(self.enemy_shot) < 800:
                         cx = 100
                         cy = 60
                         radius = 1
                         radius_max = 80
                         radius_incremental = 0.05
                         rotation_omega_incremental = 2
                         new_enemy_shot = Enemy_shot()
                         new_enemy_shot.update(ENEMY_SHOT_CIRCLE_BULLET,ID00, cx+radius,cy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, cx,cy,  -0.05,0,   1,     1,1,   0,0, 0,    1,0,0,  0,0,PRIORITY_FRONT, 0,0,  0,rotation_omega_incremental,radius,radius_max, 0,0, radius_incremental, 0,0, 0, 0,0, 0,0,   0,0)
                         self.enemy_shot.append(new_enemy_shot)

                         cx = 100
                         cy = 60
                         radius = 1
                         radius_max = 80
                         radius_incremental = 0.05
                         rotation_omega_incremental = -2
                         new_enemy_shot = Enemy_shot()
                         new_enemy_shot.update(ENEMY_SHOT_CIRCLE_BULLET,ID00, cx+radius,cy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, cx,cy,  -0.05,0,   1,     1,1,   0,0, 0,    1,0,0,  0,0,PRIORITY_FRONT, 0,0,  0,rotation_omega_incremental,radius,radius_max, 0,0, radius_incremental, 0,0, 0, 0,0, 0,0,   0,0)
                         self.enemy_shot.append(new_enemy_shot)
          #敵弾7(分裂弾)の発生                                       KEY J ----------------
          if(pyxel.frame_count % 3) == 0:
               if pyxel.btn(pyxel.KEY_J):
                    if len(self.enemy_shot) < 800:
                         new_enemy_shot = Enemy_shot()
                         ex,ey = 140,60
                         division_type         = 1   #自機狙いの3way
                         division_count        = 40 #分裂するまでのカウント数
                         division_count_origin = 40 #分裂するまでのカウント数(元数値)
                         division_num          = 10    #分裂する回数(ひ孫まで)
                         new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -2,0,      0.96,      1,1,    1,0, 0,1,0,          0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, 0,0, 0,0,   0,0)
                         self.enemy_shot.append(new_enemy_shot)               
          #敵弾8(狙い撃ち分裂弾弾)の発生                              KEY K ----------------
          if(pyxel.frame_count % 3) == 0:
               if pyxel.btn(pyxel.KEY_K):
                    ex,ey         = 140,60 #弾発射初期座標
                    div_type      = 1 #自機狙いの3way
                    div_count     = 40 #分裂するまでのカウント数
                    div_num       = 2 #ひ孫の代まで分裂します
                    stop_count    = 20 #その場に留まるカウント数
                    accel         = 1.02 #加速係数
                    self.enemy_aim_bullet(ex,ey,div_type,div_count,div_num,stop_count,accel)
          #敵弾9(アップ&ダウンレーザー)の発生                         KEY L ----------------
          if(pyxel.frame_count % 28) == 0:
               if pyxel.btn(pyxel.KEY_L):
                    if len(self.enemy_shot) < 800:
                         new_enemy_shot = Enemy_shot()
                         ex,ey = 80,60
                         vx,vy =    -0.1,-0.3
                         division_type         = 0
                         division_count        = 0
                         division_count_origin = 0
                         division_num          = 0
                         expansion             = 0.2
                         width_max             = 40
                         height_max            = 3
                         new_enemy_shot.update(ENEMY_SHOT_UP_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE3, 0,0, vx,vy,      1,      1,1,    1,0, 0,1,0,          0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
                         self.enemy_shot.append(new_enemy_shot)

                         new_enemy_shot = Enemy_shot()
                         ex,ey = 80,60
                         vx,vy =    -0.1,0.3
                         division_type         = 0
                         division_count        = 0
                         division_count_origin = 0
                         division_num          = 0
                         expansion             = 0.3
                         width_max             = 80
                         height_max            = 3
                         new_enemy_shot.update(ENEMY_SHOT_DOWN_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE3, 0,0, vx,vy,      1,      1,1,    1,0, 0,1,0,          0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
                         self.enemy_shot.append(new_enemy_shot)
          #敵弾10(ベクトルレーザー)の発生                             KEY M ----------------
          if(pyxel.frame_count % 10) == 0:
               if pyxel.btn(pyxel.KEY_M):
                    if len(self.enemy_shot) < 800:
                         new_enemy_shot = Enemy_shot()
                         ex,ey = 100,60
                         vx,vy =    -0.7,-0.1
                         division_type         = 0
                         division_count        = 0
                         division_count_origin = 0
                         division_num          = 0
                         expansion             = 0.3
                         width_max             = 3
                         height_max            = 90
                         new_enemy_shot.update(ENEMY_SHOT_VECTOR_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE3,ESHOT_SIZE3, 0,0, vx,vy,      0.996,      1,1,    1,0, 0,1,0,          0,   0,0,PRIORITY_TOP,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
                         self.enemy_shot.append(new_enemy_shot)

          #メッセージウィンドウを発生させる                              KEY Q
          if(pyxel.frame_count % 16) == 0:
               if pyxel.btn(pyxel.KEY_Q):
                   new_window = Window()
                   x = randint(0,100)
                   y = randint(0,100)
                   new_window.update(ID00,ID00,2,WINDOW_OPEN,\
                                     "RETURN TITLE??",DISP_CENTER,\
                                     
                                     "YES",DISP_CENTER,0,7,\
                                     "NO",DISP_CENTER,10,3,\
                                     "KOKONI",DISP_CENTER,0,2,\
                                     "TEKISUTOGA",DISP_CENTER,0,11,\
                                     "HAIRI",DISP_CENTER,0,10,\
                                     "MASU",DISP_CENTER,0,15,\
                                     "!",DISP_CENTER,10,8,\

                                     43,68   -32,   0,0,  8*8,3*8  +40,   2,1, 1,1,   0,0,    0,0)
                   
                   #new_window.update(0,1,  24,24,  0,0, 64,64, 0,0,0)
                   self.window.append(new_window)         
          #パーティクルを発生させる                                     KEY P
          if(pyxel.frame_count % 1) == 0:
               if pyxel.btn(pyxel.KEY_P):
                    x = randint(0,160)
                    y = randint(0,120)
                    
                    self.update_append_particle(PARTICLE_LINE,x,y,  0,0,0,0,0)
                    
                    #particle_number = randint(0,10) + 50
                    #for number in range(particle_number):
                    #     self.update_append_particle(PARTICLE_DOT,x,y,-0.5,-0.5, 0,0,0)        
          #背景オブジェクト雲１を発生させる                              KEY E
          if(pyxel.frame_count % 6) == 0:
               if pyxel.btn(pyxel.KEY_E):
                    t = randint(0,20)
                    y = randint(0,120+30)
                    
                    new_background_object = Background_object()
                    new_background_object.update(t, 160+10,y,  0,    1.009,1,0,0,0,0,0,0,   -3,-0.25,  0,0,   0,0,0,0,0,   0,0,0, 0,0,0,  0,0,0)
                    self.background_object.append(new_background_object)
          
          #パワーアップアイテム類を発生させる                            KEY U I O
          if(pyxel.frame_count % 8) == 0:
               if pyxel.btn(pyxel.KEY_U): #ショットアイテム
                    y = randint(0,120)
                    new_obtain_item = Obtain_item()
                    new_obtain_item.update(ITEM_SHOT_POWER_UP,WINDOW_W-20,y, 0.5,0,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   1,0,0,  0,0,0, self.pow_item_bounce_num,0)
                    self.obtain_item.append(new_obtain_item)     
               elif pyxel.btn(pyxel.KEY_I): #ミサイルアイテム
                    y = randint(0,120)
                    new_obtain_item = Obtain_item()
                    new_obtain_item.update(ITEM_MISSILE_POWER_UP,WINDOW_W-20,y, 0.5,0,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,1,0,  0,0,0, self.pow_item_bounce_num,0)
                    self.obtain_item.append(new_obtain_item) 
               elif pyxel.btn(pyxel.KEY_O): #シールドアイテム
                    y = randint(0,120)
                    new_obtain_item = Obtain_item()
                    new_obtain_item.update(ITEM_SHIELD_POWER_UP,WINDOW_W-20,y, 0.5,0,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,0,1,  0,0,0, self.pow_item_bounce_num,0)
                    self.obtain_item.append(new_obtain_item) 
          
          #自機クローを追加する                                        KEY V
          if pyxel.btnp(pyxel.KEY_V):
               self.update_append_claw()
          
          #キーボード入力によるイベントアペンドリスト書き込み  サーコイン10機編隊   KEY 0
          if (pyxel.frame_count % 8) == 0:
               if pyxel.btn(pyxel.KEY_0):
                    new_event_append_request = Event_append_request()
                    new_event_append_request.update(self.stage_count + 10,EVENT_ENEMY,CIR_COIN,WINDOW_W + 8,randint(0,WINDOW_H - 8),10)
                    self.event_append_request.append(new_event_append_request)#現在のstage_countから10カウント過ぎた時点でサーコインが発生するようイベントアペンドリストに追加する
                         
     #クローの追加
     def update_append_claw(self):
          if   len(self.claw) == 0:#1機目のクローの発生
               posx = self.my_x
               posy = self.my_y
               new_claw = Claw()
               self.claw_number = 1
               self.claw_difference = 360 / self.claw_number
               new_claw.update(0,   self.claw_type,0,    posx,posy,  0,-1,   -1,-1,  -1,0,       0,0,  0,-12,  -2,-12,    -2,-12,   -12,-1,  0,0,     90,0,2,12,    self.claw_difference,0,   0,1,   0)
               self.claw.append(new_claw)
               return

          if len(self.claw) == 1:#2機目のクローの発生
               posx = self.my_x
               posy = self.my_y
               new_claw = Claw()
               self.claw_number = 2
               self.claw_difference = 360 / self.claw_number
               new_claw.update(1,   self.claw_type,0,    posx,posy,  0,-1,   -1,1,  0,-1,        0,0, 0,-12,     -2,12,  -2,12,   -3,-9, 0,0,        90,0,2,12,    self.claw_difference,0,   0,1,   0)
               self.claw.append(new_claw)
               return

          if len(self.claw) == 2:#3機目のクローの発生
               posx = self.my_x
               posy = self.my_y
               new_claw = Claw()
               self.claw_number = 3
               self.claw_difference = 360 / self.claw_number
               new_claw.update(2,   self.claw_type,0,    posx,posy,  0,-1,   -1,-1,  0,1,        0,0,  0,-12,    -6,-24, -6,-24,  -3,8,   0,0,       90,0,2,12,    self.claw_difference,0,   0,1,     0)
               self.claw.append(new_claw)
               return

          if len(self.claw) == 3:#4機目のクローの発生
               posx = self.my_x
               posy = self.my_y
               new_claw = Claw()
               self.claw_number = 4
               self.claw_difference = 360 / self.claw_number
               new_claw.update(3,   self.claw_type,0,    posx,posy,  0,-1,    -1,1,   -1,0,        0,0, 0,-12,     -6,24,  -6,24,  -12,-1,      0,0,        90,0,2,12,   self.claw_difference,0,    0,1,       0)
               self.claw.append(new_claw)
               return
     
     #クローの消滅                                                      KEY W
     def update_delete_claw(self):
          if pyxel.btnp(pyxel.KEY_W):   #wキーが押されたら自機クローを消滅させる
              claw_count = len(self.claw)
              for i in reversed(range(claw_count)):
                   if claw_count != 0:  #クローの数が0以外なら
                       del self.claw[i] #クローのインスタンスを破棄する(クロー消滅)
              
              self.claw_number = 0      #クローの数を0機にする
     
     #フイックスクローの間隔を変化させる                                  KEY N
     def update_change_fix_claw_interval(self):
          if (pyxel.frame_count % 8) == 0:
               if pyxel.btn(pyxel.KEY_N) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT_SHOULDER) or pyxel.btn(pyxel.GAMEPAD_2_RIGHT_SHOULDER):#Nキーが押されたらフックスクローの間隔を変化させる
                    self.fix_claw_magnification += 0.1       #ボタンが押されたら0.1刻みで増加させる
                    if self.fix_claw_magnification >= 2:
                         self.fix_claw_magnification = 0.4   #2以上になったら0.4にする

     #クロースタイルの変更                                               KEY M
     def update_change_claw_style(self):
          if (pyxel.frame_count % 8) == 0:
               if pyxel.btn(pyxel.KEY_M) or pyxel.btn(pyxel.GAMEPAD_1_LEFT_SHOULDER) or pyxel.btn(pyxel.GAMEPAD_2_LEFT_SHOULDER):#Mキーが押されたらクローの種類を変更する
                    self.claw_type += 1#クローの種類を変化させる
                    if self.claw_type > 3:#もしtype3のリバースタイプを超えてしまったら0のローリングタイプにする
                         self.claw_type =0
                    
                    claw_count = len(self.claw)
                    for i in reversed(range(claw_count)):
                         self.claw[i].status = 0#全てのクローのステータスを0=回転開始や固定開始の初期位置まで動いていくにする
     
     #####################################敵関連の処理関数######################################
     #イベントリストによる敵の発生システム
     def update_enemy_append_event_system(self):
          if self.stage_count == self.event_list[self.event_index][0]:#ステージカウントとリストのカウント値が同じならリスト内容を実行する
               if   self.event_list[self.event_index][1] == EVENT_ENEMY:             #イベント「敵出現」の場合
                    #サーコイン発生！
                    if   self.event_list[self.event_index][2] == CIR_COIN:
                         for number in range(self.event_list[self.event_index][5]):
                              #編隊なので現在の編隊ＩＤナンバーであるcurrent_formation_idも出現時にenemyクラスに情報を書き込みます
                              new_enemy = Enemy()
                              new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.event_list[self.event_index][4],0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0, -1,1,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1*self.enemy_speed_mag,0,   0, HP01 * self.enemy_hp_mag,  0,0, E_SIZE_NORMAL,   30,0,0,    0,0,0,0,    E_SHOT_POW,self.current_formation_id ,0,0,0,      0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT02,PT02,  PT01,PT01,PT03)
                              self.enemy.append(new_enemy) 
                              
                         #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                         self.record_enemy_formation(self.event_list[self.event_index][5]) 
                    #追尾戦闘機ツインアロー出現
                    elif self.event_list[self.event_index][2] == TWIN_ARROW:
                         new_enemy = Enemy()
                         new_enemy.update(TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,       0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  0,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1.5 - (self.enemy_speed_mag // 2),0,  0,    HP01 * self.enemy_hp_mag,     0,0,   E_SIZE_NORMAL,  0,  0, 1.3,     0,0,0,0,    E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)                   
                    #回転戦闘機サイシーロ出現(サインカーブを描く敵)
                    elif self.event_list[self.event_index][2] == SAISEE_RO:
                         new_enemy = Enemy()
                         new_enemy.update(SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  0,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1*self.enemy_speed_mag,0,  0,  HP01 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,0.5,0.05,0,      0,0,0,0,     E_NO_POW,ID00 ,0,0,0,                 0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)    
                    #グリーンランサー 3way弾を出してくる緑の戦闘機(サインカーブを描く敵)
                    elif self.event_list[self.event_index][2] == GREEN_LANCER:
                         new_enemy = Enemy()
                         new_enemy.update(GREEN_LANCER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   0,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.1*self.enemy_speed_mag,0,  0,  HP05 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,0.5,0.01,0,      0,0,0,0,     E_MISSILE_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
                    #レイブラスター 直進して画面前方のどこかで停止→レーザービーム射出→急いで後退するレーザー系
                    elif self.event_list[self.event_index][2] == RAY_BLASTER:
                         new_enemy = Enemy()
                         new_enemy.update(RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,    -2,(randint(0,1)-0.5),        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.98*self.enemy_speed_mag,0,  0,  HP02 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,80 + randint(0,40),0,0,      0,0,0,0,      E_NO_POW,ID00 ,0,0,0,      0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
                    #ボルダー 硬めの弾バラマキ重爆撃機
                    elif self.event_list[self.event_index][2] == VOLDAR:
                         new_enemy = Enemy()
                         new_enemy.update(VOLDAR,ID00,      ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,    0,0,        0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_40,SIZE_24,   -0.07*self.enemy_speed_mag,1,  0,  HP59 * self.enemy_hp_mag,   0,0,  E_SIZE_HI_MIDDLE53,  0,0,0,      0,0,0,0,      E_SHOT_POW,ID00    ,1,0.007,0.6,      0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT10)
                         self.enemy.append(new_enemy)
               elif self.event_list[self.event_index][1] == EVENT_FAST_FORWARD_NUM:  #イベント「早回し編隊パラメーター設定」の場合
                    self.fast_forward_destruction_num   = self.event_list[self.event_index][2] #早回しの条件を満たすのに必要な「敵編隊殲滅必要数」を変数に代入する
                    self.fast_forward_destruction_count = self.event_list[self.event_index][3] #敵編隊を早回しで破壊した時にどれだけ出現時間が速くなるのか？そのカウントを変数に代入する           
               elif self.event_list[self.event_index][1] == EVENT_ADD_APPEAR_ENEMY:  #イベント「敵出現（早回しによる敵追加出現）」の場合
                    if self.add_appear_flag == 1: #「早回し敵発生フラグ」が立っているのならば
                         #サーコイン発生！
                         if self.event_list[self.event_index][2] == CIR_COIN:
                              for number in range(self.event_list[self.event_index][5]):
                                   #編隊なので現在の編隊ＩＤナンバーであるcurrent_formation_idも出現時にenemyクラスに情報を書き込みます
                                   new_enemy = Enemy()
                                   new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.event_list[self.event_index][4],0,0,       0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,  -1,1,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8, 1,0,   0, HP01,  0,0, E_SIZE_NORMAL,   30,0,0,     0,0,0,0,     E_SHOT_POW,self.current_formation_id ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                                   self.enemy.append(new_enemy) 
                              
                              #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                              self.record_enemy_formation(self.event_list[self.event_index][5]) 
                    
                    self.fast_forward_destruction_num = 0        #
                    self.fast_forward_destruction_count = 0      #
                    self.add_appear_flag = 0                     #早回し関連のパラメーター数値、フラグは全てリセットします
               elif self.event_list[self.event_index][1] == EVENT_SCROLL:            #イベント「スクロール」の場合
                    #スクロールスタート
                    if   self.event_list[self.event_index][2] == SCROLL_START:
                        self.side_scroll_speed           = 1 #スクロールスピードを通常の1にする
                        self.side_scroll_speed_set_value = 1 #設定目標値も1にする
                        self.side_scroll_speed_variation = 0 #変化量は0
                    #スクロールストップ！
                    elif self.event_list[self.event_index][2] == SCROLL_STOP:
                        self.side_scroll_speed           = 0 #スクロールスピードを0にする
                        self.side_scroll_speed_set_value = 0 #設定目標値も0にする
                        self.side_scroll_speed_variation = 0 #変化量も0
                    #スクロールスピードチェンジ
                    elif self.event_list[self.event_index][2] == SCROLL_SPEED_CHANGE:
                        self.side_scroll_speed_set_value = self.event_list[self.event_index][3] #横スクロールスピードの設定値を代入
                        self.side_scroll_speed_variation = self.event_list[self.event_index][4] #横スクロールスピードの変化量を代入
                    #縦スクロールスピードチェンジ
                    elif self.event_list[self.event_index][2] == SCROLL_SPEED_CHANGE_VERTICAL:
                        self.vertical_scroll_speed_set_value = self.event_list[self.event_index][3] #縦スクロールスピードの設定値を代入
                        self.vertical_scroll_speed_variation = self.event_list[self.event_index][4] #縦スクロールスピードの変化量を代入
                    #スクロール関連のパラメーターの設定
                    elif self.event_list[self.event_index][2] == SCROLL_NUM_SET:
                        self.side_scroll_speed_set_value     = self.event_list[self.event_index][3] #横スクロールスピードの設定値を代入
                        self.side_scroll_speed_variation     = self.event_list[self.event_index][4] #横スクロールスピードの変化量を代入
                        self.vertical_scroll_speed_set_value = self.event_list[self.event_index][5] #縦スクロールスピードの設定値を代入
                        self.vertical_scroll_speed_variation = self.event_list[self.event_index][6] #縦スクロールスピードの変化量を代入              
               elif self.event_list[self.event_index][1] == EVENT_DISPLAY_STAR:                 #イベントが「EVENT_DISPLAY_STAR」の場合
                    self.star_scroll_flag = self.event_list[self.event_index][2] #星スクロールのon/offのフラグを代入する
               elif self.event_list[self.event_index][1] == EVENT_CHANGE_BG_CLS_COLOR:          #イベントが「EVENT_CHANGE_BG_CLS_COLOR」の場合
                    self.bg_cls_color = self.event_list[self.event_index][2]     #BGをCLS(クリアスクリーン)するときの色を代入する
               elif self.event_list[self.event_index][1] == EVENT_CHANGE_BG_TRANSPARENT_COLOR:  #イベントが「EVENT_CHANGE_BG_TRANSPARENT_COLOR」の場合
                    self.bg_transparent_color = self.event_list[self.event_index][2]     #BGを敷き詰める時の透明色を指定する
               elif self.event_list[self.event_index][1] == EVENT_CLOUD:                        #イベントが「背景雲の表示設定」の場合
                    #雲のパラメータを設定します
                    if   self.event_list[self.event_index][2] == CLOUD_NUM_SET:
                        self.cloud_append_interval  = self.event_list[self.event_index][3]     #雲を追加する間隔を設定
                        self.cloud_quantity         = self.event_list[self.event_index][4]     #雲の量を設定
                        self.cloud_how_flow         = self.event_list[self.event_index][5]     #雲の流れ方を設定
                        self.cloud_flow_speed       = self.event_list[self.event_index][6]     #雲の流れるスピードを設定
                    #雲の表示を開始する
                    elif self.event_list[self.event_index][2] == CLOUD_START:
                        self.display_cloud_flag = 1 #雲の表示フラグをonにします
                    #雲の表示を停止する
                    elif self.event_list[self.event_index][2] == CLOUD_STOP:
                        self.display_cloud_flag = 0 #雲の表示フラグをoffにします
               elif self.event_list[self.event_index][1] == EVENT_RASTER_SCROLL:     #イベントが「ラスタースクロールの制御」の場合
                    search_id = self.event_list[self.event_index][3] #ラスタスクロールのidを変数に代入
                    #IDごとにラスタスクロールの表示をon/offする
                    if self.event_list[self.event_index][2] == RASTER_SCROLL_ON:      #ラスタスクロールon
                          self.disp_control_raster_scroll(search_id,RASTER_SCROLL_ON) #idを元にラスタスクロールの表示フラグを変更する関数の呼び出し
                    elif self.event_list[self.event_index][2] == RASTER_SCROLL_OFF:   #ラスタスクロールoff
                          self.disp_control_raster_scroll(search_id,RASTER_SCROLL_OFF)#idを元にラスタスクロールの表示フラグを変更する関数の呼び出し
               elif self.event_list[self.event_index][1] == EVENT_BG_SCREEN_ON_OFF:  #イベントが「BGスクリーンオンオフ」の場合
                    if   self.event_list[self.event_index][2] == BG_FRONT: #[2]で指定された数値をもとにして、各disp_flagへ、[3]に入っているDISP_OFF(0)またはDISP_ON(1)の数値を代入する
                         self.disp_flag_bg_front  = self.event_list[self.event_index][3]
                    elif self.event_list[self.event_index][2] == BG_MIDDLE:
                         self.disp_flag_bg_middle = self.event_list[self.event_index][3]
                    elif self.event_list[self.event_index][2] == BG_BACK:
                         self.disp_flag_bg_back   = self.event_list[self.event_index][3]
               elif self.event_list[self.event_index][1] == EVENT_ENTRY_SPARK_ON_OFF:#イベントが「大気圏突入の火花エフェクト表示のオンオフ」の場合
                    self.atmospheric_entry_spark_flag = self.event_list[self.event_index][2] #火花エフェクトのon/offのフラグを代入する
               elif self.event_list[self.event_index][1] == EVENT_WARNING:           #イベントが「WARNING表示」の場合
                    self.warning_dialog_flag = 1                                            #WARNING警告表示フラグをonにする
                    self.warning_dialog_display_time = self.event_list[self.event_index][2] #警告表示時間を代入(単位は1フレーム)
                    self.warning_dialog_logo_time    = self.event_list[self.event_index][3] #グラフイックロゴ表示にかける時間を代入(単位は1フレーム)
                    self.warning_dialog_text_time    = self.event_list[self.event_index][4] #テキスト表示にかける時間を代入(単位は1フレーム)

                    #pyxel.playm(0)#警告音発生！緊急地震速報Ver・・・・怖い・・・
                    pyxel.playm(2)#警告音発生！
               elif self.event_list[self.event_index][1] == EVENT_BOSS:              #イベントの内容が「BOSS」の場合
                    self.game_status = SCENE_BOSS_APPEAR                            #ゲームのステータスを「BOSS_APPEAR」ボス出現！にします
                    self.born_boss()                                                #各面のボスを生み出す関数を呼び出します

               self.event_index += 1 #イベントインデックス値を1増やして次のイベントの実行に移ります
     
     #マップスクロールによる敵の発生
     def update_enemy_append_map_scroll(self):
          if self.no_enemy_mode == 1: #敵が出ないモードがonだったら・・・
               return                 #何もせずに帰ります・・・・・
          
          #今表示したマップに（「敵出現」情報）のキャラチップが含まれていたら敵を発生させる
          for i in range(WINDOW_H // 8):
                  self.get_bg_chip(WINDOW_W,i*8,0)#画面右端のマップチップのＢＧナンバーをゲットする(iの値・・・8で割ってまた8を掛けるのはスマートじゃないかも・・・)
                  
                  if   self.bg_chip == (64 /8) * 32 +(48 / 8):#マップチップx48y64(A)だったら   敵3地上固定砲台を出現させる
                         item_number = 0 #アイテムナンバー初期化
                         self.get_bg_chip(WINDOW_W+8,i*8,0)#画面右端のマップチップの更に一つ右のあるＢＧナンバーをゲットしパワーアップアイテム情報が書き込まれてるか調べる
                         if self.bg_chip == (224 /8) *32 + 0: #マップチップx0y224だったらショットアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_SHOT_POW    #ショットアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                         elif self.bg_chip == (224 /8) *32 + (64 /8): #マップチップx64y224だったらミサイルアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_MISSILE_POW #ミサイルアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                         elif self.bg_chip == (224 /8) *32 + (128 /8): #マップチップx128y224だったらシールドアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_SHIELD_POW  #シールドアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                         self.get_bg_chip(WINDOW_W,i*8,0)#bgxの値が変化したので再度bgチップナンバーを取得する関数を呼び出す
                         new_enemy = Enemy()
                         new_enemy.update(3,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,   0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,  1,0,    0, HP01,   0,0,E_SIZE_NORMAL,0,0,0,      0,0,0,0,      item_number,ID00 ,0,0,0,     0  ,0,0,0,     0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
                         self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む                         
                  
                  elif self.bg_chip == (64 /8) * 32 +(56 / 8):#マップチップx56y64(B)だったら   敵4天井固定砲台を出現させる
                         item_number = 0 #アイテムナンバー初期化
                         self.get_bg_chip(WINDOW_W+8,i*8,0)#画面右端のマップチップの更に一つ右のあるＢＧナンバーをゲットしパワーアップアイテム情報が書き込まれてるか調べる
                         if self.bg_chip == (224 /8) *32 + 0: #マップチップx0y224だったらショットアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_SHOT_POW    #ショットアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                         elif self.bg_chip == (224 /8) *32 + (64 /8): #マップチップx64y224だったらミサイルアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_MISSILE_POW #ミサイルアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                         elif self.bg_chip == (224 /8) *32 + (128 /8): #マップチップx128y224だったらシールドアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_SHIELD_POW  #シールドアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む

                         self.get_bg_chip(WINDOW_W,i*8,0)#bgxの値が変化したので再度bgチップナンバーを取得する関数を呼び出す
                         new_enemy = Enemy()
                         new_enemy.update(4,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,  1,0,  0,  HP01,    0,0,E_SIZE_NORMAL,0,0,0,     0,0,0,0,     item_number,ID00 ,0,0,0,     0  ,0,0,0,     0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
                         self.delete_map_chip(self.bgx,i)#敵を出現させたら(「敵出現」情報)のキャラチップは不要なのでそこに（0=何もない空白）を書き込む

                  elif self.bg_chip == (64 /8) * 32 +(64 / 8):#マップチップx64y64(C)だったら   敵5を出現させる（ホッパー君mk2）
                         new_enemy = Enemy()
                         new_enemy.update(5,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,    0.4,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,      SIZE_8,SIZE_8,    0.2,0,  -1,     HP01,   0,0,   E_SIZE_NORMAL,(i * 8),-20,1,      0,0,0,0,      E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,MOVING_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
                         self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                                                
                  elif self.bg_chip == (64 /8) * 32 +(72 / 8):#マップチップx72y64(D)だったら   敵2を出現させる(サインカーブを描く敵)
                         new_enemy = Enemy()
                         new_enemy.update(SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,       0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,   0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,      SIZE_8,SIZE_8,    1,0,   0,   HP01,    0,0,   E_SIZE_NORMAL,   0.5,0.05,0,     0,0,0,0,      E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
                         self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                                             
                  elif self.bg_chip == (64 /8) * 32 +(80 / 8):#マップチップx80y64(E)だったら   敵10を出現させる(地上スクランブルハッチ)
                         new_enemy = Enemy()
                         new_enemy.update(10,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,       0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_24,SIZE_16,   0.5,0,   0,    HP10,   0,0,   E_SIZE_MIDDLE32,  (randint(0,130) + 10),  6, 20,      0,0,0,0,      E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT10,PT01)
                         self.enemy.append(new_enemy)
                         self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                                               
                  elif self.bg_chip == (64 /8) * 32 +(88 / 8):#マップチップx88y64(F)だったら   敵11を出現させる(天井スクランブルハッチ)
                         new_enemy = Enemy()
                         new_enemy.update(11,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,      SIZE_24,SIZE_16,   0.5,0,   0,    HP10,   0,0,   E_SIZE_MIDDLE32_Y_REV,  (randint(0,130) + 10),  6, 20,      0,0,0,0,      E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT10,PT01)
                         self.enemy.append(new_enemy)
                         self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                                  
                  elif self.bg_chip == (64 /8) * 32 +(96 / 8):#マップチップx96y64(G)だったら   敵14赤いアイテムキャリアーを出現させる
                         item_number = 0 #アイテムナンバー初期化
                         self.get_bg_chip(WINDOW_W+8,i*8,0)#画面右端のマップチップの更に一つ右のあるＢＧナンバーをゲットしパワーアップアイテム情報が書き込まれてるか調べる
                         if self.bg_chip == (232 /8) *32 + 0: #マップチップx0y232だったらクローアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_CLAW_POW    #クローアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                         
                         elif self.bg_chip == (232 /8) *32 + (64 /8): #マップチップx64y232だったらテイルショットアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_TAIL_SHOT_POW  #テイルショットアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                              
                         elif self.bg_chip == (232 /8) *32 + (72 /8): #マップチップx72y232だったらペネトレートロケットアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_PENETRATE_ROCKET_POW  #ペネトレートロケットアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                              
                         elif self.bg_chip == (232 /8) *32 + (80 /8): #マップチップx80y232だったらサーチレーザーアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_SEARCH_LASER_POW #サーチレーザーアイテムアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                              
                         elif self.bg_chip == (232 /8) *32 + (88 /8): #マップチップx88y232だったらホーミングミサイルアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_HOMING_MISSILE_POW  #ホーミングミサイルアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                              
                         elif self.bg_chip == (232 /8) *32 + (96 /8): #マップチップx96y232だったらショックバンパーアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_SHOCK_BUMPER_POW #ショックバンパーアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                              
                         elif self.bg_chip == (232 /8) *32 + (104 /8): #マップチップx104y232だったらトライアイングルアイテム情報を付加せよの命令のマップチップなので
                              item_number = E_TRIANGLE_POW #トライアングルアイテム
                              self.delete_map_chip(self.bgx,i)#命令マップチップを消去する（0=何もない空白）を書き込む
                              
                         
                         self.get_bg_chip(WINDOW_W,i*8,0)#bgxの値が変化したので再度bgチップナンバーを取得する関数を呼び出す
                         new_enemy = Enemy()
                         new_enemy.update(14,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,    -0.44,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_24,SIZE_8,   0,0,   0,    HP10,   0,0,   E_SIZE_NORMAL,  0,0,0,   0,0,0,0,      item_number,ID00 ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)

                         self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む 
                  
                  elif self.bg_chip == (64 /8) * 32 +(104/ 8):#マップチップx104y64(H)だったら  敵12を出現させる(直進して画面前方のどこかで停止→レーザービーム射出→急いで後退)
                         new_enemy = Enemy()
                         new_enemy.update(RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W + 8,i * 8,0,0,       0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,     -2,(randint(0,1)-0.5),      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,      SIZE_8,SIZE_8,   0.98,0,     0,    HP01,  0,0,    E_SIZE_NORMAL,   80 + randint(0,40),0,0,      0,0,0,0,      E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
                         self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                  
                  elif self.bg_chip == (64 /8) * 32 +(112/ 8):#マップチップx112y64(I)だったら  敵15を出現させる(地面を左右に動きながらチョット進んできて弾を撃つ移動砲台,何故か宇宙なのに重力の影響を受けて下に落ちたりもします)
                         new_enemy = Enemy()
                         new_enemy.update(15,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,        0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,     0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,      SIZE_8,SIZE_8,   0.8,0,     -1,    HP01,  70,80,    E_SIZE_NORMAL,   70,80,0,      0,0,0,0,        E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,MOVING_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                         self.enemy.append(new_enemy)
                         self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
     
     #BGマップチップデータ書き換えによる背景アニメーション
     def update_bg_rewrite_animation(self):
          #今表示したマップに書き換え対象のキャラチップが含まれていたらＢＧデータナンバーを1増やしてアニメーションさせる
          if self.scroll_type == SCROLL_TYPE_8FREEWAY_SCROLL_AND_RASTER: #全方向フリースクロール＋ラスタースクロールの場合
               #最前面のＢＧ書き換えアニメーション
               for w in range(WINDOW_W // 8):
                    for h in range(WINDOW_H // 8):
                         bg_animation_count = len(self.bg_animation_list) #bg_animation_listのなかにどれだけのリストが入っているのか数える
                         for i in range(bg_animation_count):
                              self.get_bg_chip_free_scroll(w * 8,h * 8    ,0)#座標(w,h)のマップチップのBGナンバーを取得する
                              bg_ani_x =     self.bg_animation_list[i][0] #BGアニメーションを開始するチップのx座標を変数に代入
                              bg_ani_y =     self.bg_animation_list[i][1] #                               y座標を変数に代入
                              bg_ani_speed = self.bg_animation_list[i][2] #                              スピードを変数に代入
                              bg_ani_num =   self.bg_animation_list[i][3] #                             パターン数を変数に代入
                              
                              if (bg_ani_y / 8) * 32 + (bg_ani_x / 8) <= self.bg_chip <= (bg_ani_y / 8) * 32 + (bg_ani_x / 8 + bg_ani_num): #マップチップがx72y80からx128y80の間なら赤い棒のアニメーションパターンなので
                                   #bg_ani_speed毎フレームに従ってbg_ani_numパターン数のアニメーションを行います
                                   self.write_map_chip_free_scroll(self.bgx,self.bgy,(bg_ani_y // 8) * 32 + (bg_ani_x // 8) + pyxel.frame_count // bg_ani_speed % bg_ani_num)
               
               
               #中間の山脈の流れる滝のアニメーション
               #マップ座標のY=250だけ山脈遠景滝BGアニメーションチップを置くルールにしているのでy座標250だけ目的のマップチップがあるかをサーチして書き換える
               #
               #参考drawクラスでの山脈遠景表示のコード pyxel.bltm(-int(self.scroll_count  // 4  % (256*8 - 160)),-(self.vertical_scroll_count // 16) + 160,  1,     0,248,    256,5,    self.bg_transparent_color)
               self.bgx = int(self.scroll_count // 32 % (256 - 20)) #bgxに山脈遠景表示時のBGマップの1番左端のx座標(0~255)が入る
               self.bgy = 250 #y座標は250で固定
               #bgx,bgyのクリッピング処理
               #bgxがMAPの外に存在するときは強制的にbgxを0または255にしちゃう(マイナスの値や256以上だとエラーになるため)
               if  self.bgx < 0:
                     self.bgx = 0
               if self.bgx > 255:
                    self.bgx = 255
               #bgyがMAPの外に存在するときは強制的にbgyを0または255にしちゃう(マイナスの値や256以上だとエラーになるため)
               if self.bgy < 0:
                    self.bgy = 0
               if self.bgy > 255:
                    self.bgy = 255  

               self.mountain_x = self.bgx
               for w in range (WINDOW_W // 8 + 1):# x座表は理論的には0~20で行けるはずなんだけど20の時書き換えると微妙に画面右端で書き換えていないのかバレるので +1してます、ハイ！
                    bg_animation_count = len(self.bg_animation_list) #bg_animation_listのなかにどれだけのリストが入っているのか数える
                    for i in range(bg_animation_count):
                         self.bg_chip = pyxel.tilemap(self.reference_tilemap).get(self.bgx + w,self.bgy) #座標(bgx+w,bgy)のマップチップのBGナンバーを取得する
                         bg_ani_x =     self.bg_animation_list[i][0] #BGアニメーションを開始するチップのx座標を変数に代入
                         bg_ani_y =     self.bg_animation_list[i][1] #                               y座標を変数に代入
                         bg_ani_speed = self.bg_animation_list[i][2] #                              スピードを変数に代入
                         bg_ani_num =   self.bg_animation_list[i][3] #                             パターン数を変数に代入
                              
                         if (bg_ani_y / 8) * 32 + (bg_ani_x / 8) <= self.bg_chip <= (bg_ani_y / 8) * 32 + (bg_ani_x / 8 + bg_ani_num): #マップチップナンバーがーアニメーションするべきチップナンバーの範囲内だったのなら
                              #bg_ani_speed毎フレームに従ってbg_ani_numパターン数のアニメーションを行い,該当するチップナンバーを書き込みます
                              pyxel.tilemap(self.reference_tilemap).set(self.bgx + w,self.bgy, (bg_ani_y // 8) * 32 + (bg_ani_x // 8) + pyxel.frame_count // bg_ani_speed % bg_ani_num)

     #座標直接指定によるBGチップデータの書き換えアニメーション (ダミーでござる)
     def update_dummy_bg_animation(self):
          for i in range(15):
               self.write_map_chip_free_scroll(95,184-i,(64 // 8) * 32 + (144 // 8) + pyxel.frame_count * 3 % 8)

     #イベントアペンドリクエスト(イベント追加依頼）による敵の発生
     def update_event_append_request(self):
          event_append_request_count = len(self.event_append_request)
          for i in reversed (range(event_append_request_count)):
               if self.stage_count == self.event_append_request[i].timer:
                    if self.event_append_request[i].event_type == EVENT_ENEMY: #イベントの内容が敵出現の場合
                         #サーコインの追加発生！
                         if self.event_append_request[i].enemy_type == CIR_COIN:
                              for e in range(self.event_append_request[i].number):
                                   #編隊なので現在の編隊ＩＤナンバーであるcurrent_formation_idも出現時にenemyクラスに情報を書き込みます
                                   new_enemy = Enemy()
                                   new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (e * 12),self.event_append_request[i].posy,0,0,      0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,  -1,1,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8, 1,0,   0, HP01,  0,0, E_SIZE_NORMAL,   30,0,0,      0,0,0,0,         E_NO_POW,self.current_formation_id ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                                   self.enemy.append(new_enemy) 
                              
                         #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                         self.record_enemy_formation(self.event_append_request[i].number)
                         del self.event_append_request[i] #敵を追加発生リクエストをリストから消去します

     #敵の更新（移動とか弾の発射とか他の敵を生み出すとか、そういう処理）
     def update_enemy(self):
          enemy_count = len(self.enemy)
          for i in range (enemy_count):
            if   self.enemy[i].enemy_type ==  1:#敵タイプ1の更新    直進して斜め後退→勢いよく後退していく10機編隊
                if self.enemy[i].enemy_flag1 == 0:
                #敵１を前進させる
                    self.enemy[i].posx = self.enemy[i].posx - self.enemy[i].move_speed#X座標をmove_speed分減らして左方向に進む
                    if self.enemy[i].posx < 20:#敵の座標が20以下なら後退処理を始める
                           self.enemy[i].enemy_flag1 = 1 #flag1 後退フラグON
                           if self.enemy[i].posy > (WINDOW_H / 2):#画面の上半分に居るのか下半分に居るのか判別
                                self.enemy[i].vy = -1#画面上半分に居たのならVYに-1を入れて下方向に移動（初期設定ではVYには１が入っているので上方向に移動することに成る）

                else:
                    if self.enemy[i].enemy_count1 > 0:#enemy_count1には斜め方向に移動する回数が入っている
                            self.enemy[i].enemy_count1 -= 1#斜め移動する回数を１減らす
                            self.enemy[i].posx += 0.5#0.5の増分で斜め右方向に逃げていく
                            self.enemy[i].posy += self.enemy[i].vy


                    else:#斜め後退処理が終わったら高速で右方向に逃げていく
                              self.enemy[i].posx = self.enemy[i].posx + 2#2ドットの増分で右方向に逃げていく
                              if self.enemy[i].posx > WINDOW_W -8 and (randint(0,self.run_away_bullet_probability) == 0):
                                  self.ex = self.enemy[i].posx
                                  self.ey = self.enemy[i].posy
                                  self.enemy_aim_bullet(self.ex,self.ey,0,0,0,0,1)#後退時に自機狙いの弾を射出して去っていく
            elif self.enemy[i].enemy_type ==  2:#敵タイプ2の更新    サインカーブを描く3機編隊
                #敵２をサインカーブを描きながら移動させる 
                 self.enemy[i].posx -= self.enemy[i].move_speed#X座標をmove_speed分減らして左方向に進む
                 self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー enemy_count_2は速度
                 self.enemy[i].posy += self.enemy[i].enemy_count1 * math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅
            elif self.enemy[i].enemy_type ==  3:#敵タイプ3の更新    固定砲台（地面に張り付く１連射タイプ）
                 #敵３を背景スクロールに合わせて左へ移動させる
                 self.enemy[i].posx -= self.side_scroll_speed * 0.5
                 if self.enemy[i].posx < WINDOW_W -80 and (randint(0,(self.run_away_bullet_probability) * 50) == 0):
                                  self.ex = self.enemy[i].posx
                                  self.ey = self.enemy[i].posy
                                  self.enemy_aim_bullet(self.ex,self.ey,0,0,0,0,1)#画面端から出現して８０ドット進んだら、自機狙いの弾を射出
            elif self.enemy[i].enemy_type ==  4:#敵タイプ4の更新    固定砲台（天井に張り付く１連射タイプ）
                 #敵４を背景スクロールに合わせて左へ移動させる
                 self.enemy[i].posx -= self.side_scroll_speed * 0.5
                 if self.enemy[i].posx < WINDOW_W -80 and (randint(0,(self.run_away_bullet_probability) * 50) == 0):
                                  self.ex = self.enemy[i].posx
                                  self.ey = self.enemy[i].posy
                                  self.enemy_aim_bullet(self.ex,self.ey,0,0,0,0,1)#画面端から出現して８０ドット進んだら、自機狙いの弾を射出
            elif self.enemy[i].enemy_type ==  5:#敵タイプ5の更新    ぴょんぴょんはねるホッパー君mk2
                 #敵５を背景スクロールに合わせて左へ移動させる
                 #
                 #enemy_count1をy_prevとして使用してます
                 #enemy_count2をFとして使用してます
                 #enemy_count3を地面に接触した時弾を出すため滞在するタイマーカウンターとして使用します
                 #マリオのジャンプアルゴリズム参考
                 #
                 #初期変数定義
                 #y_prev = pos.y
                 #F = -1 ジャンプの瞬間だけ-10 空中の状態は1
                 #
                 #メイン処理 
                 #y_temp = pos.y
                 #pos.y += (pos.y -posy_prev) + F
                 #pos.y_prev = y_temp
                 if self.enemy[i].enemy_count2 < -20:
                      self.enemy[i].enemy_count2 = -20
                 
                 
                 self.enemy[i].enemy_count3 -= 1

                 if self.enemy[i].enemy_count3 <= 0:
                      self.enemy[i].vx = 1.2
                      self.enemy[i].enemy_count3 = 0
                 else:
                      self.enemy[i].vx = 0.5

                 #x座標をVX（増加数）とdirection(-1なら左方向 1なら右方向)によって更新する
                 self.enemy[i].posx += self.enemy[i].vx * self.enemy[i].direction
                 
                 
                 if self.enemy[i].enemy_count3 <= 0:
                     self.y_tmp = self.enemy[i].posy#y_temp = y
                     self.enemy[i].posy += (self.enemy[i].posy - self.enemy[i].enemy_count1) + (self.enemy[i].enemy_count2 * self.enemy[i].move_speed) #y += ((y -y_prev) + F) * move_speed (ココが重要！)
                     self.enemy[i].enemy_count1 = self.y_tmp#y_prev = y_tmp
                     self.enemy[i].enemy_count2 = 1#F = 1

                     self.x = self.enemy[i].posx + 4
                     self.y = self.enemy[i].posy + 8
                     self.check_bg_collision(self.x,self.y,0,0)#ホッパー君の足元が障害物かどうかチェック
                     if self.collision_flag == 0:#足元に障害物が無かった時の処理→そのままで行く
                         
                             self.enemy_bound_collision_flag = 0#デバッグ用のバウンドフラグをＯＦＦにする
                             
                   
                     else:                         
                             self.x = self.enemy[i].posx + 4
                             self.y = self.enemy[i].posy - 8
                             self.check_bg_collision(self.x,self.y,0,0)#ホッパー君の頭の上が障害物なのか（足元と頭上、障害物に挟まっているのか？）チェック
                             if self.collision_flag == 0:
                                  #ホッパー君の足元は障害物、ホッパー君は障害物に今っていなかったので再ジャンプできるゾ！
                                  self.enemy[i].enemy_count2 = -20#  F=-10   Fに-10を入れて再度ジャンプさせる
                                  self.enemy_bound_collision_flag = 1#デバッグ用のバウンドフラグをＯＮにする
                                        
                                  self.enemy[i].enemy_count3 = 20#地面に留まる踏ん張りカウントを１０に設定
                                  self.enemy[i].posy -= 1#なんだかわかんないけど地面にめり込んでいくので強制的にＹ軸を上方向に移動させてやる（－１補正を入れる）
                                  if randint(0,self.run_away_bullet_probability) == 0:
                                      self.ex = self.enemy[i].posx
                                      self.ey = self.enemy[i].posy
                                      self.enemy_aim_bullet_rank(self.ex,self.ey,0,0,0,0,1)#自機狙いの弾発射！

                             else:
                                  #ホッパー君の足元は障害物＆ホッパー君も壁に挟まっていた（ガーン！）だからそのまま壁に衝突したことは無しとするッ！
                                  self.enemy_bound_collision_flag = 0#デバッグ用のバウンドフラグをＯＦＦにする
                                  self.enemy[i].enemy_count2 = -1#ジャンプ力は初期値に戻してやる
                                  self.enemy[i].enemy_count1 = self.enemy[i].posy #y_prev = posy
                                  self.enemy[i].enemy_count3 = 1
                                  

                         

                 pyxel.blt(135,WINDOW_H - 8, 0, 0,80, 8,8, 0)
                 if self.enemy[i].posx < 0:
                      self.enemy[i].direction = 1#もしx座標が0まで画面の左端に進んだら跳ね返りdirectionフラグを(+1右方向増加）にして右に反転後退していく
            elif self.enemy[i].enemy_type ==  6:#敵タイプ6の更新    謎の回転飛翔体Ｍ５４
                
                #敵6を回転させる 
                 
                 self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー(timer) enemy_count_2は速度(speed)
                 self.enemy[i].posx += self.enemy[i].enemy_count1 * math.cos(self.enemy[i].enemy_count3)
                 self.enemy[i].posy += self.enemy[i].enemy_count1 * -math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅(intensity)

                 self.enemy[i].posx -= 0.05
            elif self.enemy[i].enemy_type ==  7:#敵タイプ7の更新    追尾戦闘機 (サインカーブを描きつつ追尾してくる)
                #敵７を自機に追尾させる
                #目標までの距離を求める dに距離が入る
                self.d = math.sqrt((self.my_x - self.enemy[i].posx) * (self.my_x - self.enemy[i].posx) + (self.my_y - self.enemy[i].posy) * (self.my_y - self.enemy[i].posy))
                #弾の速度 vx,vyを求める
                #速さが一定値move_speedになるようにする
                #目標までの距離dが0の時は速度を左方向にする
                if self.d == 0:
                         self.vx = 0
                         self.vy = self.enemy[i].move_speed
                else:
                         #敵と自機との距離とＸ座標、Ｙ座標との差からＶＸ，ＶＹの増分を計算する
                         self.vx = ((self.my_x - self.enemy[i].posx) / (self.d * self.enemy[i].move_speed))
                         self.vy = ((self.my_y - self.enemy[i].posy) / (self.d * self.enemy[i].move_speed))
                #敵の座標(posx,posy)を増分(vx,vy)を加減算更新して敵を移動させる
                self.enemy[i].posx += self.vx
                self.enemy[i].posy += self.vy


               
                 
                self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー(timer) enemy_count_2は速度(speed)
                self.enemy[i].posx += self.enemy[i].enemy_count1 * math.cos(self.enemy[i].enemy_count3)
                self.enemy[i].posy += self.enemy[i].enemy_count1 * -math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅(intensity)

                self.enemy[i].posx -= 0.05
            elif self.enemy[i].enemy_type ==  8:#敵タイプ8の更新    追尾戦闘機
                #敵８を自機に追尾させる
                vx0 = self.enemy[i].vx
                vy0 = self.enemy[i].vy #敵の速度(vx,vy)を(vx0,vy0)に退避する

                #目標までの距離を求める dに距離が入る
                self.d = math.sqrt((self.my_x - self.enemy[i].posx) * (self.my_x - self.enemy[i].posx) + (self.my_y - self.enemy[i].posy) * (self.my_y - self.enemy[i].posy))
                
                #敵の速度 vx,vyを求める
                #速さが一定値move_speedになるようにする
                #目標までの距離dが0の時は速度を左方向にする
                #enemy_count3をtheta(Θ)旋回できる角度の上限として使用します
                #自機方向の速度ベクトル(vx1,vy1)を求める
                if self.d == 0:#目標（自機）までの距離は0だった？（重なっていた？）
                         vx1= 0
                         vy1 = self.enemy[i].move_speed #目標までの距離dが0の時は速度を左方向にする
                else:
                         #敵と自機との距離とＸ座標、Ｙ座標との差からＶＸ，ＶＹの増分を計算する
                         
                         vx1 = ((self.my_x - self.enemy[i].posx) / (self.d * self.enemy[i].move_speed))
                         vy1 = ((self.my_y - self.enemy[i].posy) / (self.d * self.enemy[i].move_speed))
                #右回り旋回角度上限の速度ベクトル(vx2,vy2)を求める
                #math.piはπ（円周率3.141592......)
                #ううううぅ・・・難しい・・・・数学赤点の私には難しい・・・・
                self.rad = 3.14 / 180 * self.enemy[i].enemy_count3#rad = 角度degree（theta）をラジアンradianに変換
                
                vx2 = math.cos(self.rad) * vx0 - math.sin(self.rad) * vy0
                vy2 = math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0

                #自機方向に曲がるのか？ それとも旋回角度上限一杯（面舵一杯！とか取り舵一杯！とかそういう表現）で曲がるのか判別する
                if vx0 * vx1 + vy0 * vy1 >= vx0 * vx2 + vy0 * vy2:
                     #自機方向が旋回可能範囲内の場合の処理
                     #自機方向に曲がるようにする
                     self.enemy[i].vx = vx1
                     self.enemy[i].vy = vy1
                else:
                     #自機が旋回可能範囲を超えている場合（ハンドルをいっぱいまで切っても自機に追いつけないよ～）ハンドル一杯まで切る！
                     #左回り（取り舵方向）の旋回角度上限の速度ベクトルvx3,vy3を求める
                     vx3 =  math.cos(self.rad) * vx0 + math.sin(self.rad) * vy0
                     vy3 = -math.sin(self.rad) * vx0 + math.cos(self.rad) * vy0

                     #敵から自機への相対ベクトル(px,py)を求める
                     px = self.my_x - self.enemy[i].posx
                     py = self.my_y - self.enemy[i].posy

                     #右回りか左回りを決める
                     #右回りの速度ベクトルの内積(p,v2)と左回りの速度ベクトルの内積(p,v3)の比較で右回りか左回りか判断する
                     #旋回角度が小さいほうが内積が大きくなるのでそちらの方に曲がるようにする
                     #
                     if px * vx2 + py * vy2 >= px * vx3 + py * vy3:
                          #右回り（面舵方向）の場合
                          self.enemy[i].vx = vx2
                          self.enemy[i].vy = vy2
                     else:
                          #左回り（取り舵方向）の場合
                          self.enemy[i].vx = vx3
                          self.enemy[i].vy = vy3
                    
                #敵の座標(posx,posy)を増分(vx,vy)を加減算更新して敵を移動させる(座標更新！)
                self.enemy[i].posx += self.enemy[i].vx
                self.enemy[i].posy += self.enemy[i].vy
            elif self.enemy[i].enemy_type ==  9:#敵タイプ9の更新    自機のＹ軸を合わせた後突進してくる敵
                if self.enemy[i].enemy_flag2 == 0:#自機撃墜フラグ（自機と完全に重なったフラグ）はまだ建ってない？？
                    if self.enemy[i].enemy_flag1 == 0:#自機の位置をサーチしてどちらの方向に進むかのフラグはまだ建ってない？
                        if self.my_y > self.enemy[i].posy:
                            self.enemy[i].vy = 0.5
                        else:
                            self.enemy[i].vy = -0.5
                        #自機索敵フラグenemy_flag1をonにする
                        self.enemy[i].enemy_flag1 = 1
                
                    if self.enemy[i].posy == self.my_y:#自機と敵機のY座標は同じになったかな？？？？
                        if self.my_x > self.enemy[i].posx:#自機のｘ座標を見て右方向か左方向か進む方向に増分(vx)を加減算してやる
                                self.enemy[i].vx = 1
                                self.enemy[i].vy = 0
                        else:
                                self.enemy[i].vx = -1
                                self.enemy[i].vy = 0

                
                    if self.my_x == self.enemy[i].posx and self.my_y == self.enemy[i].posy:
                         self.enemy[i].enemy_flag2 = 1#自機と敵機の座標が完全に重なっていたら自機撃墜フラグをＯＮにする
            
                if self.enemy[i].posx < 5:#x座標が左端なら弾を射出
                                  self.ex = self.enemy[i].posx
                                  self.ey = self.enemy[i].posy
                                  self.enemy_aim_bullet_rank(self.ex,self.ey,0,0,0,0,1)#後退時に自機狙いの弾を射出して去っていく
                
                #vx,vyで敵の座標posx,posy更新！移動！！
                self.enemy[i].posx += self.enemy[i].vx
                self.enemy[i].posy += self.enemy[i].vy
            elif self.enemy[i].enemy_type == 10:#敵タイプ10の更新  スクランブルハッチ（地面タイプ）
                 
                 #enemy_flag1を状態遷移フラグとして使用します
                 #    0=待機中（射出開始カウンタを減らしていく）
                 #    1～20ハッチ開放アニメーション中
                 #    21  敵機発進待機中（射出間隔用カウンタを減らしていく）カウンタがゼロになったら遷移状態「22敵機発射」にする
                 #    22  敵機発射！（敵総数カウンタを減らしていく）カウンタがゼロになったら遷移状態「23ハッチ閉鎖」にする
                 #    23以上ハッチ閉鎖アニメーション中
                 #    23以上は敵を出し切ったので何もしない
                 #enemy_flag2を敵射出間隔制御用の変数として使用します
                 #enemy_count1を出現してから突進タイプの敵を出すまでの時間のカウンタで使用します（射出開始カウンタ）（最初にどのタイミングで敵を出し始めるか数字を入れておいてね）
                 #enemy_count2を射出する敵の総数です（敵総数カウンタ）                                          （最初に何機だすか数字を入れておいてね）
                 #enemy_count3を敵を射出する間隔用カウンタとして使用します（射出間隔用カウンタ）（定数です変化はしません）
                 if self.enemy[i].enemy_flag1 == 0:#ハッチから敵を出し切ってないかどうかチェック
                      self.enemy[i].enemy_count1 -= 1#射出開始カウンタを１減らす
                      if self.enemy[i].enemy_count1 == 0:
                           self.enemy[i].enemy_flag1 = 1#射出開始カウンタが0になったら遷移状態を「ハッチ開放開始」にする
                 
                 if 1 <= self.enemy[i].enemy_flag1 <= 20:#flag1が1～20の間はハッチ開放アニメーションをするのでflag1を1増やしていく(flag1はアニメーション様にオフセットとして使う)
                      self.enemy[i].enemy_flag1 += 1

                 if self.enemy[i].enemy_flag1 == 21:#敵機発進待機中？
                       self.enemy[i].enemy_flag2 -= 1#射出間隔カウント(変数)を1減らす
                       if self.enemy[i].enemy_flag2 <= 0:#射出間隔カウンターがゼロ以下になったら敵機射出
                            self.enemy[i].enemy_flag1 = 22#遷移状態を「22敵機発射」にする
                 
                 if self.enemy[i].enemy_flag1 == 22:#敵機発射？
                       if len(self.enemy) < 400:
                              new_enemy = Enemy()#敵９を1機生み出す
                              new_enemy.update(9,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.enemy[i].posx + 7,self.enemy[i].posy - 2,0,0,       0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,  -self.side_scroll_speed * 0.5,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,      SIZE_8,SIZE_8,   1.2,0,   0,    HP01,     0,0,   E_SIZE_NORMAL,  0,0,0,       0,0,0,0,        E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                              self.enemy.append(new_enemy)#リストにアペンド追加！

                       self.enemy[i].enemy_count2  -= 1#敵射出数を1減らす
                       if self.enemy[i].enemy_count2 == 0:#射出する敵の数はもうゼロになったかな？
                            self.enemy[i].enemy_flag1 = 23#敵を全部出し切ったのなら遷移状態を「23ハッチ閉鎖中」にする
                       else:
                            self.enemy[i].enemy_flag2 = self.enemy[i].enemy_count3#射出間隔カウンターを設定した初期に戻す
                            self.enemy[i].enemy_flag1 = 21#遷移状態を「21敵機発進待機中」にする

                 if 23 <= self.enemy[i].enemy_flag1 <= 46:#flag1が23以上の間はハッチ閉鎖アニメーションするのでflag1を1増やしていく(flag1はアニメーション様にオフセット値として使う４６まで引っ張る)
                      self.enemy[i].enemy_flag1 += 1
                      self.enemy[i].status = ENEMY_STATUS_DEFENSE #敵９を出し切った後は防御モードにする
                 #敵１０を背景スクロールに合わせて左へ移動させる
                 self.enemy[i].posx -= self.side_scroll_speed * 0.5#基本BGスクロールスピードは0.5、それと倍率扱いのside_scroll_speedを掛け合わせてスクロールと同じように移動させてやる（地面スクロールに引っ付いた状態で飛んでいくように見せるため）           
            elif self.enemy[i].enemy_type == 11:#敵タイプ11の更新  スクランブルハッチ（天井タイプ）

                 #enemy_flag1を状態遷移フラグとして使用します
                 #    0=待機中（射出開始カウンタを減らしていく）
                 #    1～20ハッチ開放アニメーション中
                 #    21  敵機発進待機中（射出間隔用カウンタを減らしていく）カウンタがゼロになったら遷移状態「22敵機発射」にする
                 #    22  敵機発射！（敵総数カウンタを減らしていく）カウンタがゼロになったら遷移状態「23ハッチ閉鎖」にする
                 #    23以上ハッチ閉鎖アニメーション中
                 #    23以上は敵を出し切ったので何もしない
                 #enemy_flag2を敵射出間隔制御用の変数として使用します
                 #enemy_count1を出現してから突進タイプの敵を出すまでの時間のカウンタで使用します（射出開始カウンタ）（最初にどのタイミングで敵を出し始めるか数字を入れておいてね）
                 #enemy_count2を射出する敵の総数です（敵総数カウンタ）                                          （最初に何機だすか数字を入れておいてね）
                 #enemy_count3を敵を射出する間隔用カウンタとして使用します（射出間隔用カウンタ）（定数です変化はしません）
                 if self.enemy[i].enemy_flag1 == 0:#ハッチから敵を出し切ってないかどうかチェック
                      self.enemy[i].enemy_count1 -= 1#射出開始カウンタを１減らす
                      if self.enemy[i].enemy_count1 == 0:
                           self.enemy[i].enemy_flag1 = 1#射出開始カウンタが0になったら遷移状態を「ハッチ開放開始」にする
                 
                 if 1 <= self.enemy[i].enemy_flag1 <= 20:#flag1が1～20の間はハッチ開放アニメーションをするのでflag1を1増やしていく(flag1はアニメーション様にオフセットとして使う)
                      self.enemy[i].enemy_flag1 += 1

                 if self.enemy[i].enemy_flag1 == 21:#敵機発進待機中？
                       self.enemy[i].enemy_flag2 -= 1#射出間隔カウント(変数)を1減らす
                       if self.enemy[i].enemy_flag2 <= 0:#射出間隔カウンターがゼロ以下になったら敵機射出
                            self.enemy[i].enemy_flag1 = 22#遷移状態を「22敵機発射」にする
                 
                 if self.enemy[i].enemy_flag1 == 22:#敵機発射？
                       if len(self.enemy) < 400:
                              new_enemy = Enemy()#敵９を1機生み出す
                              new_enemy.update(9,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.enemy[i].posx + 7,self.enemy[i].posy + 10,0,0,        0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,  -self.side_scroll_speed * 0.5,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,      SIZE_8,SIZE_8,   1.2,0,    0,    HP01,     0,0,   E_SIZE_NORMAL,  0,0,0,      0,0,0,0,          E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                              self.enemy.append(new_enemy)#リストにアペンド追加！

                       self.enemy[i].enemy_count2  -= 1#敵射出数を1減らす
                       if self.enemy[i].enemy_count2 == 0:#射出する敵の数はもうゼロになったかな？
                            self.enemy[i].enemy_flag1 = 23#敵を全部出し切ったのなら遷移状態を「23ハッチ閉鎖中」にする
                       else:
                            self.enemy[i].enemy_flag2 = self.enemy[i].enemy_count3#射出間隔カウンターを設定した初期に戻す
                            self.enemy[i].enemy_flag1 = 21#遷移状態を「21敵機発進待機中」にする

                 if 23 <= self.enemy[i].enemy_flag1 <= 46:#flag1が23以上の間はハッチ閉鎖アニメーションするのでflag1を1増やしていく(flag1はアニメーション様にオフセット値として使う４６まで引っ張る)
                      self.enemy[i].enemy_flag1 += 1
                      self.enemy[i].status = ENEMY_STATUS_DEFENSE #敵９を出し切った後は防御モードにする
                 #敵１１を背景スクロールに合わせて左へ移動させる
                 self.enemy[i].posx -= self.side_scroll_speed * 0.5 #基本BGスクロールスピードは0.5、それと倍率扱いのside_scroll_speedを掛け合わせてスクロールと同じように移動させてやる（地面スクロールに引っ付いた状態で飛んでいくように見せるため）
            elif self.enemy[i].enemy_type == 12:#敵タイプ12の更新  直進して画面前方のどこかで停止→レーザービーム射出→急いで後退
                #enemy_flag1を状態遷移フラグとして使用します
                #  0=前進中
                #  1=レーザービーム発射スタート
                #  2～28=レーザービーム発射中(アニメーションパターン用の補正数値として使用します)
                #  28～56=後退アニメーションしつつ後退中
                #  57以上  ただの後退
                #enemy_count1を敵が前進してくる限界のＸ座標として設定してます
                
                if self.enemy[i].enemy_flag1 == 0:
                    #遷移状態が「前進中」なら敵１２を前進させる
                    self.enemy[i].vx = self.enemy[i].vx * self.enemy[i].move_speed#VXをmove_speed分掛けて少しづつ小さくしていく（減速させる）
                    self.enemy[i].posx += self.enemy[i].vx#x座標を更新
                    self.enemy[i].vy = self.enemy[i].vy * self.enemy[i].move_speed#VYをmove_speed分掛けて少しづつ小さくしていく（減速させる）
                    self.enemy[i].posy += self.enemy[i].vy#Y座標を更新
                    if self.enemy[i].posx < self.enemy[i].enemy_count1:#敵の座標が前進限界以下なら後退処理を始める
                             self.enemy[i].enemy_flag1 = 1#敵のＸ座標が前進限界以下なら 遷移状態を「レーザービーム発射中にする」
                elif self.enemy[i].enemy_flag1 == 1:
                     #遷移状態が「レーザービーム発射スタート」ならレーザー発射関数を呼び出し
                     self.enemy_laser(self.enemy[i].posx,self.enemy[i].posy,30,2)#レーザーの長さ30 スピード2
                     self.enemy[i].enemy_flag1 = 2#遷移状態を「レーザービーム発射中」にする

                elif 2 <= self.enemy[i].enemy_flag1 <= 28:
                     self.enemy[i].enemy_flag1 += 1#遷移状態が「レーザービーム発射中」ならフラグを1増やしていく（その場にとどまるので座標の更新は無し）
                
                elif 28 <= self.enemy[i].enemy_flag1 <= 46:#遷移状態が「後退中」なら高速で右方向に逃げていく
                     self.enemy[i].enemy_flag1 += 1#アニメーションしたいのでflag1だけは増やしていく
                     self.enemy[i].posx = self.enemy[i].posx + 1#2ドットの増分で右方向に逃げていく
                else:
                     self.enemy[i].posx = self.enemy[i].posx + 2#2ドットの増分で右方向に逃げていく                     
            elif self.enemy[i].enemy_type == 13:#敵タイプ13の更新  ゆらゆら浮遊する3way弾を発射する硬い敵(倒すとショットパワーアップアイテム)
                 #敵１３をサインカーブを描きながら移動させる 
                 self.enemy[i].posx -= self.enemy[i].move_speed#X座標をmove_speed分減らして左方向に進む
                 self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー enemy_count_2は速度
                 self.enemy[i].posy += self.enemy[i].enemy_count1 * math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅

                 self.enemy[i].enemy_flag1 += 1 #flag1を利用してカウント90ごとに弾を発射させる
                 if self.enemy[i].enemy_flag1 == 90:
                      self.enemy_forward_3way_bullet(self.enemy[i].posx,self.enemy[i].posy) #前方3way弾発射
                      self.enemy[i].enemy_flag1 = 0
            elif self.enemy[i].enemy_type == 14:#敵タイプ14の更新  ゆっくり直進してくる赤いアイテムキャリアー
                 #vx,vyで敵の座標posx,posy更新！移動！！
                self.enemy[i].posx += self.enemy[i].vx
                self.enemy[i].posy += self.enemy[i].vy
            elif self.enemy[i].enemy_type == 15:#敵タイプ15の更新  地面を左右に動きながらチョット進んできて弾を撃つ移動砲台
                 #敵１５を背景スクロールに合わせて移動させる（地上キャラなので不自然が無いように・・・）
                 self.enemy[i].posx -= self.side_scroll_speed * 0.5
                 if self.enemy[i].posx < WINDOW_W -80 and (randint(0,(self.run_away_bullet_probability) * 50) == 0):
                                  self.ex = self.enemy[i].posx
                                  self.ey = self.enemy[i].posy
                                  self.enemy_aim_bullet(self.ex,self.ey,0,0,0,0,1)#画面端から出現して８０ドット進んだら、自機狙いの弾を射出
                 
                 #directionは -1=左方向に移動 1=右方向に移動
                 #enemy_count1は左に動く原本カウント enemy_flag1はその変数として使用します
                 #enemy_count2は右に動く原本カウント enemy_flag2はその変数として使用します
                 if self.enemy[i].vy == 0: #地面を移動中の場合は(vy=0の時は横方向だけの移動)
                      if self.enemy[i].direction == -1: #左に移動
                           self.check_bg_collision(self.enemy[i].posx - 8,self.enemy[i].posy,0,0) #左側が障害物かどうかチェックする
                           if self.enemy[i].enemy_flag1 <= 0 or self.collision_flag == 1:#左移動のカウンタが0以下、又は左に障害物があったら
                                self.enemy[i].direction = 1                   #方向転換して右移動にする
                                self.enemy[i].enemy_flag2 = self.enemy[i].enemy_count2 #右移動するカウントを原本からコピーしてやる
                                self.enemy[i].vx = 0                #方向転換する瞬間なのでx軸の移動ベクトルは0にします
                           else:
                                self.enemy[i].enemy_flag1 -= 1 #左移動のカウンタを1減らします
                                self.enemy[i].vx = -1                #x軸の移動ベクトルは左方向です
                      elif self.enemy[i].direction == 1: #右に移動
                           self.check_bg_collision(self.enemy[i].posx + 8,self.enemy[i].posy,0,0) #右側が障害物かどうかチェックする
                           if self.enemy[i].enemy_flag2 <= 0 or self.collision_flag == 1:#右移動のカウンタが0以下、又は右に障害物があったら
                                self.enemy[i].direction = -1                  #方向転換して左移動にする
                                self.enemy[i].enemy_flag1 = self.enemy[i].enemy_count1 #左移動するカウントを原本からコピーしてやる
                                self.enemy[i].vx = 0                #方向転換する瞬間なのでx軸の移動ベクトルは0にします
                           else:
                                self.enemy[i].enemy_flag2 -= 1 #右移動のカウンタを1減らします
                                self.enemy[i].vx = 1                #x軸の移動ベクトルは右方向です
                 
                 self.check_bg_collision(self.enemy[i].posx + 4,self.enemy[i].posy + 8,0,0) #足元が障害物かどうかチェックする
                 if self.collision_flag == 0:#もし足元に障害物が無かった時は
                      self.enemy[i].vy = 0.5  #y軸の移動ベクトルを1にして下方向(落下方向)にする
                      self.enemy[i].vx = self.enemy[i].vx * 0.8 #x軸方向の移動ベクトルもだんだんと小さくしていく
                 else:
                      self.enemy[i].vy = 0  #障害物があった時はy軸のベクトルを0にする
                 
                 self.enemy[i].posx += self.enemy[i].vx * self.enemy[i].move_speed #移動ベクトル分加減算して移動！
                 self.enemy[i].posy += self.enemy[i].vy * self.enemy[i].move_speed
            elif self.enemy[i].enemy_type == 16:#敵タイプ16の更新  2機一体で挟みこみ攻撃をしてくるクランパリオン
                 #enemy_flag1は自機とx座標が一致して挟みこむ行動を開始するかのフラグ 0=off 1=on
                 if self.enemy[i].enemy_flag1 == 0 and -3 <= self.enemy[i].posx - self.my_x <= 3: #もしflag1がたっていない&自機と敵のx座標の差が+-3以内だったら
                      self.enemy[i].enemy_flag1 = 1  #挟みこみ開始フラグをonにする
                      self.enemy[i].vx = 0 #x軸はもう動かないようx方向の速度ベクトルvxを0にする
                      self.enemy[i].move_speed = 1.02 #移動スピードを加速気味にする
                      if self.enemy[i].posy < self.my_y: #自機より敵が上に居たのならば
                           self.enemy[i].vy = 0.92 #速度ベクトルのy軸を下方向にする
                      else:
                           self.enemy[i].vy = -0.92 #そうでないのなら逆に速度ベクトルのy軸を上方向にする
                 self.enemy[i].vx = self.enemy[i].vx * self.enemy[i].move_speed #速度ベクトルをだんだん大きくさせていく（挟み込み時）
                 self.enemy[i].vy = self.enemy[i].vy * self.enemy[i].move_speed
                 self.enemy[i].posx += self.enemy[i].vx #移動ベクトル分加減算して移動！
                 self.enemy[i].posy += self.enemy[i].vy
            elif self.enemy[i].enemy_type == 17:#敵タイプ17の更新  ベジェ曲線で定点まで移動して離脱する敵 ロールブリッツ
                if self.enemy[i].status == ENEMY_STATUS_MOVE_COORDINATE_INIT: #「移動用座標初期化」ベジェ曲線で移動するための移動元、移動先、制御点をまず初めに取得する
                         enemy_type = self.enemy[i].enemy_type
                         self.enemy_get_bezier_curve_coordinate(enemy_type,i) #敵をベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                         self.enemy[i].status = ENEMY_STATUS_MOVE_BEZIER_CURVE #状態遷移を「ベジェ曲線で移動」に設定
                
                elif self.enemy[i].status == ENEMY_STATUS_MOVE_BEZIER_CURVE: #「ベジェ曲線で移動」
                    t =  self.enemy[i].obj_time / self.enemy[i].obj_totaltime
                    if t >= 1: #tの値が1になった時は現在の座標が移動目的座標と同じ座標になった状況となるので・・・(行き過ぎ防止で念のため１以上で判別してます)
                        self.enemy[i].obj_time = 0    #タイムフレーム番号を0にしてリセットする
                        self.enemy[i].move_index += 1 #目的座標のリストのインデックスを1進める
                        if self.enemy_move_data17[self.enemy[i].move_index][0] == 9999:#x座標がエンドコード9999の場合は
                            self.enemy[i].move_index = 0 #リストインデックス値を0にしてリセットする
                        enemy_type = self.enemy[i].enemy_type
                        self.enemy_get_bezier_curve_coordinate(enemy_type,i) #敵をベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                        t = self.enemy[i].obj_time / self.enemy[i].obj_totaltime #違う座標データ群を読み込んだのでt値を再計算してやる
                        
                        #新たに移動先を設定した時は自機狙いの弾を撃つ
                        ex,ey = self.enemy[i].posx,self.enemy[i].posy
                        div_type,div_count,div_num,stop_count = 0,0,0,0
                        accel = 1.01
                        self.enemy_aim_bullet_rank(ex,ey,div_type,div_count,div_num,stop_count,accel)

                    #ベジェ曲線で移動させる方法の説明はボスキャラの所と同じなのでそれを参考にしてくださいな
                    p1x = (1-t) * self.enemy[i].ax + t * self.enemy[i].qx
                    p1y = (1-t) * self.enemy[i].ay + t * self.enemy[i].dy
                    p2x = (1-t) * self.enemy[i].qx + t * self.enemy[i].dx
                    p2y = (1-t) * self.enemy[i].qy + t * self.enemy[i].dy   
                    px = (1-t) * p1x + t * p2x
                    py = (1-t) * p1y + t * p2y
                    self.enemy[i].posx = px + self.enemy[i].offset_x #(px,py)にオフセット値を加減算したものを(posx,posy)にします（こうするとあらかじめ決められたルートからずれた位置も通らせることができるのです）
                    self.enemy[i].posy = py + self.enemy[i].offset_y

                    self.enemy[i].move_speed = self.enemy[i].move_speed * self.enemy[i].acceleration #スピードの値に加速度を掛け合わせ加速させたり減速させたりします

                    if self.enemy[i].move_speed < 0.2: #スピードは0.2以下にならないように補正してやります・・(まったく動かなくなる状況にさせないため）
                        self.enemy[i].move_speed = 0.2
                    self.enemy[i].obj_time += self.enemy[i].move_speed * self.enemy[i].move_speed_offset #タイムフレーム番号を(スピード*スピードオフセット)分加算していく
            elif self.enemy[i].enemy_type == 18:#敵タイプ18の更新  ボルダー 硬めの弾バラマキ重爆撃機 大きいサイズ
                 #敵18をサインカーブを描きながら移動させる 
                 self.enemy[i].posx += self.enemy[i].move_speed  #X座標をmove_speed分加減算する
                 self.enemy[i].timer += self.enemy[i].speed      #タイマーをスピード分増やしていく
                 self.enemy[i].posy += self.enemy[i].intensity * math.sin(self.enemy[i].timer)#振れ幅と時間を使ってサインカーブのy軸の値を求める

                 self.enemy[i].enemy_flag1 += 1 #flag1(弾発射間隔カウント)を利用してカウント190ごとに弾を発射させる
                 if self.enemy[i].enemy_flag1 == 190:
                      if self.to_my_ship_distance(self.enemy[i].posx,self.enemy[i].posy) < 100: #自機との距離が100より小さかったら
                           self.enemy[i].status = ENEMY_STATUS_BERSERK #ステータス「怒り」にする
                           #自機狙い4way発射*3連
                           for num in range(3):
                                theta = 30
                                n = 4
                                division_type = 0
                                division_count = 0
                                division_num = 0
                                stop_count = 5 * num
                                if self.my_x < self.enemy[i].posx + 4*8: #自機とのx座標の位置を見て前と後ろのどちらの銃口から発射するのか判定する
                                     self.enemy_aim_bullet_nway(self.enemy[i].posx      ,self.enemy[i].posy + 8 ,theta,n,division_type,division_count,division_num,stop_count) #後ろから発射  
                                else:
                                     self.enemy_aim_bullet_nway(self.enemy[i].posx + 4*8,self.enemy[i].posy + 10,theta,n,division_type,division_count,division_num,stop_count) #前から発射

                           self.enemy[i].enemy_flag1 = 20   #カウンター値を多めにしてリセット
                      else:#そうでなかったら
                           self.enemy[i].status = ENEMY_STATUS_NORMAL #ステータスを「通常」にする
                           self.enemy_forward_3way_bullet(self.enemy[i].posx,self.enemy[i].posy) #前方3way弾発射
                           self.enemy[i].enemy_flag1 = 0 #カウンターリセット
               
                 self.enemy[i].intensity = self.enemy[i].intensity * 0.9997#振れ幅を徐々に小さくしていく

                 if self.enemy[i].posx < 0 and self.enemy[i].enemy_flag2 == 0: #座標がマイナス＆flag2(反転離脱フラグ)が立っていないのなら
                      self.enemy[i].enemy_flag2 = 1 #flag2(反転離脱フラグ)を立てる
                      self.enemy[i].move_speed = self.enemy[i].move_speed * -1 #移動方向を反転させる

                      #反転開始時は分裂弾を発射
                      new_enemy_shot = Enemy_shot()
                      division_type         = ENEMY_SHOT_DIVISION_3WAY   #自機狙いの3way
                      division_count        = 80 #分裂するまでのカウント数
                      division_count_origin = 80 #分裂するまでのカウント数(元数値)
                      division_num          = 0    #分裂する回数
                      new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00, self.enemy[i].posx + 4*8,self.enemy[i].posy + 10,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, 1,0,      0.95,      1,1,    1,0, 0,1,0,          0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, 0,0, 0,0,   0,0)
                      self.enemy_shot.append(new_enemy_shot)              
                 
                 if self.enemy[i].enemy_flag2 == 1: #反転離脱中の時は
                      self.enemy[i].move_speed += 0.002 #加速して離脱していく
     
     #画面外に出た敵を消去する
     def update_clip_enemy(self):
          enemy_count = len(self.enemy)
          for i in reversed(range (enemy_count)):
              if -30 < self.enemy[i].posx and self.enemy[i].posx < WINDOW_W + 200:#敵のx座標は-30~160+200以内？
                    if -50 < self.enemy[i].posy and self.enemy[i].posy < WINDOW_H + 50:#敵のY座標は-50~120+50以内？
                        continue
                    else:
                        if self.enemy[i].formation_id != 0: #編隊機の場合は・・・・・
                             self.check_enemy_formation_exists(self.enemy[i].formation_id) #画面上の編隊総数を減らす関数をよびだす
                        del self.enemy[i]#敵が画面外に存在するときはインスタンスを破棄する(敵消滅)
              else:
                  if self.enemy[i].formation_id != 0: #編隊機の場合は・・・・・
                             self.check_enemy_formation_exists(self.enemy[i].formation_id) #画面上の編隊総数を減らす関数をよびだす
                  del self.enemy[i]
     
     ####################################ボス関連の処理関数########################################
     #ボスの更新
     def update_boss(self):
          boss_count = len(self.boss)
          for i in reversed (range(boss_count)):
               if   self.boss[i].boss_type == BOSS_FATTY_VALGUARD: #ボスタイプ1の更新 ファッティ・バルガード ###########################
                    if   self.boss[i].status == BOSS_STATUS_MOVE_COORDINATE_INIT:  #「移動用座標初期化」ベジェ曲線で移動するための移動元、移動先、制御点をまず初めに取得する
                         self.boss_get_bezier_curve_coordinate(i) #ボスをベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                         self.boss[i].status = BOSS_STATUS_MOVE_BEZIER_CURVE #状態遷移を「ベジェ曲線で移動」に設定
                         
                    elif self.boss[i].status == BOSS_STATUS_MOVE_BEZIER_CURVE:     #「ベジェ曲線で移動」
                         t = self.boss[i].obj_time / self.boss[i].obj_totaltime
                         if t >= 1: #tの値が1になった時は現在の座標が移動目的座標と同じ座標になった状況となるので・・・(行き過ぎ防止で念のため１以上で判別してます)
                              self.boss[i].obj_time = 0    #タイムフレーム番号を0にしてリセットする                         
                              self.boss[i].move_index += 1 #目的座標のリストのインデックスを1進める
                              if self.boss_move_data1[self.boss[i].move_index][0] == 9999:#x座標がエンドコード9999の場合は
                                   self.boss[i].move_index = 0 #リストインデックス値を0にしてリセットする
                              self.boss_get_bezier_curve_coordinate(i) #ボスをベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                              t = self.boss[i].obj_time / self.boss[i].obj_totaltime #違う座標データ群を読み込んだのでt値を再計算してやる

                         #            A(移動元)--D(移動先)
                         #              \    点P /      
                         #(AとQの内分点)P1\      /P2(QとDの内分点)    
                         #                 \   /
                         #                  Q(制御点)
                         #
                         #内分の公式からP1の座標は((1-t)ax+t*qx,(1-t)ay+t*qy)
                         #             P2の座標は((1-t)qx+t*dx,(1-t)qy+t*dy)
                         #したがってPの座標も内分の公式から求められる
                         #P1の座標を(p1x,p1y),P2の座標を(p2x,p2y)とすると点Pの座標は
                         #         ((1-t)p1x+t*p2x,(1-t)p1y+t*p2y)となり
                         #先に求めたP1,P2を代入してやると
                         #         ((1-t)(1-t)ax+t*qx+t*(1-t)qx+t*dx,(1-t)(1-t)ay+t*qy+t*(1-t)qy+t*dy)となる
                         p1x = (1-t) * self.boss[i].ax + t * self.boss[i].qx
                         p1y = (1-t) * self.boss[i].ay + t * self.boss[i].dy
                         p2x = (1-t) * self.boss[i].qx + t * self.boss[i].dx
                         p2y = (1-t) * self.boss[i].qy + t * self.boss[i].dy

                         px = (1-t) * p1x + t * p2x
                         py = (1-t) * p1y + t * p2y

                         self.boss[i].posx = px 
                         self.boss[i].posy = py

                         self.boss[i].speed = self.boss[i].speed * self.boss[i].acceleration #スピードの値に加速度を掛け合わせ加速させたり減速させたりします
                         if self.boss[i].speed < 0.2: #スピードは0.2以下にならないように補正してやります・・(まったく動かなくなる状況にさせないため）
                              self.boss[i].speed = 0.2
                         self.boss[i].obj_time += self.boss[i].speed #タイムフレーム番号をスピード分加算していく
                    
                    elif self.boss[i].status == BOSS_STATUS_MOVE_LEMNISCATE_CURVE: #前方でレムニスケート曲線を使った上下運動をさせる
                         self.boss[i].degree += 0.009 #degree角度は0~360までの間を0.009の増分で増加させていく
                         if self.boss[i].degree >= 360:
                              self.boss[i].degree = 0
                    
                         #(x**2+y**2)**2=2a**2(x**2-y**2) (ベルヌーイのレムニスケート曲線)を使用
                         #極座標を(r,θ）とする
                         #
                         #x**2 + y**2 = r**2
                         #x = r*cos(θ)
                         #y = r*cos(θ)より
                         #(r**2)**2 = 2(r**2(cos(θ)**2) - r**2(sin(θ)**2)
                         #(r**2)**2 = 2r**2(cos(θ)**2 - sin(θ)**2)
                         #
                         #cos(θ)**2 + sin(θ)**2 = 1 尚且つ・・・
                         #cos(θ)**2 - sin(θ)**2 = cos(2θ) となるので・・・
                         #
                         #(r**2)**2 = 2r**2(cos(2θ))
                         #r**2 = 2a2cos(2θ)
                         #となるはず・・・・多分
                         #
                         #
                         #x = sqrt(2)*cos(degree) / (sin(degree)**2+1)
                         #y = sqrt(2)*cos(degree)*sin(degree) / (sin(degree)**2+1)
                         #
                         #？？？「ベルヌーイだよ、レムニスケートは別名ヤコブ・ベルヌーイのレムニスケートとも呼ばれてるよ」
                         #
                         #横スクロールシューティングで縦に倒した状態のレムニスケート曲線を描きたいのでx座標とy座標を入れ替えて使用します
                         self.boss[i].posy = (math.sqrt(2)*math.cos(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 35 + 50
                         self.boss[i].posx = (math.sqrt(2)*math.cos(self.boss[i].degree) * math.sin(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 30 + 80
                    
                    elif self.boss[i].status == BOSS_STATUS_EXPLOSION_START:       #ボス撃破！爆発開始！の処理
                         self.boss[i].attack_method = BOSS_ATTACK_NO_FIRE #ボスの攻撃方法は「ノーファイア」何も攻撃しないにする、まぁ撃破したからね
                         
                         self.boss[i].vx = (WINDOW_W / 2 - self.boss[i].posx ) / 480 * 1.5 #ボスが居た位置に乗じた加速度を設定する vxは画面中央を境にプラスマイナスに分かれる 480で割っているのは480フレーム掛けて画面の端まで動くためです
                         self.boss[i].vy = (WINDOW_H - self.boss[i].posy) / 480 - 0.3      #vyは爆発した瞬間少し上に跳び上がった感じにしたいので -0.3しています
                         self.boss[i].count1 = 240 #count1を爆裂分裂開始までのカウントとして使います
                         self.boss[i].status = BOSS_STATUS_EXPLOSION #ボスの状態遷移ステータスを「爆発中」にする
                    
                    elif self.boss[i].status == BOSS_STATUS_EXPLOSION:             #ボスステータスが「爆発中」の処理
                         #爆発中サウンド再生
                         pyxel.play(3,11)

                         new_explosion = Explosion()
                         new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + randint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + randint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                         self.explosions.append(new_explosion)

                         self.boss[i].posx += self.boss[i].vx
                         self.boss[i].posy += self.boss[i].vy
                         self.boss[i].vy += 0.001 #1フレームごとに下方向へ0.001加速して落ちていきます

                         self.boss[i].count1 -= 1 #count1(爆裂分裂開始までのカウント)を１減らしていきます
                         if self.boss[i].count1 <= 0: #爆裂分裂開始までのカウントが0になったのなら
                              self.boss[i].status = BOSS_STATUS_BLAST_SPLIT_START #状態遷移ステータスを「爆発分離開始」にします

                    elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT_START:     #ボスステータスが「爆発分離開始」の処理
                         self.boss[i].count2 = 480 #count2をボス破壊後に分裂するシーン全体のフレーム数を登録します

                         #爆発分離開始のサウンド再生
                         pyxel.playm(1)
                         #ランダムな場所に爆発パターンを育成
                         new_explosion = Explosion()
                         new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + randint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + randint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                         self.explosions.append(new_explosion)

                         self.boss[i].status = BOSS_STATUS_BLAST_SPLIT #ボスステータスを「爆発分離」にします
                    
                    elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT:           #ボスステータスが「爆発分離」の処理
                         #ランダムな場所に爆発パターンを育成
                         new_explosion = Explosion()
                         new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + randint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + randint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                         self.explosions.append(new_explosion)
                         
                         #ボスの爆発破片3を育成 ホワイト系のスパーク
                         if self.boss[i].count2 % 3 == 0:
                             self.update_append_particle(PARTICLE_BOSS_DEBRIS3,self.boss[i].posx + 30 + randint(0,30) -15 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,12,0,0)

                         #ボスの爆発破片4を育成 橙色系の落下する火花
                         if self.boss[i].count2 % 1 == 0:
                             self.update_append_particle(PARTICLE_BOSS_DEBRIS4,self.boss[i].posx + 30 + randint(0,40) -20 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,8,0,0)

                         
                         self.boss[i].posx += self.boss[i].vx / 1.5
                         self.boss[i].posy += self.boss[i].vy / 1.5
                         self.boss[i].vy += 0.001  / 1.5#1フレームごとに下方向へ0.001加速して落ちていきます
                         
                         self.boss[i].count2 -= 1 #count2(ボス消滅までのカウント)を１減らしていきます
                         if self.boss[i].count2 <= 0: #ボス消滅までのカウントが0になったのなら
                              self.boss[i].status = BOSS_STATUS_DISAPPEARANCE #ボスステータスを「ボス消滅」にします
                    
                    elif self.boss[i].status == BOSS_STATUS_DISAPPEARANCE:         #ボスステータスが「ボス消滅」の処理
                         self.game_status = SCENE_STAGE_CLEAR_MOVE_MY_SHIP #ゲームステータス(状態遷移)を「ステージクリア自機自動移動」にする
                         
                         self.stage_clear_dialog_flag          = 1   #STAGE CLEARダイアログ表示フラグをonにする
                         self.stage_clear_dialog_display_time  = 300 #STAGE CLEARダイアログ表示時間その1を代入(単位は1フレーム)
                         
                         self.stage_clear_dialog_logo_time1    = 90 #グラフイックロゴ表示にかける時間を代入その1(単位は1フレーム)
                         self.stage_clear_dialog_logo_time2    = 90 #グラフイックロゴ表示にかける時間を代入その2(単位は1フレーム)
                         self.stage_clear_dialog_text_time            = 180 #テキスト表示にかける時間を代入(単位は1フレーム)だんだん減っていく
                         self.stage_clear_dialog_text_time_master     = 180 #テキスト表示にかける時間を代入(単位は1フレーム)元の値が入ります

                         self.auto_move_mode = 1                              #自機のオートムーブモードをonにして自動移動を開始する
                         self.auto_move_mode_x,self.auto_move_mode_y = 25,40  #移動先の座標を指定 

                         del self.boss[i]                           #ボスのインスタンスを消去する・・・さよならボス・・（けもふれ？）
                         break                                      #ループから抜け出す

                    ####ここからはボスの攻撃パターンです############################################################
                    if   self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY:           #画面上部を左から右に弧を描いて移動中
                         if (pyxel.frame_count % 60) == 0 and self.boss[i].parts1_flag == 1: #5way砲台が健在なら60フレーム毎に
                              ex = self.boss[i].posx
                              ey = self.boss[i].posy + 18
                              self.enemy_forward_5way_bullet(ex,ey) #前方5way発射！
                         if (pyxel.frame_count % 100) == 0 and self.boss[i].parts2_flag == 1: #尾翼レーザー部が健在なら100フレーム毎に
                              ex = self.boss[i].posx + 16
                              ey = self.boss[i].posy
                              length = 2
                              speed =  1
                              self.enemy_red_laser(ex,ey,length,speed) #レッドレーザービーム発射！
                    
                    elif self.boss[i].attack_method == BOSS_ATTACK_RIGHT_GREEN_LASER:    #背後で下から上に移動中
                         if (pyxel.frame_count % 30) == 0: #30フレーム毎に
                              ex = self.boss[i].posx + 48
                              ey = self.boss[i].posy + 27
                              length = 4
                              speed = -3 #画面左端にボスが居るので右方向にレーザー発射（マイナスのスピードだと反転され右方向に射出される）
                              self.enemy_green_laser(ex,ey,length,speed) #グリーンレーザービーム発射！
                         
                         if (pyxel.frame_count % 30) == 0 and self.boss[i].parts2_flag == 1: #尾翼レーザー部が健在なら30フレーム毎に
                              ex = self.boss[i].posx + 16
                              ey = self.boss[i].posy
                              length = 2
                              speed =  1
                              self.enemy_red_laser(ex,ey,length,speed) #レッドレーザービーム発射！
                   
                    elif self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY_AIM_BULLET:#前方で上から下に移動中
                         if (pyxel.frame_count % 40) == 0: #40フレーム毎に
                              ex = self.boss[i].posx + 40
                              ey = self.boss[i].posy + 18
                              self.enemy_forward_5way_bullet(ex,ey) #前方5way発射！

                              ex = self.boss[i].posx + 40
                              ey = self.boss[i].posy + 18
                              self.enemy_aim_bullet(ex,ey,0,0,0,0,1)          #狙い撃ち弾発射
                    
                    elif self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY_HOMING:    #下部を右から左に弧を描いて移動中
                         if (pyxel.frame_count % 60) == 0 and self.boss[i].parts1_flag == 1: #60フレーム毎に5way砲台が健在なら
                              ex = self.boss[i].posx
                              ey = self.boss[i].posy + 18
                              self.enemy_forward_5way_bullet(ex,ey) #前方5way発射！
                         if self.boss[i].posx < 10:
                              if (pyxel.frame_count % 20) == 0: #20フレーム毎に
                                   if len(self.enemy) < 400:
                                        new_enemy = Enemy()#敵8ツインアローを1機生み出す
                                        new_enemy.update(TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.boss[i].posx + 48,self.boss[i].posy + 8,0,0,       0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,   1,-1,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   1,0,   0,    HP01,     0,0,   E_SIZE_NORMAL,  0,0,1,        0,0,0,0,         E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,     0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                                        self.enemy.append(new_enemy)#リストにアペンド追加！
                         
               elif self.boss[i].boss_type == BOSS_BREEZARDIA:     #ボスタイプ0の更新 ブリザーディア ##################################
                    #flag1  = 主砲が発射中なのかのフラグ
                    #direction = 前進か更新かの方向フラグ(1=前進 0=後進)
                    #count1 = 主砲が何発撃ったのか？のカウント用
                    #count2 = ボスを破壊した時に真っ二つになる演出全体のフレーム数
                    #count3 = 主砲の待ち時間用カウンタ
                    #offset_x = x軸のオフセット値
                    #weapon2を前部グリーンレーザー砲とします
                    if   self.boss[i].status == BOSS_STATUS_MOVE_LEMNISCATE_CURVE: #前方でレムニスケート曲線を使った上下運動をさせる
                         if self.boss[i].direction == 0: #x軸の移動方向が後進だったのなら
                              self.boss[i].offset_x -= 0.05 #x軸のオフセット値を減らす
                         else:
                              self.boss[i].offset_x += 0.3 #前進だったのでx軸のオフセット値を増やす
                         
                         self.boss[i].degree += 0.009 #degree角度は0~360までの間を0.009の増分で増加させていく
                         if self.boss[i].degree >= 360:
                              self.boss[i].degree = 0
                    
                
                         self.boss[i].posy = (math.sqrt(2)*math.cos(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 40 + 60
                         self.boss[i].posx = (math.sqrt(2)*math.cos(self.boss[i].degree) * math.sin(self.boss[i].degree) / (math.sin(self.boss[i].degree)**2+1)) * 35 + 80/2 + 20 + self.boss[i].offset_x
                         
                         if self.boss[i].posx > WINDOW_W - 40: #x座標が画面右端を超えたのなら
                              self.boss[i].direction = 0           #方向を後退(0)にする
                         elif self.boss[i].posx < -60:         #x座標が画面左端を超えたのなら
                              self.boss[i].direction = 1           #方向を前進(1)にする

                    elif self.boss[i].status == BOSS_STATUS_EXPLOSION_START:       #ボス撃破！爆発開始！の処理
                         self.boss[i].attack_method = BOSS_ATTACK_NO_FIRE #ボスの攻撃方法は「ノーファイア」何も攻撃しないにする、まぁ撃破したからね
                         
                         self.boss[i].vx = (WINDOW_W / 2 - self.boss[i].posx ) / 480 * 1.5 #ボスが居た位置に乗じた加速度を設定する vxは画面中央を境にプラスマイナスに分かれる 480で割っているのは480フレーム掛けて画面の端まで動くためです
                         self.boss[i].vy = (WINDOW_H - self.boss[i].posy) / 480 - 0.3      #vyは爆発した瞬間少し上に跳び上がった感じにしたいので -0.3しています
                         self.boss[i].count1 = 240 #count1を爆裂分裂開始までのカウントとして使います
                         self.boss[i].status = BOSS_STATUS_EXPLOSION #ボスの状態遷移ステータスを「爆発中」にする
                    
                    elif self.boss[i].status == BOSS_STATUS_EXPLOSION:             #ボスステータスが「爆発中」の処理
                         #爆発中サウンド再生
                         pyxel.play(3,11)

                         new_explosion = Explosion()
                         new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + randint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + randint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                         self.explosions.append(new_explosion)

                         self.boss[i].posx += self.boss[i].vx
                         self.boss[i].posy += self.boss[i].vy
                         self.boss[i].vy += 0.001 #1フレームごとに下方向へ0.001加速して落ちていきます

                         self.boss[i].count1 -= 1 #count1(爆裂分裂開始までのカウント)を１減らしていきます
                         if self.boss[i].count1 <= 0: #爆裂分裂開始までのカウントが0になったのなら
                              self.boss[i].status = BOSS_STATUS_BLAST_SPLIT_START #状態遷移ステータスを「爆発分離開始」にします

                    elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT_START:     #ボスステータスが「爆発分離開始」の処理
                         self.boss[i].count2 = 480 #count2をボス破壊後に分裂するシーン全体のフレーム数を登録します

                         #爆発分離開始のサウンド再生
                         pyxel.playm(1)
                         #ランダムな場所に爆発パターンを育成
                         new_explosion = Explosion()
                         new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + randint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + randint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                         self.explosions.append(new_explosion)

                         self.boss[i].status = BOSS_STATUS_BLAST_SPLIT #ボスステータスを「爆発分離」にします
                    
                    elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT:           #ボスステータスが「爆発分離」の処理
                         #ランダムな場所に爆発パターンを育成
                         new_explosion = Explosion()
                         new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + randint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + randint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                         self.explosions.append(new_explosion)
                         
                         #ボスの爆発破片3を育成 ホワイト系のスパーク
                         if self.boss[i].count2 % 3 == 0:
                             self.update_append_particle(PARTICLE_BOSS_DEBRIS3,self.boss[i].posx + 30 + randint(0,30) -15 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,12,0,0)

                         #ボスの爆発破片4を育成 橙色系の落下する火花
                         if self.boss[i].count2 % 1 == 0:
                             self.update_append_particle(PARTICLE_BOSS_DEBRIS4,self.boss[i].posx + 30 + randint(0,40) -20 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,8,0,0)

                         
                         self.boss[i].posx += self.boss[i].vx / 1.5
                         self.boss[i].posy += self.boss[i].vy / 1.5
                         self.boss[i].vy += 0.001  / 1.5#1フレームごとに下方向へ0.001加速して落ちていきます
                         
                         self.boss[i].count2 -= 1 #count2(ボス消滅までのカウント)を１減らしていきます
                         if self.boss[i].count2 <= 0: #ボス消滅までのカウントが0になったのなら
                              self.boss[i].status = BOSS_STATUS_DISAPPEARANCE #ボスステータスを「ボス消滅」にします 
                    
                    elif self.boss[i].status == BOSS_STATUS_DISAPPEARANCE:         #ボスステータスが「ボス消滅」の処理
                         self.game_status = SCENE_STAGE_CLEAR_MOVE_MY_SHIP #ゲームステータス(状態遷移)を「ステージクリア自機自動移動」にする
                         
                         self.stage_clear_dialog_flag          = 1   #STAGE CLEARダイアログ表示フラグをonにする
                         self.stage_clear_dialog_display_time  = 300 #STAGE CLEARダイアログ表示時間その1を代入(単位は1フレーム)
                         
                         self.stage_clear_dialog_logo_time1    = 90 #グラフイックロゴ表示にかける時間を代入その1(単位は1フレーム)
                         self.stage_clear_dialog_logo_time2    = 90 #グラフイックロゴ表示にかける時間を代入その2(単位は1フレーム)
                         self.stage_clear_dialog_text_time            = 180 #テキスト表示にかける時間を代入(単位は1フレーム)だんだん減っていく
                         self.stage_clear_dialog_text_time_master     = 180 #テキスト表示にかける時間を代入(単位は1フレーム)元の値が入ります

                         self.auto_move_mode = 1                              #自機のオートムーブモードをonにして自動移動を開始する
                         self.auto_move_mode_x,self.auto_move_mode_y = 25,40  #移動先の座標を指定 

                         del self.boss[i]                           #ボスのインスタンスを消去する・・・さよならボス・・（けもふれ？）
                         break                                      #ループから抜け出す
                    
                    ####ここからはボスの攻撃パターンです############################################################
                    if self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY: #画面上部を左から右に弧を描いて移動中
                         if (pyxel.frame_count % 120) == 0 and self.boss[i].parts1_flag == 1: #5way砲台が健在なら120フレーム毎に
                              ex = self.boss[i].posx
                              ey = self.boss[i].posy + 18
                              self.enemy_forward_3way_bullet(ex,ey) #前方3way発射！
                         if (pyxel.frame_count % 180) == 0 and self.boss[i].parts4_flag == 1: #上部グリーンカッターが健在なら180フレーム毎に
                              ex = self.boss[i].posx
                              ey = self.boss[i].posy
                              new_enemy_shot = Enemy_shot()
                              new_enemy_shot.update(ENEMY_SHOT_GREEN_CUTTER,ID00,ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE12,    0,0,  -1,0,       1.05,    1,1,    0,0,  0,0,0,              0,   0,0,PRIORITY_BOSS_BACK,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                              self.enemy_shot.append(new_enemy_shot)
                         
                         if self.boss[i].weapon1_status == WEAPON_READY and self.boss[i].parts3_flag == 1: #上部主砲が健在で主砲待機中ならば・・
                              if self.boss[i].weapon1_cool_down_time > 0:
                                   self.boss[i].weapon1_cool_down_time -= 1 #主砲の休憩時間カウンタを1減らして行く
                              
                              if self.my_x > self.boss[i].posx + 48 and self.my_y < self.boss[i].posy + 4 and self.boss[i].weapon1_cool_down_time == 0: #自機主砲の右上に居るかどうか判別し・・・更に主砲の休憩時間が0以下になったのなら
                                   self.boss[i].weapon1_status = WEAPON_FIRE #主砲発射中フラグを建てる
                              
                         if self.boss[i].weapon1_status == WEAPON_FIRE and pyxel.frame_count % self.boss[i].weapon1_interval == 0: #主砲発射中フラグが建っており尚且つweapon1_interval(4フレームごとに)・・
                              posx = self.boss[i].posx + 48
                              posy = self.boss[i].posy + 4
                              self.enemy_aim_bullet_nway(posx,posy,20,3, 0,0,0,0) #自機狙い3way発射！
                              
                              self.boss[i].weapon1_rapid_num += 1 #主砲が発射した弾数を1増やす
                              if self.boss[i].weapon1_rapid_num >= 3: #3連射したのならば・・
                                   self.boss[i].weapon1_rapid_num = 0    #主砲が発射した弾数をリセット
                                   self.boss[i].weapon1_cool_down_time = 600  #主砲の待ち時間用カウンタを設定してやる
                                   self.boss[i].weapon1_status  = WEAPON_READY    #主砲発射中フラグを降ろす


                         if self.boss[i].posx <= -30: #x座標がマイナスの時(左画面外)時,は右方向にグリーンレーザーを出す
                              if pyxel.frame_count % self.boss[i].weapon2_interval == 0:
                                   ex = self.boss[i].posx + 8*13 +4
                                   ey = self.boss[i].posy + 8*4 -3
                                   length = 2
                                   speed = -2
                                   self.enemy_green_laser(ex,ey,length,speed)
                              
     #自機と敵との衝突判定
     def update_collision_my_ship_enemy(self):
          if self.invincible_counter > 0: #無敵時間が残っていた場合は・・・
               return                     #衝突判定はせずそのまま帰っちゃう・・・無敵最高！
          enemy_count = len(self.enemy)
          for i in range (enemy_count):
               #敵が自機に当たっているか判別
               #敵と自機の位置の2点間の距離を求める
               self.dx = (self.enemy[i].posx - self.my_x)
               self.dy = (self.enemy[i].posy - self.my_y)
               self.distance = math.sqrt(self.dx * self.dx + self.dy * self.dy)
               if self.distance <= self.enemy[i].enemy_size:
                    self.update_my_ship_damage(1)#自機の中心位置と敵の中心位置の距離がenemy_sizeより小さいなら衝突したと判定し自機のシールド値を１減らす
     
     #自機とボスとの衝突判定
     def update_collision_my_ship_boss(self):
          if self.invincible_counter > 0: #無敵時間が残っていた場合は・・・
               return                     #衝突判定はせずそのまま帰っちゃう・・・無敵最高！
          boss_count = len(self.boss)
          for i in range (boss_count):
               if self.boss[i].invincible != 1: #もしボスが無敵状態で無いのならば
                    #自機がボスの当たり判定矩形の中に存在するのか判別する、存在していたらボスと自機は衝突しています
                    #ボス本体当たり判定1との判定
                    if      self.boss[i].posx + self.boss[i].col_main1_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main1_x + self.boss[i].col_main1_w\
                        and self.boss[i].posy + self.boss[i].col_main1_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main1_y + self.boss[i].col_main1_h\
                        and self.boss[i].col_main1_w != 0:
                        self.update_my_ship_damage(1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                    #ボス本体当たり判定2との判定
                    elif    self.boss[i].posx + self.boss[i].col_main2_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main2_x + self.boss[i].col_main2_w\
                        and self.boss[i].posy + self.boss[i].col_main2_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main2_y + self.boss[i].col_main2_h\
                        and self.boss[i].col_main2_w != 0:
                        self.update_my_ship_damage(1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                    #ボス本体当たり判定3との判定
                    elif    self.boss[i].posx + self.boss[i].col_main3_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main3_x + self.boss[i].col_main3_w\
                        and self.boss[i].posy + self.boss[i].col_main3_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main3_y + self.boss[i].col_main3_h\
                        and self.boss[i].col_main3_w != 0:
                        self.update_my_ship_damage(1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                    #ボス本体当たり判定4との判定
                    elif    self.boss[i].posx + self.boss[i].col_main4_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main4_x + self.boss[i].col_main4_w\
                        and self.boss[i].posy + self.boss[i].col_main4_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main4_y + self.boss[i].col_main4_h\
                        and self.boss[i].col_main4_w != 0:
                        self.update_my_ship_damage(1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす               
                    
                    #ボス本体当たり判定5との判定
                    elif    self.boss[i].posx + self.boss[i].col_main5_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main5_x + self.boss[i].col_main5_w\
                        and self.boss[i].posy + self.boss[i].col_main5_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main5_y + self.boss[i].col_main5_h\
                        and self.boss[i].col_main5_w != 0:
                        self.update_my_ship_damage(1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす               
                    #ボス本体当たり判定6との判定
                    elif    self.boss[i].posx + self.boss[i].col_main6_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main6_x + self.boss[i].col_main6_w\
                        and self.boss[i].posy + self.boss[i].col_main6_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main6_y + self.boss[i].col_main6_h\
                        and self.boss[i].col_main6_w != 0:
                        self.update_my_ship_damage(1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす               
                    #ボス本体当たり判定7との判定
                    elif    self.boss[i].posx + self.boss[i].col_main7_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main7_x + self.boss[i].col_main7_w\
                        and self.boss[i].posy + self.boss[i].col_main7_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main7_y + self.boss[i].col_main7_h\
                        and self.boss[i].col_main7_w != 0:
                        self.update_my_ship_damage(1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす               
                    #ボス本体当たり判定8との判定
                    elif    self.boss[i].posx + self.boss[i].col_main8_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main8_x + self.boss[i].col_main8_w\
                        and self.boss[i].posy + self.boss[i].col_main8_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_main8_y + self.boss[i].col_main8_h\
                        and self.boss[i].col_main8_w != 0:   
                        self.update_my_ship_damage(1) #ボスの当たり判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす               
               


               
                    #パーツ1との当たり判定
                    elif    self.boss[i].posx + self.boss[i].col_parts1_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_parts1_x + self.boss[i].col_parts1_w\
                        and self.boss[i].posy + self.boss[i].col_parts1_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_parts1_y + self.boss[i].col_parts1_h\
                        and self.boss[i].parts1_flag == 1:
                        self.update_my_ship_damage(1) #ボスのパーツ1の判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                    #パーツ2との当たり判定
                    elif    self.boss[i].posx + self.boss[i].col_parts2_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_parts2_x + self.boss[i].col_parts2_w\
                        and self.boss[i].posy + self.boss[i].col_parts2_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_parts2_y + self.boss[i].col_parts2_h\
                        and self.boss[i].parts2_flag == 1:
                        self.update_my_ship_damage(1) #ボスのパーツ2の判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                    #パーツ3との当たり判定
                    elif    self.boss[i].posx + self.boss[i].col_parts3_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_parts3_x + self.boss[i].col_parts3_w\
                        and self.boss[i].posy + self.boss[i].col_parts3_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_parts3_y + self.boss[i].col_parts3_h\
                        and self.boss[i].parts3_flag == 1:
                        self.update_my_ship_damage(1) #ボスのパーツ3の判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす
                    #パーツ4との当たり判定
                    elif    self.boss[i].posx + self.boss[i].col_parts4_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_parts4_x + self.boss[i].col_parts4_w\
                        and self.boss[i].posy + self.boss[i].col_parts4_y <= self.my_y + 4 <= self.boss[i].posy + self.boss[i].col_parts4_y + self.boss[i].col_parts4_h\
                        and self.boss[i].parts4_flag == 1:
                        self.update_my_ship_damage(1) #ボスのパーツ4の判定矩形の中に自機が存在していたので衝突したと判定し自機のシールド値を１減らす

     #自機と背景障害物との当たり判定
     def update_collision_my_ship_bg(self):
          if self.bg_collision_Judgment_flag == 0: #デバッグ用の当たり判定を行うフラグが立っていなかったら
               return                              #衝突判定はせずそのまま帰っちゃう
          if self.invincible_counter > 0: #無敵時間が残っていた場合は・・・
               return                     #衝突判定はせずそのまま帰っちゃう・・・無敵最高！
          self.check_bg_collision(self.my_x + 6,self.my_y + 4,0,0)
          if self.collision_flag == 1: #コリジョンフラグが建っていたのなら
              self.update_my_ship_damage(1) #障害物に当たったので自機のシールド値を減らす
     
     #ゲームパッドのYが推されたらサブウェポンを切り替える                     GAMEPAD Y
     def update_change_sub_weapon(self):
          if pyxel.btnp(pyxel.GAMEPAD_1_Y) or pyxel.btnp(pyxel.GAMEPAD_2_Y) and self.select_sub_weapon_id != -1:#サブウェポン切り替えボタンが押された＆サブウェポンを一つでも所維持しているのなら以下の命令を実行する
               for __i in range(5):#5回繰り返す
                   self.select_sub_weapon_id += 1#サブウェポンIDを増やして切り替えていく
                   if self.select_sub_weapon_id >= 5:#idナンバーが5以上になったら
                        self.select_sub_weapon_id = 0#強制的にidナンバーを0にする
               
                   if self.sub_weapon_list[self.select_sub_weapon_id] != 0:#サブウェポンを変更してそれが所持しているものならば
                        break#ブレイクしてループを抜け出す
                    #そうでないのならばサブウェポンは5種類あるので,最大5回ループして所持しているものを見つけ出すまで繰り返す
     
     #自機が被弾しダメージを受け、シールドパワー減少、ダメージ音再生、ダメージを受けた後の無敵時間の設定
     def update_my_ship_damage(self,damage):
          self.my_shield -= damage#シールドパワーをdamage分減少させる
          if self.my_shield < 0:
               self.my_shield = 0 #シールドパワーがマイナスまで行ってしまったら0に修正する
          
          pyxel.play(0,15) #自機ダメージ音再生
          self.invincible_counter = self.invincible_time #ダメージ後の無敵時間を設定する

     #自機のシールドパワーがまだあるのかチェックする
     def update_check_my_shield(self):
          if self.my_shield <= 0:
               self.game_status = SCENE_EXPLOSION #シールドパワーが0以下になってしまったのでステータスを爆発中にする
               #自機の座標に爆発を生成する
               new_explosion = Explosion()
               new_explosion.update(EXPLOSION_MY_SHIP,PRIORITY_MORE_FRONT,self.my_x - 4 ,self.my_y-2,0,0,64,RETURN_BULLET_NONE,0,  1,1)
               self.explosions.append(new_explosion)
               
               #爆発音再生
               pyxel.play(2,3)

     #パワーアップアイテム類の更新
     def update_obtain_item(self):
          obtain_item_count = len(self.obtain_item)
          for i in reversed(range (obtain_item_count)):
               if    ITEM_SHOT_POWER_UP      <= self.obtain_item[i].item_type <= ITEM_CLAW_POWER_UP\
                  or ITEM_TAIL_SHOT_POWER_UP <= self.obtain_item[i].item_type <= ITEM_SHOCK_BUMPER_POWER_UP: #ショット、ミサイル、シールド クロー テイルショット~ショックバンパーパワーアップの更新
                   self.obtain_item[i].vx -= 0.009 #vx速度ベクトルをだんだんと減らしていく
                   self.obtain_item[i].intensity -= 0.001 #振れ幅をだんだん減らしていく
                   if self.obtain_item[i].intensity < 0.001: #振れ幅は0.001より小さくならないようにします
                        self.obtain_item[i].intensity = 0.001
                   self.obtain_item[i].posx  += self.obtain_item[i].vx#X座標をvx分減らして左方向に進む
                   self.obtain_item[i].timer += self.obtain_item[i].speed
                   self.obtain_item[i].posy  += self.obtain_item[i].intensity * math.sin(self.obtain_item[i].timer)

                   if self.obtain_item[i].posx <= 0 and self.obtain_item[i].bounce >= 1:#x座標が0以下で画面左端まで行き、bounceが1以上なら
                        self.obtain_item[i].vx = 0.2 + self.obtain_item[i].bounce * 0.2 #vxを右側のベクトルにする(跳ね返り回数の1.2倍の整数値)
                        self.obtain_item[i].bounce -= 1 #跳ね返る回数を1減らす
                   #dに自機とアイテムの距離を計算した値を代入！ 
                   d = abs(math.sqrt((self.obtain_item[i].posx - self.my_x) * (self.obtain_item[i].posx - self.my_x) + (self.obtain_item[i].posy - self.my_y) * (self.obtain_item[i].posy - self.my_y)))
                   if d <= 800: #アイテムと自機との距離が800以内の場合アイテムのx,y座標を自機の方向へ向かうよう補正を入れる
                        self.obtain_item[i].posy += ((self.my_y >= self.obtain_item[i].posy) - (self.my_y <= self.obtain_item[i].posy)) / (d / 5)
                        self.obtain_item[i].posx += ((self.my_x >= self.obtain_item[i].posx) - (self.my_x <= self.obtain_item[i].posx)) / (d / 5)
               
               elif self.obtain_item[i].item_type == ITEM_TRIANGLE_POWER_UP: #トライアングルアイテムの場合
                    #flag1は正三角形の内部に自機が居るかどうかの判別で使用します(0=外部に居る 1=内部に居る)
                    #flag2は現在の三角形内部に自機が居た時間（一度でも外に出ると0に戻されます）
                    #flag3は三角形内部に自機が居た時間がこの数値まで達したらアイテムを入手できるかの数値です
                    #statusは状態遷移を示します
                    #0=画面スクロールに合わせて左に流れる状態
                    #1=アイテム取得時の高速回転状態
                    #2=取得アニメーション描画中
                    #3=取得完了
                    if self.obtain_item[i].status == 0:#状態遷移statusが「画面スクロールに合わせて左に流れる状態」の場合
                         self.obtain_item[i].posx  -= self.obtain_item[i].vx      #X座標をvx分減らして左方向に進む
                         if (pyxel.frame_count % 2) == 0:
                              if self.obtain_item[i].radius < self.obtain_item[i].radius_max:#もし回転半径が回転半径最大値で無いのなら
                                   self.obtain_item[i].radius += 1 #回転半径を1増やして、回転半径最大値まで増加させていく
                         #dに自機とアイテムの距離を計算した値を代入！ 
                         d = abs(math.sqrt((self.obtain_item[i].posx - self.my_x) * (self.obtain_item[i].posx - self.my_x) + (self.obtain_item[i].posy - self.my_y) * (self.obtain_item[i].posy - self.my_y)))
                         if d > self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]:#離れている距離数がトライアングルアイテムの回転半径より大きい場合は三角形の外なので...
                              self.obtain_item[i].flag2 = 0   #現在の三角形内部に自機が居た時間を強制的に0に戻す
                         else:
                              self.obtain_item[i].flag2 += 1  #現在の三角形内部に自機が居た時間を1増やす
                              if self.obtain_item[i].flag2 >= self.obtain_item[i].flag3:#内部に居た時間が設定時間以上になったのなら
                                   self.obtain_item[i].status = 1 #状態遷移を「アイテム取得時の高速回転状態」にする
                    
                    elif self.obtain_item[i].status == 1:#状態遷移statusが「アイテム取得時の高速回転状態」の場合
                         self.obtain_item[i].posx  -= self.obtain_item[i].vx / 4    #X座標を(vx/4)分減らして左方向に進む
                         if self.obtain_item[i].speed <= 40:  #SPEED(トライアングルアイテムの場合は回転スピードとして使用してます)が10以下なら
                              self.obtain_item[i].speed +=0.5 #回転スピードをだんだん増やしていく
                         
                         self.obtain_item[i].radius -= 0.2 #回転半径を0.2小さくしていく
                         if self.obtain_item[i].radius <= 6: #回転半径が6より大きいのなら
                              self.obtain_item[i].radius = 6 #回転半径は6より小さくしない
                              self.obtain_item[i].animation_number = 0 #アニメーションナンバーをリセット
                              self.obtain_item[i].status = 2 #状態遷移を「取得アニメーション描画中」にする
                    
                    elif self.obtain_item[i].status == 2:#状態遷移statusが「取得アニメーション描画中」の場合
                         if pyxel.frame_count % 4 == 0: #3フレーム毎に
                              self.obtain_item[i].animation_number += 1 #アニメーションパターンオフセット値を増やしていく
                         if self.obtain_item[i].animation_number == 8: #最後のパターン数までいったのなら
                              self.obtain_item[i].status = 3 #状態遷移を「取得完了」にする


                    elif self.obtain_item[i].status == 3:#状態遷移statusが「取得完了」の場合
                         self.shot_exp    += self.obtain_item[i].shot    #ショット経験値をショットパワーの増加量の分だけパワーアップさせる
                         self.missile_exp += self.obtain_item[i].missile #ミサイル経験値をミサイルパワーの増加量の分だけパワーアップさせる
                         self.my_shield   += self.obtain_item[i].shield  #シールド値（ヒットポイント）をシールドパワーの増加量の分だけパワーアップさせる
                         
                         pyxel.play(0,0)              #パワーアップアイテムゲットの音を鳴らすのだ
                         self.level_up_my_shot()      #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
                         self.level_up_my_missile()   #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す

                         del self.obtain_item[i]#パワーアップアイテムのインスタンスを破棄する(アイテム消滅)
                         if self.shot_level > 10:     #ショットレベルは10を超えないようにする
                              self.shot_level = 10
                         if self.missile_level > 2:   #ミサイルレベルは2を超えないようにする
                              self.missile_level = 2

     #パワーアップアイテム類と自機の当たり判定（パワーアップアイテムゲット！！）
     def update_collision_my_ship_obtain_item(self):
          obtain_item_count = len(self.obtain_item)
          for i in reversed(range (obtain_item_count)):
               #パワーアップアイテム類が自機に当たっているか判別
               #パワーアップアイテム類と自機の位置の2点間の距離を求める
               self.dx = (self.obtain_item[i].posx - self.my_x)
               self.dy = (self.obtain_item[i].posy - self.my_y)
               self.distance = math.sqrt(self.dx * self.dx + self.dy * self.dy)
               if self.distance <= 8: #自機の中心位置とパワーアップアイテム類の中心位置の距離が8より小さいなら重なったと判定する
                    if ITEM_SHOT_POWER_UP <= self.obtain_item[i].item_type <= ITEM_SHIELD_POWER_UP: #ショット、ミサイル、シールドパワーアップの処理
                         self.shot_exp    += self.obtain_item[i].shot    #ショット経験値をショットパワーの増加量の分だけパワーアップさせる
                         self.missile_exp += self.obtain_item[i].missile #ミサイル経験値をミサイルパワーの増加量の分だけパワーアップさせる
                         self.my_shield   += self.obtain_item[i].shield  #シールド値（ヒットポイント）をシールドパワーの増加量の分だけパワーアップさせる
                         
                         pyxel.play(0,0)              #パワーアップアイテムゲットの音を鳴らすのだ
                         self.level_up_my_shot()      #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
                         self.level_up_my_missile()   #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す

                         del self.obtain_item[i]#パワーアップアイテムのインスタンスを破棄する(アイテム消滅)
                         if self.shot_level > 10:     #ショットレベルは10を超えないようにする
                              self.shot_level = 10
                         if self.missile_level > 2:   #ミサイルレベルは2を超えないようにする
                              self.missile_level = 2
                    
                    elif self.obtain_item[i].item_type == ITEM_CLAW_POWER_UP: #クローパワーアップの処理
                         pyxel.play(0,0)              #パワーアップアイテムゲットの音を鳴らすのだ
                         del self.obtain_item[i]      #クローアイテムのインスタンスを破棄する(アイテム消滅)
                         self.update_append_claw()    #クローの発生関数の呼び出し
                    
                    elif self.obtain_item[i].item_type == ITEM_TAIL_SHOT_POWER_UP: #テイルショットパワーアップの処理
                         pyxel.play(0,0)              #パワーアップアイテムゲットの音を鳴らすのだ
                         del self.obtain_item[i]      #インスタンスを破棄する(アイテム消滅)
                         self.sub_weapon_list[0] += 1  #サブウェポンリスト内のテイルショットの所持数を１増やす
                         if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                              self.select_sub_weapon_id = 0 #強制的にテイルショットを選択させる
                    elif self.obtain_item[i].item_type == ITEM_PENETRATE_ROCKET_POWER_UP: #ペネトレートロケットパワーアップの処理
                         pyxel.play(0,0)              #パワーアップアイテムゲットの音を鳴らすのだ
                         del self.obtain_item[i]      #インスタンスを破棄する(アイテム消滅)
                         self.sub_weapon_list[1] += 1  #サブウェポンリスト内のペネトレートロケットの所持数を１増やす
                         if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                              self.select_sub_weapon_id = 1 #強制的にペネトレートロケットを選択させる
                    elif self.obtain_item[i].item_type == ITEM_SEARCH_LASER_POWER_UP: #サーチレーザーパワーアップの処理
                         pyxel.play(0,0)              #パワーアップアイテムゲットの音を鳴らすのだ
                         del self.obtain_item[i]      #インスタンスを破棄する(アイテム消滅)
                         self.sub_weapon_list[2] += 1  #サブウェポンリスト内のサーチレーザーの所持数を１増やす
                         if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                              self.select_sub_weapon_id = 2 #強制的にサーチレーザーを選択させる
                    elif self.obtain_item[i].item_type == ITEM_HOMING_MISSILE_POWER_UP: #ホーミングミサイルパワーアップの処理
                         pyxel.play(0,0)              #パワーアップアイテムゲットの音を鳴らすのだ
                         del self.obtain_item[i]      #インスタンスを破棄する(アイテム消滅)
                         self.sub_weapon_list[3] += 1  #サブウェポンリスト内のホーミングミサイルの所持数を１増やす
                         if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                              self.select_sub_weapon_id = 3 #強制的にホーミングミサイルを選択させる
                    elif self.obtain_item[i].item_type == ITEM_SHOCK_BUMPER_POWER_UP: #ショックバンバーパワーアップの処理
                         pyxel.play(0,0)              #パワーアップアイテムゲットの音を鳴らすのだ
                         del self.obtain_item[i]      #インスタンスを破棄する(アイテム消滅)
                         self.sub_weapon_list[4] += 1  #サブウェポンリスト内のショックバンバーの所持数を１増やす
                         if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                              self.select_sub_weapon_id = 4 #強制的にショックバンバーを選択させる
     
     #画面外に出たパワーアップアイテム類を消去する
     def update_clip_obtain_item(self):
          obtain_item_count = len(self.obtain_item)
          for i in reversed(range (obtain_item_count)):
              if -50 < self.obtain_item[i].posx < WINDOW_W + 150 and -100 < self.obtain_item[i].posy < WINDOW_H + 100: #xは-50~160+150 Yは-100~120+100以内？
                   continue
              else:
                  del self.obtain_item[i]#パワーアップアイテムが画面外に存在するときはインスタンスを破棄する(アイテム消滅)
     
     #ボス破壊後にリペアアイテムを出現させる 
     def uddate_present_repair_item(self):
         if self.present_repair_item_flag == 0: #ボーナスアイテムを出したフラグがまだ建っていないのなら
             #ボーナスアイテムを出現させる
             for _i in range(self.repair_shield):
                    y = randint(30,80)
                    new_obtain_item = Obtain_item()
                    new_obtain_item.update(ITEM_SHIELD_POWER_UP,WINDOW_W,y, 0.5+ (randint(0,1)-0.5)* 0.2,0 + (randint(0,4)-2) * 0.6,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,0,1,  0,0,0, self.pow_item_bounce_num,0)
                    self.obtain_item.append(new_obtain_item)
             self.present_repair_item_flag = 1 #フラグを立ててもう出ないようにする

     #爆発パターンの更新
     def update_explosion(self):
          explosioncount = len(self.explosions)
          for i in reversed(range(explosioncount)):
              #爆発パターンを背景スクロールに合わせて移動させる
              self.explosions[i].posx -= self.side_scroll_speed * 0.5#基本BGスクロールスピードは0.5、それと倍率扱いのside_scroll_speedを掛け合わせてスクロールと同じように移動させてやる（地面スクロールに引っ付いた状態で爆発してるように見せるため）           
              self.explosions[i].explosion_count -= 1#爆発育成時に設定したカウントを１減らし0になったら爆発リストをDELしちゃう（お前・・消えるのか・・・？）
              if self.explosions[i].explosion_type == EXPLOSION_MIDDLE: #中間サイズの爆発パターンの場合は
                  #1フレームごとに通常爆発パターンを追加発生させる
                  new_explosion = Explosion()
                  new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.explosions[i].posx + 4 + randint(0,24)-12,self.explosions[i].posy + 4 + randint(0,12)-6,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                  self.explosions.append(new_explosion)

                  
              
              if self.explosions[i].explosion_count == 0:
                  del self.explosions[i]
     
     #パーティクルの追加（発生＆育成）
     def update_append_particle(self,particle_type,x,y,dx,dy,life,wait,color):
          if len(self.particle) < 1000: #パーティクルの総数が1000以下なら追加発生させる
               if particle_type == PARTICLE_DOT or particle_type == PARTICLE_CIRCLE: #ドットパーティクル 円形パーティクルの追加
                    new_particle = Particle()
                    new_particle.update(particle_type, x+4,y+4,    randint(0,1),     random() * 2 - 0.5 + dx,    random() * 2 - 1 + dy,   randint(5,20), 0,  randint(1,14))
                    self.particle.append(new_particle)
               
               elif particle_type == PARTICLE_LINE: #ラインパーティクル（線状の尾を引くようなパーティクルです）
                    for i in range(10):
                         new_particle = Particle()
                         new_particle.update(particle_type, x-2,y+4,    1,     -0.8-random(), random()-0.2,    10,   i, 6)
                         self.particle.append(new_particle)

                         #ボスにダメージを与えたとき
                         #new_particle = Particle()
                         #new_particle.update(particle_type, x-4,y+4,    1,     -0.8-random(), random()-0.2,    30,   i, 8)
                         #self.particle.append(new_particle)




               elif particle_type == PARTICLE_MISSILE_DEBRIS: #ミサイルの破片の追加
                    new_particle = Particle()
                    new_particle.update(particle_type, x,y,    0,     0,0,   7,   0,0)
                    self.particle.append(new_particle)
               
               elif particle_type == PARTICLE_BOSS_DEBRIS1: #ボスの破片1の追加
                    new_particle = Particle()
                    new_particle.update(particle_type, x,y,    0,     dx,dy,   life,   0,0)
                    self.particle.append(new_particle)
               elif particle_type == PARTICLE_BOSS_DEBRIS2: #ボスの破片2の追加
                    new_particle = Particle()
                    new_particle.update(particle_type, x,y,    0,     dx,dy,   life,   0,0)
                    self.particle.append(new_particle)
               elif particle_type == PARTICLE_BOSS_DEBRIS3: #ボスの破片3の追加
                    new_particle = Particle()
                    new_particle.update(particle_type, x,y,    0,     dx,dy,   life,   0,0)
                    self.particle.append(new_particle)
               elif particle_type == PARTICLE_BOSS_DEBRIS4: #ボスの破片4の追加
                    new_particle = Particle()
                    new_particle.update(particle_type, x,y,    0,     dx,dy,   life,   0,0)
                    self.particle.append(new_particle)
               elif particle_type == PARTICLE_BOSS_DEBRIS5: #ボスの破片5の追加
                    new_particle = Particle()
                    new_particle.update(particle_type, x,y,    0,     dx,dy,   life,   0,0)
                    self.particle.append(new_particle)
               elif particle_type == PARTICLE_BOSS_DEBRIS6: #ボスの破片6の追加
                    new_particle = Particle()
                    new_particle.update(particle_type, x,y,    0,     dx,dy,   life,   0,0)
                    self.particle.append(new_particle)
     
     #パーティクルの更新
     def update_particle(self):
          particlecount = len(self.particle)
          for i in reversed(range(particlecount)):#パーティクルのリストの要素数を数えてその数の分だけループ処理する（delしちゃう可能性があるのでreversedするよ）
               if self.particle[i].wait == 0: #ウェイトカウンターが0になったら位置を更新（移動する）
                    self.particle[i].posx += self.particle[i].vx #パーティクルの座標x,yを速度ベクトルvx,vyで位置更新する
                    self.particle[i].posy += self.particle[i].vy
               else: #ウェイトカウンターがまだ残っていたのなら１減らし、移動（更新）はしないでその場に留まらせておく
                    self.particle[i].wait -= 1
               
               if  self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS1:#ボスの破片の時は
                    self.particle[i].vy += 0.009 #y軸下方向に徐々に加速して落ちていくようにする
               elif self.particle[i].particle_type == PARTICLE_LINE: #パーティクルタイプ ラインタイプ
                    if   self.particle[i].life < 6:  #lifeが減るごとにcolorを6→12→5→1と変化させる
                         self.particle[i].color = 12
                    elif self.particle[i].life < 5:
                         self.particle[i].color = 5
                    elif self.particle[i].life < 4:
                         self.particle[i].color = 1
               elif self.particle[i].particle_type == PARTICLE_FIRE_SPARK: #パーティクルタイプ 大気圏突入時の火花タイプ
                    if   self.particle[i].life > 14:  #lifeが減るごとにcolorを10→9→8→2→1と変化させる
                         self.particle[i].color = 10
                    elif self.particle[i].life > 11:
                         self.particle[i].color = 9
                    elif self.particle[i].life > 9:
                         self.particle[i].color = 8
                    elif self.particle[i].life > 7:
                         self.particle[i].color = 2
                    elif self.particle[i].life > 4:
                         self.particle[i].color = 1
               
               if self.particle[i].life < 10: #パーティクルの体力？生命力が10より小さい場合は
                    self.particle[i].size = 0 #強制的にサイズを0にして、小さくさせる

               self.particle[i].life -= 1 #パーティクルの体力（生命力？）を１減少させる
               if self.particle[i].life <= 0: #パーティクルの体力が0以下になったら
                    del self.particle[i] #パーティクルは消えちゃうのです・・・はかない命・・まるで火花・・・

     #背景オブジェクトの更新
     def update_background_object(self):
          object_count = len(self.background_object)
          for i in reversed(range(object_count)):#背景オブジェクトのリストの要素数を数えてその数の分だけループ処理する（delしちゃう可能性があるのでreversedするよ）

               
               if BG_OBJ_CLOUD1 <= self.background_object[i].background_object_type <= BG_OBJ_CLOUD21: #雲1~21の場合
                    self.background_object[i].posx += self.background_object[i].vx
                    self.background_object[i].posy += self.background_object[i].vy

               self.background_object[i].vx = self.background_object[i].vx * self.background_object[i].ax #速度に加速度を掛けあわせて加速もしくは減速させていく
               self.background_object[i].vy = self.background_object[i].vy * self.background_object[i].ay

               #オブジェクトのクリッピング処理
               if      -100 <= self.background_object[i].posx <= WINDOW_W + 100\
                  and  -100 <= self.background_object[i].posx <= WINDOW_H + 100:
                  continue
               else:
                    del self.background_object[i] #描画範囲外になったのでインスタンスを破棄する
     
     #雲の追加(背景オブジェクト)
     def update_append_cloud(self):
         if (pyxel.frame_count % self.cloud_append_interval) == 0 and self.display_cloud_flag == 1: #表示インタバールが0になった&表示フラグがonだったのなら
             if self.cloud_quantity == 0: #雲の量が0の時は「雲小」のみ表示する
                 t = randint(BG_OBJ_CLOUD1,BG_OBJ_CLOUD10)
             elif self.cloud_quantity == 1: #雲の量が1の時は「雲小～中」まで表示する
                 t = randint(BG_OBJ_CLOUD1,BG_OBJ_CLOUD18)
             elif self.cloud_quantity == 2: #雲の量が2の時は「雲小～中～大」まで表示する
                 t = randint(BG_OBJ_CLOUD1,BG_OBJ_CLOUD21)
             
             y = randint(0,120+30)
                    
             new_background_object = Background_object()
             new_background_object.update(t, 160+10,y,  0,    1.009,1,0,0,0,0,0,0,   -3*self.cloud_flow_speed,self.cloud_how_flow,  0,0,   0,0,0,0,0,   0,0,0, 0,0,0,  0,0,0)
             self.background_object.append(new_background_object)

     #タイマーフレアの更新(接触した物質の時間経過を遅くするフレアエフェクト)
     def update_timer_flare(self):
          if self.timer_flare_flag == 0: #タイマーフレアのフラグが建っていなかったらそのまま戻る
               return

          for i in range(30):
               new_particle = Particle()
               new_particle.update(PARTICLE_LINE, self.my_x+3,self.my_y+3,    1,     -random()-0.5, random()-0.5,    80,   i*6, 6)
               self.particle.append(new_particle)
     
     #大気圏突入時の火花の更新
     def update_atmospheric_entry_spark(self):
          if self.atmospheric_entry_spark_flag == SPARK_OFF: #大気圏突入時の火花のフラグが建っていなかったらそのまま戻る
               return
          
          for _i in range(10):
               new_particle = Particle()
               # new_particle.update(PARTICLE_DOT, self.my_x+1,self.my_y+5,    1,     -random() * self.side_scroll_speed * 4, (random() - 0.97) * self.vertical_scroll_speed * 8,    30,   _i // 2, 10)
               new_particle.update(PARTICLE_FIRE_SPARK, self.my_x+3,self.my_y+4,    1,     -random() * self.side_scroll_speed, -(random()+0.5)  * self.vertical_scroll_speed * 2,    2.5 * self.side_scroll_speed,   1, 10)

               self.particle.append(new_particle)

     #ラスタースクロールの更新
     def update_raster_scroll(self):
           if self.raster_scroll_flag == 0: #ラスタスクロール更新＆表示のフラグがたっていなかったらそのまま何もしないで戻る
                return

           raster_scroll_count = len(self.raster_scroll)
           for i in range(raster_scroll_count):#ラスタースクロールのリストの要素数を数えてその数の分だけループ処理する
                if self.raster_scroll[i].raster_type == RASTER_NORMAL: #通常のラスタースクロールの場合
                     #x座標をラスタースクロールのspeedと背景の横軸スクロールspeedを掛け合わせた分だけ加減算して更新
                     self.raster_scroll[i].posx += self.raster_scroll[i].speed * self.side_scroll_speed
                     #y座標は現在の垂直スクロールカウント+y軸オフセット値+上から何番目のラインかを示す数値を直接指定代入する
                     self.raster_scroll[i].posy = (184 - self.vertical_scroll_count // 16) + self.raster_scroll[i].scroll_line_no + self.raster_scroll[i].offset_y
                     #  self.raster_scroll[i].posy = self.raster_scroll[i].offset_y + self.raster_scroll[i].scroll_line_no
                
                     if self.raster_scroll[i].posx <= -self.raster_scroll[i].width: #描画ライン幅のドット数ぶん画面外までスクロールアウトしたのなら
                          self.raster_scroll[i].posx = 0 #初期値であるx座標0を代入する
                
                elif self.raster_scroll[i].raster_type == RASTER_WAVE: #ウェーブラスタースクロールの場合
                     #x座標をラスタースクロールのspeedと背景の横軸スクロールspeedを掛け合わせた分だけ加減算して更新する
                     self.raster_scroll[i].posx += self.raster_scroll[i].speed *self.side_scroll_speed
                     
                     #y座標は現在の垂直スクロールカウント+y軸オフセット値+上から何番目のラインかを示す数値を直接指定代入する
                     self.raster_scroll[i].posy = (184 - self.vertical_scroll_count // 16) + self.raster_scroll[i].scroll_line_no + self.raster_scroll[i].offset_y
                     
                     #ウェーブラスターで波打ってずれる分のoffset_xを計算してやる
                     self.raster_scroll[i].wave_timer += self.raster_scroll[i].wave_speed #timer += speed
                     self.raster_scroll[i].offset_x = self.raster_scroll[i].wave_intensity * math.sin(self.raster_scroll[i].wave_timer) # offset_x = intensity * sin(timer)
                     
                     if self.raster_scroll[i].posx <= -self.raster_scroll[i].width: #描画ライン幅のドット数ぶん画面外までスクロールアウトしたのなら
                          self.raster_scroll[i].posx = 0 #初期値であるx座標0を代入する

     #ポーズメニュー                                                       KEY TAB     GAMEPAD START
     def update_game_pause(self):
          if pyxel.btnp(pyxel.KEY_TAB) or pyxel.btnp(pyxel.GAMEPAD_1_START) or pyxel.btnp(pyxel.GAMEPAD_2_START):
               if     self.game_status == SCENE_PLAY\
                   or self.game_status == SCENE_BOSS_APPEAR\
                   or self.game_status == SCENE_BOSS_BATTLE\
                   or self.game_status == SCENE_BOSS_EXPLOSION:#ステータスが「PLAY」もしくは「BOSS関連」のときにポーズボタンが押されたときは・・

                    self.record_games_status = self.game_status #ステータスを一時記憶しておく
                    self.game_status = SCENE_PAUSE              #ステータスを「PAUSE」にする
               elif self.game_status == SCENE_PAUSE:            #ポーズ状態でポーズボタンが押されたときは・・・
                    self.game_status = self.record_games_status #一時記憶しておいたゲームステータスを元に戻してあげます
                    self.star_scroll_speed = 1 #星のスクロールスピードを倍率1に戻す
               else:
                    return

     #プレイ時間の計算処理を行う
     def update_calc_playtime(self):
          self.playtime_frame_counter += 1           #フレームカウンターをインクリメント
          if self.playtime_frame_counter >= 60:      #フレームカウンターが60以上になったら
               self.playtime_frame_counter = 0       #フレームカウンターをリセットして
               self.one_game_playtime_seconds   += 1 #1プレイタイムを1秒増加させる
               self.total_game_playtime_seconds += 1 #総ゲームプレイ時間も1秒増加させる
               
     #ハイスコアのチェックを行う関数
     def update_check_hi_score(self):
          if self.score > self.hi_score: #スコアがハイスコアより大きければ
               self.hi_score = self.score #ハイスコアにスコアを代入する

     #セレクトカーソルの更新
     def update_select_cursor(self):
         # 上入力されたら  y座標を  -8する(1キャラ分)
          if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD_1_UP) or pyxel.btnp(pyxel.GAMEPAD_2_UP):
              if self.cursor_item != 0: #指し示しているアイテムナンバーが一番上の項目の0以外なら上方向にカーソルは移動できるので・・・
                  self.cursor_y -= 8 #y座標を8ドット（1キャラ分）上に
                  self.cursor_item -= 1 #現在指し示しているアイテムナンバーを1減らす

          # 下入力されたら  y座標を  +8する(1キャラ分)
          if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD_1_DOWN) or pyxel.btnp(pyxel.GAMEPAD_2_DOWN):
              if self.cursor_item != self.cursor_max_item: #指し示しているアイテムナンバーが最大項目数でないのなら下方向にカーソルは移動できるので・・
               self.cursor_y += 8
               self.cursor_item += 1
          
          if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD_1_A) or pyxel.btnp(pyxel.GAMEPAD_2_A) or pyxel.btnp(pyxel.GAMEPAD_1_B) or pyxel.btnp(pyxel.GAMEPAD_2_B):
               self.cursor_decision_item = self.cursor_item #ボタンが押されて決定されたら、いま指示しているアイテムナンバーをcursor_decision_itemに代入！

     #!###############################################################################################################################
     #!################################################################################################################################
     #!draw関数から呼び出される関数群 ###################################################################################################
     #!###############################################################################################################################
     #!################################################################################################################################
     #IPLメッセージの表示#######################################
     def draw_ipl(self):
          #テキストスクリーンリスト全体の行数を数える
          text_number_of_lines_count = len(self.text_screen)
          #どれだけの行が画面上に流れていったのか計算します
          #標準フォントの縦ドット数は6で行間空白として1ドット取りたいので全体で縦7ドット
          #120÷7 =17.14 で画面全体では約17行表示出来ることに成ります
          if text_number_of_lines_count > 17: #テキストスクリーンの行数が17を超えていたら上にスクロールアウトしていることに成るので・・
               self.text_console_scroll_counter = text_number_of_lines_count - 17 #上にスクロールした行数を計算します       
          for i in range(text_number_of_lines_count):
               text_mes = self.text_screen[i][0]
               text_col = self.text_screen[i][1]
               pyxel.text(0,i*6 - self.text_console_scroll_counter * 6 ,str(text_mes),text_col) #y軸をスクロールした行数分だけマイナス方向に補正し画面外(上方向)から前部のテキストを表示するときちんと表示されます
          
     #タイトルの表示#######################################
     def draw_title(self):
          for i in range(160):
               pyxel.blt(0,16 + i  * self.title_oscillation_count % 200 - self.title_slash_in_count,    IMG2,  0,192,  i*1.09,32,   0)
          for i in range(160+1000):
               pyxel.blt(0,16 + i % 1000 * self.title_oscillation_count - self.title_oscillation_count, IMG2,  0,192,  i     ,32,   0)
          
          #デバッグ用に現在のステージ数とループ数とその他いろいろ表示する
          #ステージ数の表示
          pyxel.text(160-3*8+8,1,"ST " + str(self.stage_number), 9)
          #周回数の表示
          pyxel.text(160-3*8+8,8,"LP " + str(self.stage_loop), 7)
          #ボスモード選択中の表示
          pyxel.text(160-6*8,1,"BOSS " + str(self.boss_test_mode),8)
          #ボスヒットボックス
          pyxel.text(160-19*3+8,8,"HITBOX " + str(self.boss_collision_rect_display_flag),10)
          #難易度の表示
          pyxel.text(0,1,"DIFFICULTY " + str(self.game_difficulty),10)
     
     #背景の星の表示
     def draw_star(self):
          stars_count = len(self.stars)
          for i in range(stars_count):
               pyxel.pset(self.stars[i].posx, self.stars[i].posy,self.stars[i].posx  // 4 % 15) 
               #pyxel.pset(self.stars[i].posx, self.stars[i].posy,randint(0,7)) 
     
     #敵の表示
     def draw_enemy(self):
          enemy_count = len(self.enemy)
          for i in range(enemy_count):
               if   self.enemy[i].enemy_type == 1:#敵タイプ１の表示   直進して斜め後退→勢いよく後退していく10機編隊
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2,self.anime_enemy001[pyxel.frame_count % 15],40,SIZE_8,SIZE_8,0)
               elif self.enemy[i].enemy_type == 2:#敵タイプ２の表示   サインカーブを描く3機編隊
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2,self.anime_enemy002[pyxel.frame_count % 40],24,SIZE_8,SIZE_8,0)
               elif self.enemy[i].enemy_type == 3:#敵タイプ３の表示   固定砲台（地面に張り付く単装砲タイプ）
                    self.reverse_flag = 8
                    if self.my_x > self.enemy[i].posx:
                         self.reverse_flag =-8
                    
                    #論理式(enemy[i].item != 0)はitem=0の場合falseで0 item=1または2か3の場合はtrueで1となる（つまりアイテムを持っていたらカッコ内は1となる）
                    #アイテム所持していれば1*24で24ドット横、つまり3キャラチップ横の黄色い固定砲台が表示される事となる
                    if self.my_x == self.enemy[i].posx:
                          pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2, 48 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,SIZE_8, 0)
                    elif self.my_y < self.enemy[i].posy:
                          pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2, 40 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,SIZE_8, 0)
                    elif self.enemy[i].posy < self.my_y:
                          pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2, 32 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,SIZE_8, 0)
                    else:
                          pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2, 40 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,SIZE_8, 0)
               elif self.enemy[i].enemy_type == 4:#敵タイプ４の表示   固定砲台（天井に張り付く単装砲タイプ）
                    self.reverse_flag = 8
                    if self.my_x > self.enemy[i].posx:
                         self.reverse_flag =-8

                    #論理式(enemy[i].item != 0)はitem=0の場合falseで0 item=1または2か3の場合はtrueで1となる（つまりアイテムを持っていたらカッコ内は1となる）
                    #アイテム所持していれば1*24で24ドット横、つまり3キャラチップ横の黄色い固定砲台が表示される事となる
                    if self.my_x == self.enemy[i].posx:
                          pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2, 48 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,-(SIZE_8), 0)
                    elif self.my_y > self.enemy[i].posy:
                          pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2, 40 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,-(SIZE_8), 0)
                    elif self.enemy[i].posy > self.my_y:
                          pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2, 32 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,-(SIZE_8), 0)
                    else:
                          pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2, 40 + (self.enemy[i].item != 0) * 24,32, self.reverse_flag,-(SIZE_8), 0)
               elif self.enemy[i].enemy_type == 5:#敵タイプ５の表示   ぴょんぴょんはねるホッパーちゃんmk2
                  pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2,self.anime_enemy005[pyxel.frame_count % 40],24,SIZE_8,SIZE_8,0)        
               elif self.enemy[i].enemy_type == 6:#敵タイプ６の表示   謎の回転飛翔体Ｍ５４
                  pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2,24+(((self.stage_count // 30) % 2) * 8),24,SIZE_8,SIZE_8,0)
               elif self.enemy[i].enemy_type == 7:#敵タイプ７の表示   追尾戦闘機（サインカーブを描きつつ追尾してくる）
                  pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2,   88,32,   SIZE_8,SIZE_8,  0)
               elif self.enemy[i].enemy_type == 8:#敵タイプ８の表示   追尾戦闘機
                   if self.enemy[i].vy < 0:
                       up_down_reverse = 8
                   else:
                       up_down_reverse = -8
                                  
                   if   self.enemy[i].vx < 0:
                       right_left_reverse = 8
                   else:
                       right_left_reverse = -8

                   
                   
                   pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2,   96 ,32,   right_left_reverse,up_down_reverse,  0)
               elif self.enemy[i].enemy_type == 9:#敵タイプ９の表示   Ｙ軸を合わせた後突っ込んで来る敵機
                pyxel.blt(self.enemy[i].posx, self.enemy[i].posy, IMG2,      self.anime_enemy009[pyxel.frame_count % 40],48,     SIZE_8,SIZE_8,    0)
               elif self.enemy[i].enemy_type == 10:#敵タイプ10の表示  スクランブルハッチ地面タイプ
                    pyxel.blt(self.enemy[i].posx, self.enemy[i].posy, IMG2,  112,32,  3*8,2*8,  0)
                    if 0 <= self.enemy[i].enemy_flag1 <= 43:
                         pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy, IMG2,  136+(self.enemy[i].enemy_flag1 // 6) * 8,40,  SIZE_8,SIZE_8,  0)
                    if 43 <= self.enemy[i].enemy_flag1 <= 86:
                         pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy, IMG2,  184-(self.enemy[i].enemy_flag1 // 7) * 8,40,  SIZE_8,SIZE_8,  0)
               elif self.enemy[i].enemy_type == 11:#敵タイプ11の表示  スクランブルハッチ天井タイプ
                    pyxel.blt(self.enemy[i].posx, self.enemy[i].posy, IMG2,  112,32,  3*8,-(2*8),  0)
                    if 0 <= self.enemy[i].enemy_flag1 <= 43:
                         pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy + 8, IMG2,  136+(self.enemy[i].enemy_flag1 // 6) * 8,40,  SIZE_8,-(SIZE_8),  0)
                    if 43 <= self.enemy[i].enemy_flag1 <= 86:
                         pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy + 8, IMG2,  184-(self.enemy[i].enemy_flag1 // 7) * 8,40,  SIZE_8,-(SIZE_8),  0)
               elif self.enemy[i].enemy_type == 12:#敵タイプ12の表示  レーザービームを発射した後、高速で後退する敵
                   pyxel.blt(self.enemy[i].posx, self.enemy[i].posy, IMG2,  144 + ((self.enemy[i].enemy_flag1 // 7) * 8),32,  SIZE_8,SIZE_8,  0)#数値をいじったらうまくいった　良かった・・たまたまだけど                  
               elif self.enemy[i].enemy_type == 13:#敵タイプ13の表示  3way弾を射出する硬い奴（ショットパワーアップアイテムを持っている）
                    pyxel.blt(self.enemy[i].posx, self.enemy[i].posy,IMG2, 0,24, SIZE_8,SIZE_8, 0)
               elif self.enemy[i].enemy_type == 14:#敵タイプ14の表示  ゆっくり直進してくる赤いアイテムキャリアー（パワーアップアイテムを持っている）
                    pyxel.blt(self.enemy[i].posx    , self.enemy[i].posy,IMG2, 104                                     ,104,   SIZE_8,SIZE_8,  0) #コックピット部表示
                    pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy,IMG2, 112 + (self.stage_count // 2  % 4) * 16,104,  SIZE_16,SIZE_8,  0) #エンジンノズル＆噴射パターン表示
               elif self.enemy[i].enemy_type == 15:#敵タイプ15の表示  地面だったり天井を左右に動きながらチョット進んできて弾を撃つ移動砲台
                    pyxel.blt(self.enemy[i].posx    , self.enemy[i].posy,IMG2, 208 + self.stage_count // 3 % 6 * 8,32,   SIZE_8,SIZE_8,  0)   
               elif self.enemy[i].enemy_type == 16:#敵タイプ16の表示  2機一体で挟みこみ攻撃をしてくるクランパリオン
                    pyxel.blt(self.enemy[i].posx    , self.enemy[i].posy,IMG2,       (self.stage_count // 2) % 4   * 8, 56,     SIZE_8 ,SIZE_8, 0)
                    pyxel.blt(self.enemy[i].posx + 8, self.enemy[i].posy,IMG2, 176 + (pyxel.frame_count // 2  % 3) * 8,104,   -(SIZE_8),SIZE_8, 0) #イオンエンジン噴射の描画
               elif self.enemy[i].enemy_type == 17:#敵タイプ17の表示  スプライン曲線で定点まで移動して離脱する敵 ロールブリッツ
                    pyxel.blt(self.enemy[i].posx    , self.enemy[i].posy,IMG2,       0, 32,     SIZE_8 ,SIZE_8, 0)
               elif self.enemy[i].enemy_type == 18:#敵タイプ18の表示  チョット大き目で硬いばらまき弾の敵 ボルダー
                    pyxel.blt(self.enemy[i].posx    , self.enemy[i].posy,IMG2,       80,48,     SIZE_40 ,SIZE_24, 15)     
     
     #ボスの表示
     def draw_boss(self):
          boss_count = len(self.boss)
          for i in range(boss_count):
               if    self.boss[i].boss_type == BOSS_FATTY_VALGUARD:#ファッティ・バルガード(前線基地ボス)
                   offset_x = 0 #真っ二つになる描画用のx軸オフセット値(離れた距離)をリセットする
                   if self.boss[i].count2 !=0: #カウントが0だと0で割ってしまってエラーになるのでスキップする
                       offset_x = 10 - self.boss[i].count2 // 48 #count2が少なくなるごとにoffset_xが増加することに成る
                                                                 #count2の数値は最初は480フレームで最終的に0となり,この計算式からoffset_xは480フレームの間で0から10まで変化することに成る

                   pyxel.blt(self.boss[i].posx + offset_x, self.boss[i].posy + offset_x // 16,  IMG0,   64,128,8*8,5*8,     15) #ファッティバルガード前部表示
                   pyxel.blt(self.boss[i].posx - offset_x, self.boss[i].posy                 ,  IMG0,    0,184,5*8,3*8,     15) #ファッティバルガード後部表示 
               
                   if self.boss[i].parts1_flag == 1: #パーツフラグ1(5way砲台)が生存していたのなら描画する
                         pyxel.blt(self.boss[i].posx - offset_x, self.boss[i].posy + 16,        IMG0,    0,176,    2*8,8,     15)
                   if self.boss[i].parts2_flag == 1: #パーツフラグ2(尾翼レーザーユニット)が生存していたのなら描画する
                         pyxel.blt(self.boss[i].posx - offset_x, self.boss[i].posy,             IMG0,   16,176,    3*8,8,     15)
                   if self.boss[i].parts3_flag == 1: #パーツフラグ3(赤色爆雷ユニット)が生存していたのなら描画する
                         pyxel.blt(self.boss[i].posx - offset_x + 8, self.boss[i].posy + 24,    IMG0,   40,176,    2*8,8,     15)
               
               elif  self.boss[i].boss_type == BOSS_BREEZARDIA:    #ブリザーディア(山岳地帯ボス)
                   offset_x = 0 #真っ二つになる描画用のx軸オフセット値(離れた距離)をリセットする
                   if self.boss[i].count2 !=0: #カウントが0だと0で割ってしまってエラーになるのでスキップする
                       offset_x = 10 - self.boss[i].count2 // 48 #count2が少なくなるごとにoffset_xが増加することに成る
                                                                 #count2の数値は最初は480フレームで最終的に0となり,この計算式からoffset_xは480フレームの間で0から10まで変化することに成る

                   pyxel.blt(self.boss[i].posx + offset_x, self.boss[i].posy + offset_x // 16,  IMG0,   40,184,self.boss[i].width,self.boss[i].height,     15) #ブリザーディア前部表示
                   
                   if self.boss[i].parts1_flag == 1: #パーツフラグ1(右下赤砲台)が生存していたのなら描画する
                         pyxel.blt(self.boss[i].posx - offset_x + 10*8, self.boss[i].posy + 4*8,        IMG0,    152,216,    2*8,2*8,     15)
                   if self.boss[i].parts2_flag == 1: #パーツフラグ2(右下緑砲台)が生存していたのなら描画する
                         pyxel.blt(self.boss[i].posx - offset_x +  8*8, self.boss[i].posy + 4*8,        IMG0,    152,200,    2*8,2*8,     15)
                   if self.boss[i].parts3_flag == 1: #パーツフラグ3(上部主砲)が生存していたのなら描画する
                         pyxel.blt(self.boss[i].posx - offset_x +  4*8, self.boss[i].posy + self.boss[i].weapon1_cool_down_time // 100,        IMG0,      0,216,    3*8,2*8,     15)
                   if self.boss[i].parts4_flag == 1: #パーツフラグ4(上部グリーンカッター)が生存していたのなら描画する
                         #グリーンカッター本体
                         pyxel.blt(self.boss[i].posx - offset_x       , self.boss[i].posy      ,        IMG0,      0,232,    4*8,3*8,     15)
                         #グリーンカッター手前にある後部ユニット部
                         pyxel.blt(self.boss[i].posx - offset_x +  1*8, self.boss[i].posy + 1*8,        IMG0,     32,240,    2*8,2*8,     15)

               #デバッグ用の当たり判定矩形の表示
               self.draw_boss_collision_rectangle(i)     #ボス本体の当たり判定矩形を表示する関数の呼び出し
                    
     #ボスの耐久力の表示 (同じコードをコピペしまくりなのでいつかキチンとループ処理して短くしたい・・・)
     def draw_boss_hp(self):
          boss_count = len(self.boss)
          for i in range(boss_count):
               if self.boss[i].display_time_main_hp_bar >= 0: #ボス本体の耐久力を表示するタイムカウントが残っていたのなら
                    hp = self.boss[i].main_hp / 4
                    if hp > 32:
                         hp = 31
                    x = self.boss[i].posx + self.boss[i].main_hp_bar_offset_x
                    y = self.boss[i].posy + self.boss[i].main_hp_bar_offset_y
                    self.display_boss_hp_bar(x,y,hp)
                    self.boss[i].display_time_main_hp_bar -= 1 #タイムカウントを１減らす
                    
               if self.boss[i].display_time_parts1_hp_bar >= 0: #パーツ１(ファッティバルガードの場合5way砲台)の耐久力を表示するタイムカウントが残っていたのなら
                    hp = self.boss[i].parts1_hp / 12
                    if hp > 12:
                         hp = 12
                    x,y = self.boss[i].posx + self.boss[i].parts1_hp_bar_offset_x,self.boss[i].posy + self.boss[i].parts1_hp_bar_offset_y
                    self.display_boss_hp_short_bar(x,y,hp)
                    self.boss[i].display_time_parts1_hp_bar -= 1 #タイムカウントを１減らす
                    
               if self.boss[i].display_time_parts2_hp_bar >= 0: #パーツ2(ファッティバルガードの場合尾翼レーザーユニット)の耐久力を表示するタイムカウントが残っていたのなら
                    hp = self.boss[i].parts2_hp / 12
                    if hp > 12:
                         hp = 12
                    x,y = self.boss[i].posx + self.boss[i].parts2_hp_bar_offset_x,self.boss[i].posy + self.boss[i].parts2_hp_bar_offset_y
                    self.display_boss_hp_short_bar(x,y,hp)
                    self.boss[i].display_time_parts2_hp_bar -= 1 #タイムカウントを１減らす

               if self.boss[i].display_time_parts3_hp_bar >= 0: #パーツ3(ファッティバルガードの場合赤色爆雷ユニット)の耐久力を表示するタイムカウントが残っていたのなら
                    hp = self.boss[i].parts3_hp / 32
                    if hp > 8:
                         hp = 8
                    x,y = self.boss[i].posx + self.boss[i].parts3_hp_bar_offset_x,self.boss[i].posy + self.boss[i].parts3_hp_bar_offset_y
                    self.display_boss_hp_short2_bar(x,y,hp)
                    self.boss[i].display_time_parts3_hp_bar -= 1 #タイムカウントを１減らす           
               
               if self.boss[i].display_time_parts4_hp_bar >= 0: #パーツ4の耐久力を表示するタイムカウントが残っていたのなら
                    hp = self.boss[i].parts4_hp / 32
                    if hp > 8:
                         hp = 8
                    x,y = self.boss[i].posx + self.boss[i].parts4_hp_bar_offset_x,self.boss[i].posy + self.boss[i].parts4_hp_bar_offset_y
                    self.display_boss_hp_short2_bar(x,y,hp)
                    self.boss[i].display_time_parts4_hp_bar -= 1 #タイムカウントを１減らす
               
               if self.boss[i].display_time_parts5_hp_bar >= 0: #パーツ5の耐久力を表示するタイムカウントが残っていたのなら
                    hp = self.boss[i].parts5_hp / 32
                    if hp > 8:
                         hp = 8
                    x,y = self.boss[i].posx + self.boss[i].parts5_hp_bar_offset_x,self.boss[i].posy + self.boss[i].parts5_hp_bar_offset_y
                    self.display_boss_hp_short2_bar(x,y,hp)
                    self.boss[i].display_time_parts5_hp_bar -= 1 #タイムカウントを１減らす
               
               if self.boss[i].display_time_parts6_hp_bar >= 0: #パーツ6の耐久力を表示するタイムカウントが残っていたのなら
                    hp = self.boss[i].parts6_hp / 32
                    if hp > 8:
                         hp = 8
                    x,y = self.boss[i].posx + self.boss[i].parts6_hp_bar_offset_x,self.boss[i].posy + self.boss[i].parts6_hp_bar_offset_y
                    self.display_boss_hp_short2_bar(x,y,hp)
                    self.boss[i].display_time_parts6_hp_bar -= 1 #タイムカウントを１減らす
               
               if self.boss[i].display_time_parts7_hp_bar >= 0: #パーツ7の耐久力を表示するタイムカウントが残っていたのなら
                    hp = self.boss[i].parts7_hp / 32
                    if hp > 8:
                         hp = 8
                    x,y = self.boss[i].posx + self.boss[i].parts7_hp_bar_offset_x,self.boss[i].posy + self.boss[i].parts7_hp_bar_offset_y
                    self.display_boss_hp_short2_bar(x,y,hp)
                    self.boss[i].display_time_parts7_hp_bar -= 1 #タイムカウントを１減らす
               
               if self.boss[i].display_time_parts8_hp_bar >= 0: #パーツ8の耐久力を表示するタイムカウントが残っていたのなら
                    hp = self.boss[i].parts8_hp / 32
                    if hp > 8:
                         hp = 8
                    x,y = self.boss[i].posx + self.boss[i].parts8_hp_bar_offset_x,self.boss[i].posy + self.boss[i].parts8_hp_bar_offset_y
                    self.display_boss_hp_short2_bar(x,y,hp)
                    self.boss[i].display_time_parts8_hp_bar -= 1 #タイムカウントを１減らす
               
               if self.boss[i].display_time_parts9_hp_bar >= 0: #パーツ9の耐久力を表示するタイムカウントが残っていたのなら
                    hp = self.boss[i].parts9_hp / 32
                    if hp > 8:
                         hp = 8
                    x,y = self.boss[i].posx + self.boss[i].parts9_hp_bar_offset_x,self.boss[i].posy + self.boss[i].parts9_hp_bar_offset_y
                    self.display_boss_hp_short2_bar(x,y,hp)
                    self.boss[i].display_time_parts9_hp_bar -= 1 #タイムカウントを１減らす

     #ボス本体の当たり判定矩形の表示(i=ボスクラスのインデックス値となります)(デバッグ用)(同じコードをコピペしまくりなのでいつかキチンとループ処理して短くしたい・・・)
     def draw_boss_collision_rectangle(self,i):
          if self.boss_collision_rect_display_flag != 1: #デバッグ時に使う当たり判定矩形表示フラグがonでないのならば
               return                                    #何もしないで戻ります
          
          if self.boss[i].col_main1_w != 0: #本体当たり判定1の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_main1_x,self.boss[i].posy + self.boss[i].col_main1_y,self.boss[i].col_main1_w,self.boss[i].col_main1_h,self.blinking_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].col_main2_w != 0: #本体当たり判定2の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_main2_x,self.boss[i].posy + self.boss[i].col_main2_y,self.boss[i].col_main2_w,self.boss[i].col_main2_h,self.blinking_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].col_main3_w != 0: #本体当たり判定3の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_main3_x,self.boss[i].posy + self.boss[i].col_main3_y,self.boss[i].col_main3_w,self.boss[i].col_main3_h,self.blinking_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].col_main4_w != 0: #本体当たり判定4の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_main4_x,self.boss[i].posy + self.boss[i].col_main4_y,self.boss[i].col_main4_w,self.boss[i].col_main4_h,self.blinking_color[pyxel.frame_count // 8 % 10]) 
          if self.boss[i].col_main5_w != 0: #本体当たり判定5の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_main5_x,self.boss[i].posy + self.boss[i].col_main5_y,self.boss[i].col_main5_w,self.boss[i].col_main5_h,self.blinking_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].col_main6_w != 0: #本体当たり判定6の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_main6_x,self.boss[i].posy + self.boss[i].col_main6_y,self.boss[i].col_main6_w,self.boss[i].col_main6_h,self.blinking_color[pyxel.frame_count // 8 % 10])     
          if self.boss[i].col_main7_w != 0: #本体当たり判定7の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_main7_x,self.boss[i].posy + self.boss[i].col_main7_y,self.boss[i].col_main7_w,self.boss[i].col_main7_h,self.blinking_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].col_main8_w != 0: #本体当たり判定8の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_main8_x,self.boss[i].posy + self.boss[i].col_main8_y,self.boss[i].col_main8_w,self.boss[i].col_main8_h,self.blinking_color[pyxel.frame_count // 8 % 10])     
          
          if self.boss[i].parts1_flag == 1:#パーツ1が健在なら表示する
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts1_x,self.boss[i].posy + self.boss[i].col_parts1_y,self.boss[i].col_parts1_w,self.boss[i].col_parts1_h,self.red_flash_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].parts2_flag == 1:#パーツ2が健在なら表示する
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts2_x,self.boss[i].posy + self.boss[i].col_parts2_y,self.boss[i].col_parts2_w,self.boss[i].col_parts2_h,self.green_flash_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].parts3_flag == 1:#パーツ3が健在なら表示する
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts3_x,self.boss[i].posy + self.boss[i].col_parts3_y,self.boss[i].col_parts3_w,self.boss[i].col_parts3_h,self.yellow_flash_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].parts4_flag == 1:#パーツ4が健在なら表示する
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts4_x,self.boss[i].posy + self.boss[i].col_parts4_y,self.boss[i].col_parts4_w,self.boss[i].col_parts4_h,self.monochrome_flash_color[pyxel.frame_count // 8 % 15])
          if self.boss[i].parts5_flag == 1:#パーツ5が健在なら表示する
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts5_x,self.boss[i].posy + self.boss[i].col_parts5_y,self.boss[i].col_parts5_w,self.boss[i].col_parts5_h,self.red_flash_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].parts6_flag == 1:#パーツ6が健在なら表示する
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts6_x,self.boss[i].posy + self.boss[i].col_parts6_y,self.boss[i].col_parts6_w,self.boss[i].col_parts6_h,self.green_flash_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].parts7_flag == 1:#パーツ7が健在なら表示する
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts7_x,self.boss[i].posy + self.boss[i].col_parts7_y,self.boss[i].col_parts7_w,self.boss[i].col_parts7_h,self.yellow_flash_color[pyxel.frame_count // 8 % 10])
          if self.boss[i].parts8_flag == 1:#パーツ8が健在なら表示する
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts8_x,self.boss[i].posy + self.boss[i].col_parts8_y,self.boss[i].col_parts8_w,self.boss[i].col_parts8_h,self.monochrome_flash_color[pyxel.frame_count // 8 % 15])
          if self.boss[i].parts9_flag == 1:#パーツ9が健在なら表示する
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_parts9_x,self.boss[i].posy + self.boss[i].col_parts9_y,self.boss[i].col_parts9_w,self.boss[i].col_parts9_h,self.yellow_flash_color[pyxel.frame_count // 8 % 10])


          if self.boss[i].col_damage_point1_w != 0: #ボスのダメージポイント(弱点)1の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_damage_point1_x,self.boss[i].posy + self.boss[i].col_damage_point1_y,self.boss[i].col_damage_point1_w,self.boss[i].col_damage_point1_h,self.rainbow_flash_color[pyxel.frame_count // 3 % 15])
          if self.boss[i].col_damage_point2_w != 0: #ボスのダメージポイント(弱点)2の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_damage_point2_x,self.boss[i].posy + self.boss[i].col_damage_point2_y,self.boss[i].col_damage_point2_w,self.boss[i].col_damage_point2_h,self.rainbow_flash_color[pyxel.frame_count // 3 % 15])
          if self.boss[i].col_damage_point3_w != 0: #ボスのダメージポイント(弱点)3の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_damage_point3_x,self.boss[i].posy + self.boss[i].col_damage_point3_y,self.boss[i].col_damage_point3_w,self.boss[i].col_damage_point3_h,self.rainbow_flash_color[pyxel.frame_count // 3 % 15])
          if self.boss[i].col_damage_point4_w != 0: #ボスのダメージポイント(弱点)4の表示 当たり判定の横幅が0の場合はスキップして表示しない
               pyxel.rectb(self.boss[i].posx + self.boss[i].col_damage_point4_x,self.boss[i].posy + self.boss[i].col_damage_point4_y,self.boss[i].col_damage_point4_w,self.boss[i].col_damage_point4_h,self.rainbow_flash_color[pyxel.frame_count // 3 % 15])

     #敵の弾の表示
     def draw_enemy_shot(self,p): #pの数値と一致するプライオリティナンバーを持つ敵弾だけを描画します
          enemy_shot_count = len(self.enemy_shot)
          for i in range(enemy_shot_count):
               if self.enemy_shot[i].priority == p:
                    if   self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_LASER:             #通常レーザーの表示
                         pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy, IMG2,   152,16,    8, 8,    0)#敵レーザービームの表示
                    elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_GREEN_LASER:       #ボスのグリーンレーザーの表示
                         pyxel.line(self.enemy_shot[i].posx,self.enemy_shot[i].posy,  self.enemy_shot[i].posx + 8,self.enemy_shot[i].posy  ,11) #グリーンレーザービームの表示
                         #pyxel.line(self.enemy_shot[i].posx,self.enemy_shot[i].posy+1,self.enemy_shot[i].posx + 8,self.enemy_shot[i].posy+1,3) #影部分の線を描画
                    elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_RED_LASER:         #ボスのレッドレーザーの表示
                         pyxel.line(self.enemy_shot[i].posx,self.enemy_shot[i].posy,  self.enemy_shot[i].posx + 8,self.enemy_shot[i].posy  ,8)#レッドレーザービームの表示
                    elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_HOMING_LASER:      #ホーミングレーザーの表示
                         pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy, IMG2,   200,16,    8, 8,    0)#ホーミングレーザーの頭の表示
                    elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_HOMING_LASER_TAIL: #ホーミングレーザーの尻尾の表示
                         pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy, IMG2,   160+(self.enemy_shot[i].disappearance_count // 12) * 8,16,    8, 8,    0)#ホーミングレーザーの尻尾の表示
                    elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_SEARCH_LASER:      #サーチレーザーの表示
                         if self.enemy_shot[i].search_flag == 0: #自機サーチ完了フラグがたっていない場合は横状態のグラフイックを表示する
                              pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy, IMG2,   216,40,    8, 8,    0)#サーチレーザーの頭の表示(横)
                         else: ##自機サーチ完了フラグがたってたら縦状態のグラフイックを表示する
                              pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy, IMG2,   216,48,    8, 8 * ((self.enemy_shot[i].vy < 0)-(self.enemy_shot[i].vy > 0)),    0)#サーチレーザーの頭の表示(縦),vyの符号を求めてグラフイックを反転してます(論理式を使用)                     
                    elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_SEARCH_LASER_TAIL: #サーチレーザーの尻尾の表示
                         if self.enemy_shot[i].search_flag == 0:
                              pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy, IMG2,   224+8*(self.enemy_shot[i].disappearance_count < 30)+8*(self.enemy_shot[i].disappearance_count < 15),40,    8, 8,    0)#サーチレーザーの尻尾(横)の表示
                         else:
                              pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy, IMG2,   224+8*(self.enemy_shot[i].disappearance_count < 30)+8*(self.enemy_shot[i].disappearance_count < 15),48,    8, 8*((self.enemy_shot[i].vy < 0)-(self.enemy_shot[i].vy > 0)),    0)#サーチレーザーの尻尾(縦)の表示,vyの符号を求めてグラフイックを反転してます(論理式を使用)
                    elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_UP_LASER:          #アップレーザーの表示
                         pyxel.line(self.enemy_shot[i].posx,self.enemy_shot[i].posy+4,  self.enemy_shot[i].posx + self.enemy_shot[i].width,self.enemy_shot[i].posy+4  ,11) #アップレーザーの表示
                    elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_DOWN_LASER:        #ダウンレーザーの表示
                         pyxel.line(self.enemy_shot[i].posx,self.enemy_shot[i].posy+4,  self.enemy_shot[i].posx + self.enemy_shot[i].width,self.enemy_shot[i].posy+4  ,9) #ダウンレーザーの表示
                    elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_VECTOR_LASER:      #ベクトルレーザーの表示
                         pyxel.line(self.enemy_shot[i].posx+4,self.enemy_shot[i].posy,  self.enemy_shot[i].posx+4,self.enemy_shot[i].posy + self.enemy_shot[i].height   ,8) #ベクトルレーザーの表示
                    elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_GREEN_CUTTER:      #ブリザーディア」が尾翼部から射出するグリーンカッターの表示
                         pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy, IMG2,   64,56,    SIZE_16, SIZE_16,    15)
                    else:                                                                    #通常弾の表示
                         pyxel.blt(self.enemy_shot[i].posx, self.enemy_shot[i].posy, IMG2,   32 + (self.enemy_shot[i].posx // 8) % 4 * 8,0,     8, 8,    13)#敵通常弾の表示 posxを使用してアニメーションパターンのオフセット値を計算する                    
     
     #爆発パターンの表示
     def draw_explosion(self,disp_priority):
          explosioncount = len(self.explosions)
          for i in reversed(range(explosioncount)):
              if self.explosions[i].priority == disp_priority: #指定されたプライオリティナンバーの爆発だけ表示する
                  if    self.explosions[i].explosion_type == EXPLOSION_NORMAL:#敵爆発の通常タイプの爆発パターン表示
                      pyxel.blt(self.explosions[i].posx,self.explosions[i].posy,IMG2,136 -(self.explosions[i].explosion_count * 8)       ,0,  SIZE_8,SIZE_8,0)
                  elif  self.explosions[i].explosion_type == EXPLOSION_MIDDLE:#スクランブルハッチや重爆撃機系の敵を倒したときの中くらいの爆発パターン
                      pyxel.blt(self.explosions[i].posx,self.explosions[i].posy,IMG2,48  -(self.explosions[i].explosion_count // 2 * 16),176,SIZE_16,SIZE_16 * self.explosions[i].y_reverse,0)
                  elif  self.explosions[i].explosion_type == EXPLOSION_MY_SHIP:#自機爆発の爆発パターン表示
                      pyxel.blt(self.explosions[i].posx,self.explosions[i].posy,IMG2,240 -(self.explosions[i].explosion_count // 8 * 16),240, SIZE_16,SIZE_8,0)

     #パーティクルの表示
     def draw_particle(self):
          particlecount = len(self.particle)
          for i in reversed(range(particlecount)):
               if self.particle[i].particle_type == PARTICLE_DOT: #パーティクルタイプ 1~2ドット描画タイプ
                    pyxel.pset(self.particle[i].posx,self.particle[i].posy,self.particle[i].color) #正方形1ドット分のパーティクルを描画
                    if self.particle[i].size > 0: #sizeが0より大きかったら横長2ドット分のパーティクルを描画する
                         pyxel.pset(self.particle[i].posx + 1,self.particle[i].posy,self.particle[i].color)
               
               elif self.particle[i].particle_type == PARTICLE_LINE or\
                    self.particle[i].particle_type == PARTICLE_FIRE_SPARK: #パーティクルタイプ ラインタイプまたは大気圏突入時の火花タイプ
                    pyxel.pset(self.particle[i].posx,self.particle[i].posy,self.particle[i].color) #正方形1ドット分のパーティクルを描画
               
               elif self.particle[i].particle_type == PARTICLE_CIRCLE: #パーティクルタイプ 円形パーティクルタイプ
                    pyxel.circ(self.particle[i].posx,self.particle[i].posy,self.particle[i].size,self.particle[i].color) #半径size分の円形パーティクルを描画
               
               elif self.particle[i].particle_type == PARTICLE_MISSILE_DEBRIS: #パーティクルタイプ ミサイルの破片
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy,IMG2,184 + (7 - self.particle[i].life) * 8,0, 8,8, 0) #ミサイル破片デブリをlifeの値をアニメーションパターンオフセット値としてスプライト表示する
               
               elif self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS1: #パーティクルタイプ ボスの破片その1
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy,IMG2,160 + (12 - (self.particle[i].life % 12)) * 8,216, 8,8, 0) #ボス破片デブリ1をlifeの値をアニメーションパターンオフセット値としてスプライト表示する
     
               elif self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS2: #パーティクルタイプ ボスの破片その2
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy,IMG2,160 + (6 - (self.particle[i].life % 6)) * 8,208, 8,8, 0) #ボス破片デブリ2をlifeの値をアニメーションパターンオフセット値としてスプライト表示する
               
               elif self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS3: #パーティクルタイプ ボスの破片その3
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy,IMG2,160 + (12 - (self.particle[i].life % 12)) * 8,200, 8,8, 0) #ボス破片デブリ3をlifeの値をアニメーションパターンオフセット値としてスプライト表示する
               
               elif self.particle[i].particle_type == PARTICLE_BOSS_DEBRIS4: #パーティクルタイプ ボスの破片その4
                    pyxel.blt(self.particle[i].posx,self.particle[i].posy,IMG2,192 + (8 - (self.particle[i].life % 8)) * 8,192, 8,8, 0) #ボス破片デブリ4をlifeの値をアニメーションパターンオフセット値としてスプライト表示する
     #背景オブジェクトの表示
     def draw_background_object(self):
          object_count = len(self.background_object)
          for i in reversed(range(object_count)):
               if   self.background_object[i].background_object_type == BG_OBJ_CLOUD1: #雲小1
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     240,240,    16, 9,     1) #雲小1を描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD2: #雲小2
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     232,232,     8, 8,     1) #雲小2を描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD3: #雲小3
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     224,248,     8, 8,     1) #雲小3を描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD4: #雲小4
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     200,248,     8, 8,     1) #雲小4を描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD5: #雲小5
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     192,248,     8, 8,     1) #雲小5を描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD6: #雲小6
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     176,248,     8, 8,     1) #雲小6を描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD7: #雲小7
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     184,248,     7, 8,     1) #雲小7を描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD8: #雲小8
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     224,248,    16, 8,     1) #雲小8を描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD9: #雲小9
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     240,248,    16, 8,     1) #雲小9を描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD10: #雲小10
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     224,224,    16, 8,     1) #雲小10を描画

               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD11: #雲中11
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     176,232,    16,16,     1) #雲中11を描画(正方形っぽい)
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD12: #雲中12
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     240,224,    16,16,     1) #雲中12を描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD13: #雲中13
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     192,224,    48, 8,     1) #雲中13を描画(かなり横長)
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD14: #雲中14
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,      88,248,    24, 8,     1) #雲中14を描画(ちょこっと横長)
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD15: #雲中15
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,       0,240,    48,48,     1) #雲中15を描画(かなり横長)
                   pyxel.blt(self.background_object[i].posx +7*8,self.background_object[i].posy + 8,    1,      48,248,     8, 8,     1) #雲中15右下の尻尾部分描画
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD16: #雲中16
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,      88,216,    48, 8,     1) #雲中16を描画(かなり横長)
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD17: #雲中17
                   pyxel.blt(self.background_object[i].posx,self.background_object[i].posy,    IMG1,     168,216,    24,16,     1) #雲中17を描画(チョット正方形ッポイ？)
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD18: #雲中18
                   pyxel.blt(self.background_object[i].posx     ,self.background_object[i].posy    ,  IMG1, 192,232,    48,16,     1) #雲中18を描画(中サイズで一番大きいかも？) 
                   pyxel.blt(self.background_object[i].posx +5*8,self.background_object[i].posy + 8,  IMG1, 232,240,     8, 8,     1) #雲中18の尻尾を描画
                   pyxel.blt(self.background_object[i].posx +2*8,self.background_object[i].posy +16,  IMG1, 208,248,    16, 8,     1) #雲中18のお腹のあたりを描画
               
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD19: #雲大19
                   pyxel.blt(self.background_object[i].posx     ,self.background_object[i].posy   ,  IMG1,   0,216,    46,24,     1) #雲大19を描画
                   pyxel.blt(self.background_object[i].posx +6*8,self.background_object[i].posy +8,  IMG1,  48,224,     8,10,     1) #雲大19の尻尾部分を描画 
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD20: #雲大20(おにぎり雲)
                   pyxel.blt(self.background_object[i].posx +2*8,self.background_object[i].posy +1  ,  IMG1,  64,209,    24,15,     1) #雲大20の三角山頂部分描画
                   pyxel.blt(self.background_object[i].posx +1*8,self.background_object[i].posy +2*8,  IMG1,  56,224,    40,16,     1) #雲大20の中腹部分を描画 
                   pyxel.blt(self.background_object[i].posx +1*8,self.background_object[i].posy +4*8,  IMG1,  56,240,    40,16,     1) #雲大20の下腹部分を描画 
                   pyxel.blt(self.background_object[i].posx   +1,self.background_object[i].posy +3*8,  IMG1,  49,232,    16,16,     1) #雲大20のおにぎりの左足（？）部分を描画
                   pyxel.blt(self.background_object[i].posx +5*8,self.background_object[i].posy +5*8,  IMG1,  88,248,    16, 8,     1) #雲大20の右下の離れ小島部分を描画  
               elif self.background_object[i].background_object_type == BG_OBJ_CLOUD21: #雲大21(みぎでっかち雲)
                   pyxel.blt(self.background_object[i].posx +5*8,self.background_object[i].posy     ,  IMG1, 136,216,    32,40,     1) #雲大21の右頭本体部分描画
                   pyxel.blt(self.background_object[i].posx     ,self.background_object[i].posy +1*8,  IMG1,  96,224,    48,18,     1) #雲大21の中央本体部分描画
                   pyxel.blt(self.background_object[i].posx +9*8,self.background_object[i].posy +2*8,  IMG1, 160,232,    16,24,     1) #雲大21の右先端描画
                   pyxel.blt(self.background_object[i].posx +3*8,self.background_object[i].posy +3*8,  IMG1, 112,240,    64,16,     1) #雲大21の下部右描画
                   pyxel.blt(self.background_object[i].posx     ,self.background_object[i].posy +2*8,  IMG1,  96,232,    24,16,     1) #雲大21の左のしっぽ描画
     
     #ラスタースクロールの表示
     def draw_raster_scroll(self,disp_priority):
           if self.raster_scroll_flag == 0: #ラスタスクロール更新＆表示のフラグがたっていなかったらそのまま何もしないで戻る
                return

           raster_scroll_count = len(self.raster_scroll)
           for i in range(raster_scroll_count):#ラスタースクロールのリストの要素数を数えてその数の分だけループ処理する
                if self.raster_scroll[i].display == 1 and self.raster_scroll[i].priority == disp_priority: #dispiay == 1(on) & priority == 引数のdisp_priorityの時だけ描画する
                     pyxel.blt(self.raster_scroll[i].posx + self.raster_scroll[i].offset_x,self.raster_scroll[i].posy,
                          self.raster_scroll[i].img_bank,
                          self.raster_scroll[i].posu,self.raster_scroll[i].posv,
                          self.raster_scroll[i].width,self.raster_scroll[i].height,
                          self.raster_scroll[i].transparent_color)
                
                     #右横に更に同じラインを描画する
                     pyxel.blt(self.raster_scroll[i].posx + self.raster_scroll[i].offset_x + self.raster_scroll[i].width,self.raster_scroll[i].posy,
                          self.raster_scroll[i].img_bank,
                          self.raster_scroll[i].posu,self.raster_scroll[i].posv,
                          self.raster_scroll[i].width,self.raster_scroll[i].height,
                          self.raster_scroll[i].transparent_color)
                
                     #更にその右横に同じラインを描画
                     pyxel.blt(self.raster_scroll[i].posx + self.raster_scroll[i].offset_x + self.raster_scroll[i].width * 2,self.raster_scroll[i].posy,
                          self.raster_scroll[i].img_bank,
                          self.raster_scroll[i].posu,self.raster_scroll[i].posv,
                          self.raster_scroll[i].width,self.raster_scroll[i].height,
                          self.raster_scroll[i].transparent_color)
                     
                     pyxel.blt(self.raster_scroll[i].posx + self.raster_scroll[i].offset_x + self.raster_scroll[i].width * 3,self.raster_scroll[i].posy,
                          self.raster_scroll[i].img_bank,
                          self.raster_scroll[i].posu,self.raster_scroll[i].posv,
                          self.raster_scroll[i].width,self.raster_scroll[i].height,
                          self.raster_scroll[i].transparent_color)
                     pyxel.blt(self.raster_scroll[i].posx + self.raster_scroll[i].offset_x + self.raster_scroll[i].width * 4,self.raster_scroll[i].posy,
                          self.raster_scroll[i].img_bank,
                          self.raster_scroll[i].posu,self.raster_scroll[i].posv,
                          self.raster_scroll[i].width,self.raster_scroll[i].height,
                          self.raster_scroll[i].transparent_color)
                     #同じラインパターンを5個右横に並べれば違和感なくx座標を0にしても目立たないんじゃないかな？の精神！

     #自機弾の表示
     def draw_my_shot(self):
          shot_count = len(self.shots)
          for i in range(shot_count):
               if   0 <= self.shot_level <= 6: #ショットがバルカンショットとレーザーの場合
                    pyxel.blt(self.shots[i].posx, self.shots[i].posy,      IMG2,     (self.shots[i].shot_type * 8),8,       8,8,     1)
               elif      self.shot_level == 7: #ウェーブカッターLv1の場合
                    pyxel.blt(self.shots[i].posx, self.shots[i].posy,      IMG2,     (self.shots[i].shot_type * 8),8,       8,8,     1)
                    pyxel.blt(self.shots[i].posx, self.shots[i].posy + 8,  IMG2,     (self.shots[i].shot_type * 8),8,       8,8,     1)
               elif      self.shot_level == 8: #ウェーブカッターLv2の場合
                    pyxel.blt(self.shots[i].posx, self.shots[i].posy,      IMG2,     (self.shots[i].shot_type * 8),8,       8, 8,    1)
                    pyxel.blt(self.shots[i].posx, self.shots[i].posy + 8 , IMG2,     (self.shots[i].shot_type * 8),16,      8, 8,    1)
                    pyxel.blt(self.shots[i].posx, self.shots[i].posy + 16, IMG2,     (self.shots[i].shot_type * 8),8,       8,-8,    1)
               elif 9 <= self.shot_level <= 10:#ウェーブカッターLv3とLv4の場合
                    pyxel.blt(self.shots[i].posx, self.shots[i].posy,      IMG2,     (self.shots[i].shot_type * 8),8,       8, 8,    1)
                    pyxel.blt(self.shots[i].posx, self.shots[i].posy + 8 , IMG2,     (self.shots[i].shot_type * 8),16,      8, 8,    1)
                    pyxel.blt(self.shots[i].posx, self.shots[i].posy + 16, IMG2,     (self.shots[i].shot_type * 8),16,      8,-8,    1)
                    pyxel.blt(self.shots[i].posx, self.shots[i].posy + 24, IMG2,     (self.shots[i].shot_type * 8),8,       8,-8,    1)

     #ミサイルの表示
     def draw_missile(self):
          missile_count = len(self.missile)
          for i in range(missile_count):
              if 0 <= self.missile[i].missile_type <= 3:#通常ミサイル（地を這うミサイル）の表示
                  pyxel.blt(self.missile[i].posx, self.missile[i].posy, IMG2,   (self.missile[i].missile_flag1 * 8),16,    self.missile[i].x_reverse * 8,self.missile[i].y_reverse * 8,  0)
              elif self.missile[i].missile_type == 4:#テイルショットの表示
                  pyxel.blt(self.missile[i].posx, self.missile[i].posy, IMG2,   24,16,    8,8,  1)
              elif self.missile[i].missile_type == 5:#ペネトレートロケットの表示
                  pyxel.blt(self.missile[i].posx, self.missile[i].posy, IMG2,   16,16,    8,8,  1)
              elif self.missile[i].missile_type == 6:#サーチレーザーの表示
                   if   self.missile[i].missile_flag1 == 0:#状態遷移が(直進中=0)なら前方直進レーザーの画像を表示する
                        pyxel.blt(self.missile[i].posx - 8, self.missile[i].posy, IMG2,   32,16,   16,8,  13)
                   elif self.missile[i].missile_flag1 == 1:#状態遷移が(屈折中=1)なら曲がっているレーザーの画像を表示
                        pyxel.blt(self.missile[i].posx    , self.missile[i].posy, IMG2,   48,16,   8,8  * -(self.missile[i].y_reverse),  13)
                   elif self.missile[i].missile_flag1 == 2:#状態遷移が(縦に進行中=2)なら上方向＆下方向のレーザーの画像を表示
                        pyxel.blt(self.missile[i].posx    , self.missile[i].posy + (self.missile[i].y_reverse) * 8, IMG2,   88,8,    8,16 * -(self.missile[i].y_reverse),  13)
              elif self.missile[i].missile_type == 7:#ホーミングミサイルの表示
                  pyxel.blt(self.missile[i].posx, self.missile[i].posy, IMG2,   56,16,    8,8,  13)

     #クローの表示
     def draw_claw(self):
          claw_count = len(self.claw)
          for i in range(claw_count):
              pyxel.blt(self.claw[i].posx, self.claw[i].posy,      IMG2,     184 + (((self.stage_count // 2.5 ) % 9) * 8),96,       8,8,     0)
              #pyxel.blt(self.claw[i].posx, self.claw[i].posy,      IMG2,     144 + (((self.stage_count // 2.5 ) % 14) * 8),8,       8,8,     0)
          
     #クローショットの表示
     def draw_claw_shot(self):
          claw_shot_count = len(self.claw_shot)
          for i in range(claw_shot_count):
               pyxel.blt(self.claw_shot[i].posx, self.claw_shot[i].posy, IMG2,   240,0,    8,8,  1)
     
     #自機表示
     def draw_my_ship(self):
          if self.invincible_counter > 0: #無敵中のカウントが0より大きい時は無敵状態なので点滅表示する
              if pyxel.frame_count % 4 == 0: #4フレーム置きに自機を表示
                  pyxel.blt(self.my_x   ,self.my_y,IMG2,8 + ((self.my_rolling_flag) * 8),0,SHIP_W,SHIP_H,0) #自機本体の表示
              
              self.invincible_counter -= 1 #無敵時間カウントを1減らす

          else:
              pyxel.blt(self.my_x   ,self.my_y,IMG2,8 + ((self.my_rolling_flag) * 8),0,SHIP_W,SHIP_H,0) #自機本体の表示
          
          
          if self.game_status == SCENE_STAGE_CLEAR_MY_SHIP_BOOST:
               pyxel.blt(self.my_x -6*8,self.my_y,IMG2,    208,120 + (pyxel.frame_count // 2  % 2) * 8,    6*8,8,0) #ブーストモードイオンエンジン噴射の描画
          else:
               pyxel.blt(self.my_x   -8,self.my_y,IMG2,    176 + (pyxel.frame_count // 2  % 3) * 8,104,      8,8,0) #イオンエンジン噴射の描画
    
     #パワーアップアイテム類の表示
     def draw_obtain_item(self):
          obtain_item_count = len(self.obtain_item)
          for i in reversed(range(obtain_item_count)):
               if    self.obtain_item[i].item_type == ITEM_SHOT_POWER_UP:      #ショットパワーアップカプセル（赤）の表示
                    pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy,IMG2, pyxel.frame_count // 8  % 8 * 8      ,224,    8,8,0)
               elif  self.obtain_item[i].item_type == ITEM_MISSILE_POWER_UP:   #ミサイルパワーアップカプセル（緑）の表示
                    pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy,IMG2, pyxel.frame_count // 8  % 8 * 8 + 64 ,224,    8,8,0)
               elif  self.obtain_item[i].item_type == ITEM_SHIELD_POWER_UP:    #シールドパワーアップカプセル（青）の表示
                    pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy,IMG2, pyxel.frame_count // 8  % 8 * 8 + 128,224,    8,8,0)
               
               elif  self.obtain_item[i].item_type == ITEM_CLAW_POWER_UP:      #クローパワーアップカプセル （黄）の表示
                    pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy,IMG2, pyxel.frame_count // 8  % 8 * 8      ,232,    8,8,0)
               
               elif  self.obtain_item[i].item_type == ITEM_TRIANGLE_POWER_UP:  #トライアングルアイテム(正三角形)ショット、ミサイル、シールドの表示
                    self.draw_obtain_item_triangle_item(i)

               elif  self.obtain_item[i].item_type == ITEM_TAIL_SHOT_POWER_UP:       #テイルショットカプセルの表示
                    pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy,IMG2,    64,232,    8,8,13)
                    self.draw_obtain_item_rotation_box(i)
               elif  self.obtain_item[i].item_type == ITEM_PENETRATE_ROCKET_POWER_UP:#ペネトレートロケットカプセルの表示
                    pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy,IMG2,    72,232,    8,8,13)
                    self.draw_obtain_item_rotation_box(i)
               elif  self.obtain_item[i].item_type == ITEM_SEARCH_LASER_POWER_UP:    #サーチレーザーカプセルの表示
                    pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy,IMG2,    80,232,    8,8,13)
                    self.draw_obtain_item_rotation_box(i)
               elif  self.obtain_item[i].item_type == ITEM_HOMING_MISSILE_POWER_UP:  #ホーミングミサイルカプセルの表示
                    pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy,IMG2,    88,232,    8,8,13)
                    self.draw_obtain_item_rotation_box(i)
               elif  self.obtain_item[i].item_type == ITEM_SHOCK_BUMPER_POWER_UP:    #ショックバンパーカプセルの表示
                    pyxel.blt(self.obtain_item[i].posx,self.obtain_item[i].posy,IMG2,    96,232,    8,8,13)
                    self.draw_obtain_item_rotation_box(i)

     #パワーアップアイテムの回転する四角形外枠の描画表示
     def draw_obtain_item_rotation_box(self,i): #iはobtain_itemクラスのインデックス値となります
         self.obtain_item[i].degree +=0.5 #0.5度回転
         self.obtain_item[i].degree = self.obtain_item[i].degree % 360#角度は３６０で割った余りとする(0~359)
         #アイテムのある座標は(x=0,y=0)となります
         #           (x1,y1)  
         #        ／    !     ＼
         #      ／      !3      ＼
         #(x2,y2)--3--ITEM--3--(x4,y4)
         #     ＼       !       ／
         #        ＼    !3    ／
         #           (x3,y3)
         x1 =   0
         y1 = - 3 - self.expansion_shrink_number[self.stage_count // 3 % 37] #expansion_shrink_numberのリストを使ってラインの点座標を大きくしたり小さくさせます
         x2 = - 3 - self.expansion_shrink_number[self.stage_count // 3 % 37]
         y2 =   0
         x3 =   0
         y3 =   3 + self.expansion_shrink_number[self.stage_count // 3 % 37]
         x4 =   3 + self.expansion_shrink_number[self.stage_count // 3 % 37]
         y4 =   0

         #現在の角度に従って点座標を回転させます
         rotx1 = x1 * math.cos(math.radians(self.obtain_item[i].degree)) - y1 * math.sin(math.radians(self.obtain_item[i].degree))
         roty1 = x1 * math.sin(math.radians(self.obtain_item[i].degree)) + y1 * math.cos(math.radians(self.obtain_item[i].degree))
         rotx2 = x2 * math.cos(math.radians(self.obtain_item[i].degree)) - y2 * math.sin(math.radians(self.obtain_item[i].degree))
         roty2 = x2 * math.sin(math.radians(self.obtain_item[i].degree)) + y2 * math.cos(math.radians(self.obtain_item[i].degree))
         rotx3 = x3 * math.cos(math.radians(self.obtain_item[i].degree)) - y3 * math.sin(math.radians(self.obtain_item[i].degree))
         roty3 = x3 * math.sin(math.radians(self.obtain_item[i].degree)) + y3 * math.cos(math.radians(self.obtain_item[i].degree))
         rotx4 = x4 * math.cos(math.radians(self.obtain_item[i].degree)) - y4 * math.sin(math.radians(self.obtain_item[i].degree))
         roty4 = x4 * math.sin(math.radians(self.obtain_item[i].degree)) + y4 * math.cos(math.radians(self.obtain_item[i].degree))
        
         #アイテムの座標を中心として回転四角形を描画する
         pyxel.line(self.obtain_item[i].posx +3 + rotx1,self.obtain_item[i].posy + 3 + roty1,self.obtain_item[i].posx + 3 + rotx2,self.obtain_item[i].posy + 3 + roty2, self.blinking_color[pyxel.frame_count // 8 % 10])
         pyxel.line(self.obtain_item[i].posx +3 + rotx2,self.obtain_item[i].posy + 3 + roty2,self.obtain_item[i].posx + 3 + rotx3,self.obtain_item[i].posy + 3 + roty3, self.blinking_color[pyxel.frame_count // 8 % 10])
         pyxel.line(self.obtain_item[i].posx +3 + rotx3,self.obtain_item[i].posy + 3 + roty3,self.obtain_item[i].posx + 3 + rotx4,self.obtain_item[i].posy + 3 + roty4, self.blinking_color[pyxel.frame_count // 8 % 10])
         pyxel.line(self.obtain_item[i].posx +3 + rotx4,self.obtain_item[i].posy + 3 + roty4,self.obtain_item[i].posx + 3 + rotx1,self.obtain_item[i].posy + 3 + roty1, self.blinking_color[pyxel.frame_count // 8 % 10])
     
     #トライアングルアイテム（ショット、ミサイル、シールド）の表示
     def draw_obtain_item_triangle_item(self,i): #iはobtain_itemクラスのインデックス値となります
         self.obtain_item[i].degree -= self.obtain_item[i].speed #SPEED分,右回転する
         self.obtain_item[i].degree = self.obtain_item[i].degree % 360#角度は３６０で割った余りとする(0~359)
         #アイテムのある座標(x=0,y=0)は中心となります
         #そしてアイテムを中心に半径(radius)から等角度120度ごとの円の点がそれぞれ(x1,y1)(x2,y2)(x3,y3)となります
         #           (ax,ay)赤玉  
         #            ／! ＼
         #          ／  !   ＼
         #        ／   ITEM(半径radius)
         #      ／      !       ＼
         #(bx,by)緑玉-------------(cx,cy)青玉
         #
         
         #正三角形の３頂点の座標を計算する
         if self.obtain_item[i].status == 0: #状態遷移が「画面スクロールに合わせて左に流れる状態」の時は三角形は膨張収縮する
              ax = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *   math.cos(math.radians(self.obtain_item[i].degree))
              ay = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *  -math.sin(math.radians(self.obtain_item[i].degree))

              bx = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *   math.cos(math.radians(self.obtain_item[i].degree + 120))
              by = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *  -math.sin(math.radians(self.obtain_item[i].degree + 120))

              cx = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *   math.cos(math.radians(self.obtain_item[i].degree + 240))
              cy = (self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]) *  -math.sin(math.radians(self.obtain_item[i].degree + 240))
         elif 1 <= self.obtain_item[i].status <= 2: #状態遷移が「アイテム取得時の高速回転状態」から「取得アニメーション描画中」までの時は三角形はそのままで描画する
              ax = self.obtain_item[i].radius *  math.cos(math.radians(self.obtain_item[i].degree))
              ay = self.obtain_item[i].radius * -math.sin(math.radians(self.obtain_item[i].degree))

              bx = self.obtain_item[i].radius *  math.cos(math.radians(self.obtain_item[i].degree + 120))
              by = self.obtain_item[i].radius * -math.sin(math.radians(self.obtain_item[i].degree + 120))

              cx = self.obtain_item[i].radius *  math.cos(math.radians(self.obtain_item[i].degree + 240))
              cy = self.obtain_item[i].radius * -math.sin(math.radians(self.obtain_item[i].degree + 240))

         #self.point_in_triangle(self.my_x,self.my_y,ax,ay,bx,by,cx,cy) 外積を使った三角形の内外判定は上手くいかなかったのでボツに。。。。
         if self.obtain_item[i].status == 0 or self.obtain_item[i].status == 1:#「画面スクロールに合わせて左に流れる状態」「アイテム取得時の高速回転状態」の時
              d = abs(math.sqrt((self.obtain_item[i].posx - self.my_x) * (self.obtain_item[i].posx - self.my_x) + (self.obtain_item[i].posy - self.my_y) * (self.obtain_item[i].posy - self.my_y)))#dに自機からアイテムまでの距離が入る
              if d > self.obtain_item[i].radius + self.expansion_shrink_number[self.stage_count // 3 % 37]:#離れている距離数がトライアングルアイテムの回転半径より大きい場合は三角形の外なので普通のライン描画
                   pyxel.line(self.obtain_item[i].posx + ax,self.obtain_item[i].posy + ay,self.obtain_item[i].posx + bx,self.obtain_item[i].posy + by, self.blinking_color[pyxel.frame_count // 8 % 10])
                   pyxel.line(self.obtain_item[i].posx + bx,self.obtain_item[i].posy + by,self.obtain_item[i].posx + cx,self.obtain_item[i].posy + cy, self.blinking_color[pyxel.frame_count // 8 % 10])
                   pyxel.line(self.obtain_item[i].posx + cx,self.obtain_item[i].posy + cy,self.obtain_item[i].posx + ax,self.obtain_item[i].posy + ay, self.blinking_color[pyxel.frame_count // 8 % 10])
                   #ショット赤玉表示 範囲外なので玉の回転アニメーションはしない
                   pyxel.blt(self.obtain_item[i].posx + ax -4,self.obtain_item[i].posy + ay -4,IMG2,  0,224,    8,8,0)
                   #ミサイル緑玉表示
                   pyxel.blt(self.obtain_item[i].posx + bx -4,self.obtain_item[i].posy + by -4,IMG2, 64,224,    8,8,0)
                   #シールド青玉表示
                   pyxel.blt(self.obtain_item[i].posx + cx -4,self.obtain_item[i].posy + cy -4,IMG2,128,224,    8,8,0)
              else:#範囲内なので塗りつぶし三角描画
                   pyxel.tri(self.obtain_item[i].posx + ax,self.obtain_item[i].posy + ay,self.obtain_item[i].posx + bx,self.obtain_item[i].posy + by,self.obtain_item[i].posx + cx,self.obtain_item[i].posy + cy,self.blinking_color[pyxel.frame_count // 8 % 10])

                   #ショット赤玉表示 範囲内なので玉の回転アニメーションを行う
                   pyxel.blt(self.obtain_item[i].posx + ax -4,self.obtain_item[i].posy + ay -4,IMG2, pyxel.frame_count % 8 * 8      ,224,    8,8,0)
                   #ミサイル緑玉表示
                   pyxel.blt(self.obtain_item[i].posx + bx -4,self.obtain_item[i].posy + by -4,IMG2, pyxel.frame_count % 8 * 8 + 64 ,224,    8,8,0)
                   #シールド青玉表示
                   pyxel.blt(self.obtain_item[i].posx + cx -4,self.obtain_item[i].posy + cy -4,IMG2, pyxel.frame_count % 8 * 8 + 128,224,    8,8,0)
         elif self.obtain_item[i].status == 2: #「取得アニメーション中」の時
              #ショット赤消滅アニメーション
              pyxel.blt(self.obtain_item[i].posx + ax -4,self.obtain_item[i].posy + ay -4,IMG2, 184 + self.obtain_item[i].animation_number * 8,232,    8,8,0)
              #ミサイル緑消滅アニメーション
              pyxel.blt(self.obtain_item[i].posx + bx -4,self.obtain_item[i].posy + by -4,IMG2, 184 + self.obtain_item[i].animation_number * 8,232,    8,8,0)
              #シールド青消滅アニメーション
              pyxel.blt(self.obtain_item[i].posx + cx -4,self.obtain_item[i].posy + cy -4,IMG2, 184 + self.obtain_item[i].animation_number * 8,232,    8,8,0)
     
     #l'sシールド表示
     def draw_ls_shield(self):
          if self.ls_shield_hp > 0:
               pyxel.blt(self.my_x + 8,self.my_y - 8,IMG2,208 + (self.stage_count // 3) % 6 * 8,64,8,24,13)

     #サブウェポンセレクトゲージの表示（画面上部にいま所持しているサブウェポンアイコンを描画する）
     def draw_sub_weapon_select_gauge(self):
         for i in range(5):
             #論理式(sub_weapon_list[i]が0)の場合括弧の中の値がtrue=1となるので y座標は16+1*8=24となる
             pyxel.blt(60 + i * 10,0,  IMG2, 216 + i * 8,16 + (self.sub_weapon_list[i] == 0) * 8,   8,8, 13)
     
     #サブウェポンセレクトガイドボックスの表示（今選択しているサブウェポンを示す四角い矩形輪郭線）
     def draw_sub_weapon_select_guidebox(self):
          if self.select_sub_weapon_id != -1:#サブウェポンを全く所持していない状態（id=-1）以外ならガイドボックスを点滅表示させる
               pyxel.rectb(60 -1 + self.select_sub_weapon_id * 10,-1, 10,8, self.blinking_color[pyxel.frame_count // 8 % 10])
     
     #スコア表示やスピード、自機耐久力などのステータスの表示（画面上部の物）
     def draw_status(self):
          s = "{:>7}".format(self.score)
          pyxel.text(9, 1, s, 1) #点数の影部分の表示
          if self.score >= self.hi_score: #スコアがハイスコア以上なら(ハイスコア更新状態)
               pyxel.blt(0,0, IMG2, 88,72, 8,8, 0)
               pyxel.text(8, 1, s, 10) #黄色でスコア表示
          else:
               pyxel.blt(0,0, IMG2, 80,72, 8,8, 0)
               pyxel.text(8, 1, s, 7)  #違っていたら白色でスコア表示

          #自機スピード表示
          if self.my_speed == 1:
               pyxel.blt(126,-1,IMG2, 104,72, 8,8, 0)
          if self.my_speed == 1.5:
               pyxel.blt(126,-1,IMG2, 112,72, 8,8, 0)
          if self.my_speed == 1.75:
               pyxel.blt(126,-1,IMG2, 120,72, 8,8, 0)
          #pyxel.text(32, 1, "SPEED " + str(self.my_speed), 7)
          #自機シールドパワー表示
          pyxel.blt(137,0,IMG2, 72,72, 8,8, 0)
          pyxel.text(148,1,str(self.my_shield), 1)
          pyxel.text(147,1,str(self.my_shield), 7)
               
     #デバッグ用ステータスの表示
     def draw_debug_status(self):
          if self.debug_menu_status == 0: #デバッグメニュー表示ステータスが0なら表示せずリターンする
              return
          
          #星の数の表示
          pyxel.blt(143,WINDOW_H - 8, IMG2, 64,72, 8,8, 0)
          pyxel.text(153,WINDOW_H - 6,str(len(self.stars)),1)
          pyxel.text(152,WINDOW_H - 6,str(len(self.stars)),7)
          #敵ホッパータイプのバウンドフラグの表示（地面と衝突したか？）
          pyxel.blt(131,WINDOW_H - 7, IMG2, (self.enemy_bound_collision_flag * 8),80, 8,8, 0)
          #敵の数の表示
          pyxel.blt(0,WINDOW_H - 8, IMG2, 128,72, 8,8, 0)
          pyxel.text(10,WINDOW_H - 6,str(len(self.enemy)),1)
          pyxel.text(9 ,WINDOW_H - 6,str(len(self.enemy)),7)
          #敵弾数の表示
          pyxel.blt(20,WINDOW_H - 8,IMG2, 136,72, 8,8, 0)
          pyxel.text(30,WINDOW_H - 6,str(len(self.enemy_shot)),1)
          pyxel.text(29,WINDOW_H - 6,str(len(self.enemy_shot)),7)
          #スクロールカウントの表示(ＭＡＰチップ単位)
          pyxel.blt(40,WINDOW_H -8,IMG2, 96,72, 8,8, 0)
          pyxel.text(50,WINDOW_H -6,str(((self.scroll_count // 8) -256) // 2),1)
          pyxel.text(49,WINDOW_H -6,str(((self.scroll_count // 8) -256) // 2),7)

          #ステージカウントの表示(生データ)
          pyxel.text(37,1,str(self.stage_count),1)
          pyxel.text(36,1,str(self.stage_count),11)

          #ショット経験値表示
          pyxel.text(148,7,str(self.shot_exp), 1)
          pyxel.text(147,7,str(self.shot_exp), 8)
          #ミサイル経験値表示
          pyxel.text(148,13,str(self.missile_exp), 1)
          pyxel.text(147,13,str(self.missile_exp), 3)     

          #自機が存在するＭＡＰ位置のＸ、Ｙ座標の表示
          #MAPの外に存在するときは強制的にＸ座標を0にしちゃう
          self.bgy = ((self.my_y + 4 ) // 8)
          self.bgx = (((self.scroll_count // 8) -256) // 2) + self.my_x // 8
          if  0 > self.bgx:
              self.bgx = 0
          if self.bgx > 255:
              self.bgx = 0

          self.bg_chip = pyxel.tilemap(0).get(self.bgx,self.bgy)
          pyxel.text(70,WINDOW_H - 6,str(self.bgx),7)
          pyxel.text(85,WINDOW_H - 6,str(self.bgy),7)
  
          #自機に重なっているキャラチップが収納されたタイルのＸ，Ｙ座標の表示
          pyxel.text(95,WINDOW_H - 6,str(self.bg_chip // 4),6)
          pyxel.text(110,WINDOW_H - 6,str((self.bg_chip % 16) * 8),6)

          #自機に重なっているキャラチップを表示
          pyxel.blt(120,WINDOW_H - 8,IMG2, (self.bg_chip % 16) * 8,(self.bg_chip // 4), 8,8)
          
          #ミサイルタイプチェッカーのカウント数の表示 デバッグ用
          #通常ミサイルの総数
          self.count_missile_type(0,1,2,3)
          pyxel.text(WINDOW_W - 8, WINDOW_H - 14,str(self.type_check_quantity),7)
          #前方高速トマホークミサイルの総数
          self.count_missile_type(5,5,5,5)
          pyxel.text(WINDOW_W - 15,WINDOW_H - 14,str(self.type_check_quantity),3)

          #ゲームステータス（ゲームの状態）の表示
          pyxel.text(0,8,str(self.game_status),6)
          
          #イベントインデックス値の表示
          pyxel.text(10,8,str(self.event_index),10)
          #イベントデータリストの表示
          pyxel.text(20,7,str(self.event_list[self.event_index]),9)

          #編隊ＩＤと総数の表示
          pyxel.text(1,14,str(self.current_formation_id),9) #現時点での編隊ID
          #編隊群リストの長さの表示
          pyxel.text(1,20,str(len(self.enemy_formation)),14) #現時点での編隊ID
          
          #編隊IDリストの表示(5リストまでの暫定表示です)
          if len(self.enemy_formation) >= 1:
               pyxel.text(14,14,str(self.enemy_formation[0].formation_id),7)
               pyxel.text(22,14,str(self.enemy_formation[0].formation_number),4)
               pyxel.text(30,14,str(self.enemy_formation[0].on_screen_formation_number),8)
               pyxel.text(38,14,str(self.enemy_formation[0].shoot_down_number),8)    
          if  len(self.enemy_formation) >= 2:
               pyxel.text(14,20,str(self.enemy_formation[1].formation_id),7)
               pyxel.text(22,20,str(self.enemy_formation[1].formation_number),4)
               pyxel.text(30,20,str(self.enemy_formation[1].on_screen_formation_number),8)
               pyxel.text(38,20,str(self.enemy_formation[1].shoot_down_number),8)
          if  len(self.enemy_formation) >= 3:
               pyxel.text(14,26,str(self.enemy_formation[2].formation_id),7)
               pyxel.text(22,26,str(self.enemy_formation[2].formation_number),4)
               pyxel.text(30,26,str(self.enemy_formation[2].on_screen_formation_number),8)
               pyxel.text(38,26,str(self.enemy_formation[2].shoot_down_number),8)
          if  len(self.enemy_formation) >= 4:
               pyxel.text(14,32,str(self.enemy_formation[3].formation_id),7)
               pyxel.text(22,32,str(self.enemy_formation[3].formation_number),4)
               pyxel.text(30,32,str(self.enemy_formation[3].on_screen_formation_number),8)
               pyxel.text(38,32,str(self.enemy_formation[3].shoot_down_number),8)
          if  len(self.enemy_formation) >= 5:
               pyxel.text(14,38,str(self.enemy_formation[4].formation_id),7)
               pyxel.text(22,38,str(self.enemy_formation[4].formation_number),4)
               pyxel.text(30,38,str(self.enemy_formation[4].on_screen_formation_number),8)
               pyxel.text(38,38,str(self.enemy_formation[4].shoot_down_number),8)
          #早回しフラグの表示
          pyxel.text(160-8*3+4,19,"ADD " + str(self.add_appear_flag), 10)
          #早回し条件が成立するまでの必要殲滅編隊数の表示
          pyxel.text(160-8*3+4,25,"NUM " + str(self.fast_forward_destruction_num), 9)

          #プレイ時間の表示(分)
          pyxel.text(160-8*3,31,"   :", 10)
          minutes = "{:>3}".format(self.one_game_playtime_seconds // 60)
          seconds = "{:0>2}".format(self.one_game_playtime_seconds % 60)
          pyxel.text(160-8*3,31,minutes, 10)
          pyxel.text(160-8  ,31,seconds, 10)

          pyxel.text(160-8*3,37,"   :", 13)
          total_minutes = "{:>3}".format(self.total_game_playtime_seconds // 60)
          total_seconds = "{:0>2}".format(self.total_game_playtime_seconds % 60)
          pyxel.text(160-8*3,37,total_minutes, 13)
          pyxel.text(160-8  ,37,total_seconds, 13)

          #ステージ数の表示
          pyxel.text(160-8*3+8,43,"ST " + str(self.stage_number), 9)
          #周回数の表示
          pyxel.text(160-8*3+8,49,"LP " + str(self.stage_loop), 7)

          #ワールドマップＢＧのxy座標の表示
          world_x = "{:>3}".format(int(self.scroll_count          // 8 % 256))
          pyxel.text(160-16,55,"X",8)
          pyxel.text(160-12,55,world_x,7)
          world_y = "{:>3}".format(int(self.vertical_scroll_count // 8 % 256))
          pyxel.text(160-16,61,"Y",8)
          pyxel.text(160-12,61,world_y,7)

          #背景山のx座標
          mou_x = "{:>3}".format(int(self.mountain_x))
          pyxel.text(160-20,67,"mX",8)
          pyxel.text(160-12,67,mou_x,10)
          
          #1番目のクローの座標の表示
          if self.claw_number >= 1:
               pyxel.text(0,WINDOW_H - 13,str(self.claw[0].posx),6)
               pyxel.text(0,WINDOW_H - 20,str(self.claw[0].posy),6)
          #2番目のクローの座標の表示
          if self.claw_number >= 2:
               pyxel.text(72,WINDOW_H - 13,str(self.claw[1].posx),5)
               pyxel.text(72,WINDOW_H - 20,str(self.claw[1].posy),5)
          
     #BGチップデータ書き換えアニメーション実装のために作ったダミーテスト関数 画面左から2列目の縦1列を取得し、そのＢＧデータを画面左端1列目に表示する
     def draw_dummy_put_bg_xy(self):
          if self.scroll_type == SCROLL_TYPE_8FREEWAY_SCROLL_AND_RASTER: #全方向フリースクロール＋ラスタースクロールの場合
               for h in range(15): #縦は15キャラ分 8ドット*15キャラ=120ドット
                    self.get_bg_chip_free_scroll(8,h * 8,0)#画面左端＋１のマップチップのBGの数値を取得する
                    bg_num = "{:>3}".format(self.bg_chip)
                    pyxel.text(16,h * 8,bg_num,7)

                    pyxel.text(30,h * 8,str(self.bgx), 8)
                    pyxel.text(46,h * 8,str(self.bgy), 8)

                    pyxel.text(60,h * 8,str((self.bg_chip  % 32) * 8), 9)
                    pyxel.text(75,h * 8,str((self.bg_chip // 32) * 8), 9)

                    pyxel.blt(0,h * 8, 1,    (self.bg_chip  % 32) * 8,(self.bg_chip // 32) * 8, 8,8, 0)#画面左端＋１にBGマップチップを描画する

     #WARNING警告ダイアログの表示(ボス出現)
     def draw_warning_dialog(self):
          if self.warning_dialog_display_time <= 0: #WARNING表示時間が0以下だったらリターンする
               return
          
          for i in range(8*8):
               pyxel.blt(48+i,48+(self.warning_dialog_logo_time // 2) + i // 64 + self.warning_dialog_logo_time * i,     IMG2,      64+i,120,                          1,8 -(self.warning_dialog_logo_time // 2) - i // 68,   0)
          
          warning_mes1 = "Unidentified flying object approaching"
          warning_mes2 = "Destroy if necessary!"
          lenstr1 = len(warning_mes1)
          lenstr2 = len(warning_mes2)
          
          pyxel.text(4 +  self.warning_dialog_text_time // 1,59,     warning_mes1[0:lenstr1 - int(self.warning_dialog_text_time //2.5)],7)
          pyxel.text(40 + self.warning_dialog_text_time // 1,66,     warning_mes2[0:lenstr2 - int(self.warning_dialog_text_time //2.5)],7)

          self.warning_dialog_display_time -= 1   #WARNING表示時間を1減らす       
          
          if self.warning_dialog_logo_time > 0:   #ロゴ表示に掛ける時間が0より大きいのなら
               self.warning_dialog_logo_time -= 1 #WARNINGグラフイックロゴ表示に掛ける時間を1減らす
          
          if self.warning_dialog_text_time > 0:   #テキスト表示に掛ける時間が0より大きいのなら
               self.warning_dialog_text_time -= 1 #WARNINGテキスト表示に掛ける時間を1減らす
          
     #STAGE CLEARダイアログの表示(ステージクリア！)
     def draw_stage_clear_dialog(self):
          if self.stage_clear_dialog_display_time <= 0: #STAGE CLEAR表示時間が0以下だったらリターンする
               return
          
          #画像「STAGE」の表示
          for i in range(8):
               pyxel.blt(40     + self.stage_clear_dialog_logo_time1 / 16 * i,48 + i,      IMG2,     128,    120 +i,   8,1,   0)
          for i in range(8):
               pyxel.blt(40 + 8 + self.stage_clear_dialog_logo_time1 / 8  * i,48 + i,      IMG2,     128 + 8,120 +i,   8,1,   0)
          for i in range(8):
               pyxel.blt(40 +16 + self.stage_clear_dialog_logo_time1 / 4  * i,48 + i,      IMG2,     128 +16,120 +i,   8,1,   0)
          for i in range(8):
               pyxel.blt(40 +24 + self.stage_clear_dialog_logo_time1 / 2  * i,48 + i,      IMG2,     128 +24,120 +i,   8,1,   0)
          for i in range(8):
               pyxel.blt(40 +32 + self.stage_clear_dialog_logo_time1      * i,48 + i,      IMG2,     128 +32,120 +i,   8,1,   0)
          
          if self.stage_clear_dialog_logo_time1 > 0:   #ロゴ表示時間その1が0より大きいのなら
               self.stage_clear_dialog_logo_time1 -= 1 #1減らす

          #画像「CLEAR」の表示
          if self.stage_clear_dialog_logo_time1 <= 0:   #ロゴ表示時間その1の数値が0以下の場合は画像「STAGE」は表示し終わったので「CLEAR」を表示開始する
               for i in range(8):
                    pyxel.blt(40 +40 + self.stage_clear_dialog_logo_time2 / 16 * i,48 + i,      IMG2,     128 +40,120 +i,   8,1,   0)
               for i in range(8):
                    pyxel.blt(40 +48 + self.stage_clear_dialog_logo_time2 / 8  * i,48 + i,      IMG2,     128 +48,120 +i,   8,1,   0)
               for i in range(8):
                    pyxel.blt(40 +56 + self.stage_clear_dialog_logo_time2 / 4  * i,48 + i,      IMG2,     128 +56,120 +i,   8,1,   0)
               for i in range(8):
                    pyxel.blt(40 +64 + self.stage_clear_dialog_logo_time2 / 2  * i,48 + i,      IMG2,     128 +64,120 +i,   8,1,   0)
               for i in range(8):
                    pyxel.blt(40 +72 + self.stage_clear_dialog_logo_time2      * i,48 + i,      IMG2,     128 +72,120 +i,   8,1,   0)
               
               if self.stage_clear_dialog_logo_time2 > 0:   #ロゴ表示時間その2が0より大きいのなら
                    self.stage_clear_dialog_logo_time2 -= 1 #1減らす
          #任務完了！速やかに次のステージへ移動せよ
          #
          #う～～～～ん・・・イマイチ文字列操作の仕方がよくわからない・・適当な数値補正入れて現状は上手く見せてるだけだけど
          stage_clear_mes1 = "MISSION COMPLETE!!"
          stage_clear_mes2 = "Move quickly to the next stage!!"
          lenstr1 = len(stage_clear_mes1)
          lenstr2 = len(stage_clear_mes2)
          
          if self.stage_clear_dialog_logo_time2 == 0:   #ロゴ表示時間その2が0なら「STAGE CLEAR」の表示は終わったのでメッセージの表示を始める
               pyxel.text(46,59,     stage_clear_mes1[0:- int(self.stage_clear_dialog_text_time / self.stage_clear_dialog_text_time_master * lenstr1) - 1],7)
               pyxel.text(20,66,     stage_clear_mes2[0:- int(self.stage_clear_dialog_text_time / self.stage_clear_dialog_text_time_master * lenstr2) - 1],7)

               self.stage_clear_dialog_display_time -= 1     #STAGE CLEAR表示時間を1減らす
               if self.stage_clear_dialog_display_time == 0: #STAGE CLEAR表示時間が0になったら
                    self.game_status = SCENE_STAGE_CLEAR_FADE_OUT #ゲームステータスを「ステージクリア後のフェードアウト」にする
          
               if self.stage_clear_dialog_text_time > 0:   #テキスト表示に掛ける時間が0より大きいのなら
                    self.stage_clear_dialog_text_time -= 1 #STAGE CLEARテキスト表示に掛ける時間を1減らす
    
     #一時停止・ポーズメッセージの表示
     def draw_pause_message(self):
          pyxel.text(80-8, 52, "PAUSE", 7)
          self.star_scroll_speed -= 0.01 #ポーズをかけると星のスクロールスピードの倍率を毎フレームごと0.01減らしていく
          if self.star_scroll_speed < 0:
               self.star_scroll_speed = 0 #0以下になったら強制的に0を代入
          #a=randint(0,100)
          #if a == 0:
          pyxel.text(0, 62, "The space-time interference system still",7)
          pyxel.text(0, 70, "  seems to take a long time to work on",7)
          pyxel.text(0, 78, "     a much more distant object.", 7)
          #時空干渉システムはやはりはるか遠くの天体に作用するのに時間が掛るようだ
     
     #ウィンドウの表示
     def draw_window(self):
         window_count = len(self.window)
         for i in range(window_count):
             #ウィンドウ下地描画###############################################################
             for h in range(self.window[i].height // 8 + 1):
                 for w in range((self.window[i].width // 8 + 1)) :
                     pyxel.blt(self.window[i].posx + w * 8,self.window[i].posy + h * 8,               
                                IMG2,
                                96 + self.window[i].window_type * 32,88,
                                8,8, 13)

             #ウィンドウ横パーツ描画#############################################################
             for w in range(self.window[i].width // 8 + 1):
                 #上部の横パーツ描画
                 pyxel.blt(self.window[i].posx + w * 8,self.window[i].posy,                               
                           IMG2,
                           96 + self.window[i].window_type * 32,80,
                           8,8, 13)
                 #下部の横パーツ描画
                 pyxel.blt(self.window[i].posx + w * 8,self.window[i].posy + self.window[i].height,
                           IMG2,
                           96 + self.window[i].window_type * 32,96,
                           8,8, 13)
             #ウィンドウ縦パーツ描画####################################################
             for h in range(self.window[i].height // 8 + 1):
                 #左の縦パーツ描画
                 pyxel.blt(self.window[i].posx                           ,self.window[i].posy + h * 8,
                           IMG2,
                          80 + self.window[i].window_type * 32,88,
                           8,8, 13)
                 #右の縦パーツ描画
                 pyxel.blt(self.window[i].posx + self.window[i].width,self.window[i].posy + h * 8,
                           IMG2,
                           104 + self.window[i].window_type * 32,88,
                           8,8, 13)
             
             #################ウィンドウ四隅の角の描画#####################################
             #左上のウィンドウパーツの描画
             pyxel.blt(self.window[i].posx                           ,self.window[i].posy                             ,
                       IMG2,
                       80  + self.window[i].window_type * 32,80,
                       8,8,  13)
             #右上のウィンドウパーツの描画
             pyxel.blt(self.window[i].posx + self.window[i].width,self.window[i].posy                             ,
                       IMG2,
                       104 + self.window[i].window_type * 32,80,
                       8,8,  13)
             #左下のウィンドウパーツの描画
             pyxel.blt(self.window[i].posx                           ,self.window[i].posy + self.window[i].height ,
                       IMG2,
                       80  + self.window[i].window_type * 32,96,
                       8,8,  13)
             #左下のウィンドウパーツの描画
             pyxel.blt(self.window[i].posx + self.window[i].width ,self.window[i].posy + self.window[i].height  ,
                       IMG2,
                       104 + self.window[i].window_type * 32,96,
                       8,8,  13)
             
             #タイトルバーの表示######################################
             pyxel.text(self.window[i].posx + 6 + self.window[i].width // 2 - len(self.window[i].window_title) * 2,self.window[i].posy + 5,str(self.window[i].window_title),0)
             pyxel.text(self.window[i].posx + 6 + self.window[i].width // 2 - len(self.window[i].window_title) * 2,self.window[i].posy + 6,str(self.window[i].window_title),0)
             
             
             pyxel.text(self.window[i].posx + 5 + self.window[i].width // 2 - len(self.window[i].window_title) * 2,self.window[i].posy + 5,str(self.window[i].window_title),7)

             if self.window[i].window_status == WINDOW_OPEN: #ステータスがウィンドウ開き中ならば
                  if self.window[i].width < self.window[i].open_width:#widthをopen_widthの数値になるまで増加させていく
                       self.window[i].width += int(self.window[i].vx * self.window[i].open_speed)
                  
                  if self.window[i].height < self.window[i].open_height:#heightをopen_heightの数値になるまで増加させていく
                       self.window[i].height += int(self.window[i].vy * self.window[i].open_speed)
                  
                  #ウィンドウが開ききったのか判断する
                  if   -2 <= self.window[i].open_width  - self.window[i].width  <= 2 and\
                       -2 <= self.window[i].open_height - self.window[i].height <= 2:#もしwidthとheightの値がopenした時の数値と+-2以内になったのなら
                       self.window[i].window_status = WINDOW_WRITE_MESSAGE#ウィンドウは完全に開ききったとみなしてステータスをWINDOW_WRITE_MESSAGEにしてメッセージを表示開始する

                       self.window[i].width  = self.window[i].open_width #小数点以下の座標の誤差を修正するために強制的にopen時の座標数値を現在座標数値に代入してやる
                       self.window[i].height = self.window[i].open_height
               
             if      self.window[i].window_status == WINDOW_WRITE_MESSAGE \
                  or self.window[i].window_status == WINDOW_OPEN_COMPLETED: #ステータスがテキストメッセージの表示中もしくはオープン完了ならば
                  if self.window[i].mes1 != "":#メッセージ1行目の描画 ループで処理したいけどどうやったら良いのかわからぬ・・・クラスの横方向（？）に補正値を入れるのどうやったらいいのん？？？
                       pyxel.text(self.window[i].posx + self.window[i].mes1_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes1) * 2,self.window[i].posy + 5 +8 ,str(self.window[i].mes1),0)
                       pyxel.text(self.window[i].posx + self.window[i].mes1_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes1) * 2,self.window[i].posy + 6 +8 ,str(self.window[i].mes1),0)
             
                       pyxel.text(self.window[i].posx + self.window[i].mes1_ox + 5 + self.window[i].width // 2 - len(self.window[i].mes1) * 2,self.window[i].posy + 5 +8 ,str(self.window[i].mes1),self.window[i].mes1_color)
                  
                  if self.window[i].mes2 != "":#メッセージ2行目の描画
                       pyxel.text(self.window[i].posx + self.window[i].mes2_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes2) * 2,self.window[i].posy + 5 +16,str(self.window[i].mes2),0)
                       pyxel.text(self.window[i].posx + self.window[i].mes2_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes2) * 2,self.window[i].posy + 6 +16,str(self.window[i].mes2),0)
             
                       pyxel.text(self.window[i].posx + self.window[i].mes2_ox + 5 + self.window[i].width // 2 - len(self.window[i].mes2) * 2,self.window[i].posy + 5 +16,str(self.window[i].mes2),self.window[i].mes2_color)
                  
                  if self.window[i].mes3 != "":#メッセージ3行目の描画
                       pyxel.text(self.window[i].posx + self.window[i].mes3_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes3) * 2,self.window[i].posy + 5 +24,str(self.window[i].mes3),0)
                       pyxel.text(self.window[i].posx + self.window[i].mes3_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes3) * 2,self.window[i].posy + 6 +24,str(self.window[i].mes3),0)
             
                       pyxel.text(self.window[i].posx + self.window[i].mes3_ox + 5 + self.window[i].width // 2 - len(self.window[i].mes3) * 2,self.window[i].posy + 5 +24,str(self.window[i].mes3),self.window[i].mes3_color)
                  
                  if self.window[i].mes4 != "":#メッセージ4行目の描画
                       pyxel.text(self.window[i].posx + self.window[i].mes4_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes4) * 2,self.window[i].posy + 5 +32,str(self.window[i].mes4),0)
                       pyxel.text(self.window[i].posx + self.window[i].mes4_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes4) * 2,self.window[i].posy + 6 +32,str(self.window[i].mes4),0)
             
                       pyxel.text(self.window[i].posx + self.window[i].mes4_ox + 5 + self.window[i].width // 2 - len(self.window[i].mes4) * 2,self.window[i].posy + 5 +32,str(self.window[i].mes4),self.window[i].mes4_color)
                  
                  if self.window[i].mes5 != "":#メッセージ5行目の描画
                       pyxel.text(self.window[i].posx + self.window[i].mes5_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes5) * 2,self.window[i].posy + 5 +40,str(self.window[i].mes5),0)
                       pyxel.text(self.window[i].posx + self.window[i].mes5_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes5) * 2,self.window[i].posy + 6 +40,str(self.window[i].mes5),0)
             
                       pyxel.text(self.window[i].posx + self.window[i].mes5_ox + 5 + self.window[i].width // 2 - len(self.window[i].mes5) * 2,self.window[i].posy + 5 +40,str(self.window[i].mes5),self.window[i].mes5_color)
                  
                  if self.window[i].mes6 != "":#メッセージ6行目の描画
                       pyxel.text(self.window[i].posx + self.window[i].mes6_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes6) * 2,self.window[i].posy + 5 +48,str(self.window[i].mes6),0)
                       pyxel.text(self.window[i].posx + self.window[i].mes6_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes6) * 2,self.window[i].posy + 6 +48,str(self.window[i].mes6),0)
             
                       pyxel.text(self.window[i].posx + self.window[i].mes6_ox + 5 + self.window[i].width // 2 - len(self.window[i].mes6) * 2,self.window[i].posy + 5 +48,str(self.window[i].mes6),self.window[i].mes6_color)
                  
                  if self.window[i].mes7 != "":#メッセージ7行目の描画
                       pyxel.text(self.window[i].posx + self.window[i].mes7_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes7) * 2,self.window[i].posy + 5 +56,str(self.window[i].mes7),0)
                       pyxel.text(self.window[i].posx + self.window[i].mes7_ox + 6 + self.window[i].width // 2 - len(self.window[i].mes7) * 2,self.window[i].posy + 6 +56,str(self.window[i].mes7),0)
             
                       pyxel.text(self.window[i].posx + self.window[i].mes7_ox + 5 + self.window[i].width // 2 - len(self.window[i].mes7) * 2,self.window[i].posy + 5 +56,str(self.window[i].mes7),self.window[i].mes7_color)
                  
                  
                  self.window[i].window_status == WINDOW_OPEN_COMPLETED #ウィンドウオープン完了！

     #セレクトカーソルの表示
     def draw_select_cursor(self):
          if self.cursor_show == True: #セレクトカーソルを表示するかどうかのフラグが建っていたらカーソルを表示する
               pyxel.blt(self.cursor_x, self.cursor_y,      IMG2,     184 + (((pyxel.frame_count // 2.5 ) % 9) * 8),96,       8,8,     0)

     #ゲームオーバーダイアログを表示する
     def draw_gameover_dialog(self):
          pyxel.blt(47, 48, IMG2, 0,72, 64,8, 0)
     
     #フェードイン＆フェードアウト用のエフェクトスクリーン用描画関数
     def draw_fade_in_out_screen(self,fade_in_out_flag,chip_type):
          for lx in range(self.fade_in_out_counter):
               for ly in range(15): #y軸は15キャラ分なので15回繰り返す
                    pyxel.blt(self.fade_in_out_counter // 8 * 8  - lx*8 -8,ly*8,   IMG2,   self.fade_in_out_counter // 8 * 4,248,   8,8,   13)

          if self.fade_in_out_counter >= 160 * 3 + 24:
                   self.fade_complete_flag = 1 #右端まで描画したら完了フラグを立てる
          else:
               self.fade_in_out_counter += 3 #開始Ｘ軸（キャラ単位）を1増やして隣の列に移る

          return()

     #シャドウイン用のエフェクトスクリーン用描画関数
     def draw_shadow_in_screen(self,shadow_width,col):
          for lx in range(self.shadow_in_out_counter):
               pyxel.rect(0,          0,             lx,WINDOW_H,     col)#左側の長方形描画
               pyxel.rect(WINDOW_W-lx,0,             lx,WINDOW_H,     col)#右側の長方形描画
               
               


          if self.shadow_in_out_counter == (WINDOW_W - shadow_width) // 2:
                   self.shadow_in_out_complete_flag = 1 #右端まで描画したら完了フラグを立てる
          else:
               if (pyxel.frame_count % 2) == 0:
                    self.shadow_in_out_counter += 1 #カウンタを1増やす

          return()

     #シャドウアウト用のエフェクトスクリーン用描画関数
     def draw_shadow_out_screen(self,shadow_width,col):
          pyxel.rect(              - self.shadow_in_out_counter,0,             WINDOW_W // 2,WINDOW_H,     col)#左側の長方形描画
          pyxel.rect(WINDOW_W // 2 + self.shadow_in_out_counter,0,             WINDOW_W // 2,WINDOW_H,     col)#右側の長方形描画
               
               


          if self.shadow_in_out_counter == shadow_width:
                   self.shadow_in_out_complete_flag = 1 #右端まで描画したら完了フラグを立てる
          else:
               if (pyxel.frame_count % 2) == 0:
                    self.shadow_in_out_counter += 1 #カウンタを1増やす

          return()
     
     #######################################################################
     #######################################################################
     #######################################################################
     #      ゲームで扱う情報を更新したり、キー入力（コントロ―ラー入力）を行う    # 
     #                    あっぷで～～と☆彡    KANSUU                       #
     #######################################################################
     #######################################################################
     #            ウィンドウズアップデートはあってはならない文明               #
     #                           滅ぶべし・・・                             #
     #######################################################################
     #パイソンはどうして関数を呼び出すだけなのにselfを付けないといけないのか     #
     #謎である                                                              # 
     #######################################################################
     def update(self):
          ################################起動処理中 IPL ###################################################################
          if self.game_status == SCENE_IPL:             #ゲームステータスが「SCENE_IPL」の場合IPLメッセージの更新を行う
               self.update_ipl()                        #IPLの更新
          ################################ タイトル関連の変数を初期化 ###################################################################
          if self.game_status == SCENE_TITLE_INIT:      #ゲームステータスが「SCENE_TITLE_INIT」の場合タイトル関連の変数を初期化する関数を呼び出す
               self.update_title_init()                 #タイトル関連の変数の初期化関数を呼び出す
          ################################ タイトル ###################################################################
          if self.game_status == SCENE_TITLE:           #ゲームステータスが「SCENE_TITLE」の場合タイトルの更新を行う
               self.update_title()                      #タイトルの更新
               self.update_append_star()                #背景の星の追加＆発生育成関数呼び出し
               self.update_star()                       #背景の星の更新（移動）関数呼び出し
          ################################ タイトルでメニュー選択中 ###################################################################
          if self.game_status == SCENE_TITLE_MENU_SELECT:
               self.update_title_menu_select()          #タイトルでのメニュー選択処理をする関数の呼び出し
               self.update_append_star()                #背景の星の追加＆発生育成関数呼び出し
               self.update_star()                       #背景の星の更新（移動）関数呼び出し
               self.update_select_cursor()              #セレクトカーソルでメニューを選択する関数を呼び出す

          ################################ ゲームスタート時の初期化 #################################################################
          if self.game_status == SCENE_GAME_START_INIT: #ゲームステータスが「GAME_START_INIT」の場合（ゲームスタート時の状態遷移）は以下を実行する
              self.update_game_start_init()             #ゲーム開始前の初期化    スコアやシールド値、ショットレベルやミサイルレベルなどの初期化
              self.game_status = SCENE_STAGE_START_INIT #ゲームステータスを「STAGE_START_INIT」にする
          ################################ステージスタート時の初期化 #################################################################
          if self.game_status == SCENE_STAGE_START_INIT: #ゲームステータスが「GAME_START_INIT」の場合（ゲームスタート時の状態遷移）は以下を実行する
              self.update_stage_start_init()             #ステージ開始前の初期化   自機の座標や各リストの初期化、カウンター類の初期化
              self.game_status = SCENE_PLAY              #ゲームステータスを「STAGE_START_INIT」にする
          ################################ ゲームプレイ中！！！！！！ ###############################################################
          if       self.game_status == SCENE_PLAY\
                or self.game_status == SCENE_EXPLOSION\
                or self.game_status == SCENE_STAGE_CLEAR\
                or self.game_status == SCENE_GAME_OVER\
                or self.game_status == SCENE_BOSS_APPEAR\
                or self.game_status == SCENE_BOSS_BATTLE\
                or self.game_status == SCENE_BOSS_EXPLOSION\
                or self.game_status == SCENE_STAGE_CLEAR\
                or self.game_status == SCENE_STAGE_CLEAR_MOVE_MY_SHIP\
                or self.game_status == SCENE_STAGE_CLEAR_MY_SHIP_BOOST\
                or self.game_status == SCENE_STAGE_CLEAR_FADE_OUT:
               #自機関連の処理######################################################################################
               # ##################################################################################################
               self.update_my_ship()                    #自機の更新処理（移動処理）関数を呼び出す
               self.update_my_ship_record_coordinate()  #自機の座標を過去履歴リストに書き込んでいく関数（トレースクローの座標として使用します）を呼び出す
               self.update_clip_my_ship()               #自機をはみ出さないようにする関数を呼び出す
               #パワーアップ関連の処理################################################
               self.update_powerup_shot()               #ショットのパワーアップ処理関数を呼び出し
               self.update_powerup_missile()            #ミサイルのパワーアップ処理関数の呼び出し
               self.update_change_speed()               #自機スピードのチェンジ処理関数呼び出し
               #自機ショット関連の処理#################################################
               self.update_my_shot()                    #自機弾の更新関数を呼び出す
               self.update_clip_my_shot()               #自機弾をはみ出さないようにする関数を呼び出す
               self.update_collision_my_shot_bg()       #自機弾と背景との当たり判定を行う関数を呼び出す
               self.update_collision_my_shot_enemy()    #自機弾と敵の当たり判定
               self.update_collision_my_shot_boss()     #自機弾とボスの当たり判定
               #ミサイル関連の処理###################################################################
               self.update_my_missile()                 #自機ミサイルの更新（移動処理）関数を呼び出す
               self.update_clip_my_missile()            #自機ミサイルをはみ出さないようにする関数を呼び出す
               self.update_collision_missile_enemy()    #自機ミサイルと敵との当たり判定を行う関数の呼び出す
               #クロー関連の処理 ####################################################################
               self.update_claw()                       #クローの更新（移動処理）関数を呼び出す
               self.update_claw_shot()                  #クローの弾の更新（移動処理）を呼び出す
               self.update_collision_claw_shot_enemy()  #クローの弾と敵との当たり判定関数を呼び出す
               self.update_collision_claw_shot_bg()     #クローの弾と背景との当たり判定関数を呼び出す

               #敵の弾関連の処理 ###################################################################################
               ####################################################################################################
               self.update_enemy_shot()                 #敵の弾の更新（移動処理とか）＆自機と敵弾と自機との当たり判定の関数の呼び出し
               self.update_clip_enemy_shot()            #敵の弾が画面からはみ出したら消去する関数の呼び出し
               self.update_collision_enemy_shot_bg()    #敵の弾と背景との当たり判定を行う関数の呼び出し
          
               #クロー関連の処理###########################################################################################################
               self.update_delete_claw()                #クローの消滅関数の呼び出し
               self.update_change_fix_claw_interval()   #フイックスクローの間隔を変化させる関数を呼び出す
               self.update_change_claw_style()          #クロースタイルを変更する関数を呼び出す     

               #敵関連の処理###############################################################################################################
               self.update_enemy_append_event_system()  #イベントリストシステムによる敵の発生関数を呼び出す
               self.update_enemy_append_map_scroll()    #マップスクロールによる敵の発生関数を呼び出す
               self.update_event_append_request()       #イベントアペンドリストによる敵の追加発生関数を呼び出す（早回しなどの追加注文発生とかの処理）(イベント追加依頼）
               self.update_enemy()                      #敵の更新（移動とか）関数を呼び出す
               self.update_clip_enemy()                 #画面からはみ出た敵を消去する関数を呼び出し
               #ボス関連の処理#############################################################################################################
               self.update_boss()                       #ボスの更新移動とかを行う関数を呼び出す
               #パワーアップアイテム類の処理################################################################################################
               self.update_obtain_item()                #パワーアップアイテム類の更新（移動とか）する関数を呼び出します
               self.update_clip_obtain_item()           #画面からはみ出したパワーアップアイテム類を消去する関数を呼び出します
               self.stage_count += 1                    #ステージ開始から経過したフレームカウント数を1増加させる
               
               #スクロール関連の処理#########################################################################################################
               if self.boss_test_mode == 0:                  #ボス戦テストモードオフの時だけ
                    self.scroll_count += self.side_scroll_speed   #スクロールカウント数をスクロールスピード分(通常は1)増加させていく
                    self.vertical_scroll_count += self.vertical_scroll_speed   #縦スクロールカウント数を縦スクロールスピード分(大抵のステージは縦スクロールしないので0)増加させていく

               #横スクロールのスピード調整##################################################################################################
               if self.side_scroll_speed != self.side_scroll_speed_set_value: #現在の横スクロールスピードと設定値が違っていたのならば
                   self.side_scroll_speed += self.side_scroll_speed_variation #スピード変化量を加算減算してやって設定値まで近づけていきます
                   if  -0.01 <= self.side_scroll_speed - self.side_scroll_speed_set_value <= 0.01:
                       self.side_scroll_speed = self.side_scroll_speed_set_value #横スクロールスピードが設定値の近似値(誤差-0.01~0.01)なら強制的に現在スピードを設定値にしちゃうのだ！
               #縦スクロールのスピード調整###################################################################################################
               if self.vertical_scroll_speed != self.vertical_scroll_speed_set_value: #現在の縦スクロールスピードと設定値が違っていたのならば
                   self.vertical_scroll_speed += self.vertical_scroll_speed_variation #スピード変化量を加算減算してやって設定値まで近づけていきます
                   if  -0.01 <= self.vertical_scroll_speed - self.vertical_scroll_speed_set_value <= 0.01:
                       self.vertical_scroll_speed = self.vertical_scroll_speed_set_value #縦スクロールスピードが設定値の近似値(誤差-0.01~0.01)なら強制的に現在スピードを設定値にしちゃうのだ！
               #ラスタスクロールの更新#######################################################################################################
               self.update_raster_scroll()                 #ラスタースクロールの更新関数の呼び出し
               #マップチップナンバー書き換えによるアニメーション関連の更新######################################################################
               self.update_bg_rewrite_animation()          #BG書き換えによるアニメーション関数の呼び出し
               # self.update_dummy_bg_animation()          #BG 座標直接指定による書き換えダミーテスト
               
          if     self.game_status == SCENE_PLAY\
              or self.game_status == SCENE_BOSS_APPEAR\
              or self.game_status == SCENE_BOSS_BATTLE\
              or self.game_status == SCENE_BOSS_EXPLOSION :#「プレイ中」とボス関連の時だけ自機の当たり判定関連とシールド値のチェック&ボタンを押したら何かをする処理を実行する
               #自機と色んなオブジェクトとの当たり判定処理#############################
               self.update_collision_my_ship_enemy()        #自機と敵との当たり判定関数を呼び出す                
               self.update_collision_my_ship_bg()           #自機と背景障害物との当たり判定関数を呼び出す
               self.update_collision_my_ship_obtain_item()  #自機とパワーアップアイテム類の当たり判定（パワーアップゲットしたかな？どうかな？）
               self.update_collision_my_ship_boss()         #ボスと自機との当たり判定を行う関数を呼び出す
               #自機シールドのチェック###############################################
               self.update_check_my_shield()                #自機のシールドが残っているのかチェックする関数を呼び出す
               #武器発射関連の処理##################################################
               self.update_fire_shot()                 #ショットを発射する関数を呼び出す
               self.update_fire_missile()              #ミサイルを発射する関数を呼び出す
               self.update_fire_claw_shot()            #クローが弾を発射する関数を呼び出す

               self.update_change_sub_weapon()          #サブウェポンの切り替え関数を呼び出す
               #デバッグモードによる敵や敵弾の追加発生（ボタンを押したら敵が出てくる！？）###################################################
               # self.update_debug_mode_enemy_append()   #デバッグモードによる敵＆敵弾追加発生
               #プレイ時間の計算#####################################################
               self.update_calc_playtime()             #プレイ時間を計算する関数を呼び出す
               #ハイスコアの更新チェック##############################################
               self.update_check_hi_score()            #ハイスコアが更新されているか調べる関数を呼び出す
               #タイマーフレア放出###################################################
               self.update_timer_flare()               #タイマーフレア放出の更新処理関数を呼び出す
               #大気圏突入時の火花の発生#############################################
               self.update_atmospheric_entry_spark()   #大気圏突入時の火花を発せさせる関数の呼び出し

          if self.game_status == SCENE_BOSS_EXPLOSION:            #「BOSS_EXPLOSION」の時は
               self.uddate_present_repair_item()                  #リペアアイテムを出現させる関数の呼び出し
          if self.game_status == SCENE_EXPLOSION:                #「EXPLOSION」の時は
               self.my_ship_explosion_timer += 1                 # my_ship_explosionタイマーを加算していき
               if self.my_ship_explosion_timer >= SHIP_EXPLOSION_TIMER_LIMIT:#リミット値まで行ったのなら
                    self.game_status = SCENE_GAME_OVER           #「GAME_OVER」にする
          
          #######ゲームオーバー後の処理###############
          if self.game_status == SCENE_GAME_OVER:                #「GAME_OVER」の時は
               self.game_over_timer += 1                         # game_overタイマーを加算していき
               if self.game_over_timer >= GAME_OVER_TIMER_LIMIT: #リミット値まで行ったのなら
                    self.game_status = SCENE_GAME_OVER_FADE_OUT  #「ゲームオーバーフェードアウト開始」にする
          
          if self.game_status == SCENE_GAME_OVER_FADE_OUT:       #「GAME_OVER_FADE_OUT」の時は
              if self.fade_complete_flag == 1:                   #フェードアウト完了のフラグが建ったのなら
                  self.game_status = SCENE_GAME_OVER_SHADOW_IN   #「GAME_OVER_SHADOW_IN」状態にする
                  self.bg_cls_color = 0                          #クリアスクリーン時の塗りつぶし色を初期値の0(黒)に戻す（イベントとかで変化する場合があるため） 
                  self.star_scroll_flag = 1                      #背景星のスクロール表示をonにする（イベントとかで変化する場合があるため） 

          if self.game_status == SCENE_GAME_OVER_SHADOW_IN:      #「GAME_OVER_SHADOW_IN」の時は
              if self.shadow_in_out_complete_flag == 1:          #シャドウイン完了のフラグが建ったのなら
                  self.game_status = SCENE_GAME_OVER_STOP        #「GAME_OVER_STOP」状態にする
          
          if self.game_status == SCENE_GAME_OVER_STOP:           #「GAME_OVER_STOP」の時は
              new_window = Window()
              new_window.update(0,0,2,WINDOW_OPEN,\
                    "RETURN TITLE??",DISP_CENTER,\
                    "YES",DISP_CENTER,0,7,\
                    "NO",DISP_CENTER,0,3,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\
                    "",DISP_CENTER,0,7,\

                    43,68,   0,0,  8*8,3*8,   2,1, 1,1,   0,0,    0,0)
              self.window.append(new_window)                           #「TITLE RETURN」選択メニューを育成する
              self.cursor_show = True                                  #選択カーソル表示をonにする
              self.cursor_x = 64                                       #セレクトカーソルの座標を設定します
              self.cursor_y = 80
              self.cursor_item = 0                                     #いま指示しているアイテムナンバーは0の「YES」
              self.cursor_decision_item = -1                           #まだボタンも押されておらず未決定状態なのでdecision_itemは-1
              self.cursor_max_item = 1                                 #最大項目数は「YES」「NO」の2項目なので 2-1=1を代入
              self.game_status = SCENE_RETURN_TITLE                    #ゲームステータスを「RETURN_TITLE」にする
              
          if self.game_status == SCENE_RETURN_TITLE:             #「RETURN_TITLE」の時は              
              if pyxel.btnp(pyxel.KEY_ENTER):                    #リターンキーが押されたら
                  self.game_status = SCENE_TITLE_INIT            #ゲームステータスを「GAME_START_INIT」にしてゲーム全体を初期化＆リスタートする
                  self.game_playing_flag = 0                     #ゲームプレイ中のフラグを降ろす
              if self.cursor_decision_item == 0:                 #メニューでアイテムナンバー0の「YES」が押されたら
                  self.game_status = SCENE_TITLE_INIT            #ゲームステータスを「GAME_START_INIT」にしてゲーム全体を初期化＆リスタートする
                  self.game_playing_flag = 0                     #ゲームプレイ中のフラグを降ろす
                  
          #########ステージクリア後の処理#################
          if self.game_status == SCENE_STAGE_CLEAR_FADE_OUT:     #「SCENE_STAGE_CLEAR_FADE_OUT」の時は
              if self.fade_complete_flag == 1:                   #フェードアウト完了のフラグが建ったのなら
                   self.stage_number += 1    #ステージ数を1増やす
                   if self.stage_number == STAGE_VOLCANIC_BELT: #ステージ3 火山地帯はまだ未完成なので・・・
                        self.stage_number = STAGE_MOUNTAIN_REGION #ステージ1 山岳地帯に戻してやります
                        self.stage_loop += 1 #ループ数を1増やします
                        if self.stage_loop >= 4: #4周目以降は作っていないので\\\
                             self.stage_loop = 1 #1周目に戻ります
                        
                   self.game_status = SCENE_STAGE_START_INIT     #ゲームステータスを「STAGE_START_INIT」にして次のステージへ・・・・
          
          if self.game_playing_flag == 1: #ゲームプレイ中のフラグが立っていたのなら以下の処理を行う
               self.update_debug_status()       #デバッグステータス表示＆非表示の切り替え
               #映像オブジェクト関連の処理################################################################################################
               self.update_append_star()        #背景の星の追加＆発生育成関数呼び出し
               self.update_append_cloud()       #背景の雲の追加＆発生育成関数呼び出し
               self.update_star()               #背景の星の更新（移動）関数呼び出し
               self.update_particle()           #パーティクルの更新関数呼び出し
               self.update_background_object()  #背景オブジェクトの更新関数の呼び出し
               self.update_explosion()          #爆発パターンの更新関数呼び出し 
               #一時停止(pause)の処理###################################################################################################
               self.update_game_pause()         #ボタンが押されたらポーズをかける関数を呼び出し
               #メニューカーソル関連の処理###############################################################################################
               self.update_select_cursor()      #メニューカーソルの更新（移動とか）関数を呼び出し
          
     ###########################################################
     ###########################################################
     ###########################################################
     # ゲーム内での描画処理を行う              どろ～～☆彡       #
     ###########################################################
     ###########################################################
     ###########################################################
     def draw(self):
          pyxel.cls(self.bg_cls_color)                   #背景を指定色で消去する(初期値は0なので真っ黒になります)
          if self.game_status == SCENE_IPL:
               self.draw_ipl()
          if self.game_status == SCENE_TITLE or self.game_status == SCENE_TITLE_MENU_SELECT:
               self.draw_star()          #背景の星を表示する関数の呼び出し
               self.draw_title()         #タイトルロゴの表示関数の呼び出し
               self.draw_window()        #メニューウィンドウの表示関数の呼び出し
               self.draw_select_cursor() #セレクトカーソルの表示関数の呼び出し
     
          if self.game_playing_flag == 1 and self.star_scroll_flag == 1:#ゲームプレイ中フラグon,星スクロールフラグonの時は背景の星を表示する
               self.draw_star()          #背景の星を表示する関数の呼び出し 
          
          if      self.game_status == SCENE_PLAY\
               or self.game_status == SCENE_BOSS_APPEAR\
               or self.game_status == SCENE_BOSS_BATTLE\
               or self.game_status == SCENE_BOSS_EXPLOSION\
               or self.game_status == SCENE_EXPLOSION\
               or self.game_status == SCENE_STAGE_CLEAR\
               or self.game_status == SCENE_STAGE_CLEAR_MOVE_MY_SHIP\
               or self.game_status == SCENE_STAGE_CLEAR_MY_SHIP_BOOST\
               or self.game_status == SCENE_STAGE_CLEAR_FADE_OUT\
               or self.game_status == SCENE_GAME_OVER\
               or self.game_status == SCENE_GAME_OVER_FADE_OUT\
               or self.game_status == SCENE_PAUSE:
               
               #一番奥の背景の表示
               if   self.stage_number == STAGE_MOUNTAIN_REGION:
                   #雲ウェーブラスタースクロールの表示
                   self.draw_raster_scroll(0)  #ラスタースクロール描画関数呼び出し 山より奥で描画します

                   #奥の雲スクロールの表示
                   if self.disp_flag_bg_back == DISP_ON:
                        pyxel.bltm(-int(self.scroll_count  // 10 % (256*8 - 160)),-(self.vertical_scroll_count // 28) + 97,  1,     0,235,    256,7,    1)
                   
                   #影が強めの奥の山を描画
                   if self.disp_flag_bg_middle == DISP_ON:
                        pyxel.bltm(-int(self.scroll_count  // 8  % (256*8 - 160)),-(self.vertical_scroll_count // 24) + 116,  1,     0,243,    256,5,    self.bg_transparent_color)
                   
                   #手前の小さめの山を描画
                   if self.disp_flag_bg_front == DISP_ON:
                        pyxel.bltm(-int(self.scroll_count  // 4  % (256*8 - 160)),-(self.vertical_scroll_count // 16) + 160,  1,     0,248,    256,5,    self.bg_transparent_color)
                   
                   #湖面のラスタースクロールの表示、成層圏と大気圏の境目のラスタースクロールの表示
                   self.draw_raster_scroll(1)  #ラスタースクロール描画関数呼び出し 山より手前で描画しますっ！
               
               elif self.stage_number == STAGE_ADVANCE_BASE:
                    pyxel.bltm(-(self.scroll_count // 8) + 250,0,0,0,240,256,120,self.bg_transparent_color)
               
               ####################背景表示
               ###################pyxel.bltm(-(pyxel.frame_count // 8),0,0,((pyxel.frame_count / 2) - 160) ,0,160,120,0)最初はこれで上手くいかなかった・・・・なぜ？
               ###################奥の背景表示
               ###################pyxel.bltm(-(pyxel.frame_count // 4) + 400,0,0,0,16,256,120,0)

               if self.stage_number == STAGE_ADVANCE_BASE:
                    pyxel.bltm(-(self.scroll_count // 4) + 400,0,0,0,224,256,120,self.bg_transparent_color)
               
               elif self.stage_number == STAGE_MOUNTAIN_REGION:
                         if self.disp_flag_bg_front == DISP_ON:
                              pyxel.bltm(-int(self.scroll_count % (256*8 - 160)),      -self.vertical_scroll_count,  1,     0,0,    256,256,    self.bg_transparent_color)
               
               self.draw_background_object()    #背景オブジェクトの描画関数の呼び出し
               
               self.draw_enemy_shot(PRIORITY_BOSS_BACK)   #敵の弾を表示する関数を呼び出す(ボスキャラの真後ろ)---------------------------
               self.draw_boss()          #ボスを表示する関数を呼び出す
               self.draw_boss_hp()       #ボスの耐久力を表示する関数を呼び出す
               self.draw_enemy_shot(PRIORITY_BOSS_FRONT)   #敵の弾を表示する関数を呼び出す(ボスキャラのすぐ手前)-------------------------
                  
               self.draw_obtain_item()   #パワーアップアイテム類の表示
               
               self.draw_enemy()         #敵を表示する関数を呼び出す
               self.draw_enemy_shot(PRIORITY_FRONT)       #敵の弾を表示する関数を呼び出す (前面)---------------------------------------
               self.draw_enemy_shot(PRIORITY_MORE_FRONT)  #敵の弾を表示する関数を呼び出す (敵弾の中でもさらに前面)-----------------------
               PRIORITY_MORE_FRONT
               self.draw_particle()      #パーティクルを表示する関数の呼び出し

               self.draw_my_shot()       #自機弾の表示
               self.draw_missile()       #ミサイルの表示
               self.draw_claw_shot()     #クローショットの表示

               #手前の背景表示
               #結局なんでこれでキチンとスクロール表示されたのか謎・・・結局はじめは-1024ドットのx座標位置からスクロール開始していくことに・・
               #pyxel.bltm(-(pyxel.frame_count // 2) + 1024,0,0,0,0,256,120,0)
               if self.stage_number == STAGE_ADVANCE_BASE:
                    if   self.stage_loop == 1:
                         pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  0,     0,0,    256,120,    self.bg_transparent_color) #1周目マップ
                    elif self.stage_loop == 2:
                         pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  0,     0,16,   256,120,    self.bg_transparent_color) #2周目マップ
                    elif self.stage_loop == 3:
                         pyxel.bltm(-(self.scroll_count // 2) + 1024,0,  0,     0,32,   256,120,    self.bg_transparent_color) #3周目マップ
               self.draw_enemy_shot(PRIORITY_TOP)         #敵の弾を表示する関数を呼び出す (最前面)-------------------------------------
          #自機、クロー、シールドの表示###############################################
          if      self.game_status == SCENE_PLAY\
               or self.game_status == SCENE_BOSS_APPEAR\
               or self.game_status == SCENE_BOSS_BATTLE\
               or self.game_status == SCENE_BOSS_EXPLOSION\
               or self.game_status == SCENE_STAGE_CLEAR\
               or self.game_status == SCENE_STAGE_CLEAR_MOVE_MY_SHIP\
               or self.game_status == SCENE_STAGE_CLEAR_MY_SHIP_BOOST\
               or self.game_status == SCENE_STAGE_CLEAR_FADE_OUT\
               or self.game_status == SCENE_PAUSE:
               
               self.draw_my_ship()       #自機表示
               self.draw_claw()          #クローの表示
               self.draw_ls_shield()     #Ｌ'sシールドシステムの表示
          
          if self.game_playing_flag == 1:#「ゲームプレイ中」の時は爆発パターン表示
               self.draw_explosion(PRIORITY_FRONT)      #爆発パターン(前面)の表示
               self.draw_explosion(PRIORITY_MORE_FRONT) #爆発パターン(さらに前面)の表示

          #フェードアウトスクリーンの表示###############################################
          if     self.game_status == SCENE_GAME_OVER_FADE_OUT\
              or self.game_status == SCENE_STAGE_CLEAR_FADE_OUT:
              
              self.draw_fade_in_out_screen(FADE_OUT,0)         #フェードイン＆フェードアウト用のエフェクトスクリーンの描画表示
               
          #画面中央80ドットだけ表示する処理###########################################
          if     self.game_status == SCENE_GAME_OVER_SHADOW_IN\
              or self.game_status == SCENE_GAME_OVER_STOP\
              or self.game_status == SCENE_RETURN_TITLE:
              
              self.draw_shadow_out_screen(40,0)  #中央付近80ドット分だけ残してシャドウアウトする
          
          if self.game_playing_flag == 1:#「ゲームプレイ中」の時は以下の処理も行う
               self.draw_sub_weapon_select_guidebox()  #選択中のサブウェポンのカーソルガイドボックスの表示
               self.draw_sub_weapon_select_gauge()     #サブウェポン一覧表示

               self.draw_status()                     #スコアやスピード、自機耐久力などの表示関数の呼び出し （通常ステータス表示）
               self.draw_debug_status()               #デバッグ用ステータスの表示関数の呼び出し            （デバック用ステータス表示）
               self.draw_window()                     #メッセージウィンドウの表示
               self.draw_select_cursor()              #セレクトカーソルの表示

               self.draw_warning_dialog()             #WARNINGダイアログの表示
               self.draw_stage_clear_dialog()         #STAGE CLEARダイアログの表示

               # self.draw_dummy_put_bg_xy()            #BG Get&Put dummy test

          #一時停止・ポーズメッセージの表示#########################################
          if self.game_status == SCENE_PAUSE:
               self.draw_pause_message() #一時停止・ポーズメッセージの表示
          
          #ゲームオーバー画像の表示##################################################
          if      self.game_status == SCENE_GAME_OVER\
               or self.game_status == SCENE_GAME_OVER_FADE_OUT\
               or self.game_status == SCENE_GAME_OVER_SHADOW_IN\
               or self.game_status == SCENE_GAME_OVER_STOP\
               or self.game_status == SCENE_RETURN_TITLE:
               self.draw_gameover_dialog()            #ゲームオーバー表示をする関数呼び出し
App()