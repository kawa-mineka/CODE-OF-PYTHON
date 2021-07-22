class App:
    #!###############################################################################################################################
    #!###############################################################################################################################
    #!update関数から呼び出される関数群 ################################################################################################
    #!###############################################################################################################################
    #!###############################################################################################################################
    #IPLの更新#######################################
    def update_ipl(self):
        self.display_ipl_time -= 1    #IPLメッセージを表示する時間カウンターを1減らす
        if self.display_ipl_time <= 0: #カウンターが0以下になったら・・・
            self.game_status = SCENE_TITLE_INIT #ゲームステータスを「SCENE_TITLE_INIT(タイトル表示に必要な変数を初期化)」にする
        
        if (pyxel.frame_count % 10) == 0:
            if len(self.ipl_mes1) > self.ipl_mes_write_line_num: #まだ書き込むべき文字列があるのなら・・・
                text_mes = str(self.ipl_mes1[self.ipl_mes_write_line_num][0])
                text_col = str(self.ipl_mes1[self.ipl_mes_write_line_num][1])
                self.text_screen.append([text_mes,text_col]) #文字列群をテキストスクリーンのリストに追加する
                self.ipl_mes_write_line_num +=1  #スクリーンに表示したIPLメッセージデータの行数カウンタを1インクリメント

    #タイトル表示に必要な変数を設定＆初期化する##############
    def update_title_init(self):
        pyxel.load("assets/graphic/min-sht2.pyxres") #タイトル＆ステージ1＆2のリソースファイルを読み込む
        #タイトル関連の変数を初期化
        
        self.display_title_time = 204               #タイトルを表示する時間
        self.title_oscillation_count = 200          #タイトルグラフイックの振れ幅カウンター
        self.title_slash_in_count =    100          #タイトルグラフイックが下から切り込んで競りあがってくる時に使うカウンター
        
        # self.display_title_time      = 10         #タイトルを表示する時間
        # self.title_oscillation_count = 10         #タイトルグラフイックの振れ幅カウンター
        # self.title_slash_in_count =    10         #タイトルグラフイックが下から切り込んで競りあがってくる時に使うカウンター
        
        self.stars = []                        #タイトル表示時も背景の星を流したいのでリストをここで初期化してやります
        self.star_scroll_speed = 1             #背景の流れる星のスクロールスピード 1=通常スピード 0.5なら半分のスピードとなります
        self.window = []                       #タイトル表示時もメッセージウィンドウを使いたいのでリストをここで初期化してあげます
        self.cursor = []                       #タイトル表示時もウィンドウカーソルを使いたいのでリストをここで初期化してあげます
        
        #リプレイ記録用に使用する横無限大,縦50ステージ分の空っぽのリプレイデータリストを作成します
        self.replay_recording_data =[[] for i in range(50)]
        
        self.bg_cls_color = 0         #BGをCLS(クリアスクリーン)するときの色の指定(通常は0=黒色です)ゲーム時に初期値から変更されることがあるのでここで初期化する
        
        # セレクトカーソル関連の変数宣言   タイトル画面でセレクトカーソルを使いたいのでここで変数などを宣言＆初期化します
        self.cursor_type = CURSOR_TYPE_NO_DISP #セレクトカーソルを表示するかしないかのフラグ用
        self.cursor_x = 0                      #セレクトカーソルのx座標
        self.cursor_y = 0                      #セレクトカーソルのy座標
        self.cursor_step_x = 4                 #横方向の移動ドット数(初期値は4ドット)
        self.cursor_step_y = 7                 #縦方向の移動ドット数(初期値は7ドット)
        self.cursor_page = 0                   #いま指し示しているページナンバー
        self.cursor_pre_page = 0               #前フレームで表示していたページ数 pre_pageとpageが同じなら新規ウィンドウは育成しない
        self.cursor_page_max = 0               #セレクトカーソルで捲ることが出来る最多ページ数
        self.cursor_item_x = 0                 #いま指し示しているアイテムナンバーx軸方向
        self.cursor_item_y = 0                 #いま指し示しているアイテムナンバーy軸方向
        self.cursor_decision_item_x = -1       #ボタンが押されて「決定」されたアイテムのナンバーx軸方向 -1は未決定 ここをチェックしてどのアイテムが選択されたのか判断する
        self.cursor_decision_item_y = -1       #ボタンが押されて「決定」されたアイテムのナンバーy軸方向 -1は未決定 ここをチェックしてどのアイテムが選択されたのか判断する
        self.cursor_max_item_x = 0             #x軸の最大項目数 5の場合(0~4)の5項目分カーソルが移動することになります 3だったら(0~2)って感じで
        self.cursor_max_item_y = 0             #y軸の最大項目数 5の場合(0~4)の5項目分カーソルが移動することになります 3だったら(0~2)って感じで
        self.cursor_color = 0                  #セレクトカーソルの色
        self.cursor_menu_layer = 0             #現在選択中のメニューの階層の数値が入ります
        self.cursor_pre_decision_item_y = 0    #前の階層で選択したアイテムのナンバーを入れます
                                            #選択してcursor_decision_item_yに入ったアイテムナンバーをcursor_pre_decision_item_yに入れて次の階層に潜るって手法かな？
        self.cursor_move_direction = 0         #セレクトカーソルがどう動かせることが出来るのか？の状態変数です
        self.cursor_move_data = 0              #カーソルが実際に動いた方向のデータが入ります
        self.cursor_size      = 0              #セレクトカーソルの大きさです(囲み矩形タイプで使用します)
        
        self.active_window_id = 0              #アクティブになっているウィンドウのIDが入ります
        self.active_window_index = 0           #アクティブになっているウィンドウのインデックスナンバー(i)が入ります(ウィンドウIDを元にして全ウィンドウデータから検索しインデックス値を求めるのです！)
        #system-data.pyxresリソースファイルからこれらの設定値を読み込むようにしたのでコメントアウトしています
        # self.game_difficulty = GAME_NORMAL         #難易度                  タイトルメニューで難易度を選択して変化させるのでここで初期化します
        
        self.stage_number = STAGE_MOUNTAIN_REGION  #最初に出撃するステージ   タイトルメニューでステージを選択して変化させるのでここで初期化します
        self.stage_loop   = 1                      #ループ数(ステージ周回数) タイトルメニューで周回数を選択して変化させるのでここで初期化します
        
        pygame.mixer.init(frequency = 44100)     #pygameミキサー関連の初期化
        pygame.mixer.music.set_volume(0.7)       #音量設定(0~1の範囲内)
        pygame.mixer.music.load('assets/music/BGM200-171031-konotenitsukame-intro.wav') #タイトルイントロ部分のwavファイルを読み込み
        pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
        pygame.mixer.music.play(1)               #イントロを1回だけ再生
        
        self.game_status = SCENE_TITLE           #ゲームステータスを「SCENE_TITLE」にしてタイトル表示を開始する

    #タイトルの更新#######################################
    def update_title(self):
        self.display_title_time -= 1          #タイトルを表示する時間カウンターを1減らす
        if self.display_title_time <= 0:      #カウンターが0以下になったら・・・
            self.display_title_time = 0       #強制的に0の状態にする
        
        self.title_oscillation_count -= 1     #タイトルグラフイックの振れ幅カウンターを1減らす
        if self.title_oscillation_count < 0:  #カウンターが0以下になったら・・・
            self.title_oscillation_count = 0  #強制的に0の状態にする
        
        self.title_slash_in_count -= 1        #タイトルグラフイックが下から切り込んで競りあがってくる時に使うカウンターを1減らす
        if self.title_slash_in_count < 0:     #カウンターが0以下になったら・・・
            self.title_slash_in_count = 0     #強制的に0の状態にする
        
        #BGMイントロ再生が終了したらBGMループ部分を再生し始める
        if pygame.mixer.music.get_pos() == -1:      #pygame.mixer.music.get_posはBGM再生が終了すると-1を返してきます
            pygame.mixer.init(frequency = 44100)    #pygameミキサー関連の初期化
            pygame.mixer.music.set_volume(0.7)      #音量設定(0~1の範囲内)
            pygame.mixer.music.load('assets/music/BGM200-171031-konotenitsukame-loop.wav') #タイトルBGMループ部分のwavファイルを読み込み
            pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
            pygame.mixer.music.play(-1)             #タイトルBGMをループ再生
        
        #全てのカウンター類が0になったらゲームメニューウィンドウを育成する
        if self.title_oscillation_count == 0 and self.title_slash_in_count == 0 and self.display_title_time == 0:
            self.create_window(WINDOW_ID_MAIN_MENU,0,0)         #メニューウィンドウを作製
            #選択カーソル表示をon,カーソルは上下移動のみ,いま指示しているアイテムナンバーは0,まだボタンも押されておらず未決定状態なのでdecision_item_yは-1
            #選択できる項目数は13項目なので 13-1=12を代入,メニューの階層は最初は0にします,カーソル移動ステップはx4,y7
            self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,MAIN_MENU_X+5,MAIN_MENU_Y+10,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,13-1,0,MENU_LAYER0)
            self.active_window_id = WINDOW_ID_MAIN_MENU         #このウィンドウIDを最前列アクティブなものとする
            self.game_status = SCENE_TITLE_MENU_SELECT          #ゲームステータスを「TITLE_MENU_SELECT」(タイトルでメニューを選択中)」にする

    #タイトルメニューの選択中の更新#####################################
    def update_title_menu_select(self):
        if   self.cursor_menu_layer == MENU_LAYER0: #メニューが0階層目の選択分岐
            if   self.cursor_decision_item_y == MENU_GAME_START:        #GAME STARTが押されたら
                self.cursor_type = CURSOR_TYPE_NO_DISP      #セレクトカーソルの表示をoffにする
                self.move_mode = MOVE_MANUAL                #移動モードを「手動移動」にする
                self.replay_status = REPLAY_RECORD          #リプレイデータを「記録中」にする
                self.start_stage_number = self.stage_number #リプレイファイル保存用にゲーム開始時のステージナンバーとループ数を保管しておきます（リプレイデータはゲーム終了後にセーブされるのでstage_numberなどの値が変化するのでstart_stage_numberって変数を作ってリプレイ記録時にはこれを使うのです)
                self.start_stage_loop   = self.stage_loop
                self.game_status = SCENE_GAME_START_INIT    #ゲームステータスを「GAME_START_INIT」にしてゲーム全体を初期化＆リスタートする
                self.active_window_id = WINDOW_ID_MAIN_MENU #メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_decision_item_y == MENU_SELECT_STAGE:      #SELECT STAGEが押されて
                if self.search_window_id(WINDOW_ID_SELECT_STAGE_MENU) == -1: #SELECT_STAGE_MENUウィンドウが存在しないのなら・・
                    self.move_left_main_menu_window() #メインメニューウィンドウを左にずらす関数の呼び出し
                    
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「SELECT STAGE」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_MAIN_MENU)       #メインメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_SELECT_STAGE_MENU,0,0)  #ステージセレクトウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「1」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は3項目なので 3-1=2を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,92,71,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,3-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_SELECT_STAGE_MENU #このウィンドウIDを最前列アクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_SELECT_LOOP:       #SELECT LOOPが押されて
                if self.search_window_id(WINDOW_ID_SELECT_LOOP_MENU) == -1: #SELECT_LOOP_MENUウィンドウが存在しないのなら・・
                    self.move_left_main_menu_window() #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「SELECT LOOP」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_SELECT_LOOP_MENU,0,0)      #ループセレクトウィンドウの作成
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「1」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は3項目なので 3-1=2を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,90+24,72+5,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,3-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_SELECT_LOOP_MENU  #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_BOSS_MODE:         #BOSS MODEが押されて
                if self.search_window_id(WINDOW_ID_BOSS_MODE_MENU) == -1: #BOSS MODEウィンドウが存在しないのなら・・
                    self.move_left_main_menu_window() #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「BOSS MODE」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_BOSS_MODE_MENU,0,0)        #ボスモードon/offウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「ON」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は2項目なので 2-1=1を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,96+5,69+self.boss_test_mode * STEP7,STEP4,STEP7,0,0,0,self.boss_test_mode,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_BOSS_MODE_MENU    #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_HITBOX:            #HITBOXが押されて....
                if self.search_window_id(WINDOW_ID_HITBOX_MENU) == -1: #HITBOXウィンドウが存在しないのなら・・
                    self.move_left_main_menu_window() #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「HITBOX」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_HITBOX_MENU,0,0)           #ヒットボックスon/offウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「OFF」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は2項目なので 2-1=1を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,96+5,69+self.boss_collision_rect_display_flag * STEP7,STEP4,STEP7,0,0,0,self.boss_collision_rect_display_flag,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_HITBOX_MENU       #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_DIFFICULTY:        #DIFFICULTYが押されて
                if self.search_window_id(WINDOW_ID_SELECT_DIFFICULTY) == -1: #SELECT_DIFFICULTYウィンドウが存在しないのなら・・
                    self.move_left_main_menu_window() #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「DIFFICULTY」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_SELECT_DIFFICULTY,0,0)     #「SELECT DIFFICULTY」ウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは2の「NORMAL」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は6項目なので 6-1=5を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,96,63 + self.game_difficulty * STEP7,STEP4,STEP7,0,0,0,self.game_difficulty,UNSELECTED,UNSELECTED,0,6-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_SELECT_DIFFICULTY #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_SCORE_BOARD:       #SCORE BOARDが押されて...
                if self.search_window_id(WINDOW_ID_SCORE_BOARD) == -1: #SCORE_BOARDウィンドウが存在しないのなら・・
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「SCORE BOARD」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    self.window_score_board(GAME_NORMAL)                #スコアボードウィンドウを育成=============
                    #選択カーソル表示をoff,カーソルは表示せずLRキーもしくはLショルダーRショルダーで左右に頁をめくる動作,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「1」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は1項目なので 1-1=0を代入,いま指し示しているページナンバー 0=very easy,#最大ページ数 難易度は0~5の範囲 なのでMAX5,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_NO_DISP,CURSOR_MOVE_SHOW_PAGE,92,71,STEP4,STEP7,0,5,0,0,UNSELECTED,UNSELECTED,0,0,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_SCORE_BOARD       #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_NAME_ENTRY:        #NAME ENTRYが押されて...
                if self.search_window_id(WINDOW_ID_INPUT_YOUR_NAME) == -1: #INPUT_YOUR_NAMEウィンドウが存在しないのなら・・
                    self.move_left_main_menu_window() #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_x = self.cursor_decision_item_x #現時点で選択されたアイテム「NAME ENTRY」を前のレイヤー選択アイテムとしてコピーする
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「NAME ENTRY」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_INPUT_YOUR_NAME,0,0)       #「ENTER YOUR NAME」ウィンドウの作製
                    #選択カーソルのタイプはアンダーバーの点滅にします,カーソルは左右でスライダー入力,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーx軸は0,y軸は0(縦には動かないので常に0となります)
                    #まだボタンも押されておらず未決定状態なのでdecision_item_x,decision_item_yはUNSELECTED,最大項目数x軸方向は(8文字+OKボタンなので)合計9項目 9-1=8を代入,最大項目数y軸方向は0,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_UNDER_BAR,CURSOR_MOVE_LR_SLIDER,100,66,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,9-1,0,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_INPUT_YOUR_NAME   #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_CONFIG:            #CONFIGが押されて
                if self.search_window_id(WINDOW_ID_CONFIG) == -1: #SELECT_CONFIGウィンドウが存在しないのなら・・
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「CONFIG」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_CONFIG,0,0)                #「CONFIG」ウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動+左右によるパラメーターの変更,カーソル移動ステップはx4,y9,いま指示しているアイテムナンバーは0の
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は11項目なので11-1=10を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD_SLIDER,9,17,STEP4,STEP9,0,0,0,0,UNSELECTED,UNSELECTED,0,11-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_CONFIG #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_REPLAY:            #REPLAYが押されたら
                self.game_status = SCENE_SELECT_LOAD_SLOT           #ゲームステータスを「SCENE_SELECT_LOAD_SLOT」にしてロードデータスロットの選択に移る
                self.window_replay_data_slot_select()               #リプレイデータファイルスロット選択ウィンドウの表示
                #選択カーソル表示をonにする,カーソルは上下移動のみ,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「1」
                #まだボタンも押されておらず未決定状態なのでdecision_item_yは-1最大項目数は「1」「2」「3」「4」「5」「6」「7」の7項目なので 7-1=6を代入,メニューの階層が増えたので,MENU_LAYER0からMENU_LAYER1にします
                self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,67,55,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,6,0,MENU_LAYER1)
                self.active_window_id = WINDOW_ID_SELECT_FILE_SLOT  #このウィンドウIDを最前列でアクティブなものとする
                pyxel.play(0,self.window[self.active_window_index].cursor_push_se) #カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_MEDAL:             #MEDALが押されて
                if self.search_window_id(WINDOW_ID_MEDAL_LIST) == -1: #MEDAL_LISTウィンドウが存在しないのなら・・
                    self.move_left_main_menu_window() #メインメニューウィンドウを左にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「MEDAL_LIST」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_MEDAL_LIST,0,0)                #「MEDAL_LIST」ウィンドウの作製
                    #カーソルは点滅囲み矩形タイプ,カーソルは4方向,カーソル移動ステップはx10y10,いま指し示しているitem_x,item_yは(0,0)
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,x最大項目数は9項目なので9-1=8を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_BOX_FLASH,CURSOR_MOVE_4WAY,46,60,STEP10,STEP10,0,0,0,0,UNSELECTED,UNSELECTED,9-1,3-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_MEDAL_LIST #このウィンドウIDを最前列でアクティブなものとする
                    self.make_medal_list_window_comment_disp_flag_table() #メダルリストウィンドウで「存在するアイテム」を調べ上げコメント表示フラグテーブルを作製する関数の呼び出す
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == MENU_EXIT:              #EXITが押されたら・・・
                if self.search_window_id(WINDOW_ID_EXIT) == -1: #ゲーム終了(退出)ウィンドウが存在しないのなら・・
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「EXIT」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_EXIT,0,0)                  #ゲーム終了(退出)ウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「NO」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は2項目なので 2-1=1を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,66,69,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_EXIT    #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
            
        elif self.cursor_menu_layer == MENU_LAYER1: #メニューが1階層目の選択分岐
            if   self.cursor_pre_decision_item_y == MENU_SELECT_STAGE and self.cursor_decision_item_y == 0:
                #「SELECT STAGE」→「1」
                self.stage_number   = 1                          #ステージナンバー1
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                
                i = self.search_window_id(WINDOW_ID_SELECT_STAGE_MENU)
                self.window[i].vx = 0.6            #WINDOW_ID_SELECT_STAGE_MENUウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1 * self.stage_number
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_SELECT_STAGE and self.cursor_decision_item_y == 1:
                #「SELECT STAGE」→「2」
                self.stage_number   = 2                         #ステージナンバー2
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                
                i = self.search_window_id(WINDOW_ID_SELECT_STAGE_MENU)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_STAGE_MENUウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1 * self.stage_number
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_SELECT_STAGE and self.cursor_decision_item_y == 2:
                #「SELECT STAGE」→「3」
                self.stage_number   = 3                        #ステージナンバー3
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                
                i = self.search_window_id(WINDOW_ID_SELECT_STAGE_MENU)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_STAGE_MENUウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.1 * self.stage_number
                self.window[i].vy_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_SELECT_LOOP and self.cursor_decision_item_y == 0:
                #「SELECT LOOP NUMBER」→「1」
                self.stage_loop = 1                           #ループ数に1週目を代入
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                i = self.search_window_id(WINDOW_ID_SELECT_LOOP_MENU)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_LOOP_MENUウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_SELECT_LOOP and self.cursor_decision_item_y == 1:
                #「SELECT LOOP NUMBER」→「2」
                self.stage_loop = 2                           #ループ数に2週目を代入
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                i = self.search_window_id(WINDOW_ID_SELECT_LOOP_MENU)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_LOOP_MENUウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_SELECT_LOOP and self.cursor_decision_item_y == 2:
                #「SELECT LOOP NUMBER」→「3」
                self.stage_loop = 3                          #ループ数に3週目を代入
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                i = self.search_window_id(WINDOW_ID_SELECT_LOOP_MENU)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_LOOP_MENUウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_BOSS_MODE and self.cursor_decision_item_y == 0:
                #「BOSS MODE」→「OFF」
                self.boss_test_mode = 0        #ボステストモードをoff
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                i = self.search_window_id(WINDOW_ID_BOSS_MODE_MENU)
                self.window[i].vx = 0.3            #WINDOW_ID_BOSS_MODE_MENUウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_BOSS_MODE and self.cursor_decision_item_y == 1:
                #「BOSS MODE」→「ON」
                self.boss_test_mode = 1                              #ボステストモードをon
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                i = self.search_window_id(WINDOW_ID_BOSS_MODE_MENU)
                self.window[i].vx = 0.3            #WINDOW_ID_BOSS_MODE_MENUウィンドウを右下にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].vy = 0.2
                self.window[i].vy_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_HITBOX and self.cursor_decision_item_y == 0:
                #「HITBOX」→「OFF」
                self.boss_collision_rect_display_flag = 0            #ボス当たり判定表示をoff
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                i = self.search_window_id(WINDOW_ID_HITBOX_MENU)
                self.window[i].vx = 0.3            #WINDOW_ID_HITBOX_MENUウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_HITBOX and self.cursor_decision_item_y == 1:
                #「HITBOX」→「ON」
                self.boss_collision_rect_display_flag = 1            #ボス当たり判定表示をon
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                i = self.search_window_id(WINDOW_ID_HITBOX_MENU)
                self.window[i].vx = 0.3            #WINDOW_ID_HITBOX_MENUウィンドウを右下にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].vy = 0.2
                self.window[i].vy_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_DIFFICULTY and self.cursor_decision_item_y == GAME_VERY_EASY:
                #「DIFFICULTY」→「VERY_EASY」
                self.game_difficulty = GAME_VERY_EASY
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                i = self.search_window_id(WINDOW_ID_SELECT_DIFFICULTY)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].vy = -0.1
                self.window[i].vy_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_DIFFICULTY and self.cursor_decision_item_y == GAME_EASY:
                #「DIFFICULTY」→「EASY」
                self.game_difficulty = GAME_EASY
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                i = self.search_window_id(WINDOW_ID_SELECT_DIFFICULTY)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].vy = -0.05
                self.window[i].vy_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_DIFFICULTY and self.cursor_decision_item_y == GAME_NORMAL:
                #「DIFFICULTY」→「NORMAL」
                self.game_difficulty = GAME_NORMAL
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                i = self.search_window_id(WINDOW_ID_SELECT_DIFFICULTY)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_DIFFICULTY and self.cursor_decision_item_y == GAME_HARD:
                #「DIFFICULTY」→「HARD」
                self.game_difficulty = GAME_HARD
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                i = self.search_window_id(WINDOW_ID_SELECT_DIFFICULTY)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].vy = 0.1
                self.window[i].vy_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_DIFFICULTY and self.cursor_decision_item_y == GAME_VERY_HARD:
                #「DIFFICULTY」→「VERY_HARD」
                self.game_difficulty = GAME_VERY_HARD
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                i = self.search_window_id(WINDOW_ID_SELECT_DIFFICULTY)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].vy = 0.2
                self.window[i].vy_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_DIFFICULTY and self.cursor_decision_item_y == GAME_INSAME:
                #「DIFFICULTY」→「INSAME」
                self.game_difficulty = GAME_INSAME
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                i = self.search_window_id(WINDOW_ID_SELECT_DIFFICULTY)
                self.window[i].vx = 0.3            #WINDOW_ID_SELECT_DIFFICULTYウィンドウを右にフッ飛ばしていく
                self.window[i].vx_accel = 1.2
                self.window[i].vy = 0.3
                self.window[i].vy_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.window[i].flag_list = self.master_flag_list #ボステストフラグを更新→マスターフラグデータリスト更新→ウィンドウのフラグリストに書き込んで更新します
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_SCORE_BOARD and self.cursor_page == GAME_VERY_EASY and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                if self.cursor_move_data == PAD_RIGHT:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                else:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                
                self.window_score_board(GAME_VERY_EASY)                           #スコアボードウィンドウ育成
                self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
            elif self.cursor_pre_decision_item_y == MENU_SCORE_BOARD and self.cursor_page == GAME_EASY      and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                if self.cursor_move_data == PAD_RIGHT:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                else:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                
                self.window_score_board(GAME_EASY)                           #スコアボードウィンドウ育成
                self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
            elif self.cursor_pre_decision_item_y == MENU_SCORE_BOARD and self.cursor_page == GAME_NORMAL    and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                if self.cursor_move_data == PAD_RIGHT:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                else:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                
                self.window_score_board(GAME_NORMAL)                           #スコアボードウィンドウ育成
                self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
            elif self.cursor_pre_decision_item_y == MENU_SCORE_BOARD and self.cursor_page == GAME_HARD      and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                if self.cursor_move_data == PAD_RIGHT:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                else:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                
                self.window_score_board(GAME_HARD)                           #スコアボードウィンドウ育成
                self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
            elif self.cursor_pre_decision_item_y == MENU_SCORE_BOARD and self.cursor_page == GAME_VERY_HARD and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                if self.cursor_move_data == PAD_RIGHT:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                else:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                
                self.window_score_board(GAME_VERY_HARD)                           #スコアボードウィンドウ育成
                self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
            elif self.cursor_pre_decision_item_y == MENU_SCORE_BOARD and self.cursor_page == GAME_INSAME    and self.cursor_pre_page != self.cursor_page: #前に表示していたページ数と現在のページ数に変化があった時だけ
                if self.cursor_move_data == PAD_RIGHT:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD, 0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを右方向にフッ飛ばしていく
                else:
                    self.all_move_window(WINDOW_ID_SCORE_BOARD,-0.3,0, 1.2,0) #すべてのSCORE_BOARDウィンドウを左方向にフッ飛ばしていく
                
                self.window_score_board(GAME_INSAME)                           #スコアボードウィンドウ育成
                self.cursor_pre_page = self.cursor_page              #前回のページ数を保存
            elif self.cursor_pre_decision_item_y == MENU_SCORE_BOARD and self.cursor_decision_item_y != -1: #何かしらのアイテムの所でボタンが押されたのなら
                #SCORE BOARDはキー入力のタイミングで同じウィンドウIDを持つウィンドウが複数存在してしまう可能性があるので
                #ウィンドウIDナンバーを元にすべての同一IDウィンドウを調べ上げ画面外にフッ飛ばすようにする
                self.all_move_window(WINDOW_ID_SCORE_BOARD,0,0.3,0,1.2) #すべてのSCORE_BOARDウィンドウを下方向にフッ飛ばしていく
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)               #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED                    #前回選択したアイテムも未決定に
                pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_NAME_ENTRY and self.cursor_decision_item_x == 8:
                self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                #「ENTER YOUR NAME」→「OK」ボタンを押した
                text = self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT]
                self.my_name = text[:8] #文字列textの先頭から8文字までをmy_nameとします
                self.all_move_window(WINDOW_ID_INPUT_YOUR_NAME,0.2,0.3,1.2,1.2) #すべてのINPUT_YOUR_NAMEウィンドウを右下方向にフッ飛ばしていく
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルOK音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_CONFIG and self.cursor_decision_item_y == 10:
                self.restore_master_flag_list() #フラグ＆データ関連のマスターリストを参照して個別のフラグ変数へリストアする
                i = self.search_window_id(WINDOW_ID_CONFIG)
                self.window[i].vx = -0.1            #WINDOW_ID_CONFIGウィンドウを左下にフッ飛ばしていく
                self.window[i].vx_accel = 1.1
                self.window[i].vy = 0.2
                self.window[i].vy_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.save_system_data()                            #システムデータをセーブします
                pyxel.load("assets/graphic/min-sht2.pyxres") #タイトル＆ステージ1＆2のリソースファイルを読み込む
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                
            elif self.cursor_pre_decision_item_y == MENU_MEDAL and self.cursor_decision_item_y == 2:
                if 6 <= self.cursor_decision_item_x <= 8:
                    self.move_right_main_menu_window() #メインメニューウィンドウを右にずらす関数の呼び出し
                    self.create_master_flag_list() #フラグ＆データ関連のマスターリスト作成関数を呼び出す
                    i = self.search_window_id(WINDOW_ID_MEDAL_LIST)
                    self.window[i].vx = 0.3            #WINDOW_ID_MEDAL_LISTウィンドウを右にフッ飛ばしていく
                    self.window[i].vx_accel = 1.2
                    self.window[i].vy = 0.1
                    self.window[i].vy_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                    self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                    self.cursor_pre_decision_item_y = UNSELECTED
                    pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                    self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
                    self.cursor_size = CURSOR_SIZE_NORMAL       #矩形囲みタイプのセレクトカーソルのサイズを通常サイズに戻す
                
            elif self.cursor_pre_decision_item_y == MENU_EXIT and self.cursor_decision_item_y == 0:
                i = self.search_window_id(WINDOW_ID_EXIT)
                self.window[i].vy = -0.3            #WINDOW_ID_EXITウィンドウを右上にフッ飛ばしていく
                self.window[i].vy_accel = 1.2
                self.window[i].vx = 0.1
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.pop_cursor_data(WINDOW_ID_MAIN_MENU)          #メインメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                self.active_window_id = WINDOW_ID_MAIN_MENU #1階層前メインメニューウィンドウIDを最前列でアクティブなものとする
            elif self.cursor_pre_decision_item_y == MENU_EXIT and self.cursor_decision_item_y == 1:
                self.star_scroll_flag  = 1
                i = self.search_window_id(WINDOW_ID_EXIT)
                self.window[i].vy = -0.1            #WINDOW_ID_EXITウィンドウを右上にフッ飛ばしていく
                self.window[i].vy_accel = 1.05
                self.window[i].vx = 0.1
                self.window[i].vx_accel = 1.09
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                
                i = self.search_window_id(WINDOW_ID_MAIN_MENU)
                self.window[i].vy = -0.1            #メインメニューウィンドウを左上にフッ飛ばしていく
                self.window[i].vy_accel = 1.1
                self.window[i].vx = -0.1
                self.window[i].vx_accel = 1.1
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.game_quit_from_playing = 0                  #タイトルメニューからの終了
                self.game_status = SCENE_GAME_QUIT_START         #ステータスを「GAME QUIT START」ゲーム終了工程開始にする

    #!ゲームスタート時の初期化#########################################
    def update_game_start_init(self):
        self.score = 0               #スコア
        self.my_shield = 5           #自機のシールド耐久値
        self.my_speed = 1            #自機の初期スピード
        
        self.my_x = 24    #自機のx座標の初期値
        self.my_y = 50    #自機のy座標の初期値
        self.my_vx = 1    #自機のx方向の移動量
        self.my_vy = 0    #自機のy方向の移動量
        
        self.run_away_bullet_probability = 10 #敵が過ぎ去っていくときに弾を出す確率
        
        self.game_playing_flag = 1     #ゲームプレイフラグを「ゲームプレイ中」にする
        self.select_cursor_flag = 0   #セレクトカーソルの移動更新は行わないのでフラグを降ろす
        
        self.select_shot_id = 0        #現在使用しているショットのIDナンバー(ナンバーの詳細はshot_levelを参照するのです！)
        
        self.shot_exp = 0                   #自機ショットの経験値 パワーアップアイテムを取ることにより経験値がたまりショットのレベルが上がっていく
        self.shot_level = 0                 #自機ショットのレベル  0~3バルカンショット  4=レーザー 5=ツインレーザー 6=3WAYレーザー
                                            #7=ウェーブカッターLv1  8=ウェーブカッターLv2  9=ウェーブカッターLv3   10=ウェーブカッターLv4
        self.shot_speed_magnification=1     #自機ショットのスピードに掛ける倍率(vxに掛け合わせる)  
        self.shot_rapid_of_fire = 1         #自機ショットの連射数  初期値は1連射
        
        self.missile_exp = 0               #自機ミサイルの経験値 パワーアップアイテムを取ることにより経験値が溜まりミサイルのレベルが上がっていく
        self.missile_level = 0             #自機ミサイルのレベル  0~2 0=右下のみ  1=右下左上前方2方向  2=右下右上  左下左上4方向
        self.missile_speed_magnification=1 #自機ミサイルのスピードに掛ける倍率(vxに掛け合わせる)
        self.missile_rapid_of_fire = 1     #自機ミサイルの連射数  初期値は1連射
        
        self.select_sub_weapon_id = 0      #現在使用しているサブウェポンのIDナンバー -1だと何も所有していない状態
        self.sub_weapon_list = [5,10,10,3,10] #どのサブウェポンを所持しているかのリスト(インデックスオフセット値)
                                        #0=テイルショット 1=ペネトレートロケット 2=サーチレーザー 3=ホーミングミサイル 4=ショックバンバー
        self.star_scroll_speed = 1          #背景の流れる星のスクロールスピード 1=通常スピード 0.5なら半分のスピードとなります
        #self.pow_item_bounce_num = 6       #パワーアップアイテムが画面の左端で跳ね返って戻ってくる回数
                                            #初期値は6でアップグレードすると増えていくです
        
        self.playtime_frame_counter    = 0 #プレイ時間(フレームのカウンター) 60フレームで＝1秒        
        self.one_game_playtime_seconds = 0 #1プレイでのゲームプレイ時間(秒単位)
        
        self.game_play_count = 0        #ゲーム開始から経過したフレームカウント数(1フレームは60分の1秒)1面～今プレイしている面までのトータルフレームカウント数です
        self.rnd09_num = 0              #乱数0~9ルーレットの初期化
        
        self.replay_stage_num = 0       #リプレイ再生、録画時のステージ数を0で初期化します(1ステージ目=0→2ステージ目=1→3ステージ目=2って感じ)
        
        if self.replay_status != REPLAY_PLAY:       #リプレイデータでの再生時は乱数の種の更新は行いません、それ以外の時は更新します
            self.rnd_seed = pyxel.frame_count % 256 #線形合同法を使った乱数関数で使用する乱数種を現在のフレーム数とします(0~255の範囲)
            self.master_rnd_seed = self.rnd_seed    #リプレイデータ記録用として元となる乱数種を保存しておきます
        
        self.claw_type = 0              # クローのタイプ 
                                        # 0=ローリングクロー 1=トレースクロー 2=フィックスクロー 3=リバースクロー
        self.claw_number = 0            # クローの装備数 0=装備無し 1=1機 2=2機 3=3機 4=4機
        self.claw_difference = 360      # クロ―同士の角度間隔 1機=360 2機=180度 3機=120度 4機=90度
        self.trace_claw_index = 0       #トレースクロー（オプション）時のトレース用配列のインデックス値
        self.trace_claw_distance = 12   #トレースクロー同士の間隔
        self.fix_claw_magnification = 1 #フイックスクロー同士の間隔の倍率 0.5~2まで0.1刻み
        self.reverse_claw_svx = 1       #リバースクロー用の攻撃方向ベクトル(x軸)
        self.reverse_claw_svy = 0       #リバースクロー用の攻撃方向ベクトル(y軸)
        self.claw_shot_speed = 2        #クローショットのスピード（初期値は移動量２ドット）
        
        self.ls_shield_hp = 0           #L'sシールドの耐久力 0=シールド装備していない 1以上はシールド耐久値を示す
        
        self.claw = []                  #クローのリスト初期化 クローのリストはステージスタート時に初期化してしまうと次のステージに進んだときクローが消滅してしまうのでgame_start_initで初期化します
        
        #難易度に応じた数値をリストから取得する
        self.get_difficulty_data() #難易度データリストから数値を取り出す関数の呼び出し
        #ランクに応じた数値をリストから取得する
        self.get_rank_data() #ランクデータリストから数値を取り出す関数の呼び出し
        
        self.shot_table_list = self.j_python_shot_table_list      #とりあえずショットテーブルリストは初期機体のj_pythonのものをコピーして使用します
                                                        #将来的には選択した機体で色々な機体のリストがコピーされるはず
        self.missile_table_list = self.j_python_missile_table_list #とりあえずミサイルテーブルリストは初期機体のj_pythonのものをコピーして使用します
                                                        #将来的には選択した機体で色々な機体のリストがコピーされるはず・・・ほんとかなぁ？
        
        #ゲームスタート時のいろいろなボーナスの処理
        self.shot_exp  += self.start_bonus_shot
        self.missile_exp += self.start_bonus_missile
        self.my_shield += self.start_bonus_shield
        self.level_up_my_shot()            #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
        self.level_up_my_missile()         #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
        if self.start_claw == ONE_CLAW:    #ゲーム開始時クローの数が1の時は
            self.update_append_claw()      #クロー追加ボーナスの数値の回数分、追加関数を呼び出す
        elif self.start_claw == TWO_CLAW:  #ゲーム開始時クローの数が2の時は
            self.update_append_claw()      #2回呼び出し
            self.update_append_claw()
        elif self.start_claw == THREE_CLAW:#ゲーム開始時クローの数が3の時は
            self.update_append_claw()       #3回呼び出し
            self.update_append_claw()
            self.update_append_claw()

    #!ステージスタート時の初期化#######################################
    def update_stage_start_init(self):
        #画像リソースファイルを読み込みます
        pyxel.load("assets/graphic/min-sht2.pyxres")
        pygame.mixer.init(frequency = 44100)    #pygameミキサー関連の初期化
        pygame.mixer.music.set_volume(0.7)      #音量設定(0~1の範囲内)
        self.load_stage_bgm()                   #BGMファイルの読み込み
        pygame.mixer.music.play(-1)             #BGMループ再生
        self.my_x = 24    #自機のx座標の初期値
        self.my_y = 50    #自機のy座標の初期値
        self.my_vx = 1    #自機のx方向の移動量
        self.my_vy = 0    #自機のy方向の移動量
        
        if self.replay_status == REPLAY_RECORD:
            self.update_save_replay_stage_data()    #リプレイ保存時は,ステージスタート時のパラメーターをセーブする関数を呼び出します(リプレイ再生で使用)
            
        elif self.replay_status == REPLAY_PLAY:
            
            self.update_load_replay_stage_data()    #リプレイ再生時は,ステージスタート時のパラメーターをロードする関数を呼び出します
        
        self.pad_data_h = 0b00000000#パッド入力用ビットパターンデータを初期化します
        self.pad_data_l = 0b00000000#各ビットの詳細
                                    #上位バイトから 0,0,0,0, RS,LS,START,SELECT
                                    #下位バイトは   BY,BX,BB,BA, R,L,D,U
                                    # U=上 D=下 L=左 R=右 BA~BY=各ボタン START,SELECT=スタート,セレクト LS,RS=左ショルダー,右ショルダーボタン
        self.replay_frame_index = 0 #リプレイ時のフレームインデックス値を初期化
        
        #各ステージに応じた数値をリストから取得する
        self.get_stage_data()             #ステージデータリストからステージごとに設定された数値を取り出す関数の呼び出し
        
        self.present_repair_item_flag = 0 #ボス破壊後の爆発シーンでリペアアイテムを出すときに使用するフラグ 0=まだアイテム出してない 1=アイテム放出したよ～
        self.rank_down_count = 0          #ダメージを受けて難易度別に設定された規定値まで行ったかどうかをカウントする変数
        self.bg_cls_color = 0             #BGをCLS(クリアスクリーン)するときの色の指定(通常は0=黒色です) ゲーム中のイベントで変化することもあるのでステージスタート時でも初期化する
        self.bg_transparent_color = 0     #BGタイルマップを敷き詰めるときに指定する透明色です          ゲーム中のイベントで変化することもあるのでステージスタート時でも初期化する
        
        self.my_boost_injection_count = 0 #ステージクリア後のブースト噴射用のカウンター
        
        self.timer_flare_flag = 0         #タイマーフレア（触れると物質の時間経過が遅くなるフレア）を放出するかどうかのフラグ
        
        self.move_mode_auto_x,self.move_mode_auto_y = 0,0 #自動移動モードがonの時はこの座標に向かって毎フレームごと自動で移動して行きます
        self.move_mode_auto_complete                = 0   #自動移動モードで目標座標まで移動したらこのフラグを立てます
        
        self.add_appear_flag = 0     #敵を追加発生させる時に立てるフラグです
        
        self.record_games_status = 0 #ポーズを掛けたときに直前のゲームステータスを記録しておく変数
        
        self.scroll_count = 0           #ステージ開始からスクロールした背景のドット数カウンタ
                                        #(スクロールスピードが小数になったときはこのカウントも少数になるので注意！)
        self.vertical_scroll_count = 0  #ステージ開始から縦スクロールした背景のドット数カウンタ 主に縦スクロールするステージで使用します
                                        #(スクロールスピードが小数になったときはこのカウントも小数になるので注意！)
        
        self.stage_count = 0          #ステージ開始から経過したフレームカウント数(1フレームは60分の1秒)常に整数だよ
        
        self.side_scroll_speed              =1  #横スクロールするスピードの現在値が入ります 1フレームで1ドットスクロール(実数ですのん)
        self.side_scroll_speed_set_value    =1  #横スクロールスピードの設定値(変化量の分だけ1フレームごと増加減させ、この設定値までもって行く)
        self.side_scroll_speed_variation    =0  #横スクロールスピードを変化させる時の差分(変化量)
        
        self.vertical_scroll_speed           =0  #縦スクロールするスピードの現在値が入ります 1フレームで1ドットスクロール(実数ですのん)
        self.vertical_scroll_speed_set_value =0  #縦スクロールスピードの設定値(変化量の分だけ1フレームごと増加減させ、この設定値までもって行く)
        self.vertical_scroll_speed_variation =0  #縦スクロールスピードを変化させる時の差分(変化量)
        
        self.display_cloud_flag    = 0    #背景の流れる雲を表示するかどうかのフラグ(0=表示しない 1=表示する)
        
        self.cloud_append_interval = 6    #雲を追加させる間隔
        self.cloud_quantity        = 0    #雲の量
        self.cloud_how_flow        = 0    #雲の流れ方
        self.cloud_flow_speed      = 0    #雲の流れるスピード
        
        self.warning_dialog_flag         = 0 #WARINIGダイアログを表示するかどうかのフラグ
        self.warning_dialog_display_time = 0 #WARINIGダイアログの表示時間(フレーム単位)
        self.warning_dialog_logo_time    = 0 #WARNINGグラフイックロゴの表示に掛ける時間(フレーム単位)
        self.warning_dialog_text_time    = 0 #WARNINGテキスト表示に掛ける時間(フレーム単位)
        
        self.stage_clear_dialog_flag         = 0 #STAGE CLEARダイアログを表示するかどうかのフラグ
        self.stage_clear_dialog_display_time = 0 #STAGE CLEARダイアログの表示時間(フレーム単位)
        self.stage_clear_dialog_logo_time1   = 0 #STAGE CLEARグラフイックロゴの表示に掛ける時間その１(フレーム単位)
        self.stage_clear_dialog_logo_time2   = 0 #STAGE CLEARグラフイックロゴの表示に掛ける時間その２(フレーム単位)
        self.stage_clear_dialog_text_time    = 0 #STAGE CLEARテキスト表示に掛ける時間(フレーム単位)
        
        self.event_index = 0                #イベントリストのインデックス値（イベントリストが現在どの位置にあるのかを示す値です）
        self.type_check_quantity = 0        #特定のショットタイプがリストにどれだけあるのかチェックして数えた数がここに入る
        self.my_ship_explosion_timer = 0    #自機が爆発した後、まだどれだけゲームが進行するかのタイマーカウント
        self.game_over_timer = 0            #ゲームオーバーダイアログを表示した後まだどれだけゲームが進行するかのタイマーカウント
        self.fade_in_out_counter = 0        #フェードイン＆フェードアウト用エフェクトスクリーン用のカウンタ（基本的にx軸(キャラクター単位）の値です)
                                            #0~19 で 19になった状態が一番右端を描画したという事になります
                                            #19になった時点で完了となります
        self.fade_complete_flag = 0             #フェードイン＆フェードアウトが完了したかのフラグが入る所(0=まだ終わっていない 1=完了！)
        self.shadow_in_out_counter = 0          #シャドウイン＆シャドウアウト用エフェクトスクリーン用のカウンタ
        self.shadow_in_out_complete_flag = 0    #シャドウイン＆シャドウアウトが完了したかのフラグが入る所(0=まだ終わっていない 1=完了！)
        
        self.current_formation_id = 1   #現在の敵編隊のＩＤナンバー（0は単独機で編隊群は1からの数字が割り当てられます）
                                        #編隊が1編隊出現するごとにこの数字が1増えていく
                                        #例 1→2→3→4→5→6→7→8→9→10みたいな感じで増えていく
        self.fast_forward_destruction_num = 0       #早回しの条件を満たすのに必要な「破壊するべき編隊の総数」が入ります
        self.fast_forward_destruction_count = 0     #破壊するべき編隊の総数」が1以上ならば編隊を破壊すると次の編隊の出現カウントがこの数値だけ少なくなり出現が早まります
        self.add_appear_flag = 0                    #早回しの条件をすべて満たしたときに建つフラグです、このフラグが立った時、イベントリストに「EVENT_ADD_APPEAR_ENEMY」があったらそこで敵編隊を追加発生させます
        
        self.my_rolling_flag = 0    #0=通常の向き  1=下方向に移動中のキャラチップ使用  2=上方向に移動中のキャラチップ使用
        self.my_moved_flag = 0      #自機が移動したかどうかのフラグ（トレースクローの時、自機のＸＹ座標を履歴リストに記録するのか？しないのか？で使う）
                                    #0=自機は止まっているので座標履歴リストに記録はしない 
                                    #1=自機は移動したので座標履歴リストに記録する
        
        self.invincible_counter = 0 #無敵時間(単位はフレーム)のカウンタ 0の時以外は無敵状態です
        
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
        self.enemy = []                #敵のリスト
        self.enemy_shot = []           #敵の弾のリスト
        self.obtain_item = []          #取得アイテム類のリスト(パワーアップカプセルなど)
        self.stars = []                #背景の流れる星々のリスト         当たり判定はありません
        self.explosions = []           #爆発パターン群のリスト           当たり判定はありません
        self.particle = []             #パーティクル（火花の粒子）のリスト  当たり判定はありません
        self.background_object = []    #背景オブジェクトのリスト         当たり判定はありません
        self.window = []               #メッセージウィンドウのリスト       当たり判定はありません
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
        #EVENT_ENEMY            敵の出現                [敵キャラのＩＤナンバー,出現x座標,出現y座標,編隊群の場合は編隊数の指定]
        #EVENT_WARNING          ワーニングダイアログ表示     [警告表示時間,グラフイックロゴ表示に掛ける時間,テキスト表示に掛ける時間](単位は全てフレームです)
        #EVENT_BOSS            各ステージに対応したボスを出現させる
        #EVENT_ADD_APPEAR_ENEMY   早回しの条件が成立したとき敵を出現させる [敵キャラのＩＤナンバー,出現x座標,出現y座標,編隊数]
        #EVENT_SCROLL           スクロール制御
        #   SCROLL_NUM_SET        スクロール関連のパラメーター設定 [横スクロールスピード設定値,横スクロールスピードの変化量,縦スクロールスピード設定値,縦スクロールスピードの変化量]
        #   SCROLL_START          スクロールの開始（横スクロールでスピードは通常の1)
        #   SCROLL_STOP           スクロールの停止
        #   SCROLL_SPEED_CHANGE    スクロールスピードを変化させる[スクロールスピードの設定値(-ならバックスクロール),スクロールスピードの変化量(-なら減速,+なら加速)]
        #   VERTICAL_SCROLL_START   縦スクロールの開始
        #   VERTICAL_SCROLL_STOP    縦スクロールのスタート
        #EVENT_DISPLAY_STAR      背景星スクロールのon/off [0=off/1=on]
        #EVENT_CHANGE_BG_CLS_COLOR 背景でまず最初に塗りつぶす色の指定 0~15 pyxelのカラーコード
        #EVENT_CHANGE_BG_TRANSPARENT_COLOR 背景マップチップを敷き詰める時に使用する透明色の指定 0~15 pyxelのカラーコード
        #EVENT_CLOUD            背景の雲の制御
        #   CLOUD_NUM_SET          雲のパラメータ設定[発生させる間隔(単位はフレーム),
        #                                    雲の量(0=比較的小さい雲だけ,1=小中サイズの雲を流す,2=小中大すべての種類の雲を流す),
        #                                    流れ方(0=そのまま左に素直に流れていく-0.25=上方向に流されていく0.25=下方向に流されていく),
        #                                    流れるスピード(倍率となります,通常は1,少数も使用可です)
        #                                    ]            
        #   CLOUD_START            雲を流すのを開始する
        #   CLOUS_STOP            雲を流すのを停止する
        #EVENT_RASTER_SCROLL        ラスタースクロールの制御
        #   RASTER_SCROLL_OFF         ラスタースクロールの表示をoffにする[表示オフにするラスタスクロールのid]
        #   RASTER_SCROLL_ON          ラスタースクロールの表示をonにする [表示オンにするラスタスクロールのid]
        #EVENT_BG_SCREEN_ON_OFF    背景ＢＧの表示のon/off
        #   BG_BACK or BG_MIDDLE or BG_FRONT  BGの種類を選択
        #   DISP_OFF or DISP_ON            表示オフ/表示オン
        #EVENT_ENTRY_SPARK_ON_OFF  大気圏突入の火花表示のon/off
        #   SPARK_OFF or SPARK_ON           火花表示on/off
        
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
            
            [ 200,EVENT_ENEMY,CIR_COIN    ,160, 40   ,6],
            [ 300,EVENT_SCROLL,SCROLL_NUM_SET,    2,0.5,        0.5,0.01],
            [ 303,EVENT_ENTRY_SPARK_ON_OFF,SPARK_ON],
            [ 350,EVENT_SCROLL,SCROLL_NUM_SET,  2.5,0.5,        0.5,0.01],
            [ 400,EVENT_SCROLL,SCROLL_NUM_SET,    3,0.5,        0.5,0.01],
            [ 403,EVENT_ENEMY,CIR_COIN    ,160, 70   ,6],
            [ 450,EVENT_SCROLL,SCROLL_NUM_SET,  3.5,0.5,        0.5,0.01],
            [ 500,EVENT_SCROLL,SCROLL_NUM_SET,    4,0.5,        0.5,0.01],
            [ 550,EVENT_ENEMY,CIR_COIN    ,160, 40   ,6],
            [ 600,EVENT_SCROLL,SCROLL_NUM_SET,    5,0.5,        0.5,0.01],
            [ 690,EVENT_ENEMY,CIR_COIN    ,160, 70   ,6],
            [ 700,EVENT_SCROLL,SCROLL_NUM_SET,    6,0.5,        0.5,0.01],
            [ 800,EVENT_SCROLL,SCROLL_NUM_SET,    7,0.5,        0.5,0.01],
            [ 891,EVENT_ENEMY,SAISEE_RO,170, 50-10],
            [ 892,EVENT_ENEMY,SAISEE_RO,169, 50   ],
            [ 893,EVENT_ENEMY,SAISEE_RO,168, 50+10],
            [ 900,EVENT_SCROLL,SCROLL_NUM_SET,    8,0.5,        0.5,0.01],
            
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
            
            [1500,EVENT_DISPLAY_STAR,           DISP_OFF],
            [1510,EVENT_CHANGE_BG_CLS_COLOR,        12],
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
            
            [3200,EVENT_WARNING,500,120,240],
            
            
            [3320,EVENT_SCROLL,SCROLL_SPEED_CHANGE,3.0,0.0001],
            [3340,EVENT_BOSS],
            
            [3420,EVENT_SCROLL,SCROLL_SPEED_CHANGE,4.0,0.001],
            
            
            
            [99999999],]
            
        self.event_list_stage_mountain_region_l2= [
            
            [ 300,EVENT_SCROLL,SCROLL_NUM_SET,    2,0.5,        0.5,0.01],
            [ 350,EVENT_SCROLL,SCROLL_NUM_SET,  2.5,0.5,        0.5,0.01],
            [ 400,EVENT_SCROLL,SCROLL_NUM_SET,    3,0.5,        0.5,0.01],
            [ 450,EVENT_SCROLL,SCROLL_NUM_SET,  3.5,0.5,        0.5,0.01],
            [ 500,EVENT_SCROLL,SCROLL_NUM_SET,    4,0.5,        0.5,0.01],
            [ 600,EVENT_SCROLL,SCROLL_NUM_SET,    5,0.5,        0.5,0.01],
            [ 700,EVENT_SCROLL,SCROLL_NUM_SET,    6,0.5,        0.5,0.01],
            [ 800,EVENT_SCROLL,SCROLL_NUM_SET,    7,0.5,        0.5,0.01],
            [ 900,EVENT_SCROLL,SCROLL_NUM_SET,    8,0.5,        0.5,0.01],
            
            [1000,EVENT_CLOUD,CLOUD_NUM_SET,6,1,-0.25,1],
            
            [1010,EVENT_CLOUD,CLOUD_START],
            
            [1500,EVENT_DISPLAY_STAR,           0],
            [1510,EVENT_CHANGE_BG_CLS_COLOR,        12],
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
            [ 200,EVENT_ENEMY,CIR_COIN    ,160, 10   ,6],
            [ 500,EVENT_ENEMY,CIR_COIN    ,160, 90   ,6],
            [ 700,EVENT_ENEMY,CIR_COIN    ,160, 20   ,6],
            [ 900,EVENT_ENEMY,CIR_COIN    ,160, 80   ,6],
            
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
            [ 200,EVENT_ENEMY,CIR_COIN    ,160, 10   ,6],
            [ 500,EVENT_ENEMY,CIR_COIN    ,160, 90   ,6],
            [ 700,EVENT_ENEMY,CIR_COIN    ,160, 20   ,6],
            [ 900,EVENT_ENEMY,CIR_COIN    ,160, 80   ,6],
            
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
            [ 200,EVENT_ENEMY,CIR_COIN    ,160, 10   ,6],
            [ 500,EVENT_ENEMY,CIR_COIN    ,160, 90   ,6],
            [ 700,EVENT_ENEMY,CIR_COIN    ,160, 20   ,6],
            [ 900,EVENT_ENEMY,CIR_COIN    ,160, 80   ,6],
            
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
                            
                            [self.event_list_stage_advance_base_l1,
                            self.event_list_stage_advance_base_l2,
                            self.event_list_stage_advance_base_l3]
                            ]
        
        #self.game_event_list = [self.event_list_no_enemy_mode,  self.event_list_no_enemy_mode,  self.event_list_no_enemy_mode]
        
        #各ステージのＢＧ書き換えによるアニメーションの為のデータリスト群
        #フォーマットの説明
        #[アニメーションさせたいマップチップのx座標(0~255(8の倍数にしてね)),
        #                            y座標(0~255(8の倍数にしてね)),
        #                           アニメスピード(1なら1フレーム毎 2だと2フレーム毎って感じ),
        #                           アニメ枚数(横一列に並べてください)]
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
        
        self.bg_animation_list = self.bg_animation_list_mountain_region    #とりあえずBGアニメーションパターンリストはmountain_regionのものをコピーして使用します
        
        #自機のXY座標をトレースクローのXY座標としてコピーし、初期化を行う(とりあえず60要素埋め尽くす)(60要素=60フレーム分=1秒過去分まで記録される)
        for _i in range(TRACE_CLAW_BUFFER_SIZE):
            new_traceclaw = Trace_coordinates()
            new_traceclaw.update(self.my_x,self.my_y)
            self.claw_coordinates.append(new_traceclaw)
        
        self.create_raster_scroll_data() #ラスタースクロール用のデータの初期化＆育成

    #自機の移動          キーボードとゲームパッド、または移動座標先を指定しての「自動移動モード」による自機の移動処理を行う関数です
    def update_my_ship(self):
        self.my_rolling_flag = 0  #自機ローリングフラグ(旋回フラグ)を0に初期化する
        self.my_moved_flag = 0    #自機が動いたかどうかのフラグを0に初期化する
        
        if self.game_status == SCENE_STAGE_CLEAR_MY_SHIP_BOOST: #ゲームステータスが「ステージクリア後、自機がブースト加速して右に過ぎ去っていく」なら
            self.my_x += self.my_vx
            self.my_vx += 0.025                #速度0.01で加速していく
            self.my_boost_injection_count += 1 #ステージクリア後のブースト噴射用のカウンターを1増やしていく
            self.my_moved_flag = 1             #トレースクローも動かしたいので自機移動フラグOnにする
            
        elif self.replay_status != REPLAY_PLAY and self.move_mode == MOVE_MANUAL: #リプレイステータスが(再生中)では無い & 移動モードが(MANUAL)の時は
            self.my_vx,self.my_vy = 0,0 #自機の自機の移動量(vx,vy)を0に初期化する
            
            # 左入力があったのなら  x座標を  1*my_speedの数値だけ減らす
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT) or pyxel.btn(pyxel.GAMEPAD_2_LEFT):
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vx = -1
                self.pad_data_l += PAD_LEFT
            
            # 右入力があったのなら  x座標を  1*my_speedの数値だけ増やす
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT) or pyxel.btn(pyxel.GAMEPAD_2_RIGHT):
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vx = 1
                self.pad_data_l += PAD_RIGHT
            
            # 上入力があったのなら  y座標を  1*my_speedの数値だけ減らす
            if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD_1_UP) or pyxel.btn(pyxel.GAMEPAD_2_UP):
                self.my_rolling_flag = 2
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vy = -1
                self.pad_data_l += PAD_UP
            
            # 下入力があったのなら  y座標を  1*my_speedの数値だけ増やす
            if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD_1_DOWN) or pyxel.btn(pyxel.GAMEPAD_2_DOWN):
                self.my_rolling_flag = 1
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vy = 1
                self.pad_data_l += PAD_DOWN
            
            self.my_x += self.my_vx * self.my_speed #自機の移動量(vx,vy)と自機の速度(speed)を使って自機の座標を更新する（移動！）
            self.my_y += self.my_vy * self.my_speed
            
        elif self.replay_status == REPLAY_PLAY and self.move_mode == MOVE_MANUAL: #リプレイステータスが「PLAY」で移動モードが「MANUAL」のときは
            self.my_vx,self.my_vy = 0,0 #自機の自機の移動量(vx,vy)を0に初期化する
            #self.replay_frame_index    インデックス値のリストの内容はパッド入力データのHigh Byte
            #self.replay_frame_index + 1インデックス値のリストの内容はパッド入力データのLow Byte となります
            #リプレイデータを調べて左入力だったのなら  x座標を  my_speedの数値だけ減らす
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00000100 == 0b00000100:  #LowByte
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vx = -1
            
            #リプレイデータを調べて右入力があったのなら x座標を  my_speedの数値だけ増やす
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00001000 == 0b00001000:  #LowByte
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vx = 1
            
            #リプレイデータを調べて上入力があったのなら y座標を  my_speedの数値だけ減らす
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00000001 == 0b00000001:  #LowByte
                self.my_rolling_flag = 2
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vy = -1
            
            #リプレイデータを調べて下入力があったのなら y座標を  my_speedの数値だけ増やす
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00000010 == 0b00000010:  #LowByte
                self.my_rolling_flag = 1
                self.my_moved_flag = 1#自機移動フラグOn
                self.my_vy = 1
            
            self.my_x += self.my_vx * self.my_speed #自機の移動量(vx,vy)と自機の速度(speed)を使って自機の座標を更新する（移動！）
            self.my_y += self.my_vy * self.my_speed
            
        elif self.move_mode == MOVE_AUTO and self.move_mode_auto_complete == 0: #移動モード「AUTO」&まだ移動完了フラグが建っていなかったら・・・
            self.my_vx,self.my_vy = 0,0 #自機の自機の移動量(vx,vy)を0に初期化する
            
            if self.my_x > self.move_mode_auto_x:
                self.my_moved_flag = 1                #自機移動フラグOn
                self.my_vx = -0.5                     #左に自動移動
            else:
                self.my_moved_flag = 1                #自機移動フラグOn
                self.my_vx = 0.5                      #右に自動移動
            
            if self.my_y > self.move_mode_auto_y:
                self.my_rolling_flag = 2
                self.my_moved_flag = 1                #自機移動フラグOn
                self.my_vy = -0.5                     #上に自動移動
            else:
                self.my_rolling_flag = 1
                self.my_moved_flag = 1                #自機移動フラグOn
                self.my_vy = 0.5                      #下に自動移動
            
            self.my_x += self.my_vx #自機の移動量(vx,vy)を使って自機の座標を更新する（移動！）
            self.my_y += self.my_vy
            
            if -1 <= self.my_x - self.move_mode_auto_x <= 1 and -1 <= self.my_y - self.move_mode_auto_y <= 1: #自機座標(x,y)と移動目的先の座標の差が誤差+-1以内ならば
                self.move_mode_auto_complete = 1    #自動移動完了フラグをonにする
                if self.game_status == SCENE_STAGE_CLEAR_MOVE_MY_SHIP: #ゲームステータスが「ステージクリア後の自機自動移動」だったら
                    self.move_mode = MOVE_MANUAL    #自動移動モードを解除し手動移動モードに移行します
                    self.game_status = SCENE_STAGE_CLEAR_MY_SHIP_BOOST   #ゲームステータスを「ステージクリア後、自機がブーストして右へ過ぎ去っていくシーン」にする
                    self.my_vx = -1.3 #ブースト開始の初期スピードは左へ1ドット毎フレーム（ちょっと左に戻ってから加速し、右へ飛んでいく）
                    self.my_boost_injection_count = 1 #ステージクリア後のブースト噴射用のカウンターの数値を初期化
                    self.my_moved_flag = 1          #トレースクローも動かしたいので自機移動フラグOnにする
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

    #キーボードの1が推されたらショット経験値を増やしていく                              KEY 1
    def update_powerup_shot(self):
        if pyxel.btnp(pyxel.KEY_1):
            self.shot_exp += 1  #ショット経験値を１増やして武器をアップグレードさせていく
            self.level_up_my_shot() #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
            if self.shot_level > 10:
                self.shot_level = 0

    #キーボードの2が推されたらミサイル経験値を増やしていく                              KEY 2
    def update_powerup_missile(self):
        if pyxel.btnp(pyxel.KEY_2):
            self.missile_exp += 1#ミサイル経験値を１増やしてミサイルをアップグレードさせていく
            self.level_up_my_missile() #自機ミサイルの経験値を調べ可能な場合はレベルアップさせる関数を呼び出す
            if self.missile_level > 2:
                self.missile_level = 0

    #キーボードの3かゲームパッドの「SELECT」ボタンが入力されたボタンが押されたか？チェックする(スピードチェンジ)     KEY 3 GAMEPAD SELECT
    def update_check_change_speed(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index] & 0b00000001 == 0b00000001: #HighByte リプレイデータを調べてPAD SELECTが押された記録だったのなら...
                self.update_change_speed() #スピードチェンジ関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btnp(pyxel.KEY_3) or pyxel.btnp(pyxel.GAMEPAD_1_SELECT) or pyxel.btnp(pyxel.GAMEPAD_2_SELECT):
                self.pad_data_h += PAD_SELECT #パッド入力データのSELECTボタンの情報ビットを立てる
                self.update_change_speed() #スピードチェンジ関数呼び出し！

    #自機のスピードチェンジ!!!!
    def update_change_speed(self):
        if self.my_speed == 1:
            self.my_speed = 1.5
        elif self.my_speed == 1.5:
            self.my_speed = 1.75
        else:
            self.my_speed = 1

    #スペースキーかゲームパッドAが押されたかどうか？もしくはリプレイモードでショット発射したのか調べる     KEY SPACE GAMEPAD A
    def update_check_fire_shot(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1 ] & 0b00010000 == 0b00010000: #LowByte リプレイデータを調べてPAD Aが押された記録だったのなら...
                self.update_fire_shot() #ショット発射関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD_1_A) or pyxel.btn(pyxel.GAMEPAD_2_A): #パッドAかスペースキーが押されたか？
                self.pad_data_l += PAD_A #コントロールパッド入力記録にAボタンを押した情報ビットを立てて記録する
                self.update_fire_shot() #ショット発射関数呼び出し！

    #ショットを発射する!!!!!
    def update_fire_shot(self):
        if self.shot_level == SHOT_LV7_WAVE_CUTTER_LV1:#ウェーブカッターLv1発射
            if len(self.shots) < self.shot_rapid_of_fire:
            #if self.shot_type_count(self.shot_level) < 3: 
                if (pyxel.frame_count % 8) == 0:
                    pyxel.play(2,5) #チャンネル2でサウンドナンバー5を鳴らす
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y -4,      3,0,  8,16,  0,   2,1)
                    
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV8_WAVE_CUTTER_LV2:#ウェーブカッターLv2発射
            if len(self.shots) < self.shot_rapid_of_fire:
                if (pyxel.frame_count % 8) == 0:
                    pyxel.play(2,5)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y -8,      3,0,  8,24,  0,   2,1)
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV9_WAVE_CUTTER_LV3:#ウェーブカッターLv3発射
            if len(self.shots) < self.shot_rapid_of_fire:
                if (pyxel.frame_count % 8) == 0:
                    pyxel.play(2,5)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y -12,      3,0,  8,32,  0,   2,1)
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV10_WAVE_CUTTER_LV4:#ウェーブカッターLv4発射
            if len(self.shots) < self.shot_rapid_of_fire:
                if (pyxel.frame_count % 6) == 0:
                    pyxel.play(2,5)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y -12,      4,0,  8,32,  0,   2,1)
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV4_LASER:#レーザー発射
            if len(self.shots) < 20:
                if (pyxel.frame_count % 2) == 0:
                    pyxel.play(2,4)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y,         3,1,  8,8,  0,   0.3,1)
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV5_TWIN_LASER:#ツインレーザー発射
            if len(self.shots) < 40:
                if (pyxel.frame_count % 2) == 0:
                    pyxel.play(2,4)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y - 3,     3,1,  8,8,  -3,  0.3,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 5,self.my_y + 3,     3,1,  8,8,    3, 0.3,1)
                    self.shots.append(new_shot)
        
        if self.shot_level == SHOT_LV6_3WAY_LASER:#３ＷＡＹレーザー発射
            if len(self.shots) < 80:
                if (pyxel.frame_count % 2) == 0:
                    pyxel.play(2,4)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 1,self.my_y  -1,    1,-1.08,   8,8,   -1,  0.2,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y,       3,1,      8,8,    0,  0.3,1)
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
            new_missile.update(5,self.my_x + 4,self.my_y,   -1,-0.8,   6,    1   ,0,0,   0,1,    8,8, 0,0,  0,0) #ペネトレートロケット
            self.missile.append(new_missile)#ペネトレートロケット育成
            
            new_missile = Missile()
            new_missile.update(5,self.my_x + 4,self.my_y,   -1,-0.8,   6,    1   ,0,0,   0,-1,    8,8, 0,0,  0,0) #ペネトレートロケット
            self.missile.append(new_missile)#ペネトレートロケット育成
        
        self.count_missile_type(4,4,4,4) #ミサイルタイプ4(テイルショット）がいくつ存在するのか調べる    
        if self.type_check_quantity < self.sub_weapon_tail_shot_level_data_list[self.sub_weapon_list[TAIL_SHOT]-1][1] and self.select_sub_weapon_id == TAIL_SHOT and (pyxel.frame_count % 6) == 0:#もしテイルショットが全く存在しないのなら発射する！！！
            level = self.sub_weapon_list[TAIL_SHOT] #現在のテイルショットのレベルを取得する
            #テイルショットのレベルデータリストから現時点のレベルに応じたデータを取得する
            speed = self.sub_weapon_tail_shot_level_data_list[level - 1][2] #スピード
            power = self.sub_weapon_tail_shot_level_data_list[level - 1][3] #攻撃力
            n_way = self.sub_weapon_tail_shot_level_data_list[level - 1][4] #n_way数
            if n_way == 1 or n_way == 3: #真後ろにテイルショット発射
                new_missile = Missile()
                new_missile.update(4,self.my_x - 4,self.my_y,   -2*speed,0,   power,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                self.missile.append(new_missile)#真後ろに射出されるテイルショット育成
                if n_way == 3: #3wayの場合は更に斜め後ろ方向にテイルショット発射
                    new_missile = Missile()
                    new_missile.update(4,self.my_x - 4,self.my_y - 2,   -2*speed,-0.5,   power,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                    self.missile.append(new_missile)#斜め後ろ(上)のテイルショット育成
                    
                    new_missile = Missile()
                    new_missile.update(4,self.my_x - 4,self.my_y + 2,   -2*speed, 0.5,   power,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                    self.missile.append(new_missile)#斜め後ろ(下)のテイルショット育成
                
            elif n_way == 2: #ツインテイルショット発射
                new_missile = Missile()
                new_missile.update(4,self.my_x - 4,self.my_y - 2,   -2*speed,0,   power,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                self.missile.append(new_missile)#ツインテイルショット(上)育成
                
                new_missile = Missile()
                new_missile.update(4,self.my_x - 4,self.my_y + 2,   -2*speed,0,   power,1,   0,0,   0,0,   8,8,  0,0,  0,0) #テイルショット
                self.missile.append(new_missile)#ツインテイルショット(下)育成
        
        self.count_missile_type(6,6,6,6) #ミサイルタイプ6(サーチレーザー）がいくつ存在するのか調べる
        if self.type_check_quantity <= 1 and self.select_sub_weapon_id == SEARCH_LASER and pyxel.frame_count % 32 == 0: #サーチレーザーが全く存在しないのなら発射する！！！
            new_missile = Missile()
            new_missile.update(6,self.my_x + 14,self.my_y,   2,0,   1,1,   0,1,   0,0,   16,8,  0,0,  0,0) #サーチレーザー(flag2=1なのでちょっとｘ軸前方向に対して索敵する)
            self.missile.append(new_missile)#サーチレーザー育成
            
            new_missile = Missile()
            new_missile.update(6,self.my_x    ,self.my_y,   2,0,   1,1,   0,0,   0,0,   16,8,  0,0,  0,0) #サーチレーザー
            self.missile.append(new_missile)#サーチレーザー育成
        
        self.count_missile_type(7,7,7,7) #ミサイルタイプ7(ホーミングミサイル）がいくつ存在するのか調べる
        if self.type_check_quantity <= self.sub_weapon_homing_missile_level_data_list[self.sub_weapon_list[HOMING_MISSILE]-1][1] - 4 and self.select_sub_weapon_id == HOMING_MISSILE and pyxel.frame_count % 8 == 0: #ホーミングミサイルの個数が1以下なら発射する！！！
            level = self.sub_weapon_list[HOMING_MISSILE] #現在のホーミングミサイルのレベルを取得する
            #ホーミングミサイルのレベルデータリストから現時点のレベルに応じたデータを取得する
            speed = self.sub_weapon_homing_missile_level_data_list[level - 1][2] #スピード
            power = self.sub_weapon_homing_missile_level_data_list[level - 1][3] #攻撃力
            new_missile = Missile()
            new_missile.update(7,self.my_x - 4,self.my_y,   -2*speed,1*speed,   power,1,   0,0,   0,0,   8,8,     200,60,   2,1)
            self.missile.append(new_missile)#ホーミングミサイル育成
            
            new_missile = Missile()
            new_missile.update(7,self.my_x - 4,self.my_y,   -2*speed,-1*speed,   power,1,   0,0,   0,0,   8,8,     200,60,   2,1)
            self.missile.append(new_missile)#ホーミングミサイル育成
            
            
            new_missile = Missile()
            new_missile.update(7,self.my_x + 4,self.my_y + 2,   0*speed,2*speed,   power,1,   0,0,   0,0,   8,8,     200,60,   2,1)
            self.missile.append(new_missile)#ホーミングミサイル育成
            
            new_missile = Missile()
            new_missile.update(7,self.my_x + 4,self.my_y - 2,   0*speed,-2*speed,   power,1,   0,0,   0,0,   8,8,     200,60,   2,1)
            self.missile.append(new_missile)#ホーミングミサイル育成
        
        if len(self.shots) < (self.shot_rapid_of_fire + (self.shot_level) * 2):#バルカンショットの発射
            if (pyxel.frame_count % 6) == 0:    
                if self.shot_level == SHOT_LV0_VULCAN_SHOT:#初期ショット バルカンショット1連装
                    pyxel.play(2,1)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 4,self.my_y    ,4,0,  8,8,    0, 1,1)
                    self.shots.append(new_shot)
                
                if self.shot_level == SHOT_LV1_TWIN_VULCAN_SHOT:#ツインバルカンショット 2連装
                    pyxel.play(2,1)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 2,4,0,  8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 2,4,0,  8,8,     0,  1,1)
                    self.shots.append(new_shot)
                
                if self.shot_level == SHOT_LV2_3WAY_VULCAN_SHOT:#３ＷＡＹバルカンショット
                    pyxel.play(2,1)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 2  ,5,-0.3,  8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y     ,5,0,    8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 2  ,5,0.3,   8,8,    0,  1,1)
                    self.shots.append(new_shot)
                
                if self.shot_level == SHOT_LV3_5WAY_VULCAN_SHOT:#５ＷＡＹバルカンショット
                    pyxel.play(2,1)
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 2,    5,-1,    8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y - 1,    5,-0.3,   8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y,       5,0,     8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 1,    5,0.3,    8,8,    0,  1,1)
                    self.shots.append(new_shot)
                    
                    new_shot = Shot()
                    new_shot.update(self.shot_level,self.my_x + 6,self.my_y + 2,    5,1,     8,8,    0,  1,1)
                    self.shots.append(new_shot)

    #スペースキーかゲームバットBボタンが押さたかどうか？もしくはリプレイモードでミサイル発射したのか調べる KEY SPACE GAMEPAD B
    def update_check_fire_missile(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00100000 == 0b00100000: #LowByte リプレイデータを調べてPAD Bが押された記録だったのなら...
                self.update_fire_missile() #ミサイル発射関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD_1_B) or pyxel.btn(pyxel.GAMEPAD_2_B): #パッドBかスペースキーが押されたか？
                self.pad_data_l += PAD_B #コントロールパッド入力記録にBボタンを押した情報ビットを立てて記録する
                self.update_fire_missile() #ミサイル発射関数呼び出し！

    #ミサイルを発射する!!!!!
    def update_fire_missile(self):
        if (pyxel.frame_count % 10) == 0:
            self.count_missile_type(0,1,2,3)#ミサイルタイプ0,1,2,3の合計数を数える
            if self.type_check_quantity < (self.missile_level + 1) * self.missile_rapid_of_fire:  #初期段階では２発以上は出せないようにする
                if self.missile_level == MISSILE_LV0_NORMAL_MISSILE:
                    pyxel.play(2,1)
                    
                    new_missile = Missile()
                    new_missile.update(0,self.my_x + 4,self.my_y,   0.7,0.7,   3,    1   ,0,0,    1,1,  8,8  ,0,0,   0,0) #前方右下に落ちていくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                elif self.missile_level == MISSILE_LV1_TWIN_MISSILE:
                    pyxel.play(2,1)
                    
                    new_missile = Missile()
                    new_missile.update(0,self.my_x + 2,self.my_y +2,   0.7,0.7,   3,    1   ,0,0,    1,1,  8,8,  0,0,   0,0) #前方右下に落ちていくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                    new_missile = Missile()
                    new_missile.update(1,self.my_x + 2,self.my_y -2,   0.7,0.7,   3,    1   ,0,0    ,1,-1,  8,8,  0,0,  0,0) #前方右上に飛んでいくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                elif self.missile_level == MISSILE_LV2_MULTI_MISSILE:
                    pyxel.play(2,1)
                    
                    new_missile = Missile()
                    new_missile.update(0,self.my_x +2,self.my_y +2,   0.7,0.7,    3,    1   ,0,0,    1,1,   8,8,  0,0,  0,0) #前方右下に落ちていくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                    new_missile = Missile()
                    new_missile.update(1,self.my_x +2,self.my_y -2,   0.7,0.7,    3,    1   ,0,0    ,1,-1,   8,8,  0,0,  0,0) #前方右上に飛んでいくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                    new_missile = Missile()
                    new_missile.update(2,self.my_x -2,self.my_y +2,   -0.7,0.7,   3,    1   ,0,0,    -1,1,    8,8,  0,0,   0,0) #後方左下に落ちていくミサイル
                    self.missile.append(new_missile)#ミサイル育成
                    
                    new_missile = Missile()
                    new_missile.update(3,self.my_x -2,self.my_y -2,   -0.7,0.7,   3,    1   ,0,0    ,-1,-1,   8,8,  0,0,   0,0) #後方左上に飛んでいくミサイル
                    self.missile.append(new_missile)#ミサイル育成

    #自機をはみ出さないようにする
    def update_clip_my_ship(self):
        if    self.game_status == SCENE_STAGE_CLEAR_MY_SHIP_BOOST\
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
                self.shots[i].posy += self.shots[i].vy                           #弾のY座標をVY分加減算して更新
                
            elif 4 <= self.shots[i].shot_type <= 6:#ショットタイプがレーザーの場合
                self.shots[i].posx += self.shots[i].vx#弾のX座標をVX分加減算して更新
                self.shots[i].offset_y = self.shots[i].offset_y * self.shots[i].vy#Ｙ軸オフセット値 vyの倍率ごと乗算して行って上下にずらしていく
                self.shots[i].posy = self.my_y + self.shots[i].offset_y#自機のｙ座標+Ｙ軸オフセット値をレーザーのＹ座標としてコピーする（ワインダー処理）
                self.shots[i].shot_hp = 1#レーザーなのでHPは減らず強制的にＨＰ＝１にする（ゾンビ化～みたいな）
                
            elif 7 <= self.shots[i].shot_type <= 10:#ショットタイプがウェーブカッターの場合
                self.shots[i].posx += self.shots[i].vx * self.shot_speed_magnification #弾のX座標をVX*speed_magnification(倍率)分加減算して更新
                self.shots[i].posy += self.shots[i].vy                           #弾のY座標をVY分加減算して更新
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
                if      self.enemy[e].posx                    <= self.shots[h].posx + 4 <= self.enemy[e].posx + self.enemy[e].width\
                    and self.enemy[e].posy - self.shots[h].height <= self.shots[h].posy + 4 <= self.enemy[e].posy + self.enemy[e].height:
                    self.enemy[e].enemy_hp -= self.shots[h].shot_power #敵の耐久力をShot_powerの分だけ減らす
                    if self.enemy[e].enemy_hp <= 0:
                        self.enemy_destruction(e) #敵破壊処理関数呼び出し！
                        #パーティクル生成
                        for _number in range(5):
                            self.update_append_particle(PARTICLE_DOT,self.enemy[e].posx + 4,self.enemy[e].posy + 4,self.shots[h].vx / 2,self.shots[h].vy / 2, 0,0,0)
                        
                        #スコア加算
                        if   self.enemy[e].status == ENEMY_STATUS_NORMAL:   #ステータスが「通常」ならscore_normalをpointとしてスコアを加算する
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
                        else:                                     #ステータスが以上に当てはまらないときはscore_normalとする
                            point = self.enemy[e].score_normal
                        self.add_score(point) #スコアを加算する関数の呼び出し
                        del self.enemy[e] #敵リストから破壊した敵をdel消去破壊するっ！
                        
                    self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させるため
                    pyxel.play(0,2)#変な爆発音を出すのだ～～～☆彡

    #自機弾とボスとの当たり判定
    def update_collision_my_shot_boss(self):
        shot_hit = len(self.shots)
        for h in reversed(range (shot_hit)):
            boss_hit = len(self.boss)
            for e in reversed(range (boss_hit)):#ウェーブカッターの分も含めてＹ軸方向の幅の大きさも考えた当たり判定にする、Ｘ軸方向の当たり判定は普通に8ドット単位で行う
                if self.boss[e].invincible != 1: #もしボスが無敵状態で無いのならば
                    #ボス本体の当たり判定1(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main1_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main1_x + self.boss[e].col_main1_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main1_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main1_y + self.boss[e].col_main1_h\
                        and self.boss[e].col_main1_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定2(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main2_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main2_x + self.boss[e].col_main2_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main2_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main2_y + self.boss[e].col_main2_h\
                        and self.boss[e].col_main2_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定3(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main3_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main3_x + self.boss[e].col_main3_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main3_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main3_y + self.boss[e].col_main3_h\
                        and self.boss[e].col_main3_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定4(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main4_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main4_x + self.boss[e].col_main4_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main4_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main4_y + self.boss[e].col_main4_h\
                        and self.boss[e].col_main4_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定5(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main5_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main5_x + self.boss[e].col_main5_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main5_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main5_y + self.boss[e].col_main5_h\
                        and self.boss[e].col_main5_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定6(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main6_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main6_x + self.boss[e].col_main6_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main6_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main6_y + self.boss[e].col_main6_h\
                        and self.boss[e].col_main6_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定7(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main7_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main7_x + self.boss[e].col_main7_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main7_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main7_y + self.boss[e].col_main7_h\
                        and self.boss[e].col_main7_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定8(弾を消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main8_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main8_x + self.boss[e].col_main8_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_main8_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main8_y + self.boss[e].col_main8_h\
                        and self.boss[e].col_main8_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.shots[h].posx,self.shots[h].posy,0,0, 0,0,0)#自機弾の位置に消滅エフェクト育成
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    
                    
                    #パーツ１との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts1_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts1_x + self.boss[e].col_parts1_w\
                        and self.boss[e].posy + self.boss[e].col_parts1_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts1_y + self.boss[e].col_parts1_h\
                        and self.boss[e].parts1_flag == 1:
                        
                        self.boss[e].parts1_hp -= self.shots[h].shot_power #パーツ1の耐久力をShot_powerの分だけ減らす
                        if self.boss[e].parts1_hp <= 0: #パーツ1の耐久力が0以下になったのなら
                            self.boss[e].parts1_flag = 0 #パーツ1の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts1_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ1耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する   
                    #パーツ2との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts2_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts2_x + self.boss[e].col_parts2_w\
                        and self.boss[e].posy + self.boss[e].col_parts2_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts2_y + self.boss[e].col_parts2_h\
                        and self.boss[e].parts2_flag == 1:
                        
                        self.boss[e].parts2_hp -= self.shots[h].shot_power #パーツ2の耐久力をShot_powerの分だけ減らす
                        if self.boss[e].parts2_hp <= 0: #パーツ2の耐久力が0以下になったのなら
                            self.boss[e].parts2_flag = 0 #パーツ2の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts2_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ2耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる 
                        continue #これ以下の処理はせず次のループへと移行する                    
                    #パーツ3との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts3_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts3_x + self.boss[e].col_parts3_w\
                        and self.boss[e].posy + self.boss[e].col_parts3_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts3_y + self.boss[e].col_parts3_h\
                        and self.boss[e].parts3_flag == 1:
                        
                        self.boss[e].parts3_hp -= self.shots[h].shot_power #パーツ3の耐久力をShot_powerの分だけ減らす
                        if self.boss[e].parts3_hp <= 0: #パーツ3の耐久力が0以下になったのなら
                            self.boss[e].parts3_flag = 0 #パーツ3の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts3_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ3耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    #パーツ4との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts4_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts4_x + self.boss[e].col_parts4_w\
                        and self.boss[e].posy + self.boss[e].col_parts4_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts4_y + self.boss[e].col_parts4_h\
                        and self.boss[e].parts4_flag == 1:
                        
                        self.boss[e].parts4_hp -= self.shots[h].shot_power #パーツ4の耐久力をShot_powerの分だけ減らす
                        if self.boss[e].parts4_hp <= 0: #パーツ4の耐久力が0以下になったのなら
                            self.boss[e].parts4_flag = 0 #パーツ4の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts4_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ4耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    
                    #ダメージポイント1との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point1_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point1_x + self.boss[e].col_damage_point1_w\
                        and self.boss[e].posy - self.shots[h].height  + self.boss[e].col_damage_point1_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point1_y + self.boss[e].col_damage_point1_h\
                        and self.boss[e].col_damage_point1_w != 0:
                        
                        self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント2との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point2_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point2_x + self.boss[e].col_damage_point2_w\
                        and self.boss[e].posy - self.shots[h].height + self.boss[e].col_damage_point2_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point2_y + self.boss[e].col_damage_point2_h\
                        and self.boss[e].col_damage_point2_w != 0:
                        
                        self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント3との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point3_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point3_x + self.boss[e].col_damage_point3_w\
                        and self.boss[e].posy - self.shots[h].height + self.boss[e].col_damage_point3_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point3_y + self.boss[e].col_damage_point3_h\
                        and self.boss[e].col_damage_point3_w != 0:
                        
                        self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント4との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point4_x <= self.shots[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point4_x + self.boss[e].col_damage_point4_w\
                        and self.boss[e].posy - self.shots[h].height + self.boss[e].col_damage_point4_y <= self.shots[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point4_y + self.boss[e].col_damage_point4_h\
                        and self.boss[e].col_damage_point4_w != 0:
                        
                        self.boss[e].main_hp -= self.shots[h].shot_power #ボスの耐久力をShot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y   = self.shots[h].posx,self.shots[h].posy
                        hit_vx,hit_vy = self.shots[h].vx,self.shots[h].vx
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにショットを当てた後の処理の関数を呼び出す！
                        self.shots[h].shot_hp = 0#自機弾のＨＰをゼロにして自機弾移動時にチェックしリストから消去させる
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
                if     self.enemy[e].posx <= self.missile[h].posx + 4 <= self.enemy[e].posx +   self.enemy[e].width  + self.missile[h].width  / 2\
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

    #自機ミサイルとボスとの当たり判定
    def update_collision_missile_boss(self):
        missile_hit = len(self.missile)
        for h in reversed(range (missile_hit)):
            boss_hit = len(self.boss)
            for e in reversed(range (boss_hit)):
                if self.boss[e].invincible != 1: #もしボスが無敵状態で無いのならば
                    #ボス本体の当たり判定1(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main1_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main1_x + self.boss[e].col_main1_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main1_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main1_y + self.boss[e].col_main1_h\
                        and self.boss[e].col_main1_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定2(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main2_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main2_x + self.boss[e].col_main2_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main2_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main2_y + self.boss[e].col_main2_h\
                        and self.boss[e].col_main2_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定3(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main3_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main3_x + self.boss[e].col_main3_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main3_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main3_y + self.boss[e].col_main3_h\
                        and self.boss[e].col_main3_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定4(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main4_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main4_x + self.boss[e].col_main4_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main4_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main4_y + self.boss[e].col_main4_h\
                        and self.boss[e].col_main4_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定5(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main5_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main5_x + self.boss[e].col_main5_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main5_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main5_y + self.boss[e].col_main5_h\
                        and self.boss[e].col_main5_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定6(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main6_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main6_x + self.boss[e].col_main6_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main6_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main6_y + self.boss[e].col_main6_h\
                        and self.boss[e].col_main6_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定7(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main7_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main7_x + self.boss[e].col_main7_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main7_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main7_y + self.boss[e].col_main7_h\
                        and self.boss[e].col_main7_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定8(ミサイルを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main8_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main8_x + self.boss[e].col_main8_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_main8_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main8_y + self.boss[e].col_main8_h\
                        and self.boss[e].col_main8_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.missile[h].posx,self.missile[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    
                    
                    #パーツ１との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts1_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts1_x + self.boss[e].col_parts1_w\
                        and self.boss[e].posy + self.boss[e].col_parts1_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts1_y + self.boss[e].col_parts1_h\
                        and self.boss[e].parts1_flag == 1:
                        
                        self.boss[e].parts1_hp -= self.missile[h].missile_power #パーツ1の耐久力をmissile_powerの分だけ減らす
                        if self.boss[e].parts1_hp <= 0: #パーツ1の耐久力が0以下になったのなら
                            self.boss[e].parts1_flag = 0 #パーツ1の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts1_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ1耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する   
                    #パーツ2との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts2_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts2_x + self.boss[e].col_parts2_w\
                        and self.boss[e].posy + self.boss[e].col_parts2_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts2_y + self.boss[e].col_parts2_h\
                        and self.boss[e].parts2_flag == 1:
                        
                        self.boss[e].parts2_hp -= self.missile[h].missile_power #パーツ2の耐久力をmissile_powerの分だけ減らす
                        if self.boss[e].parts2_hp <= 0: #パーツ2の耐久力が0以下になったのなら
                            self.boss[e].parts2_flag = 0 #パーツ2の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts2_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ2耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                    
                    #パーツ3との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts3_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts3_x + self.boss[e].col_parts3_w\
                        and self.boss[e].posy + self.boss[e].col_parts3_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts3_y + self.boss[e].col_parts3_h\
                        and self.boss[e].parts3_flag == 1:
                        
                        self.boss[e].parts3_hp -= self.missile[h].missile_power #パーツ3の耐久力をmissile_powerの分だけ減らす
                        if self.boss[e].parts3_hp <= 0: #パーツ3の耐久力が0以下になったのなら
                            self.boss[e].parts3_flag = 0 #パーツ3の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts3_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ3耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    #パーツ4との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts4_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts4_x + self.boss[e].col_parts4_w\
                        and self.boss[e].posy + self.boss[e].col_parts4_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts4_y + self.boss[e].col_parts4_h\
                        and self.boss[e].parts4_flag == 1:
                        
                        self.boss[e].parts4_hp -= self.missile[h].missile_power #パーツ4の耐久力をmissile_powerの分だけ減らす
                        if self.boss[e].parts4_hp <= 0: #パーツ4の耐久力が0以下になったのなら
                            self.boss[e].parts4_flag = 0 #パーツ4の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts4_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ4耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    
                    #ダメージポイント1との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point1_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point1_x + self.boss[e].col_damage_point1_w\
                        and self.boss[e].posy - self.missile[h].height  + self.boss[e].col_damage_point1_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point1_y + self.boss[e].col_damage_point1_h\
                        and self.boss[e].col_damage_point1_w != 0:
                        
                        self.boss[e].main_hp -= self.missile[h].missile_power #ボスの耐久力をmissile_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント2との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point2_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point2_x + self.boss[e].col_damage_point2_w\
                        and self.boss[e].posy - self.missile[h].height + self.boss[e].col_damage_point2_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point2_y + self.boss[e].col_damage_point2_h\
                        and self.boss[e].col_damage_point2_w != 0:
                        
                        self.boss[e].main_hp -= self.missile[h].missile_power #ボスの耐久力をmissile_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント3との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point3_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point3_x + self.boss[e].col_damage_point3_w\
                        and self.boss[e].posy - self.missile[h].height + self.boss[e].col_damage_point3_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point3_y + self.boss[e].col_damage_point3_h\
                        and self.boss[e].col_damage_point3_w != 0:
                        
                        self.boss[e].main_hp -= self.missile[h].missile_power #ボスの耐久力をmissile_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント4との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point4_x <= self.missile[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point4_x + self.boss[e].col_damage_point4_w\
                        and self.boss[e].posy - self.missile[h].height + self.boss[e].col_damage_point4_y <= self.missile[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point4_y + self.boss[e].col_damage_point4_h\
                        and self.boss[e].col_damage_point4_w != 0:
                        
                        self.boss[e].main_hp -= self.missile[h].missile_power #ボスの耐久力をmissile_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.missile[h].posx,self.missile[h].posy
                        hit_vx,hit_vy = self.missile[h].vx,self.missile[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにミサイルを当てた後の処理の関数を呼び出す！ 
                        self.missile[h].missile_hp = 0#ミサイルのＨＰをゼロしてミサイル移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する    

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
                    del self.missile[i]#ミサイルのＨＰが0だったらインスタンスを破棄する(ミサイル消滅)
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
                    
                    self.missile[i].posy += self.missile[i].vy                             #ミサイルのY座標をVY分加減算して更新
                
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
                    self.missile[i].posx += self.missile[i].vx          #サーチレーザーのX座標をVX分加減算して更新
                    
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
                        #self.missile[i].posx += self.missile[i].vx          #サーチレーザーのX座標をVX分加減算して更新
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
                    #      self.claw[i].status = 1#回転開始初期位置のオフセット値まで行ったのならステータスを回転開始(1)にする
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
                    #     x = r cos θ
                    #     y = r sin θ
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

    #クローが弾を発射するのか調べる関数
    def update_check_fire_claw_shot(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b00010000 == 0b00010000: #LowByte リプレイデータを調べてPAD Aが押された記録だったのなら...
                self.update_fire_claw_shot() #クローショット発射関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD_1_A) or pyxel.btn(pyxel.GAMEPAD_2_A): #パッドAかスペースキーが押されたか？
                self.update_fire_claw_shot() #クローショット発射関数呼び出し！

    #クローが弾を発射!!!!!!
    def update_fire_claw_shot(self):
            if (pyxel.frame_count % 16) == 0: #16フレーム毎だったら クローショットを育成する
                if len(self.claw_shot) < CLAW_RAPID_FIRE_NUMBER * (self.claw_number):#クローショットの要素数がクローの数x２以下なら弾を発射する
                    #ここからクローが弾を発射する実処理
                    claw_count = len(self.claw)#クローの数を数える
                    for i in range(claw_count):
                        if self.claw[i].status != 0:#ステータスが0の時は初期回転位置や初期固定位置に移動中なので弾は発射しない
                            new_claw_shot = Shot()
                            if self.claw_type == 3:#クロータイプがリバースクローの時はクローショットの方向をreverse_claw_svx,reverse_claw_svyにして8方向弾にする
                                new_claw_shot.update(0,self.claw[i].posx,self.claw[i].posy,    self.reverse_claw_svx,self.reverse_claw_svy,   8,8,   0,  1,1)
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
                if     self.enemy[e].posx <= self.claw_shot[h].posx + 4 <= self.enemy[e].posx + self.enemy[e].width\
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
                    pyxel.play(0,2)#クローショットが敵を破壊した音！

    #クローショットとボスとの当たり判定
    def update_collision_claw_shot_boss(self):
        claw_shot_hit = len(self.claw_shot)#クローの弾の数を数える
        for h in reversed(range (claw_shot_hit)):
            boss_hit = len(self.boss)
            for e in reversed(range (boss_hit)):
                if self.boss[e].invincible != 1: #もしボスが無敵状態で無いのならば
                    #ボス本体の当たり判定1(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main1_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main1_x + self.boss[e].col_main1_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main1_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main1_y + self.boss[e].col_main1_h\
                        and self.boss[e].col_main1_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定2(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main2_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main2_x + self.boss[e].col_main2_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main2_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main2_y + self.boss[e].col_main2_h\
                        and self.boss[e].col_main2_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定3(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main3_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main3_x + self.boss[e].col_main3_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main3_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main3_y + self.boss[e].col_main3_h\
                        and self.boss[e].col_main3_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定4(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main4_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main4_x + self.boss[e].col_main4_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main4_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main4_y + self.boss[e].col_main4_h\
                        and self.boss[e].col_main4_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定5(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main5_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main5_x + self.boss[e].col_main5_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main5_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main5_y + self.boss[e].col_main5_h\
                        and self.boss[e].col_main5_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定6(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main6_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main6_x + self.boss[e].col_main6_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main6_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main6_y + self.boss[e].col_main6_h\
                        and self.boss[e].col_main6_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定7(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main7_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main7_x + self.boss[e].col_main7_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main7_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main7_y + self.boss[e].col_main7_h\
                        and self.boss[e].col_main7_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ボス本体の当たり判定8(クローショットを消滅させる)との判定
                    if        self.boss[e].posx                   + self.boss[e].col_main8_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_main8_x + self.boss[e].col_main8_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_main8_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_main8_y + self.boss[e].col_main8_h\
                        and self.boss[e].col_main8_w != 0:
                        
                        self.update_append_particle(PARTICLE_LINE,self.claw_shot[h].posx,self.claw_shot[h].posy,0,0, 0,0,0)#ミサイルの位置に消滅エフェクト育成
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    
                    
                    #パーツ１との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts1_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts1_x + self.boss[e].col_parts1_w\
                        and self.boss[e].posy + self.boss[e].col_parts1_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts1_y + self.boss[e].col_parts1_h\
                        and self.boss[e].parts1_flag == 1:
                        
                        self.boss[e].parts1_hp -= self.claw_shot[h].shot_power #パーツ1の耐久力をshot_powerの分だけ減らす
                        if self.boss[e].parts1_hp <= 0: #パーツ1の耐久力が0以下になったのなら
                            self.boss[e].parts1_flag = 0 #パーツ1の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts1_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ1耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する   
                    #パーツ2との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts2_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts2_x + self.boss[e].col_parts2_w\
                        and self.boss[e].posy + self.boss[e].col_parts2_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts2_y + self.boss[e].col_parts2_h\
                        and self.boss[e].parts2_flag == 1:
                        
                        self.boss[e].parts2_hp -= self.claw_shot[h].shot_power #パーツ2の耐久力をshot_powerの分だけ減らす
                        if self.boss[e].parts2_hp <= 0: #パーツ2の耐久力が0以下になったのなら
                            self.boss[e].parts2_flag = 0 #パーツ2の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts2_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ2耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                    
                    #パーツ3との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts3_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts3_x + self.boss[e].col_parts3_w\
                        and self.boss[e].posy + self.boss[e].col_parts3_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts3_y + self.boss[e].col_parts3_h\
                        and self.boss[e].parts3_flag == 1:
                        
                        self.boss[e].parts3_hp -= self.claw_shot[h].shot_power #パーツ3の耐久力をshot_powerの分だけ減らす
                        if self.boss[e].parts3_hp <= 0: #パーツ3の耐久力が0以下になったのなら
                            self.boss[e].parts3_flag = 0 #パーツ3の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts3_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ3耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    #パーツ4との当たり判定
                    if        self.boss[e].posx + self.boss[e].col_parts4_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_parts4_x + self.boss[e].col_parts4_w\
                        and self.boss[e].posy + self.boss[e].col_parts4_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_parts4_y + self.boss[e].col_parts4_h\
                        and self.boss[e].parts4_flag == 1:
                        
                        self.boss[e].parts4_hp -= self.claw_shot[h].shot_power #パーツ4の耐久力をshot_powerの分だけ減らす
                        if self.boss[e].parts4_hp <= 0: #パーツ4の耐久力が0以下になったのなら
                            self.boss[e].parts4_flag = 0 #パーツ4の生存フラグを0にして破壊したことにする
                        
                        self.boss[e].display_time_parts4_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #パーツ4耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する                  
                    
                    #ダメージポイント1との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point1_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point1_x + self.boss[e].col_damage_point1_w\
                        and self.boss[e].posy - self.claw_shot[h].height  + self.boss[e].col_damage_point1_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point1_y + self.boss[e].col_damage_point1_h\
                        and self.boss[e].col_damage_point1_w != 0:
                        
                        self.boss[e].main_hp -= self.claw_shot[h].shot_power #ボスの耐久力をshot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント2との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point2_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point2_x + self.boss[e].col_damage_point2_w\
                        and self.boss[e].posy - self.claw_shot[h].height + self.boss[e].col_damage_point2_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point2_y + self.boss[e].col_damage_point2_h\
                        and self.boss[e].col_damage_point2_w != 0:
                        
                        self.boss[e].main_hp -= self.claw_shot[h].shot_power #ボスの耐久力をshot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント3との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point3_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point3_x + self.boss[e].col_damage_point3_w\
                        and self.boss[e].posy - self.claw_shot[h].height + self.boss[e].col_damage_point3_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point3_y + self.boss[e].col_damage_point3_h\
                        and self.boss[e].col_damage_point3_w != 0:
                        
                        self.boss[e].main_hp -= self.claw_shot[h].shot_power #ボスの耐久力をshot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する
                    #ダメージポイント4との判定
                    if        self.boss[e].posx                  + self.boss[e].col_damage_point4_x <= self.claw_shot[h].posx + 4 <= self.boss[e].posx + self.boss[e].col_damage_point4_x + self.boss[e].col_damage_point4_w\
                        and self.boss[e].posy - self.claw_shot[h].height + self.boss[e].col_damage_point4_y <= self.claw_shot[h].posy + 4 <= self.boss[e].posy + self.boss[e].col_damage_point4_y + self.boss[e].col_damage_point4_h\
                        and self.boss[e].col_damage_point4_w != 0:
                        
                        self.boss[e].main_hp -= self.claw_shot[h].shot_power #ボスの耐久力をshot_powerの分だけ減らす
                        self.boss[e].display_time_main_hp_bar = BOSS_HP_BAR_DISPLAY_TIME #耐久力バーを表示するカウントタイマーを初期値の定数に戻す
                        hit_x,hit_y = self.claw_shot[h].posx,self.claw_shot[h].posy
                        hit_vx,hit_vy = self.claw_shot[h].vx,self.claw_shot[h].vy
                        self.boss_processing_after_hitting(e,hit_x,hit_y,hit_vx,hit_vy) #ボスにクローショットを当てた後の処理の関数を呼び出す！ 
                        self.claw_shot[h].shot_hp = 0#クローショットのＨＰをゼロにして移動時にチェックしリストから消去させる
                        continue #これ以下の処理はせず次のループへと移行する    

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
                self.enemy_shot[i].posx += self.enemy_shot[i].vx      #敵の弾のx座標をvx分加減算して更新
                self.enemy_shot[i].timer += self.enemy_shot[i].speed
                self.enemy_shot[i].posy += self.enemy_shot[i].intensity * math.sin(self.enemy_shot[i].timer + 3.14 / 4)
            #コサインカーブ弾の場合
            elif self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_COS:
                self.enemy_shot[i].posx += self.enemy_shot[i].vx       #敵の弾のx座標をvx分加減算して更新
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
                    del self.enemy_shot[i]    #インスタンスを消滅させる 古い尻尾から消えていく・・・
                    continue                #これ以下の処理はせずにループを続けていく
                
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
                    del self.enemy_shot[i]    #インスタンスを消滅させる 古い尻尾から消えていく・・・
                    continue                #これ以下の処理はせずにループを続けていく
                
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
                        self.enemy_shot[i].vx = 0                         #最大幅まで広くなったのでもう横方向の移動は無し
                    
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
                        self.enemy_shot[i].vy = 0                         #最大幅まで広くなったのでもう縦方向の移動は無し
                    
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
                continue                #衝突判定はせずループだけ続ける(continue)・・・無敵っていいよね・・・うん、うん.....
            
            if self.enemy_shot[i].collision_type == ESHOT_COL_MIN88: #最小の正方形8x8ドットでの当たり判定の場合
                #敵の弾と自機の位置の2点間の距離を求める
                self.dx = (self.enemy_shot[i].posx + 4) - (self.my_x + 4)
                self.dy = (self.enemy_shot[i].posy + 4) - (self.my_y + 4)
                self.distance = math.sqrt(self.dx * self.dx + self.dy * self.dy)
                if self.distance < 3:
                    self.update_my_ship_damage(1) #敵弾と自機の位置の距離が3以下なら衝突したと判定し自機のシールド値を１減らす
                
            elif self.enemy_shot[i].collision_type == ESHOT_COL_BOX: #長方形での当たり判定の場合
                if      0 <= (self.my_x+4) - (self.enemy_shot[i].posx+4) <= self.enemy_shot[i].width\
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
            if     self.enemy_shot[i].enemy_shot_type == ENEMY_SHOT_WAVE\
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
                new_stars.update(WINDOW_W + 1,self.s_rndint(0,WINDOW_H),self.s_rndint(1,50))
                # new_stars.update(WINDOW_W + 1,randint(0,WINDOW_H),randint(1,50))
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
            elif self.debug_menu_status == 2:
                self.debug_menu_status = 3
            else:
                self.debug_menu_status = 0

    #デバッグモードによるキーボードやパッドでの敵や敵弾の強制追加発生
    def update_debug_mode_enemy_append(self):
        #敵タイプ1サーコインの発生  直進して斜め後退→勢いよく後退していく10機編隊      KEY 4 +++++++
        if (pyxel.frame_count % 8) == 0:
            if pyxel.btn(pyxel.KEY_4) or pyxel.btn(pyxel.GAMEPAD_1_LEFT_SHOULDER) or pyxel.btn(pyxel.GAMEPAD_2_LEFT_SHOULDER):
                if len(self.enemy) < 400:
                    
                    self.posy = self.s_rndint(0,WINDOW_H - 8)
                    for number in range(10):
                        new_enemy = Enemy()
                        new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.posy,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   -1,1,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1,0,    0, HP01,  0,0, E_SIZE_NORMAL,   30,0,0 ,    0,0,0,0,   E_SHOT_POW,self.current_formation_id ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                        self.enemy.append(new_enemy)
                    
                    #編隊なので編隊のＩＤナンバーと編隊の総数、現在の編隊生存数をEnemy_formationリストに登録します
                    self.record_enemy_formation(10)
        
        #敵タイプ2サイシーロの発生  サインカーブを描く3機編隊                     KEY 5 ++++++
        if (pyxel.frame_count % 8) == 0:
            if pyxel.btn(pyxel.KEY_5):
                if len(self.enemy) < 400:
                    self.posy = self.s_rndint(0,WINDOW_H)
                    for number in range(3):
                        new_enemy = Enemy()
                        new_enemy.update(SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W + 10,((self.posy)-36) + (number * 12),0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1,0,   0,  HP01,   0,0,  E_SIZE_NORMAL,0.5,0.05,0,    0,0,0,0,   E_NO_POW,ID00 ,0,0,0    ,0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                        self.enemy.append(new_enemy)        
        
        #敵タイプ6の発生（謎の飛翔体Ｍ54）                                   KEY 6 ++++++
        if (pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_6):
                if len(self.enemy) < 400:
                    self.posy = self.s_rndint(0,WINDOW_H)
                    new_enemy = Enemy()
                    new_enemy.update(6,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,self.posy,0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0, 0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1,0,   0,  HP01,   0,0,  E_SIZE_NORMAL,   0.5,0.05,0,    0,0,0,0,    E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)        
        
        #敵タイプ8ツインアローの発生 追尾戦闘機                               KEY Z ++++++
        if (pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_Z):
                if len(self.enemy) < 400:
                    self.posy = self.s_rndint(0,WINDOW_H)
                    new_enemy = Enemy()
                    new_enemy.update(TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,self.posy,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0, 0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1.5,0,  0,    HP01,    0,0,   E_SIZE_NORMAL,  0,  0, 1.3,    0,0,0,0,    E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ9の発生 縦軸合わせ突進タイプ                                KEY X ++++++
        if (pyxel.frame_count % 16) == 0:
            if pyxel.btn(pyxel.KEY_X):
                if len(self.enemy) < 400:
                    new_enemy = Enemy()
                    new_enemy.update(9,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    80,40,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.5,0,   0,    HP01,    0,0,   E_SIZE_NORMAL,  0,  0, 0,    0,0,0,0,    E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ10の発生 地面のスクランブルハッチ                             KEY C +++++
        if (pyxel.frame_count % 64) == 0:
            if pyxel.btn(pyxel.KEY_C):
                if len(self.enemy) < 400:
                    #enemy_count1を出現してから突進タイプの敵を出すまでの時間のカウンタで使用します（射出開始カウンタ）
                    #enemy_count2を射出する敵の総数です（敵総数カウンタ）
                    new_enemy = Enemy()
                    new_enemy.update(10,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    170,96,0,0,    0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_24,SIZE_26,   0.5,0,   0,    HP10,    0,0,   E_SIZE_MIDDLE32,  (self.s_rndint(0,130) + 10),  6, 20,    0,0,0,0,      E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ12の発生 レイブラスター  レーザービームを出して高速で逃げていく敵     KEY D ++++++
        if (pyxel.frame_count % 8) == 0:
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT_SHOULDER) or pyxel.btn(pyxel.GAMEPAD_2_RIGHT_SHOULDER):
                if len(self.enemy) < 400:
                    new_enemy = Enemy()
                    new_enemy.update(RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W + 8,self.s_rndint(0,WINDOW_H),0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   -2,(self.s_rndint(0,1)-0.5),       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.98,0,    0,    HP01,  0,0,    E_SIZE_NORMAL,   80 + self.s_rndint(0,40),0,0,     0,0,0,0,      E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ16の発生 2機一体で挟みこみ攻撃をしてくるクランパリオン             KEY T ++++++++
        if (pyxel.frame_count % 24) == 0:
            if pyxel.btn(pyxel.KEY_T):
                if len(self.enemy) < 400:
                    new_enemy = Enemy()
                    new_enemy.update(CLAMPARION,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    WINDOW_W,0,0,0,       0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,  -1.1,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.997,0,    0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,     0,0,0,0,    E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                    
                    new_enemy = Enemy()
                    new_enemy.update(CLAMPARION,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    WINDOW_W,WINDOW_H-8,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  -1.1,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.997,0,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,    E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ17の発生 ロールブリッツ あらかじめ決められた場所へスプライン曲線移動   KEY Y ++++++++
        if (pyxel.frame_count % 24) == 0:
            if pyxel.btn(pyxel.KEY_Y):
                if len(self.enemy) < 400:
                    new_enemy = Enemy()
                    new_enemy.update(ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    0,0,0,0,     0,0,0,0,0,0,0,0,         0,0,0,0,0,0,0,0,0,0,  0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0,1,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,      E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                    
                    new_enemy = Enemy()
                    new_enemy.update(ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    0,0,0,8,     0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,  0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0,1.05,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,    E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                    
                    new_enemy = Enemy()
                    new_enemy.update(ROLL_BLITZ,ID00,ENEMY_STATUS_MOVE_COORDINATE_INIT,ENEMY_ATTCK_ANY,    0,0,0,16,    0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0,0.95,   0,    HP01,  0,0,    E_SIZE_NORMAL,   0,0,0,    0,0,0,0,    E_NO_POW,   ID00    ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵タイプ18の発生 ボルダー 硬めの弾バラマキ重爆撃機                      KEY R ++++++++
        if (pyxel.frame_count % 24) == 0:
            if pyxel.btn(pyxel.KEY_R):
                if len(self.enemy) < 400:
                    new_enemy = Enemy()
                    new_enemy.update(VOLDAR,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   170,10,0,0,       0,0,0,0,0,0,0,0,        0,0,0,0,0,0,0,0,0,0,  0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_40,SIZE_24,   -0.07,1,   0,    HP30,  0,0,    E_SIZE_HI_MIDDLE53,   0,0,0,    0,0,0,0,    E_NO_POW,   ID00    ,1,0.007,0.6,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
        
        #敵弾1(前方加速弾&落下弾&サインコサイン弾&グリーンカッター)の発生           KEY A ----------------
        if(pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_A):
                if len(self.enemy_shot) < 800:
                    #前方加速弾
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -1,0,     1.01,     1,1,    1,0, 0,1,0,                0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    #落下弾
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_DROP_BULLET,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -0.3,-1.1,     0.02,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    
                    #サイン弾
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_SIN,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,    0,0, -1,0,       1,    1,1,    1,0,  0.06,0.06,0.6,            0,   0,0,PRIORITY_FRONT,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    #コサイン弾
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_COS,ID00,140,60,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8,    0,0,  -1,0,      1,    1,1,    1,0,  0.06,0.06,0.6,            0,   0,0,PRIORITY_FRONT,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    
                    #グリーンカッター
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_GREEN_CUTTER,ID00,140,60,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE12,    0,0,  -0.3,0,      1.01,    1,1,    0,0,  0,0,0,            0,   0,0,PRIORITY_FRONT,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #敵弾2(自機狙い6way弾)の発生                         KEY B ----------------
        if(pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_B):
                if len(self.enemy_shot) < 800:
                    ex = 80
                    ey = 60
                    theta = 30
                    n = 6
                    division_type = 0
                    division_count = 0
                    division_num = 0
                    stop_count = 0
                    self.enemy_aim_bullet_nway(ex,ey,theta,n,division_type,division_count,division_num,stop_count)    
        
        #敵弾3(前方レーザービーム)の発生                       KEY S ----------------
        if(pyxel.frame_count % 1) == 0:
            if pyxel.btn(pyxel.KEY_S):
                if len(self.enemy_shot) < 800:
                    posy = self.s_rndint(0,WINDOW_H)
                    for number in range(6):
                        new_enemy_shot = Enemy_shot()
                        new_enemy_shot.update(ENEMY_SHOT_LASER,ID00, WINDOW_W,posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0,  -2,0,   1,  1,1,   0,0,0,    1,0,0,  0,number * 2,PRIORITY_FRONT,  0,0,  0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                        self.enemy_shot.append(new_enemy_shot)
        
        #敵弾4(ホーミングレーザー)の発生                       KEY F -----------------
        if(pyxel.frame_count % 100) == 0:
            if pyxel.btn(pyxel.KEY_F):
                if len(self.enemy_shot) < 800:
                    posy = 60
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_HOMING_LASER,ID00, WINDOW_W,posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0,   0.5,0.5,   1,    1,1,   0,20,0,    1,0,0,  0,0,PRIORITY_MORE_FRONT, 8,0,  0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #敵弾5(サーチレーザー)の発生                          KEY G ------------------
        if(pyxel.frame_count % 100) == 0:
            if pyxel.btn(pyxel.KEY_G):
                if len(self.enemy_shot) < 800:
                    posx = 100
                    posy = 60
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_SEARCH_LASER,ID00, posx,posy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0,   -0.75,0,   1,    1,1,   0,0, 0,    1,0,0,  0,0,PRIORITY_MORE_FRONT, 0,0,  0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #敵弾6(回転弾)の発生                                 KEY H ------------------
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
                    new_enemy_shot.update(ENEMY_SHOT_CIRCLE_BULLET,ID00, cx+radius,cy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, cx,cy,  -0.05,0,   1,    1,1,   0,0, 0,    1,0,0,  0,0,PRIORITY_FRONT, 0,0,  0,rotation_omega_incremental,radius,radius_max, 0,0, radius_incremental, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    
                    cx = 100
                    cy = 60
                    radius = 1
                    radius_max = 80
                    radius_incremental = 0.05
                    rotation_omega_incremental = -2
                    new_enemy_shot = Enemy_shot()
                    new_enemy_shot.update(ENEMY_SHOT_CIRCLE_BULLET,ID00, cx+radius,cy,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, cx,cy,  -0.05,0,   1,    1,1,   0,0, 0,    1,0,0,  0,0,PRIORITY_FRONT, 0,0,  0,rotation_omega_incremental,radius,radius_max, 0,0, radius_incremental, 0,0, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #敵弾7(分裂弾)の発生                                 KEY J ----------------
        if(pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_J):
                if len(self.enemy_shot) < 800:
                    new_enemy_shot = Enemy_shot()
                    ex,ey = 140,60
                    division_type        = 1   #自機狙いの3way
                    division_count       = 40 #分裂するまでのカウント数
                    division_count_origin = 40 #分裂するまでのカウント数(元数値)
                    division_num        = 10    #分裂する回数(ひ孫まで)
                    new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00, ex,ey,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, -2,0,     0.96,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, 0,0, 0,0,   0,0)
                    self.enemy_shot.append(new_enemy_shot)            
        
        #敵弾8(狙い撃ち分裂弾弾)の発生                        KEY K ----------------
        if(pyxel.frame_count % 3) == 0:
            if pyxel.btn(pyxel.KEY_K):
                ex,ey        = 140,60 #弾発射初期座標
                div_type     = 1 #自機狙いの3way
                div_count    = 40 #分裂するまでのカウント数
                div_num      = 2 #ひ孫の代まで分裂します
                stop_count    = 20 #その場に留まるカウント数
                accel        = 1.02 #加速係数
                self.enemy_aim_bullet(ex,ey,div_type,div_count,div_num,stop_count,accel)
        
        #敵弾9(アップ&ダウンレーザー)の発生                    KEY L ----------------
        if(pyxel.frame_count % 28) == 0:
            if pyxel.btn(pyxel.KEY_L):
                if len(self.enemy_shot) < 800:
                    new_enemy_shot = Enemy_shot()
                    ex,ey = 80,60
                    vx,vy =    -0.1,-0.3
                    division_type        = 0
                    division_count       = 0
                    division_count_origin = 0
                    division_num        = 0
                    expansion           = 0.2
                    width_max           = 40
                    height_max          = 3
                    new_enemy_shot.update(ENEMY_SHOT_UP_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE3, 0,0, vx,vy,     1,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
                    
                    new_enemy_shot = Enemy_shot()
                    ex,ey = 80,60
                    vx,vy =    -0.1,0.3
                    division_type        = 0
                    division_count       = 0
                    division_count_origin = 0
                    division_num        = 0
                    expansion           = 0.3
                    width_max           = 80
                    height_max          = 3
                    new_enemy_shot.update(ENEMY_SHOT_DOWN_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE3, 0,0, vx,vy,     1,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #敵弾10(ベクトルレーザー)の発生                        KEY M ----------------
        if(pyxel.frame_count % 10) == 0:
            if pyxel.btn(pyxel.KEY_M):
                if len(self.enemy_shot) < 800:
                    new_enemy_shot = Enemy_shot()
                    ex,ey = 100,60
                    vx,vy =    -0.7,-0.1
                    division_type        = 0
                    division_count       = 0
                    division_count_origin = 0
                    division_num        = 0
                    expansion           = 0.3
                    width_max           = 3
                    height_max          = 90
                    new_enemy_shot.update(ENEMY_SHOT_VECTOR_LASER,ID00, ex,ey,ESHOT_COL_BOX,ESHOT_SIZE3,ESHOT_SIZE3, 0,0, vx,vy,     0.996,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_TOP,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, expansion,0,width_max,height_max,   0,0)
                    self.enemy_shot.append(new_enemy_shot)
        
        #パーティクルを発生させる                              KEY P
        if(pyxel.frame_count % 1) == 0:
            if pyxel.btn(pyxel.KEY_P):
                x = self.s_rndint(0,160)
                y = self.s_rndint(0,120)
                
                self.update_append_particle(PARTICLE_LINE,x,y,  0,0,0,0,0)
                
                #particle_number = self.s_rndint(0,10) + 50
                #for number in range(particle_number):
                #    self.update_append_particle(PARTICLE_DOT,x,y,-0.5,-0.5, 0,0,0)
        
        #背景オブジェクト雲１を発生させる                        KEY E
        if(pyxel.frame_count % 6) == 0:
            if pyxel.btn(pyxel.KEY_E):
                t = self.s_rndint(0,20)
                y = self.s_rndint(0,120+30)
                
                new_background_object = Background_object()
                new_background_object.update(t, 160+10,y,  0,    1.009,1,0,0,0,0,0,0,   -3,-0.25,  0,0,   0,0,0,0,0,   0,0,0, 0,0,0,  0,0,0)
                self.background_object.append(new_background_object)
        
        #パワーアップアイテム類を発生させる                       KEY U I O
        if(pyxel.frame_count % 8) == 0:
            if pyxel.btn(pyxel.KEY_U): #ショットアイテム
                y = self.s_rndint(0,120)
                new_obtain_item = Obtain_item()
                new_obtain_item.update(ITEM_SHOT_POWER_UP,WINDOW_W-20,y, 0.5,0,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   1,0,0,  0,0,0, self.pow_item_bounce_num,0)
                self.obtain_item.append(new_obtain_item)    
            elif pyxel.btn(pyxel.KEY_I): #ミサイルアイテム
                y = self.s_rndint(0,120)
                new_obtain_item = Obtain_item()
                new_obtain_item.update(ITEM_MISSILE_POWER_UP,WINDOW_W-20,y, 0.5,0,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,1,0,  0,0,0, self.pow_item_bounce_num,0)
                self.obtain_item.append(new_obtain_item) 
            elif pyxel.btn(pyxel.KEY_O): #シールドアイテム
                y = self.s_rndint(0,120)
                new_obtain_item = Obtain_item()
                new_obtain_item.update(ITEM_SHIELD_POWER_UP,WINDOW_W-20,y, 0.5,0,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,0,1,  0,0,0, self.pow_item_bounce_num,0)
                self.obtain_item.append(new_obtain_item) 
        
        #自機クローを追加する                                KEY V
        if pyxel.btnp(pyxel.KEY_V):
            self.update_append_claw()
        
        #キーボード入力によるイベントアペンドリスト書き込み  サーコイン10機編隊   KEY 0
        if (pyxel.frame_count % 8) == 0:
            if pyxel.btn(pyxel.KEY_0):
                new_event_append_request = Event_append_request()
                new_event_append_request.update(self.stage_count + 10,EVENT_ENEMY,CIR_COIN,WINDOW_W + 8,self.s_rndint(0,WINDOW_H - 8),10)
                self.event_append_request.append(new_event_append_request)#現在のstage_countから10カウント過ぎた時点でサーコインが発生するようイベントアペンドリストに追加する

    #クローの追加
    def update_append_claw(self):
        if   len(self.claw) == 0:#1機目のクローの発生
            posx = self.my_x
            posy = self.my_y
            new_claw = Claw()
            self.claw_number = 1
            self.claw_difference = 360 / self.claw_number
            new_claw.update(0,   self.claw_type,0,    posx,posy,  0,-1,   -1,-1,  -1,0,      0,0,  0,-12,  -2,-12,    -2,-12,   -12,-1,  0,0,    90,0,2,12,    self.claw_difference,0,   0,1,   0)
            self.claw.append(new_claw)
            return
        
        if len(self.claw) == 1:#2機目のクローの発生
            posx = self.my_x
            posy = self.my_y
            new_claw = Claw()
            self.claw_number = 2
            self.claw_difference = 360 / self.claw_number
            new_claw.update(1,   self.claw_type,0,    posx,posy,  0,-1,   -1,1,  0,-1,       0,0, 0,-12,    -2,12,  -2,12,   -3,-9, 0,0,       90,0,2,12,    self.claw_difference,0,   0,1,   0)
            self.claw.append(new_claw)
            return
        
        if len(self.claw) == 2:#3機目のクローの発生
            posx = self.my_x
            posy = self.my_y
            new_claw = Claw()
            self.claw_number = 3
            self.claw_difference = 360 / self.claw_number
            new_claw.update(2,   self.claw_type,0,    posx,posy,  0,-1,   -1,-1,  0,1,       0,0,  0,-12,    -6,-24, -6,-24,  -3,8,   0,0,      90,0,2,12,    self.claw_difference,0,   0,1,    0)
            self.claw.append(new_claw)
            return
        
        if len(self.claw) == 3:#4機目のクローの発生
            posx = self.my_x
            posy = self.my_y
            new_claw = Claw()
            self.claw_number = 4
            self.claw_difference = 360 / self.claw_number
            new_claw.update(3,   self.claw_type,0,    posx,posy,  0,-1,    -1,1,   -1,0,       0,0, 0,-12,    -6,24,  -6,24,  -12,-1,     0,0,       90,0,2,12,   self.claw_difference,0,    0,1,      0)
            self.claw.append(new_claw)
            return

    #クローの消滅                                                       KEY W
    def update_delete_claw(self):
        if pyxel.btnp(pyxel.KEY_W):   #wキーが押されたら自機クローを消滅させる
            claw_count = len(self.claw)
            for i in reversed(range(claw_count)):
                if claw_count != 0:  #クローの数が0以外なら
                    del self.claw[i] #クローのインスタンスを破棄する(クロー消滅)
            
            self.claw_number = 0     #クローの数を0機にする

    #フイックスクローの間隔変化ボタンが押されたかチェックする               KEY N  GAMEPAD RIGHT_SHOULDER
    def update_check_change_fix_claw_interval(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index] & 0b00001000 == 0b00001000: #HighByte リプレイデータを調べてPAD_RIGHT_Sが押された記録だったのなら...
                self.update_change_fix_claw_interval() #フイックスクローの間隔変化関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btn(pyxel.KEY_N) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT_SHOULDER) or pyxel.btn(pyxel.GAMEPAD_2_RIGHT_SHOULDER):#NキーかPAD_RIGHT_Sが押されたらフックスクローの間隔を変化させる
                self.pad_data_h += PAD_RIGHT_S #パッド入力データのRIGHT_SHOULDERボタンの情報ビットを立てる
                self.update_change_fix_claw_interval() #フイックスクローの間隔変化関数呼び出し！

    #フイックスクローの間隔を変化させる
    def update_change_fix_claw_interval(self):
        if (pyxel.frame_count % 8) == 0:
            self.fix_claw_magnification += 0.1      #ボタンが押されたら0.1刻みで増加させる
            if self.fix_claw_magnification >= 2:
                self.fix_claw_magnification = 0.4   #2以上になったら0.4にする

    #クロースタイル変更ボタンが押されたかチェックする                      KEY M  GAMEPAD LEFT_SHOULDER
    def update_check_change_claw_style(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index] & 0b00000100 == 0b00000100: #HighByte リプレイデータを調べてPAD_LEFT_Sが押された記録だったのなら...
                self.update_change_claw_style() #クロースタイル変更関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btnp(pyxel.KEY_M) or pyxel.btnp(pyxel.GAMEPAD_1_LEFT_SHOULDER) or pyxel.btnp(pyxel.GAMEPAD_2_LEFT_SHOULDER):#MキーかPAD_LEFT_Sが押されたらクローの種類を変更する
                self.pad_data_h += PAD_LEFT_S #パッド入力データのLEFT_SHOULDERボタンの情報ビットを立てる
                self.update_change_claw_style() #クロースタイル変更関数呼び出し！

    #クロースタイルの変更
    def update_change_claw_style(self):
        self.claw_type += 1#クローの種類を変化させる
        if self.claw_type > 3:#もしtype3のリバースタイプを超えてしまったら0のローリングタイプにする
            self.claw_type = 0
        
        claw_count = len(self.claw)
        for i in reversed(range(claw_count)):
            self.claw[i].status = 0#全てのクローのステータスを0=回転開始や固定開始の初期位置まで動いていくにする

    #####################################敵関連の処理関数######################################
    #イベントリストによる敵の発生システム
    def update_enemy_append_event_system(self):
        if self.stage_count == self.event_list[self.event_index][0]:#ステージカウントとリストのカウント値が同じならリスト内容を実行する
            if   self.event_list[self.event_index][1] == EVENT_ENEMY:             #イベント「敵出現」の場合
                if   self.event_list[self.event_index][2] == CIR_COIN:      #サーコイン発生！
                    for number in range(self.event_list[self.event_index][5]):
                        #編隊なので現在の編隊ＩＤナンバーであるcurrent_formation_idも出現時にenemyクラスに情報を書き込みます
                        new_enemy = Enemy()
                        new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0, -1,1,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1*self.enemy_speed_mag,0,   0, HP01 * self.enemy_hp_mag,  0,0, E_SIZE_NORMAL,   30,0,0,    0,0,0,0,    E_SHOT_POW,self.current_formation_id ,0,0,0,     0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT02,PT02,  PT01,PT01,PT03)
                        self.enemy.append(new_enemy) 
                    
                    #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                    self.record_enemy_formation(self.event_list[self.event_index][5]) 
                elif self.event_list[self.event_index][2] == TWIN_ARROW:    #追尾戦闘機ツインアロー出現
                    new_enemy = Enemy()
                    new_enemy.update(TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,      0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1.5 - (self.enemy_speed_mag // 2),0,  0,    HP01 * self.enemy_hp_mag,    0,0,   E_SIZE_NORMAL,  0,  0, 1.3,    0,0,0,0,    E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)                
                elif self.event_list[self.event_index][2] == SAISEE_RO:     #回転戦闘機サイシーロ出現(サインカーブを描く敵)
                    new_enemy = Enemy()
                    new_enemy.update(SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,  0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1*self.enemy_speed_mag,0,  0,  HP01 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,0.5,0.05,0,     0,0,0,0,    E_NO_POW,ID00 ,0,0,0,              0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)    
                elif self.event_list[self.event_index][2] == GREEN_LANCER:   #グリーンランサー 3way弾を出してくる緑の戦闘機(サインカーブを描く敵)
                    new_enemy = Enemy()
                    new_enemy.update(GREEN_LANCER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,    0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.1*self.enemy_speed_mag,0,  0,  HP05 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,0.5,0.01,0,     0,0,0,0,    E_MISSILE_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                elif self.event_list[self.event_index][2] == RAY_BLASTER:    #レイブラスター 直進して画面前方のどこかで停止→レーザービーム射出→急いで後退するレーザー系
                    new_enemy = Enemy()
                    new_enemy.update(RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,    -2,(self.s_rndint(0,1)-0.5),       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   0.98,0,  0,  HP02 * self.enemy_hp_mag,   0,0,  E_SIZE_NORMAL,80 + self.s_rndint(0,40),0,0,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,     0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                    self.enemy.append(new_enemy)
                elif self.event_list[self.event_index][2] == VOLDAR:        #ボルダー 硬めの弾バラマキ重爆撃機
                    new_enemy = Enemy()
                    new_enemy.update(VOLDAR,ID00,     ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   self.event_list[self.event_index][3],self.event_list[self.event_index][4],0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,    0,0,       0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_40,SIZE_24,   -0.07*self.enemy_speed_mag,1,  0,  HP59 * self.enemy_hp_mag,   0,0,  E_SIZE_HI_MIDDLE53,  0,0,0,     0,0,0,0,     E_SHOT_POW,ID00    ,1,0.007,0.6,     0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT10)
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
                            new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (number * 12),self.event_list[self.event_index][4],0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  -1,1,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1,0,   0, HP01 * self.enemy_hp_mag,  0,0, E_SIZE_NORMAL,   30,0,0,    0,0,0,0,    E_SHOT_POW,self.current_formation_id ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                            self.enemy.append(new_enemy) 
                            
                        #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                        self.record_enemy_formation(self.event_list[self.event_index][5]) 
                
                self.fast_forward_destruction_num = 0       #
                self.fast_forward_destruction_count = 0     #
                self.add_appear_flag = 0                 #早回し関連のパラメーター数値、フラグは全てリセットします
            elif self.event_list[self.event_index][1] == EVENT_SCROLL:            #イベント「スクロール」の場合
                #スクロールスタート
                if   self.event_list[self.event_index][2] == SCROLL_START:
                    self.side_scroll_speed         = 1 #スクロールスピードを通常の1にする
                    self.side_scroll_speed_set_value = 1 #設定目標値も1にする
                    self.side_scroll_speed_variation = 0 #変化量は0
                #スクロールストップ！
                elif self.event_list[self.event_index][2] == SCROLL_STOP:
                    self.side_scroll_speed         = 0 #スクロールスピードを0にする
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
                    self.side_scroll_speed_set_value    = self.event_list[self.event_index][3] #横スクロールスピードの設定値を代入
                    self.side_scroll_speed_variation    = self.event_list[self.event_index][4] #横スクロールスピードの変化量を代入
                    self.vertical_scroll_speed_set_value = self.event_list[self.event_index][5] #縦スクロールスピードの設定値を代入
                    self.vertical_scroll_speed_variation = self.event_list[self.event_index][6] #縦スクロールスピードの変化量を代入
                
            elif self.event_list[self.event_index][1] == EVENT_DISPLAY_STAR:                 #イベントが「EVENT_DISPLAY_STAR」の場合
                self.star_scroll_flag = self.event_list[self.event_index][2] #星スクロールのon/offのフラグを代入する
            elif self.event_list[self.event_index][1] == EVENT_CHANGE_BG_CLS_COLOR:          #イベントが「EVENT_CHANGE_BG_CLS_COLOR」の場合
                self.bg_cls_color = self.event_list[self.event_index][2]    #BGをCLS(クリアスクリーン)するときの色を代入する
            elif self.event_list[self.event_index][1] == EVENT_CHANGE_BG_TRANSPARENT_COLOR:  #イベントが「EVENT_CHANGE_BG_TRANSPARENT_COLOR」の場合
                self.bg_transparent_color = self.event_list[self.event_index][2]    #BGを敷き詰める時の透明色を指定する
            elif self.event_list[self.event_index][1] == EVENT_CLOUD:                        #イベントが「背景雲の表示設定」の場合
                #雲のパラメータを設定します
                if   self.event_list[self.event_index][2] == CLOUD_NUM_SET:
                    self.cloud_append_interval  = self.event_list[self.event_index][3]    #雲を追加する間隔を設定
                    self.cloud_quantity        = self.event_list[self.event_index][4]    #雲の量を設定
                    self.cloud_how_flow        = self.event_list[self.event_index][5]    #雲の流れ方を設定
                    self.cloud_flow_speed      = self.event_list[self.event_index][6]    #雲の流れるスピードを設定
                #雲の表示を開始する
                elif self.event_list[self.event_index][2] == CLOUD_START:
                    self.display_cloud_flag = 1 #雲の表示フラグをonにします
                #雲の表示を停止する
                elif self.event_list[self.event_index][2] == CLOUD_STOP:
                    self.display_cloud_flag = 0 #雲の表示フラグをoffにします
                
            elif self.event_list[self.event_index][1] == EVENT_RASTER_SCROLL:     #イベントが「ラスタースクロールの制御」の場合
                search_id = self.event_list[self.event_index][3] #ラスタスクロールのidを変数に代入
                #IDごとにラスタスクロールの表示をon/offする
                if self.event_list[self.event_index][2] == RASTER_SCROLL_ON:     #ラスタスクロールon
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
                self.warning_dialog_flag = 1                                    #WARNING警告表示フラグをonにする
                self.warning_dialog_display_time = self.event_list[self.event_index][2] #警告表示時間を代入(単位は1フレーム)
                self.warning_dialog_logo_time    = self.event_list[self.event_index][3] #グラフイックロゴ表示にかける時間を代入(単位は1フレーム)
                self.warning_dialog_text_time    = self.event_list[self.event_index][4] #テキスト表示にかける時間を代入(単位は1フレーム)
                
                #pyxel.playm(0)#警告音発生！緊急地震速報Ver・・・・怖い・・・
                pyxel.playm(2)#警告音発生！
            elif self.event_list[self.event_index][1] == EVENT_BOSS:              #イベントの内容が「BOSS」の場合
                self.game_status = SCENE_BOSS_APPEAR                       #ゲームのステータスを「BOSS_APPEAR」ボス出現！にします
                self.born_boss()                                       #各面のボスを生み出す関数を呼び出します
                
            self.event_index += 1 #イベントインデックス値を1増やして次のイベントの実行に移ります

    #マップスクロールによる敵の発生
    def update_enemy_append_map_scroll(self):
        if self.no_enemy_mode == 1: #敵が出ないモードがonだったら・・・
            return              #何もせずに帰ります・・・・・
        
        #今表示したマップに（「敵出現」情報）のキャラチップが含まれていたら敵を発生させる
        for i in range(WINDOW_H // 8):
            self.get_bg_chip(WINDOW_W,i*8,0)#画面右端のマップチップのＢＧナンバーをゲットする(iの値・・・8で割ってまた8を掛けるのはスマートじゃないかも・・・)
            if self.bg_chip == (64 /8) * 32 +(48 / 8):#マップチップx48y64(A)だったら   敵3地上固定砲台を出現させる
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
                new_enemy.update(3,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   0,0,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,  1,0,    0, HP01 * self.enemy_hp_mag,   0,0,E_SIZE_NORMAL,0,0,0,     0,0,0,0,     item_number,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
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
                new_enemy.update(4,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,    0,0,0,0,0,0,0,0,0,0,   0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,  1,0,  0,  HP01 * self.enemy_hp_mag,    0,0,E_SIZE_NORMAL,0,0,0,    0,0,0,0,    item_number,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                self.delete_map_chip(self.bgx,i)#敵を出現させたら(「敵出現」情報)のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == (64 /8) * 32 +(64 / 8):#マップチップx64y64(C)だったら   敵5を出現させる（ホッパー君mk2）
                new_enemy = Enemy()
                new_enemy.update(5,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,    0.4,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,    0.2*self.enemy_speed_mag,0,  -1,    HP01 * self.enemy_hp_mag,   0,0,   E_SIZE_NORMAL,(i * 8),-20,1,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,MOVING_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == (64 /8) * 32 +(72 / 8):#マップチップx72y64(D)だったら   敵2を出現させる(サインカーブを描く敵)
                new_enemy = Enemy()
                new_enemy.update(SAISEE_RO,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,    1*self.enemy_speed_mag,0,   0,   HP01 * self.enemy_hp_mag,    0,0,   E_SIZE_NORMAL,   0.5,0.05,0,    0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == (64 /8) * 32 +(80 / 8):#マップチップx80y64(E)だったら   敵10を出現させる(地上スクランブルハッチ)
                new_enemy = Enemy()
                new_enemy.update(10,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,      0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,    0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_24,SIZE_16,   0.5,0,   0,    HP10 * self.enemy_hp_mag,   0,0,   E_SIZE_MIDDLE32,  (self.s_rndint(0,130) + 10),  6, 20,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT10,PT01)
                self.enemy.append(new_enemy)
                self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == (64 /8) * 32 +(88 / 8):#マップチップx88y64(F)だったら   敵11を出現させる(天井スクランブルハッチ)
                new_enemy = Enemy()
                new_enemy.update(11,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,    0,0,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_24,SIZE_16,   0.5,0,   0,    HP10 * self.enemy_hp_mag,   0,0,   E_SIZE_MIDDLE32_Y_REV,  (self.s_rndint(0,130) + 10),  6, 20,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,GROUND_OBJ,  PT01,PT01,PT01,  PT01,PT10,PT01)
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
                new_enemy.update(14,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,     0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    -0.44,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_24,SIZE_8,   0,0,   0,    HP10,   0,0,   E_SIZE_NORMAL,  0,0,0,   0,0,0,0,     item_number,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む 
                
            elif self.bg_chip == (64 /8) * 32 +(104/ 8):#マップチップx104y64(H)だったら  敵12を出現させる(直進して画面前方のどこかで停止→レーザービーム射出→急いで後退)
                new_enemy = Enemy()
                new_enemy.update(RAY_BLASTER,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W + 8,i * 8,0,0,      0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    -2,(self.s_rndint(0,1)-0.5),     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   0.98,0,    0,    HP01 * self.enemy_hp_mag,  0,0,    E_SIZE_NORMAL,   80 + self.s_rndint(0,40),0,0,     0,0,0,0,     E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                self.enemy.append(new_enemy)
                self.delete_map_chip(self.bgx,i)#敵を出現させたら（「敵出現」情報）のキャラチップは不要なのでそこに（0=何もない空白）を書き込む
                
            elif self.bg_chip == (64 /8) * 32 +(112/ 8):#マップチップx112y64(I)だったら  敵15を出現させる(地面を左右に動きながらチョット進んできて弾を撃つ移動砲台,何故か宇宙なのに重力の影響を受けて下に落ちたりもします)
                new_enemy = Enemy()
                new_enemy.update(15,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W,i * 8,0,0,       0,0,0,0,0,0,0,0,       0,0,0,0,0,0,0,0,0,0,    0,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   0.8*self.enemy_speed_mag,0,    -1,    HP01 * self.enemy_hp_mag,  70,80,    E_SIZE_NORMAL,   70,80,0,     0,0,0,0,       E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,MOVING_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
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
                        bg_ani_x =    self.bg_animation_list[i][0] #BGアニメーションを開始するチップのx座標を変数に代入
                        bg_ani_y =    self.bg_animation_list[i][1] #                         y座標を変数に代入
                        bg_ani_speed = self.bg_animation_list[i][2] #                        スピードを変数に代入
                        bg_ani_num =   self.bg_animation_list[i][3] #                        パターン数を変数に代入
                        
                        if (bg_ani_y / 8) * 32 + (bg_ani_x / 8) <= self.bg_chip <= (bg_ani_y / 8) * 32 + (bg_ani_x / 8 + bg_ani_num): #マップチップがx72y80からx128y80の間なら赤い棒のアニメーションパターンなので
                            #bg_ani_speed毎フレームに従ってbg_ani_numパターン数のアニメーションを行います
                            self.write_map_chip_free_scroll(self.bgx,self.bgy,(bg_ani_y // 8) * 32 + (bg_ani_x // 8) + pyxel.frame_count // bg_ani_speed % bg_ani_num)
            
            #中間の山脈の流れる滝のアニメーション
            #マップ座標のY=250だけ山脈遠景滝BGアニメーションチップを置くルールにしているのでy座標250だけ目的のマップチップがあるかをサーチして書き換える
            #
            #参考drawクラスでの山脈遠景表示のコード pyxel.bltm(-int(self.scroll_count  // 4  % (256*8 - 160)),-(self.vertical_scroll_count // 16) + 160,  1,    0,248,    256,5,    self.bg_transparent_color)
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
                    bg_ani_x     = self.bg_animation_list[i][0] #BGアニメーションを開始するチップのx座標を変数に代入
                    bg_ani_y     = self.bg_animation_list[i][1] #                         y座標を変数に代入
                    bg_ani_speed = self.bg_animation_list[i][2] #                        スピードを変数に代入
                    bg_ani_num   = self.bg_animation_list[i][3] #                        パターン数を変数に代入
                    
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
                            new_enemy.update(CIR_COIN,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,   WINDOW_W - 1 + (e * 12),self.event_append_request[i].posy,0,0,     0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0,0,0,  -1,1,    0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8, 1,0,   0, HP01,  0,0, E_SIZE_NORMAL,   30,0,0,     0,0,0,0,        E_NO_POW,self.current_formation_id ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                            self.enemy.append(new_enemy) 
                    
                    #編隊なので編隊のIDナンバーと編隊の総数、現在の編隊生存数をenemy_formationリストに登録します
                    self.record_enemy_formation(self.event_append_request[i].number)
                    del self.event_append_request[i] #敵を追加発生リクエストをリストから消去します

    #敵の更新（移動とか弾の発射とか他の敵を生み出すとか、そういう処理）
    def update_enemy(self):
        enemy_count = len(self.enemy)
        for i in range (enemy_count):
            if   self.enemy[i].enemy_type ==  1:#敵タイプ1の更新   サーコイン 直進して斜め後退→勢いよく後退していく10機編隊
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
                        if self.enemy[i].posx > WINDOW_W -8 and (self.s_rndint(0,self.run_away_bullet_probability) == 0):
                            self.ex = self.enemy[i].posx
                            self.ey = self.enemy[i].posy
                            self.enemy_aim_bullet(self.ex,self.ey,0,0,0,0,1)#後退時に自機狙いの弾を射出して去っていく
                
            elif self.enemy[i].enemy_type ==  2:#敵タイプ2の更新   サイシーロ サインカーブを描く3機編隊
                #敵２をサインカーブを描きながら移動させる 
                self.enemy[i].posx -= self.enemy[i].move_speed#X座標をmove_speed分減らして左方向に進む
                self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー enemy_count_2は速度
                self.enemy[i].posy += self.enemy[i].enemy_count1 * math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅
                
            elif self.enemy[i].enemy_type ==  3:#敵タイプ3の更新  固定砲台ホウダ（地面に張り付く１連射タイプ）
                #敵３を背景スクロールに合わせて左へ移動させる
                self.enemy[i].posx -= self.side_scroll_speed * 0.5
                if self.enemy[i].posx < WINDOW_W -80 and (self.s_rndint(0,(self.run_away_bullet_probability) * 50) == 0):
                    self.ex = self.enemy[i].posx
                    self.ey = self.enemy[i].posy
                    self.enemy_aim_bullet(self.ex,self.ey,0,0,0,0,1)#画面端から出現して８０ドット進んだら、自機狙いの弾を射出
                
            elif self.enemy[i].enemy_type ==  4:#敵タイプ4の更新   固定砲台ホウダ（天井に張り付く１連射タイプ）
                #敵４を背景スクロールに合わせて左へ移動させる
                self.enemy[i].posx -= self.side_scroll_speed * 0.5
                if self.enemy[i].posx < WINDOW_W -80 and (self.s_rndint(0,(self.run_away_bullet_probability) * 50) == 0):
                    self.ex = self.enemy[i].posx
                    self.ey = self.enemy[i].posy
                    self.enemy_aim_bullet(self.ex,self.ey,0,0,0,0,1)#画面端から出現して８０ドット進んだら、自機狙いの弾を射出
                
            elif self.enemy[i].enemy_type ==  5:#敵タイプ5の更新   ホッパーチャンmk2
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
                        if self.s_rndint(0,self.run_away_bullet_probability) == 0:
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
                
            elif self.enemy[i].enemy_type ==  6:#敵タイプ6の更新   謎の回転飛翔体Ｍ５４
                #敵6を回転させる 
                
                self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー(timer) enemy_count_2は速度(speed)
                self.enemy[i].posx += self.enemy[i].enemy_count1 * math.cos(self.enemy[i].enemy_count3)
                self.enemy[i].posy += self.enemy[i].enemy_count1 * -math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅(intensity)
                self.enemy[i].posx -= 0.05
                
            elif self.enemy[i].enemy_type ==  7:#敵タイプ7の更新   真！(SIN)ツインアロー追尾戦闘機(サインカーブを描きつつ追尾してくる)
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
                
            elif self.enemy[i].enemy_type ==  8:#敵タイプ8の更新   ツインアロー追尾戦闘機
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
                
            elif self.enemy[i].enemy_type ==  9:#敵タイプ9の更新   ロルボード 自機のＹ軸を合わせた後突進してくる敵
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
                
            elif self.enemy[i].enemy_type == 10:#敵タイプ10の更新  クランブルアンダー スクランブルハッチ（地面タイプ）
                #enemy_flag1を状態遷移フラグとして使用します
                #    0=待機中（射出開始カウンタを減らしていく）
                #    1～20ハッチ開放アニメーション中
                #    21  敵機発進待機中（射出間隔用カウンタを減らしていく）カウンタがゼロになったら遷移状態「22敵機発射」にする
                #    22  敵機発射！（敵総数カウンタを減らしていく）カウンタがゼロになったら遷移状態「23ハッチ閉鎖」にする
                #    23以上ハッチ閉鎖アニメーション中
                #    23以上は敵を出し切ったので何もしない
                #enemy_flag2を敵射出間隔制御用の変数として使用します
                #enemy_count1を出現してから突進タイプの敵を出すまでの時間のカウンタで使用します（射出開始カウンタ）（最初にどのタイミングで敵を出し始めるか数字を入れておいてね）
                #enemy_count2を射出する敵の総数です（敵総数カウンタ）                                  （最初に何機だすか数字を入れておいてね）
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
                        new_enemy.update(9,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.enemy[i].posx + 7,self.enemy[i].posy - 2,0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  -self.side_scroll_speed * 0.5,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   1.2,0,   0,    HP01,    0,0,   E_SIZE_NORMAL,  0,0,0,      0,0,0,0,       E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
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
                #背景スクロールに合わせて左へ移動させる
                self.enemy[i].posx -= self.side_scroll_speed * 0.5#基本BGスクロールスピードは0.5、それと倍率扱いのside_scroll_speedを掛け合わせてスクロールと同じように移動させてやる（地面スクロールに引っ付いた状態で飛んでいくように見せるため）         
                
            elif self.enemy[i].enemy_type == 11:#敵タイプ11の更新  クランブルアッパー スクランブルハッチ（天井タイプ）
                #enemy_flag1を状態遷移フラグとして使用します
                #    0=待機中（射出開始カウンタを減らしていく）
                #    1～20ハッチ開放アニメーション中
                #    21  敵機発進待機中（射出間隔用カウンタを減らしていく）カウンタがゼロになったら遷移状態「22敵機発射」にする
                #    22  敵機発射！（敵総数カウンタを減らしていく）カウンタがゼロになったら遷移状態「23ハッチ閉鎖」にする
                #    23以上ハッチ閉鎖アニメーション中
                #    23以上は敵を出し切ったので何もしない
                #enemy_flag2を敵射出間隔制御用の変数として使用します
                #enemy_count1を出現してから突進タイプの敵を出すまでの時間のカウンタで使用します（射出開始カウンタ）（最初にどのタイミングで敵を出し始めるか数字を入れておいてね）
                #enemy_count2を射出する敵の総数です（敵総数カウンタ）                                  （最初に何機だすか数字を入れておいてね）
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
                        new_enemy.update(9,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.enemy[i].posx + 7,self.enemy[i].posy + 10,0,0,       0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,  -self.side_scroll_speed * 0.5,0,     0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,     SIZE_8,SIZE_8,   1.2,0,    0,    HP01,    0,0,   E_SIZE_NORMAL,  0,0,0,     0,0,0,0,        E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
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
                #背景スクロールに合わせて左へ移動させる
                self.enemy[i].posx -= self.side_scroll_speed * 0.5 #基本BGスクロールスピードは0.5、それと倍率扱いのside_scroll_speedを掛け合わせてスクロールと同じように移動させてやる（地面スクロールに引っ付いた状態で飛んでいくように見せるため）
                
            elif self.enemy[i].enemy_type == 12:#敵タイプ12の更新  レイブラスター 直進して画面前方のどこかで停止→レーザービーム射出→急いで後退
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
                    self.enemy_laser(self.enemy[i].posx,self.enemy[i].posy,30,2 * self.enemy_bullet_speed_mag)#レーザーの長さ30 スピード2*ランクによる倍率
                    self.enemy[i].enemy_flag1 = 2#遷移状態を「レーザービーム発射中」にする
                    
                elif 2 <= self.enemy[i].enemy_flag1 <= 28:
                    self.enemy[i].enemy_flag1 += 1#遷移状態が「レーザービーム発射中」ならフラグを1増やしていく（その場にとどまるので座標の更新は無し）
                    
                elif 28 <= self.enemy[i].enemy_flag1 <= 46:#遷移状態が「後退中」なら高速で右方向に逃げていく
                    self.enemy[i].enemy_flag1 += 1#アニメーションしたいのでflag1だけは増やしていく
                    self.enemy[i].posx = self.enemy[i].posx + 1#2ドットの増分で右方向に逃げていく
                else:
                    self.enemy[i].posx = self.enemy[i].posx + 2#2ドットの増分で右方向に逃げていく                 
                
            elif self.enemy[i].enemy_type == 13:#敵タイプ13の更新  グリーンランサー ゆらゆら浮遊する3way弾を発射する硬い敵(倒すとショットパワーアップアイテム)
                #サインカーブを描きながら移動させる 
                self.enemy[i].posx -= self.enemy[i].move_speed#X座標をmove_speed分減らして左方向に進む
                self.enemy[i].enemy_count3 += self.enemy[i].enemy_count2#enemy_count3はタイマー enemy_count_2は速度
                self.enemy[i].posy += self.enemy[i].enemy_count1 * math.sin(self.enemy[i].enemy_count3)#enemy_count_1は振れ幅
                
                self.enemy[i].enemy_flag1 += 1 #flag1を利用してカウント90ごとに弾を発射させる
                if self.enemy[i].enemy_flag1 == 90:
                    self.enemy_forward_3way_bullet(self.enemy[i].posx,self.enemy[i].posy) #前方3way弾発射
                    self.enemy[i].enemy_flag1 = 0
                
            elif self.enemy[i].enemy_type == 14:#敵タイプ14の更新  テミー ゆっくり直進してくる赤いアイテムキャリアー
                #vx,vyで敵の座標posx,posy更新！移動！！
                self.enemy[i].posx += self.enemy[i].vx
                self.enemy[i].posy += self.enemy[i].vy
                
            elif self.enemy[i].enemy_type == 15:#敵タイプ15の更新  ムーロボ 地面を左右に動きながらチョット進んできて弾を撃つ移動砲台
                #敵１５を背景スクロールに合わせて移動させる（地上キャラなので不自然が無いように・・・）
                self.enemy[i].posx -= self.side_scroll_speed * 0.5
                if self.enemy[i].posx < WINDOW_W -80 and (self.s_rndint(0,(self.run_away_bullet_probability) * 50) == 0):
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
                            self.enemy[i].direction = 1                #方向転換して右移動にする
                            self.enemy[i].enemy_flag2 = self.enemy[i].enemy_count2 #右移動するカウントを原本からコピーしてやる
                            self.enemy[i].vx = 0             #方向転換する瞬間なのでx軸の移動ベクトルは0にします
                        else:
                            self.enemy[i].enemy_flag1 -= 1 #左移動のカウンタを1減らします
                            self.enemy[i].vx = -1             #x軸の移動ベクトルは左方向です
                    elif self.enemy[i].direction == 1: #右に移動
                        self.check_bg_collision(self.enemy[i].posx + 8,self.enemy[i].posy,0,0) #右側が障害物かどうかチェックする
                        if self.enemy[i].enemy_flag2 <= 0 or self.collision_flag == 1:#右移動のカウンタが0以下、又は右に障害物があったら
                            self.enemy[i].direction = -1               #方向転換して左移動にする
                            self.enemy[i].enemy_flag1 = self.enemy[i].enemy_count1 #左移動するカウントを原本からコピーしてやる
                            self.enemy[i].vx = 0             #方向転換する瞬間なのでx軸の移動ベクトルは0にします
                        else:
                            self.enemy[i].enemy_flag2 -= 1 #右移動のカウンタを1減らします
                            self.enemy[i].vx = 1             #x軸の移動ベクトルは右方向です
                
                self.check_bg_collision(self.enemy[i].posx + 4,self.enemy[i].posy + 8,0,0) #足元が障害物かどうかチェックする
                if self.collision_flag == 0:#もし足元に障害物が無かった時は
                    self.enemy[i].vy = 0.5  #y軸の移動ベクトルを1にして下方向(落下方向)にする
                    self.enemy[i].vx = self.enemy[i].vx * 0.8 #x軸方向の移動ベクトルもだんだんと小さくしていく
                else:
                    self.enemy[i].vy = 0  #障害物があった時はy軸のベクトルを0にする
                
                self.enemy[i].posx += self.enemy[i].vx * self.enemy[i].move_speed #移動ベクトル分加減算して移動！
                self.enemy[i].posy += self.enemy[i].vy * self.enemy[i].move_speed
                
            elif self.enemy[i].enemy_type == 16:#敵タイプ16の更新  クランパリオン 2機一体で挟みこみ攻撃をしてくる
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
                
            elif self.enemy[i].enemy_type == 17:#敵タイプ17の更新  ロールブリッツ ベジェ曲線で定点まで移動して離脱する敵
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
                self.enemy[i].timer += self.enemy[i].speed     #タイマーをスピード分増やしていく
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
                                self.enemy_aim_bullet_nway(self.enemy[i].posx     ,self.enemy[i].posy + 8 ,theta,n,division_type,division_count,division_num,stop_count) #後ろから発射  
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
                    division_type        = ENEMY_SHOT_DIVISION_3WAY   #自機狙いの3way
                    division_count       = 80 #分裂するまでのカウント数
                    division_count_origin = 80 #分裂するまでのカウント数(元数値)
                    division_num        = 0    #分裂する回数
                    new_enemy_shot.update(ENEMY_SHOT_NORMAL,ID00, self.enemy[i].posx + 4*8,self.enemy[i].posy + 10,ESHOT_COL_MIN88,ESHOT_SIZE8,ESHOT_SIZE8, 0,0, 1,0,     0.95,     1,1,    1,0, 0,1,0,        0,   0,0,PRIORITY_FRONT,   0,0,0,0,0,0, division_type,division_count,  0, division_count_origin,division_num, 0, 0,0, 0,0,   0,0)
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
                    
                elif self.boss[i].status == BOSS_STATUS_MOVE_BEZIER_CURVE:    #「ベジェ曲線で移動」
                    t = self.boss[i].obj_time / self.boss[i].obj_totaltime
                    if t >= 1: #tの値が1になった時は現在の座標が移動目的座標と同じ座標になった状況となるので・・・(行き過ぎ防止で念のため１以上で判別してます)
                        self.boss[i].obj_time = 0    #タイムフレーム番号を0にしてリセットする                    
                        self.boss[i].move_index += 1 #目的座標のリストのインデックスを1進める
                        if self.boss_move_data1[self.boss[i].move_index][0] == 9999:#x座標がエンドコード9999の場合は
                            self.boss[i].move_index = 0 #リストインデックス値を0にしてリセットする
                        self.boss_get_bezier_curve_coordinate(i) #ボスをベジェ曲線で移動させるために必要な座標をリストから取得する関数の呼び出し
                        t = self.boss[i].obj_time / self.boss[i].obj_totaltime #違う座標データ群を読み込んだのでt値を再計算してやる
                    
                    #          A(移動元)--D(移動先)
                    #            \    点P /     
                    #(AとQの内分点)P1\     /P2(QとDの内分点)    
                    #              \   /
                    #               Q(制御点)
                    #
                    #内分の公式からP1の座標は((1-t)ax+t*qx,(1-t)ay+t*qy)
                    #           P2の座標は((1-t)qx+t*dx,(1-t)qy+t*dy)
                    #したがってPの座標も内分の公式から求められる
                    #P1の座標を(p1x,p1y),P2の座標を(p2x,p2y)とすると点Pの座標は
                    #        ((1-t)p1x+t*p2x,(1-t)p1y+t*p2y)となり
                    #先に求めたP1,P2を代入してやると
                    #        ((1-t)(1-t)ax+t*qx+t*(1-t)qx+t*dx,(1-t)(1-t)ay+t*qy+t*(1-t)qy+t*dy)となる
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
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION_START:      #ボス撃破！爆発開始！の処理
                    self.boss[i].attack_method = BOSS_ATTACK_NO_FIRE #ボスの攻撃方法は「ノーファイア」何も攻撃しないにする、まぁ撃破したからね
                    
                    self.boss[i].vx = (WINDOW_W / 2 - self.boss[i].posx ) / 480 * 1.5 #ボスが居た位置に乗じた加速度を設定する vxは画面中央を境にプラスマイナスに分かれる 480で割っているのは480フレーム掛けて画面の端まで動くためです
                    self.boss[i].vy = (WINDOW_H - self.boss[i].posy) / 480 - 0.3     #vyは爆発した瞬間少し上に跳び上がった感じにしたいので -0.3しています
                    self.boss[i].count1 = 240 #count1を爆裂分裂開始までのカウントとして使います
                    self.boss[i].status = BOSS_STATUS_EXPLOSION #ボスの状態遷移ステータスを「爆発中」にする
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION:           #ボスステータスが「爆発中」の処理
                    #爆発中サウンド再生
                    pyxel.play(3,11)
                    
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + self.s_rndint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + self.s_rndint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].posx += self.boss[i].vx
                    self.boss[i].posy += self.boss[i].vy
                    self.boss[i].vy += 0.001 #1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count1 -= 1 #count1(爆裂分裂開始までのカウント)を１減らしていきます
                    if self.boss[i].count1 <= 0: #爆裂分裂開始までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_BLAST_SPLIT_START #状態遷移ステータスを「爆発分離開始」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT_START:    #ボスステータスが「爆発分離開始」の処理
                    self.boss[i].count2 = 480 #count2をボス破壊後に分裂するシーン全体のフレーム数を登録します
                    
                    #爆発分離開始のサウンド再生
                    pyxel.playm(1)
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + self.s_rndint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + self.s_rndint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0, 1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].status = BOSS_STATUS_BLAST_SPLIT #ボスステータスを「爆発分離」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT:         #ボスステータスが「爆発分離」の処理
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + self.s_rndint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + self.s_rndint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    #ボスの爆発破片3を育成 ホワイト系のスパーク
                    if self.boss[i].count2 % 3 == 0:
                        self.update_append_particle(PARTICLE_BOSS_DEBRIS3,self.boss[i].posx + 30 + self.s_rndint(0,30) -15 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,12,0,0)
                    
                    #ボスの爆発破片4を育成 橙色系の落下する火花
                    if self.boss[i].count2 % 1 == 0:
                        self.update_append_particle(PARTICLE_BOSS_DEBRIS4,self.boss[i].posx + 30 + self.s_rndint(0,40) -20 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,8,0,0)
                    
                    self.boss[i].posx += self.boss[i].vx / 1.5
                    self.boss[i].posy += self.boss[i].vy / 1.5
                    self.boss[i].vy += 0.001  / 1.5#1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count2 -= 1 #count2(ボス消滅までのカウント)を１減らしていきます
                    if self.boss[i].count2 <= 0: #ボス消滅までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_DISAPPEARANCE #ボスステータスを「ボス消滅」にします
                    
                elif self.boss[i].status == BOSS_STATUS_DISAPPEARANCE:        #ボスステータスが「ボス消滅」の処理
                    self.game_status = SCENE_STAGE_CLEAR_MOVE_MY_SHIP #ゲームステータス(状態遷移)を「ステージクリア自機自動移動」にする
                    
                    self.stage_clear_dialog_flag          = 1   #STAGE CLEARダイアログ表示フラグをonにする
                    self.stage_clear_dialog_display_time  = 300 #STAGE CLEARダイアログ表示時間その1を代入(単位は1フレーム)
                    
                    self.stage_clear_dialog_logo_time1       = 90 #グラフイックロゴ表示にかける時間を代入その1(単位は1フレーム)
                    self.stage_clear_dialog_logo_time2       = 90 #グラフイックロゴ表示にかける時間を代入その2(単位は1フレーム)
                    self.stage_clear_dialog_text_time        = 180 #テキスト表示にかける時間を代入(単位は1フレーム)だんだん減っていく
                    self.stage_clear_dialog_text_time_master = 180 #テキスト表示にかける時間を代入(単位は1フレーム)元の値が入ります
                    
                    self.move_mode = MOVE_AUTO                           #自機のオートムーブモードをonにして自動移動を開始する
                    self.move_mode_auto_x,self.move_mode_auto_y = 25,40  #移動先の座標を指定 
                    
                    del self.boss[i]                      #ボスのインスタンスを消去する・・・さよならボス・・（けもふれ？）
                    break                               #ループから抜け出す
                
                ####ここからはボスの攻撃パターンです############################################################
                if   self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY:         #画面上部を左から右に弧を描いて移動中
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
                    if (pyxel.frame_count % int(40 * self.enemy_bullet_interval / 100)) == 0: #40フレーム毎に
                        ex = self.boss[i].posx + 40
                        ey = self.boss[i].posy + 18
                        self.enemy_forward_5way_bullet(ex,ey) #前方5way発射！
                        
                        ex = self.boss[i].posx + 40
                        ey = self.boss[i].posy + 18
                        self.enemy_aim_bullet(ex,ey,0,0,0,0,1)        #狙い撃ち弾発射
                    
                elif self.boss[i].attack_method == BOSS_ATTACK_FRONT_5WAY_HOMING:    #下部を右から左に弧を描いて移動中
                    if (pyxel.frame_count % 60) == 0 and self.boss[i].parts1_flag == 1: #60フレーム毎に5way砲台が健在なら
                        ex = self.boss[i].posx
                        ey = self.boss[i].posy + 18
                        self.enemy_forward_5way_bullet(ex,ey) #前方5way発射！
                    if self.boss[i].posx < 10:
                        if (pyxel.frame_count % 20) == 0: #20フレーム毎に
                            if len(self.enemy) < 400:
                                new_enemy = Enemy()#敵8ツインアローを1機生み出す
                                new_enemy.update(TWIN_ARROW,ID00,ENEMY_STATUS_NORMAL,ENEMY_ATTCK_ANY,    self.boss[i].posx + 48,self.boss[i].posy + 8,0,0,      0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,0,0,   1,-1,      0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0,0,0,0,0,0,0,    SIZE_8,SIZE_8,   1,0,   0,    HP01,    0,0,   E_SIZE_NORMAL,  0,0,1,       0,0,0,0,        E_NO_POW,ID00 ,0,0,0,    0  ,0,0,0,    0,AERIAL_OBJ,  PT01,PT01,PT01,  PT01,PT01,PT01)
                                self.enemy.append(new_enemy)#リストにアペンド追加！
                
            elif self.boss[i].boss_type == BOSS_BREEZARDIA:    #ボスタイプ0の更新 ブリザーディア ##################################
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
                        self.boss[i].direction = 0         #方向を後退(0)にする
                    elif self.boss[i].posx < -60:        #x座標が画面左端を超えたのなら
                        self.boss[i].direction = 1         #方向を前進(1)にする
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION_START:      #ボス撃破！爆発開始！の処理
                    self.boss[i].attack_method = BOSS_ATTACK_NO_FIRE #ボスの攻撃方法は「ノーファイア」何も攻撃しないにする、まぁ撃破したからね
                    
                    self.boss[i].vx = (WINDOW_W / 2 - self.boss[i].posx ) / 480 * 1.5 #ボスが居た位置に乗じた加速度を設定する vxは画面中央を境にプラスマイナスに分かれる 480で割っているのは480フレーム掛けて画面の端まで動くためです
                    self.boss[i].vy = (WINDOW_H - self.boss[i].posy) / 480 - 0.3     #vyは爆発した瞬間少し上に跳び上がった感じにしたいので -0.3しています
                    self.boss[i].count1 = 240 #count1を爆裂分裂開始までのカウントとして使います
                    self.boss[i].status = BOSS_STATUS_EXPLOSION #ボスの状態遷移ステータスを「爆発中」にする
                    
                elif self.boss[i].status == BOSS_STATUS_EXPLOSION:           #ボスステータスが「爆発中」の処理
                    #爆発中サウンド再生
                    pyxel.play(3,11)
                    
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + self.s_rndint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + self.s_rndint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].posx += self.boss[i].vx
                    self.boss[i].posy += self.boss[i].vy
                    self.boss[i].vy += 0.001 #1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count1 -= 1 #count1(爆裂分裂開始までのカウント)を１減らしていきます
                    if self.boss[i].count1 <= 0: #爆裂分裂開始までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_BLAST_SPLIT_START #状態遷移ステータスを「爆発分離開始」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT_START:    #ボスステータスが「爆発分離開始」の処理
                    self.boss[i].count2 = 480 #count2をボス破壊後に分裂するシーン全体のフレーム数を登録します
                    
                    #爆発分離開始のサウンド再生
                    pyxel.playm(1)
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + self.s_rndint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + self.s_rndint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    self.boss[i].status = BOSS_STATUS_BLAST_SPLIT #ボスステータスを「爆発分離」にします
                    
                elif self.boss[i].status == BOSS_STATUS_BLAST_SPLIT:         #ボスステータスが「爆発分離」の処理
                    #ランダムな場所に爆発パターンを育成
                    new_explosion = Explosion()
                    new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.boss[i].posx + self.boss[i].width / 2 + self.s_rndint(0,50) -25,self.boss[i].posy + self.boss[i].height / 2 + self.s_rndint(0,20) -15,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                    self.explosions.append(new_explosion)
                    
                    #ボスの爆発破片3を育成 ホワイト系のスパーク
                    if self.boss[i].count2 % 3 == 0:
                        self.update_append_particle(PARTICLE_BOSS_DEBRIS3,self.boss[i].posx + 30 + self.s_rndint(0,30) -15 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,12,0,0)
                    
                    #ボスの爆発破片4を育成 橙色系の落下する火花
                    if self.boss[i].count2 % 1 == 0:
                        self.update_append_particle(PARTICLE_BOSS_DEBRIS4,self.boss[i].posx + 30 + self.s_rndint(0,40) -20 ,self.boss[i].posy + 10,(random()- 0.5) /2,random() * 2,8,0,0)
                    
                    self.boss[i].posx += self.boss[i].vx / 1.5
                    self.boss[i].posy += self.boss[i].vy / 1.5
                    self.boss[i].vy += 0.001  / 1.5#1フレームごとに下方向へ0.001加速して落ちていきます
                    
                    self.boss[i].count2 -= 1 #count2(ボス消滅までのカウント)を１減らしていきます
                    if self.boss[i].count2 <= 0: #ボス消滅までのカウントが0になったのなら
                        self.boss[i].status = BOSS_STATUS_DISAPPEARANCE #ボスステータスを「ボス消滅」にします 
                    
                elif self.boss[i].status == BOSS_STATUS_DISAPPEARANCE:        #ボスステータスが「ボス消滅」の処理
                    self.game_status = SCENE_STAGE_CLEAR_MOVE_MY_SHIP #ゲームステータス(状態遷移)を「ステージクリア自機自動移動」にする
                    
                    self.stage_clear_dialog_flag             = 1   #STAGE CLEARダイアログ表示フラグをonにする
                    self.stage_clear_dialog_display_time     = 300 #STAGE CLEARダイアログ表示時間その1を代入(単位は1フレーム)
                    
                    self.stage_clear_dialog_logo_time1       = 90 #グラフイックロゴ表示にかける時間を代入その1(単位は1フレーム)
                    self.stage_clear_dialog_logo_time2       = 90 #グラフイックロゴ表示にかける時間を代入その2(単位は1フレーム)
                    self.stage_clear_dialog_text_time        = 180 #テキスト表示にかける時間を代入(単位は1フレーム)だんだん減っていく
                    self.stage_clear_dialog_text_time_master = 180 #テキスト表示にかける時間を代入(単位は1フレーム)元の値が入ります
                    
                    self.move_mode = MOVE_AUTO                           #自機の移動モードをを「AUTO」にして自動移動を開始する
                    self.move_mode_auto_x,self.move_mode_auto_y = 25,40  #移動先の座標を指定 
                    
                    del self.boss[i]                      #ボスのインスタンスを消去する・・・さよならボス・・（けもふれ？）
                    break                                 #ループから抜け出す
                
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
                        new_enemy_shot.update(ENEMY_SHOT_GREEN_CUTTER,ID00,ex,ey,ESHOT_COL_BOX,ESHOT_SIZE8,ESHOT_SIZE12,    0,0,  -1,0,      1.05,    1,1,    0,0,  0,0,0,            0,   0,0,PRIORITY_BOSS_BACK,   0,0, 0,0,0,0, 0,0, 0, 0,0, 0, 0,0, 0,0,   0,0)
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
                        if self.boss[i].weapon1_rapid_num >= 3 + self.enemy_bullet_append: #(3+ランクに応じた追加数)ぶん発射したのならば・・
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
            return                 #衝突判定はせずそのまま帰っちゃう・・・無敵最高！
        
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
            return                 #衝突判定はせずそのまま帰っちゃう・・・無敵最高！
        boss_count = len(self.boss)
        for i in range (boss_count):
            if self.boss[i].invincible != 1: #もしボスが無敵状態で無いのならば
                #自機がボスの当たり判定矩形の中に存在するのか判別する、存在していたらボスと自機は衝突しています
                #ボス本体当たり判定1との判定
                if     self.boss[i].posx + self.boss[i].col_main1_x <= self.my_x + 4 <= self.boss[i].posx + self.boss[i].col_main1_x + self.boss[i].col_main1_w\
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
            return                        #衝突判定はせずそのまま帰っちゃう
        if self.invincible_counter > 0: #無敵時間が残っていた場合は・・・
            return                 #衝突判定はせずそのまま帰っちゃう・・・無敵最高！
        self.check_bg_collision(self.my_x + 6,self.my_y + 4,0,0)
        if self.collision_flag == 1: #コリジョンフラグが建っていたのなら
            self.update_my_ship_damage(1) #障害物に当たったので自機のシールド値を減らす

    #サブウェポン切り替えボタンが押された＆サブウェポンを一つでも所維持しているのか？チェックする      GAMEPAD Y
    def update_check_change_sub_weapon(self):
        if self.replay_status == REPLAY_PLAY: #リプレイステータスが「再生中」の場合は
            if self.replay_data[self.replay_stage_num][self.replay_frame_index + 1] & 0b10000000 == 0b10000000: #LowByte リプレイデータを調べてPAD Yが押された記録だったのなら...
                self.update_change_sub_weapon() #サブウェポン切り替え関数呼び出し！
        elif self.move_mode == MOVE_MANUAL: #手動移動モードの場合は
            if pyxel.btnp(pyxel.GAMEPAD_1_Y) or pyxel.btnp(pyxel.GAMEPAD_2_Y) and self.select_sub_weapon_id != -1:#サブウェポン切り替えボタンが押された＆サブウェポンを一つでも所維持しているのか？
                self.pad_data_l += PAD_Y #コントロールパッド入力記録にYボタンを押した情報ビットを立てて記録する
                self.update_change_sub_weapon() #サブウェポン切り替え関数呼び出し！

    #サブウェポンを切り替える!!!!!
    def update_change_sub_weapon(self):
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
        self.invincible_counter += self.invincible_time #ダメージ後の無敵時間を加算する
        
        self.rank_down_count += 1 #ランクダウン用カウンタを１増やす
        if self.rank_down_count == self.rank_down_need_damage: #カウンタがランクダウンに必要であるダメージ分まで増えたのなら
            self.rank_down()  #1ランクダウンさせる関数の呼び出し
            self.rank_down_count = 0 #カウンターをリセット

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
            if     ITEM_SHOT_POWER_UP     <= self.obtain_item[i].item_type <= ITEM_CLAW_POWER_UP\
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
                if d <= self.item_range_of_attraction: #アイテムと自機との距離がitem_range_of_attraction以内の場合アイテムのx,y座標を自機の方向へ向かう様に補正を入れる
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
                    self.obtain_item[i].posx  -= self.obtain_item[i].vx     #X座標をvx分減らして左方向に進む
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
                    
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    self.level_up_my_shot()     #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
                    self.level_up_my_missile()   #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
                    
                    del self.obtain_item[i]#パワーアップアイテムのインスタンスを破棄する(アイテム消滅)
                    if self.shot_level > 10:    #ショットレベルは10を超えないようにする
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
                self.invincible_counter += self.get_item_invincible_time #アイテムを取ったので無敵時間のカウンターを増やす
                if ITEM_SHOT_POWER_UP <= self.obtain_item[i].item_type <= ITEM_SHIELD_POWER_UP: #ショット、ミサイル、シールドパワーアップの処理
                    self.shot_exp    += self.obtain_item[i].shot    #ショット経験値をショットパワーの増加量の分だけパワーアップさせる
                    self.missile_exp += self.obtain_item[i].missile #ミサイル経験値をミサイルパワーの増加量の分だけパワーアップさせる
                    self.my_shield   += self.obtain_item[i].shield  #シールド値（ヒットポイント）をシールドパワーの増加量の分だけパワーアップさせる
                    
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    self.level_up_my_shot()     #自機ショットの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
                    self.level_up_my_missile()   #自機ミサイルの経験値を調べ可能な場合レベルアップをさせる関数を呼び出す
                    
                    del self.obtain_item[i]#パワーアップアイテムのインスタンスを破棄する(アイテム消滅)
                    if self.shot_level > 10:    #ショットレベルは10を超えないようにする
                        self.shot_level = 10
                    if self.missile_level > 2:   #ミサイルレベルは2を超えないようにする
                        self.missile_level = 2
                    
                elif self.obtain_item[i].item_type == ITEM_CLAW_POWER_UP: #クローパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #クローアイテムのインスタンスを破棄する(アイテム消滅)
                    self.update_append_claw()    #クローの発生関数の呼び出し
                    
                elif self.obtain_item[i].item_type == ITEM_TAIL_SHOT_POWER_UP: #テイルショットパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #インスタンスを破棄する(アイテム消滅)
                    if self.sub_weapon_list[TAIL_SHOT] < SUB_WEAPON_LEVEL_MAXIMUM:#テイルショットのレベルがサブウェポンのレベル最大値を超えていないのならば
                        self.sub_weapon_list[TAIL_SHOT] += 1  #サブウェポンリスト内のテイルショットの所持数を１増やす
                    if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                        self.select_sub_weapon_id = TAIL_SHOT #強制的にテイルショットを選択させる
                    
                elif self.obtain_item[i].item_type == ITEM_PENETRATE_ROCKET_POWER_UP: #ペネトレートロケットパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #インスタンスを破棄する(アイテム消滅)
                    if self.sub_weapon_list[PENETRATE_ROCKET] < SUB_WEAPON_LEVEL_MAXIMUM:#ペネトレートロケットのレベルがサブウェポンのレベル最大値を超えていないのならば
                        self.sub_weapon_list[PENETRATE_ROCKET] += 1  #サブウェポンリスト内のペネトレートロケットの所持数を１増やす
                    if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                        self.select_sub_weapon_id = PENETRATE_ROCKET #強制的にペネトレートロケットを選択させる
                    
                elif self.obtain_item[i].item_type == ITEM_SEARCH_LASER_POWER_UP: #サーチレーザーパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #インスタンスを破棄する(アイテム消滅)
                    if self.sub_weapon_list[SEARCH_LASER] < SUB_WEAPON_LEVEL_MAXIMUM:#ーチレーザーのレベルがサブウェポンのレベル最大値を超えていないのならば
                        self.sub_weapon_list[SEARCH_LASER] += 1  #サブウェポンリスト内のサーチレーザーの所持数を１増やす
                    if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                        self.select_sub_weapon_id = SEARCH_LASER #強制的にサーチレーザーを選択させる
                    
                elif self.obtain_item[i].item_type == ITEM_HOMING_MISSILE_POWER_UP: #ホーミングミサイルパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #インスタンスを破棄する(アイテム消滅)
                    if self.sub_weapon_list[HOMING_MISSILE] < SUB_WEAPON_LEVEL_MAXIMUM:#ホーミングミサイルのレベルがサブウェポンのレベル最大値を超えていないのならば
                        self.sub_weapon_list[HOMING_MISSILE] += 1  #サブウェポンリスト内のホーミングミサイルの所持数を１増やす
                    if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                        self.select_sub_weapon_id = HOMING_MISSILE #強制的にホーミングミサイルを選択させる
                    
                elif self.obtain_item[i].item_type == ITEM_SHOCK_BUMPER_POWER_UP: #ショックバンバーパワーアップの処理
                    pyxel.play(0,0)            #パワーアップアイテムゲットの音を鳴らすのだ
                    del self.obtain_item[i]     #インスタンスを破棄する(アイテム消滅)
                    
                    if self.sub_weapon_list[SHOCK_BUMPER] < SUB_WEAPON_LEVEL_MAXIMUM:#ショックバンバーのレベルがサブウェポンのレベル最大値を超えていないのならば
                        self.sub_weapon_list[SHOCK_BUMPER] += 1  #サブウェポンリスト内のショックバンバーの所持数を１増やす
                    if self.select_sub_weapon_id == -1: #もしサブウェポンを何も所持していない状態でアイテムを取ったのなら・・・
                        self.select_sub_weapon_id = SHOCK_BUMPER #強制的にショックバンバーを選択させる

    #パワーアップアイテム類と敵弾の当たり判定(難易度によってパワーアップアイテムは敵弾を消す効果あり)
    def update_collision_obtain_item_enemy_shot(self):
        if self.item_erace_bullet_flag == 0: #パワーアップアイテムが敵弾を消すフラグが立っていないのならそのままリターンする
            return
        
        obtain_item_hit = len(self.obtain_item)
        for h in reversed(range(obtain_item_hit)):
            enemy_shot_hit = len(self.enemy_shot)
            for e in reversed(range(enemy_shot_hit)):
                if     -4 <= self.obtain_item[h].posx - self.enemy_shot[e].posx <= 4\
                    and -4 <= self.obtain_item[h].posy - self.enemy_shot[e].posy <= 4:
                    #敵弾消滅時のパーティクル生成
                    for _number in range(5):
                        self.update_append_particle(PARTICLE_DOT,self.enemy_shot[e].posx + 4,self.enemy_shot[e].posy + 4,self.obtain_item[h].vx / 2,self.obtain_item[h].vy / 2,   0,0,0)
                    
                    del self.enemy_shot[e] #敵弾をリストから消去

    #画面外に出たパワーアップアイテム類を消去する
    def update_clip_obtain_item(self):
        obtain_item_count = len(self.obtain_item)
        for i in reversed(range (obtain_item_count)):
            if -50 < self.obtain_item[i].posx < WINDOW_W + 200 and -150 < self.obtain_item[i].posy < WINDOW_H + 150: #xは-50~160+200 Yは-150~120+150以内？
                continue
            else:
                del self.obtain_item[i]#パワーアップアイテムが画面外に存在するときはインスタンスを破棄する(アイテム消滅)

    #ボス破壊後にリペアアイテムを出現させる 
    def uddate_present_repair_item(self):
        if self.present_repair_item_flag == 0: #ボーナスアイテムを出したフラグがまだ建っていないのなら
            #ボーナスアイテムを出現させる
            for _i in range(self.repair_shield):
                y = self.s_rndint(30,80)
                new_obtain_item = Obtain_item()
                new_obtain_item.update(ITEM_SHIELD_POWER_UP,WINDOW_W,y, 0.5+ (self.s_rndint(0,1)-0.5)* 0.2,0 + (self.s_rndint(0,4)-2) * 0.6,   SIZE_8,SIZE_8,   1,   0.9,  0.3,   0,0,  0.05,0,0,0,0,   0,0,1,  0,0,0, self.pow_item_bounce_num,0)
                self.obtain_item.append(new_obtain_item)
                
            self.present_repair_item_flag = 1 #フラグを立ててもう出ないようにする

    #爆発パターンの更新→撃ち返し弾の発生
    def update_explosion(self):
        explosioncount = len(self.explosions)
        for i in reversed(range(explosioncount)):
            #爆発パターンを背景スクロールに合わせて移動させる
            self.explosions[i].posx -= self.side_scroll_speed * 0.5#基本BGスクロールスピードは0.5、それと倍率扱いのside_scroll_speedを掛け合わせてスクロールと同じように移動させてやる（地面スクロールに引っ付いた状態で爆発してるように見せるため）         
            self.explosions[i].explosion_count -= 1#爆発育成時に設定したカウントを1減らす
            fire_rnd = self.s_rndint(0,100)
            if    self.explosions[i].explosion_count == 9\
                and self.stage_loop * ALL_STAGE_NUMBER + self.stage_number >= self.return_bullet_start_loop * ALL_STAGE_NUMBER + self.return_bullet_start_stage\
                and fire_rnd <= self.return_bullet_probability: 
                #カウント9の時&return_bullet_probabilityパーセントの確率&現在のループ数とステージ数がstart_loop,start_stageの数値以上ならば撃ち返し弾を出す
                if     self.explosions[i].return_bullet_type == RETURN_BULLET_AIM\
                    or self.explosions[i].return_bullet_type == RETURN_BULLET_DELAY_AIM:
                    #自機狙い弾を1発うちかえす
                    self.enemy_aim_bullet(self.explosions[i].posx,self.explosions[i].posy,0,0,0,0,1)#自機狙いの撃ち返し弾発射！
                elif    self.explosions[i].return_bullet_type == RETURN_BULLET_3WAY:
                    #自機狙いの3way弾の場合は.....
                    ex = self.explosions[i].posx
                    ey = self.explosions[i].posy
                    theta = 30
                    n = 3
                    division_type = 0
                    division_count = 0
                    division_num = 0
                    stop_count = 0
                    self.enemy_aim_bullet_nway(ex,ey,theta,n,division_type,division_count,division_num,stop_count)
                
                if    self.explosions[i].return_bullet_type == RETURN_BULLET_DELAY_AIM:
                    #ディレイをかけた打ち返し弾を発射(ちょっと加速気味)
                    self.enemy_aim_bullet(self.explosions[i].posx,self.explosions[i].posy,0,0,0,10,1.01)#その場でちょっと止まって自機狙いの撃ち返し弾発射！
                
            if self.explosions[i].explosion_type == EXPLOSION_MIDDLE: #中間サイズの爆発パターンの場合は
                #1フレームごとに通常爆発パターンを追加発生させる
                new_explosion = Explosion()
                new_explosion.update(EXPLOSION_NORMAL,PRIORITY_FRONT,self.explosions[i].posx + 4 + self.s_rndint(0,24)-12,self.explosions[i].posy + 4 + self.s_rndint(0,12)-6,0,0,10,RETURN_BULLET_NONE,0,  1,1)
                self.explosions.append(new_explosion)
                
            if self.explosions[i].explosion_count == 0: #カウントが0の時は....
                del self.explosions[i] #爆発リストをDELしちゃう（お前・・消えるのか・・・？）

    #パーティクルの追加（発生＆育成）
    def update_append_particle(self,particle_type,x,y,dx,dy,life,wait,color):
        if len(self.particle) < 1000: #パーティクルの総数が1000以下なら追加発生させる
            if particle_type == PARTICLE_DOT or particle_type == PARTICLE_CIRCLE: #ドットパーティクル 円形パーティクルの追加
                new_particle = Particle()
                new_particle.update(particle_type, x+4,y+4,    self.s_rndint(0,1),    random() * 2 - 0.5 + dx,    random() * 2 - 1 + dy,   self.s_rndint(5,20), 0,  self.s_rndint(1,14))
                self.particle.append(new_particle)
                
            elif particle_type == PARTICLE_LINE: #ラインパーティクル（線状の尾を引くようなパーティクルです）
                for i in range(10):
                    new_particle = Particle()
                    new_particle.update(particle_type, x-2,y+4,    1,    -0.8-random(), random()-0.2,    10,   i, 6)
                    self.particle.append(new_particle)
                    
                    #ボスにダメージを与えたとき
                    #new_particle = Particle()
                    #new_particle.update(particle_type, x-4,y+4,    1,    -0.8-random(), random()-0.2,    30,   i, 8)
                    #self.particle.append(new_particle)
                
            elif particle_type == PARTICLE_MISSILE_DEBRIS: #ミサイルの破片の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    0,0,   7,   0,0)
                self.particle.append(new_particle)
                
            elif particle_type == PARTICLE_BOSS_DEBRIS1: #ボスの破片1の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)
            elif particle_type == PARTICLE_BOSS_DEBRIS2: #ボスの破片2の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)
            elif particle_type == PARTICLE_BOSS_DEBRIS3: #ボスの破片3の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)
            elif particle_type == PARTICLE_BOSS_DEBRIS4: #ボスの破片4の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)
            elif particle_type == PARTICLE_BOSS_DEBRIS5: #ボスの破片5の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
                self.particle.append(new_particle)
            elif particle_type == PARTICLE_BOSS_DEBRIS6: #ボスの破片6の追加
                new_particle = Particle()
                new_particle.update(particle_type, x,y,    0,    dx,dy,   life,   0,0)
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
            if       -100 <= self.background_object[i].posx <= WINDOW_W + 100\
                and  -100 <= self.background_object[i].posx <= WINDOW_H + 100:
                continue
            else:
                del self.background_object[i] #描画範囲外になったのでインスタンスを破棄する

    #雲の追加(背景オブジェクト)
    def update_append_cloud(self):
        if (pyxel.frame_count % self.cloud_append_interval) == 0 and self.display_cloud_flag == 1: #表示インタバールが0になった&表示フラグがonだったのなら
            if self.cloud_quantity == 0: #雲の量が0の時は「雲小」のみ表示する
                t = self.s_rndint(BG_OBJ_CLOUD1,BG_OBJ_CLOUD10)
            elif self.cloud_quantity == 1: #雲の量が1の時は「雲小～中」まで表示する
                t = self.s_rndint(BG_OBJ_CLOUD1,BG_OBJ_CLOUD18)
            elif self.cloud_quantity == 2: #雲の量が2の時は「雲小～中～大」まで表示する
                t = self.s_rndint(BG_OBJ_CLOUD1,BG_OBJ_CLOUD21)
            
            y = self.s_rndint(0,120+30)
            new_background_object = Background_object()
            new_background_object.update(t, 160+10,y,  0,    1.009,1,0,0,0,0,0,0,   -3*self.cloud_flow_speed,self.cloud_how_flow,  0,0,   0,0,0,0,0,   0,0,0, 0,0,0,  0,0,0)
            self.background_object.append(new_background_object)

    #タイマーフレアの更新(接触した物質の時間経過を遅くするフレアエフェクト)
    def update_timer_flare(self):
        if self.timer_flare_flag == 0: #タイマーフレアのフラグが建っていなかったらそのまま戻る
            return
            
        for i in range(30):
            new_particle = Particle()
            new_particle.update(PARTICLE_LINE, self.my_x+3,self.my_y+3,    1,    -random()-0.5, random()-0.5,    80,   i*6, 6)
            self.particle.append(new_particle)

    #大気圏突入時の火花の更新
    def update_atmospheric_entry_spark(self):
        if self.atmospheric_entry_spark_flag == SPARK_OFF: #大気圏突入時の火花のフラグが建っていなかったらそのまま戻る
            return
            
        for _i in range(10):
            new_particle = Particle()
            # new_particle.update(PARTICLE_DOT, self.my_x+1,self.my_y+5,    1,    -random() * self.side_scroll_speed * 4, (random() - 0.97) * self.vertical_scroll_speed * 8,    30,   _i // 2, 10)
            new_particle.update(PARTICLE_FIRE_SPARK, self.my_x+3,self.my_y+4,    1,    -random() * self.side_scroll_speed, -(random()+0.5)  * self.vertical_scroll_speed * 2,    2.5 * self.side_scroll_speed,   1, 10)
            
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

    #ポーズボタンが押されたか調べる                                           KEY TAB    GAMEPAD START
    def update_check_pause_button(self):
        if pyxel.btnp(pyxel.KEY_TAB) or pyxel.btnp(pyxel.GAMEPAD_1_START) or pyxel.btnp(pyxel.GAMEPAD_2_START):
            if    self.game_status == SCENE_PLAY\
                or self.game_status == SCENE_BOSS_APPEAR\
                or self.game_status == SCENE_BOSS_BATTLE\
                or self.game_status == SCENE_BOSS_EXPLOSION:#ステータスが「PLAY」もしくは「BOSS関連」のときにポーズボタンが押されたときは・・
                
                self.record_games_status = self.game_status #ステータスを一時記憶しておく
                self.game_status = SCENE_PAUSE            #ステータスを「PAUSE」にする
                if self.search_window_id(WINDOW_ID_PAUSE_MENU) == -1: #ポーズメニューウィンドウが存在しないのなら・・
                    self.create_window(WINDOW_ID_PAUSE_MENU,0,0)          #ポーズメニューウィンドウウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「BACK TO GAMES」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は3項目なので 4-1=3を代入,メニューの階層は一番低いMENU_LAYER0にします
                    self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,46,73,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,4-1,0,MENU_LAYER0)
                    self.active_window_id = WINDOW_ID_PAUSE_MENU    #このウィンドウIDを最前列でアクティブなものとする
                    self.select_cursor_flag = 1            #セレクトカーソル移動フラグを建てる
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
            elif self.game_status == SCENE_PAUSE:          #ポーズ状態でポーズボタンが押されたときは・・・
                self.game_status = self.record_games_status #一時記憶しておいたゲームステータスを元に戻してあげます
                self.star_scroll_speed = 1                  #星のスクロールスピードを倍率1に戻す
                self.cursor_type = CURSOR_TYPE_NO_DISP      #セレクトカーソルの表示をoffにする
                if self.search_window_id(WINDOW_ID_PAUSE_MENU) != -1: #ポーズメニューウィンドウが存在するのならば・・
                    i = self.search_window_id(WINDOW_ID_PAUSE_MENU)
                    self.window[i].vy = -0.3            #WINDOW_ID_PAUSE_MENUウィンドウを右上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.2
                    self.window[i].vx = 0.1
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.select_cursor_flag = 0         #セレクトカーソル移動フラグを降ろす
                    
                    pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                
            else:
                return

    #ポーズ時の処理
    def update_pause_menu(self):
        if   self.cursor_menu_layer == MENU_LAYER0: #メニューが0階層目の選択分岐
            if   self.cursor_decision_item_y == 0:    #選択したアイテムが「BACK TO GAMES」ならば
                self.game_status = self.record_games_status #一時記憶しておいたゲームステータスを元に戻してあげます
                self.star_scroll_speed = 1                  #星のスクロールスピードを倍率1に戻す
                self.cursor_type = CURSOR_TYPE_NO_DISP      #セレクトカーソルの表示をoffにする
                if self.search_window_id(WINDOW_ID_PAUSE_MENU) != -1: #ポーズメニューウィンドウが存在するのならば・・
                    i = self.search_window_id(WINDOW_ID_PAUSE_MENU)
                    self.window[i].vy = -0.3            #WINDOW_ID_PAUSE_MENUウィンドウを右上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.2
                    self.window[i].vx = 0.1
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.select_cursor_flag = 0         #セレクトカーソル移動フラグを降ろす
                    
                    pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                
            elif self.cursor_decision_item_y == 1:    #選択したアイテムが「RETURN TITLE」ならば
                if self.search_window_id(WINDOW_ID_RETURN_TITLE) == -1: #リターンタイトルウィンドウが存在しないのなら・・
                    self.move_down_pause_menu() #ポーズメニューウィンドウを下にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「RETURN TITLE」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_PAUSE_MENU)         #ポーズメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_RETURN_TITLE,0,10)                  #リターンタイトルウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「NO」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は2項目なので 2-1=1を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,66,69+10,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_RETURN_TITLE    #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif self.cursor_decision_item_y == 3:    #選択したアイテムが「EXIT GAME」ならば
                if self.search_window_id(WINDOW_ID_EXIT) == -1: #ゲーム終了(退出)ウィンドウが存在しないのなら・・
                    self.move_down_pause_menu() #ポーズメニューウィンドウを下にずらす関数の呼び出し
                    self.cursor_pre_decision_item_y = self.cursor_decision_item_y #現時点で選択されたアイテム「EXIT GAME」を前のレイヤー選択アイテムとしてコピーする
                    self.push_cursor_data(WINDOW_ID_PAUSE_MENU)         #ポーズメニューのカーソルデータをPUSH
                    self.create_window(WINDOW_ID_EXIT,0,10)                  #ゲーム終了(退出)ウィンドウの作製
                    #選択カーソル表示をon,カーソルは上下移動のみ,,カーソル移動ステップはx4,y7,いま指示しているアイテムナンバーは0の「NO」
                    #まだボタンも押されておらず未決定状態なのでdecision_item_yはUNSELECTED,y最大項目数は2項目なので 2-1=1を代入,メニューの階層が増えたのでMENU_LAYER0からMENU_LAYER1にします
                    self.set_cursor_data(CURSOR_TYPE_NORMAL,CURSOR_MOVE_UD,66,69+10,STEP4,STEP7,0,0,0,0,UNSELECTED,UNSELECTED,0,2-1,0,MENU_LAYER1)
                    self.active_window_id = WINDOW_ID_EXIT    #このウィンドウIDを最前列でアクティブなものとする
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
            
        elif self.cursor_menu_layer == MENU_LAYER1: #メニューが1階層目の選択分岐
            if     self.cursor_pre_decision_item_y == 1 and self.cursor_decision_item_y == 0:
                self.move_up_pause_menu() #ポーズメニューウィンドウを右にずらす関数の呼び出し
                i = self.search_window_id(WINDOW_ID_RETURN_TITLE)
                self.window[i].vy = -0.3            #WINDOW_ID_RETURN_TITLEウィンドウを右上にフッ飛ばしていく
                self.window[i].vy_accel = 1.2
                self.window[i].vx = 0.1
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.pop_cursor_data(WINDOW_ID_PAUSE_MENU)          #ポーズメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                self.active_window_id = WINDOW_ID_PAUSE_MENU        #1階層前ポーズメニューウィンドウIDを最前列でアクティブなものとする
            elif   self.cursor_pre_decision_item_y == 1 and self.cursor_decision_item_y == 1:
                self.game_status = SCENE_TITLE_INIT         #ステータスを「TITLE INIT」にする
                self.game_playing_flag = 0                  #ゲームプレイ中フラグを降ろす
                self.select_cursor_flag = 0                 #セレクトカーソル移動フラグを降ろす
                self.cursor_type = CURSOR_TYPE_NO_DISP      #セレクトカーソルの表示をoffにする
                
                if self.search_window_id(WINDOW_ID_RETURN_TITLE) != -1: #リターンタイトルウィンドウが存在するのならば・・
                    i = self.search_window_id(WINDOW_ID_RETURN_TITLE)
                    self.window[i].vy = -0.3            #WINDOW_ID_RETURN_TITLEウィンドウを右上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.2
                    self.window[i].vx = 0.1
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                
                if self.search_window_id(WINDOW_ID_PAUSE_MENU) != -1: #ポーズメニューウィンドウが存在するのならば・・
                    i = self.search_window_id(WINDOW_ID_PAUSE_MENU)
                    self.window[i].vy = -0.3            #WINDOW_ID_PAUSE_MENUウィンドウを左上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.2
                    self.window[i].vx = -0.1
                    self.window[i].vx_accel = 1.2
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                
                pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルボタンプッシュ音を鳴らす
                
            elif   self.cursor_pre_decision_item_y == 3 and self.cursor_decision_item_y == 0:
                self.move_up_pause_menu() #ポーズメニューウィンドウを右にずらす関数の呼び出し
                i = self.search_window_id(WINDOW_ID_EXIT)
                self.window[i].vy = -0.3            #WINDOW_ID_EXITウィンドウを右上にフッ飛ばしていく
                self.window[i].vy_accel = 1.2
                self.window[i].vx = 0.1
                self.window[i].vx_accel = 1.2
                self.window[i].window_status = WINDOW_CLOSE
                self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.pop_cursor_data(WINDOW_ID_PAUSE_MENU)          #ポーズメニューのカーソルデータをPOP
                self.cursor_pre_decision_item_y = UNSELECTED
                pyxel.play(0,self.window[self.active_window_index].cursor_cancel_se)#カーソルキャンセル音を鳴らす
                self.active_window_id = WINDOW_ID_PAUSE_MENU        #1階層前ポーズメニューウィンドウIDを最前列でアクティブなものとする
            elif   self.cursor_pre_decision_item_y == 3 and self.cursor_decision_item_y == 1:
                if self.search_window_id(WINDOW_ID_EXIT) != -1: #ゲーム終了ウィンドウが存在するのならば・・
                    i = self.search_window_id(WINDOW_ID_EXIT)
                    self.window[i].vy = -0.1            #WINDOW_ID_EXITウィンドウを右上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.03
                    self.window[i].vx = 0.1
                    self.window[i].vx_accel = 1.04
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                
                if self.search_window_id(WINDOW_ID_PAUSE_MENU) != -1: #ポーズメニューウィンドウが存在するのならば・・
                    i = self.search_window_id(WINDOW_ID_PAUSE_MENU)
                    self.window[i].vy = -0.1            #WINDOW_ID_PAUSE_MENUウィンドウを左上にフッ飛ばしていく
                    self.window[i].vy_accel = 1.05
                    self.window[i].vx = -0.1
                    self.window[i].vx_accel = 1.04
                    self.window[i].window_status = WINDOW_CLOSE
                    self.window[i].comment_flag = COMMENT_FLAG_OFF
                self.bg_cls_color = 0                        #BGをCLS(クリアスクリーン)するときの色の指定(通常は0=黒色です)
                self.game_playing_flag = 1                   #ゲームプレイ中フラグを上げる 
                self.game_quit_from_playing = 1              #ゲームプレイ中からの終了
                self.game_status = SCENE_GAME_QUIT_START     #ステータスを「GAME QUIT START」(ゲームプレイ中からのゲーム終了工程開始)にする

    #プレイ時間の計算処理を行う
    def update_calc_playtime(self):
        self.playtime_frame_counter += 1         #フレームカウンターをインクリメント
        if self.playtime_frame_counter >= 60:     #フレームカウンターが60以上になったら
            self.playtime_frame_counter = 0      #フレームカウンターをリセットして
            self.one_game_playtime_seconds   += 1 #1プレイタイムを1秒増加させる
            self.total_game_playtime_seconds += 1 #総ゲームプレイ時間も1秒増加させる

    #1プレイタイムを見てランクを上昇させる
    def update_rank_up_look_at_playtime(self):
        if (pyxel.frame_count % self.rank_up_frame) == 0:
            if self.rank < self.rank_limit: #ランク数がランク上限限界値より小さいのなら
                self.rank += 1      #ランク数をインクリメント
                self.get_rank_data() #ランク数が変化したのでランク数をもとにしたデータをリストから各変数に代入する関数の呼び出し

    #ハイスコアのチェックを行う関数
    def update_check_hi_score(self):
        if self.score > self.hi_score: #スコアがハイスコアより大きければ
            self.hi_score = self.score #ハイスコアにスコアを代入する

    #ウィンドウの更新
    def update_window(self):
        window_count = len(self.window)
        for i in range(window_count):
            if   self.window[i].window_status == WINDOW_OPEN:     #ステータスが「オープン」の時は・・・・・・・・・・・・
                if self.window[i].width < self.window[i].open_width:#widthをopen_widthの数値になるまで増加させていく
                    self.window[i].width += int(self.window[i].change_x * self.window[i].open_speed)
                
                if self.window[i].height < self.window[i].open_height:#heightをopen_heightの数値になるまで増加させていく
                    self.window[i].height += int(self.window[i].change_y * self.window[i].open_speed)
                
                #ウィンドウが開ききったのか判断する
                if  -2 <= self.window[i].open_width  - self.window[i].width  <= 2 and\
                    -2 <= self.window[i].open_height - self.window[i].height <= 2:#もしwidthとheightの値がopenした時の数値と+-2以内になったのなら
                    self.window[i].window_status = WINDOW_WRITE_MESSAGE#ウィンドウは完全に開ききったとみなしてステータスをWINDOW_WRITE_MESSAGEにしてメッセージを表示開始する
                    
                    self.window[i].width  = self.window[i].open_width #小数点以下の座標の誤差を修正するために強制的にopen時の座標数値を現在座標数値に代入してやる
                    self.window[i].height = self.window[i].open_height
            elif self.window[i].window_status == WINDOW_CLOSE:    #ステータスが「クローズ」の時は・・・・・・・・・・・・
                if self.window[i].width > 0 :#widthを0になるまで減少させていく
                        self.window[i].width -= int(self.window[i].change_x * self.window[i].close_speed)
                    
                if self.window[i].height >0 :#heightを0になるまで減少させていく
                    self.window[i].height -= int(self.window[i].change_y * self.window[i].close_speed)
                    
                #ウィンドウが開ききったのか判断する
                if  -2 <= self.window[i].width  <= 2 and\
                    -2 <= self.window[i].height <= 2:#もしwidthとheightの値が+-2以内になったのなら
                    self.window[i].window_status = WINDOW_CLOSE_COMPLETED#ウィンドウは完全に閉めきったとみなしてステータスをWINDOW_CLOSE_COMPLETEDにする
                    
                    self.window[i].width  = 0 #小数点以下の座標の誤差を修正するために0を現在のウィンドウ縦横幅とする
                    self.window[i].height = 0
            elif self.window[i].window_status == WINDOW_MOVE:     #ステータスが「ムーブ」の時は・・・・・・・・・・・・・
                if      -3 <= self.window[i].dx - self.window[i].posx <= 3\
                    and -3 <= self.window[i].dy - self.window[i].posy <= 3: #移動先の座標(dx,dy)と現在の座標が+-3以内になったのなら
                    self.window[i].window_status = WINDOW_WRITE_MESSAGE#ウィンドウ移動は完了とみなしてステータスをWINDOW_WRITE_MESSAGEにする
                    
                    self.window[i].posx = self.window[i].dx #小数点以下の座標の誤差を修正するために強制的に移動先の座標を現在座標数値に代入してやる
                    self.window[i].posy = self.window[i].dy
                    self.window[i].vx = 0       #移動速度,加速度初期化
                    self.window[i].vy = 0
                    self.window[i].vx_accel = 1
                    self.window[i].vy_accel = 1
            
            self.window[i].vx *= self.window[i].vx_accel #速度に加速度を掛け合わせて変化させていく
            self.window[i].vy *= self.window[i].vy_accel
            self.window[i].posx += self.window[i].vx #ウィンドウ位置の更新
            self.window[i].posy += self.window[i].vy

    #ウィンドウのはみだしチェック（表示座標が完全に画面外になったのなら消去する）
    def update_clip_window(self):
        window_count = len(self.window)#ウィンドウの数を数える
        rect_ax,rect_ay = 0,0
        rect_aw,rect_ah = WINDOW_W,WINDOW_H
        for i in reversed(range(window_count)):
            #ゲームの画面(0,0)-(160,120)とウィンドウ(wx1,wy1)-(wx2,wy2)の2つの矩形の衝突判定を行い
            #衝突して一部が重なっている→ウィンドウのどこかの部分を表示しないといけないのでウィンドウは生存させる
            #衝突していない→お互いに干渉していないので画面にウィンドウが表示されることは無い→ウィンドウを消去する
            rect_bx,rect_by = self.window[i].posx,self.window[i].posy
            rect_bw,rect_bh = self.window[i].open_width,self.window[i].open_height
            
            #矩形A(ゲーム画面)と矩形B(ウィンドウ)の衝突判定を行う関数の呼び出し
            if self.collision_rect_rect(rect_ax,rect_ay,rect_aw,rect_ah,rect_bx,rect_by,rect_bw,rect_bh) == False:
                del self.window[i] #ウィンドウが画面外に存在するとき(2つの矩形が衝突していないとき)はインスタンスを破棄する(ウィンドウ消滅)

    #現在どのウィンドウがもつインデックス値が最前面にあるのか調べあげ,アクティブウィンドウインデックス値に登録し更新する
    def update_active_window(self):
        i = self.search_window_id(self.active_window_id) #アクティブなウィンドウIDを元にインデックス値を求める関数の呼び出し
        self.active_window_index = i           #アクティブになっているウィンドウのインデックスナンバー(i)を代入

    #セレクトカーソルの更新
    def update_select_cursor(self):
        # 上入力されたら  y座標を  -7する(1キャラ分)
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD_1_UP) or pyxel.btnp(pyxel.GAMEPAD_2_UP):
            self.cursor_move_data = PAD_UP
            if     self.cursor_move_direction == CURSOR_MOVE_UD\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER_BUTTON:
                if self.cursor_item_y != 0: #指し示しているアイテムナンバーが一番上の項目の0以外なら上方向にカーソルは移動できるので・・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for ty in range(len(self.window[self.active_window_index].item_text)): #item_textの長さの分ループ処理する
                        if self.window[self.active_window_index].item_text[self.cursor_item_y-1][LIST_WINDOW_TEXT] == "": #カーソル移動先にテキストが存在しない場合は・・
                            self.cursor_y -= self.cursor_step_y#y座標をcursor_step_y減算して上に移動させる
                            self.cursor_item_y -= 1 #現在指し示しているアイテムナンバーを1減らす
                            continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            self.cursor_y -= self.cursor_step_y #y座標をcursor_step_y（初期値は1キャラ7ドット）減算して上に移動させる
                            self.cursor_item_y -= 1 #現在指し示しているアイテムナンバーを1減らす
                            break #カーソルの移動先が見つかったのでループから脱出！
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_y != 0: #指し示しているアイテムナンバーが一番上の項目の0以外なら上方向にカーソルは移動できるので・・・
                    for ty in range(self.cursor_item_y): #現在のカーソルy座標の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y-(ty+1)][self.cursor_item_x] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_y-(ty+1) < 0:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                break #上方向がスキップエリアで尚且つ調べる対象のitem_yが0より小さかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            #カーソル移動先が見つかったぞ！
                            self.cursor_y -= self.cursor_step_y * (ty+1) #y座標をcursor_step_y*(ty+1)減算してカーソルを上に移動させる
                            self.cursor_item_y -= (ty+1) #現在指し示しているアイテムナンバーをty+1減らす
                            pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
            
            elif self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーx軸方向が最大項目数の場合はOKアイコンなので何もしない(それ以外の時は処理をする)
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュを鳴らす
                    
                    if self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] != "": #テキストリストに何かしらの文字列が入っている時のみ処理をする
                        text = self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT]
                        character = ord(text[self.cursor_item_x]) #カーソルの位置の文字を取得しアスキーコードを取得する
                        character += 1 #文字のアスキーコードを1増やす（今カーソルのあるアルファベットのアスキーコードを１増やす AはBに BはCに CはDに DはEになる)
                        left_text  = text[:self.cursor_item_x] #先頭からカーソルまでの文字列を切り出す(カーソルの左方向の文字列の切り出し)
                        right_text = text[self.cursor_item_x+1:] #カーソル位置から文字列の最後まで切り出す(カーソルの右方向の文字列の切り出し)
                        new_text = left_text + chr(character) + right_text #新しい文字列を作り出す(pythonの文字列はimmutable(変更不能)らしいので新しい文字列変数を作ってそれを代入するしかない？？のかな？よくわかんない)
                        self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] = new_text
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
        
        # 下入力されたら  y座標を  +7する(1キャラ分)
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD_1_DOWN) or pyxel.btnp(pyxel.GAMEPAD_2_DOWN):
            self.cursor_move_data = PAD_DOWN
            if     self.cursor_move_direction == CURSOR_MOVE_UD\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER\
                or self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER_BUTTON:
                if self.cursor_item_y != self.cursor_max_item_y: #指し示しているアイテムナンバーが最大項目数でないのなら下方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for ty in range(len(self.window[self.active_window_index].item_text)): #item_textの長さの分ループ処理する
                        if self.window[self.active_window_index].item_text[self.cursor_item_y+1][LIST_WINDOW_TEXT] == "": #カーソル移動先にテキストが存在しない場合は・・
                            self.cursor_y += self.cursor_step_y#y座標をcursor_step_y加算して下に移動させる
                            self.cursor_item_y += 1 #現在指し示しているアイテムナンバーを1増やす
                            continue #選択すべき項目テキストは見つかっていないのでまだループは継続する
                        else:
                            self.cursor_y += self.cursor_step_y #y座標をcursor_step_y（初期値は1キャラ7ドット）加算して下に移動させる
                            self.cursor_item_y += 1 #現在指し示しているアイテムナンバーを1増やす
                            break #選択すべき項目テキストが見つかったのでループから脱出！
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_y != self.cursor_max_item_y: #指し示しているアイテムナンバーが最大項目数でないのなら下方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for ty in range(self.cursor_max_item_y - self.cursor_item_y): #(y軸アイテム最大値-現在のカーソルy座標)の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y+(ty+1)][self.cursor_item_x] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_y+(ty+1) > self.cursor_max_item_y:
                                break #下方向がスキップエリアで尚且つ調べる対象がmax_item_yより大きかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            self.cursor_y += self.cursor_step_y * (ty+1) #y座標をcursor_step_y*(ty+1)加算してカーソルを下に移動させる
                            self.cursor_item_y += (ty+1) #現在指し示しているアイテムナンバーをty+1増やす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
                
            elif self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーx軸方向が最大項目数の場合はOKアイコンなので何もしない(それ以外の時は処理をする)
                    pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュ音を鳴らす
                    
                    if self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] != "": #テキストリストに何かしらの文字列が入っている時のみ処理をする
                        text = self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT]
                        character = ord(text[self.cursor_item_x]) #カーソルの位置の文字を取得しアスキーコードを取得する
                        character -= 1 #文字のアスキーコードを1減らす（今カーソルのあるアルファベットのアスキーコードを１増やす AはBに BはCに CはDに DはEになる)
                        left_text  = text[:self.cursor_item_x] #先頭からカーソルまでの文字列を切り出す(カーソルの左方向の文字列の切り出し)
                        right_text = text[self.cursor_item_x+1:] #カーソル位置から文字列の最後まで切り出す(カーソルの右方向の文字列の切り出し)
                        new_text = left_text + chr(character) + right_text #新しい文字列を作り出す(pythonの文字列はimmutable(いみゅーたぶる変更不能)らしいので新しい文字列変数を作ってそれを代入するしかない？？のかな？よくわかんない)
                        self.window[self.active_window_index].edit_text[LIST_WINDOW_TEXT] = new_text
                    
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
        
        #右入力されたらcursor_pageを +1する
        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD_1_RIGHT) or pyxel.btnp(pyxel.GAMEPAD_2_RIGHT) or pyxel.btnp(pyxel.GAMEPAD_1_RIGHT_SHOULDER) or pyxel.btnp(pyxel.GAMEPAD_2_RIGHT_SHOULDER):
            self.cursor_move_data = PAD_RIGHT
            if   self.cursor_move_direction == CURSOR_MOVE_SHOW_PAGE:
                self.cursor_page += 1 #ページ数インクリメント
                pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                if self.cursor_page > self.cursor_page_max: #カーソルページ数が最大ページ数を超えたのなら
                    self.cursor_page = 0                    #ページ数は0にする
                
            elif self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーx軸方向が最大項目数でないのなら右方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    self.cursor_x += self.cursor_step_x #x座標をcursor_step_x（初期値は1文字分4ドット）加算してカーソルを右に移動させる
                    self.cursor_item_x += 1 #現在指示しているアイテムナンバーを1増やす
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_x != self.cursor_max_item_x: #指し示しているアイテムナンバーが最大項目数でないのなら右方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    
                    for tx in range(self.cursor_max_item_x - self.cursor_item_x): #(x軸アイテム最大値-現在のカーソルx座標)の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x+(tx+1)] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_x+(tx+1) > self.cursor_max_item_x:
                                break #右方向がスキップエリアで尚且つ調べる対象がmax_item_xより大きかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            self.cursor_x += self.cursor_step_x * (tx+1) #x座標をcursor_step_x*(tx+1)加算してカーソルを右に移動させる
                            self.cursor_item_x += (tx+1) #現在指し示しているアイテムナンバーをtx+1増やす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
                
            elif self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER:
                flag_index = self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                k = self.window[self.active_window_index].flag_list[flag_index] #Kに現在表示されている数値が代入されます(on/offの表示の場合はon=1 off=0が代入されます)
                if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_TYPE] == OPE_OBJ_TYPE_NUM:#操作テキストオブジェクトが数値を左右キーで増減させるタイプの場合は
                    if k < self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MAX_NUM]: #kがLIST_WINDOW_TEXT_OPE_OBJ_MAX_NUMより小さい時は
                        k += 1 #オブジェクトの数値をインクリメント
                        pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュ音を鳴らす
                    else:
                        pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                    
                    if  k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MAX_NUM]:  #kが最大値の場合は
                        rd = DISP_OFF #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグoff
                        ld = DISP_ON  #左矢印表示フラグon
                    elif k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MIN_NUM]: #kが最小値の場合は
                        rd = DISP_ON   #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグon
                        ld = DISP_OFF  #左矢印表示フラグoff
                    else: #それ以外の場合(中間値の場合)は
                        #どちらの方向にも動けるので
                        rd = DISP_ON   #右矢印表示フラグon
                        ld = DISP_ON   #左矢印表示フラグoff
                    
                    self.window[self.active_window_index].flag_list[flag_index] = k #フラグ＆数値リストを更新
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_FLAG] = rd #右矢印表示フラグ更新
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_FLAG]  = ld #左矢印表示フラグ更新
                    
                    #編集された数値がBGMボリュームとSEボリュームの場合はすぐにマスターフラグリストを更新して音量の変化を反映させてやります
                    if     self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_BGM_VOL\
                        or self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_SE_VOL:
                        self.restore_master_flag_list()
                        pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
        
        #左入力されたらcursor_pageを -1する
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD_1_LEFT) or pyxel.btnp(pyxel.GAMEPAD_2_LEFT) or pyxel.btnp(pyxel.GAMEPAD_2_LEFT) or pyxel.btnp(pyxel.GAMEPAD_1_LEFT_SHOULDER) or pyxel.btnp(pyxel.GAMEPAD_2_LEFT_SHOULDER):
            self.cursor_move_data = PAD_LEFT
            if   self.cursor_move_direction == CURSOR_MOVE_SHOW_PAGE:
                self.cursor_page -= 1 #ページ数デクリメント
                pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                if self.cursor_page < 0:                    #カーソルページ数が0より小さくなったのなら
                    self.cursor_page = self.cursor_page_max                    #ページ数はmaxにする
                
            elif   self.cursor_move_direction == CURSOR_MOVE_LR_SLIDER:
                if self.cursor_item_x != 0: #指し示しているアイテムナンバーx軸方向が0以外ならでないのなら左方向にカーソルは移動できるので・・
                    pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                    self.cursor_x -= self.cursor_step_x #x座標をcursor_step_x（初期値は1文字分4ドット）減算してカーソルを左に移動させる
                    self.cursor_item_x -= 1#現在指示しているアイテムナンバーを1減らす
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
            elif self.cursor_move_direction == CURSOR_MOVE_4WAY:
                if self.cursor_item_x != 0: #指し示しているアイテムナンバーが一番左の項目の0以外なら左方向にカーソルは移動できるので・・・
                    for tx in range(self.cursor_item_x): #現在のカーソルx座標の数だけループ処理する
                        if self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x-(tx+1)] == SKIP_CURSOR_AREA: #カーソルの移動先がスキップエリアだったのなら・・・
                            if self.cursor_item_x-(tx+1) < 0:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                break #左方向がスキップエリアで尚且つ調べる対象のitem_xが0より小さかったらカーソルは全く動かすことはできないので座標はそのままにループから脱出する
                            else:
                                pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                                continue #カーソルの移動先はまだ見つかっていないのでまだループは継続する
                        else:
                            #カーソル移動先が見つかったぞ！
                            self.cursor_x -= self.cursor_step_x * (tx+1) #x座標をcursor_step_x*(tx+1)減算してカーソルを左に移動させる
                            self.cursor_item_x -= (tx+1) #現在指し示しているアイテムナンバーをtx+1減らす
                            pyxel.play(0,self.window[self.active_window_index].cursor_move_se)#カーソル移動音を鳴らす
                            break #カーソルの移動先が見つかったのでループから脱出
                else:
                    pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                
                #comment_disp_flagを調べてカーソルサイズを変更する
                if   self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_1:
                    self.cursor_size = CURSOR_SIZE_RIGHT2_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_2:
                    self.cursor_size = CURSOR_SIZE_LEFT1_RIGHT1_EXPAND
                elif self.window[self.active_window_index].comment_disp_flag[self.cursor_item_y][self.cursor_item_x] == SIZE3_BUTTON_3:
                    self.cursor_size = CURSOR_SIZE_LEFT2_EXPAND
                else:
                    self.cursor_size = CURSOR_SIZE_NORMAL
                
            elif self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER:
                flag_index = self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                k = self.window[self.active_window_index].flag_list[flag_index] #Kに現在表示されている数値が代入されます(on/offの表示の場合はon=1 off=0が代入されます)
                
                if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_TYPE]  == OPE_OBJ_TYPE_NUM: #操作テキストオブジェクトが数値を左右キーで増減させるタイプの場合は
                    if k > self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MIN_NUM]: #kがLIST_WINDOW_TEXT_OPE_OBJ_MIN_NUMより大きい時は
                        k -= 1 #オブジェクトの数値をデクリメント
                        pyxel.play(0,self.window[self.active_window_index].cursor_push_se)#カーソルプッシュ音を鳴らす
                    else:
                        pyxel.play(0,self.window[self.active_window_index].cursor_bounce_se)#カーソル跳ね返り音を鳴らす
                    
                    if  k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MAX_NUM]:  #kが最大値の場合は
                        rd = DISP_OFF #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグoff
                        ld = DISP_ON  #左矢印表示フラグon
                    elif k == self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_MIN_NUM]: #kが最小値の場合は
                        rd = DISP_ON   #右矢印(数値を増加できるかどうかを指し示す矢印）表示フラグon
                        ld = DISP_OFF  #左矢印表示フラグoff
                    else: #それ以外の場合(中間値の場合)は
                        #どちらの方向にも動けるので
                        rd = DISP_ON   #右矢印表示フラグon
                        ld = DISP_ON   #左矢印表示フラグoff
                    
                    self.window[self.active_window_index].flag_list[flag_index] = k #フラグ＆数値リストを更新する
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_RIGHT_MARKER_FLAG] = rd #右矢印表示フラグ更新
                    self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_LEFT_MARKER_FLAG]  = ld #左矢印表示フラグ更新
                    
                    #編集された数値がBGMボリュームとSEボリュームの場合はすぐにマスターフラグリストを更新して音量の変化を反映させてやります
                    if     self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_BGM_VOL\
                        or self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] == LIST_WINDOW_FLAG_SE_VOL:
                        self.restore_master_flag_list()
                        pygame.mixer.music.set_volume(self.master_bgm_vol / 100)
        
        #ABXYスペースキーが押された場合の処理
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD_1_A) or pyxel.btnp(pyxel.GAMEPAD_2_A) or pyxel.btnp(pyxel.GAMEPAD_1_B) or pyxel.btnp(pyxel.GAMEPAD_2_B) or pyxel.btnp(pyxel.GAMEPAD_1_X) or pyxel.btnp(pyxel.GAMEPAD_2_X) or pyxel.btnp(pyxel.GAMEPAD_1_Y) or pyxel.btnp(pyxel.GAMEPAD_2_Y):
            self.cursor_move_data = PAD_A
            self.cursor_decision_item_x = self.cursor_item_x #ボタンが押されて決定されたら、いま指示しているアイテムナンバーをcursor_decision_item_xに代入！
            self.cursor_decision_item_y = self.cursor_item_y #ボタンが押されて決定されたら、いま指示しているアイテムナンバーをcursor_decision_item_yに代入！
            if self.cursor_move_direction == CURSOR_MOVE_UD_SLIDER:
                flag_index = self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ] #flag_indexに編集対象となるオブジェクトが入ったリストインデックス値が入ります
                k = self.window[self.active_window_index].flag_list[flag_index] #Kに現在表示されている数値が代入されます(on/offの表示の場合はon=1 off=0が代入されます)
                if self.window[self.active_window_index].item_text[self.cursor_item_y][LIST_WINDOW_TEXT_OPE_OBJ_TYPE] == OPE_OBJ_TYPE_ON_OFF:#操作テキストオブジェクトは「ON」「OFF」の二つから選ぶシンプルなタイプの時は
                    if k == 0: #k=0(off)の時はk=1(on)に、k=1(on)の時はk=0(off)にする
                        k = 1
                    else:
                        k = 0
                    
                    self.window[self.active_window_index].flag_list[flag_index] = k #フラグ＆数値リストを更新する
                    pyxel.play(0,self.window[self.active_window_index].cursor_ok_se)#カーソルok音を鳴らす

    #リプレイデータの記録   自動移動モードの時とステージクリアのブーストの時とリプレイ再生中の時はリプレイデータを記録しません
    def update_record_replay_data(self):
        if     self.move_mode     == MOVE_AUTO\
            or self.game_status   == SCENE_STAGE_CLEAR_MOVE_MY_SHIP\
            or self.game_status   == SCENE_STAGE_CLEAR_MY_SHIP_BOOST\
            or self.game_status   == SCENE_STAGE_CLEAR_FADE_OUT\
            or self.replay_status == REPLAY_PLAY:
            self.pad_data_h = 0b00000000             #次のフレーム時の記録のためにデータを初期化してあげます
            self.pad_data_l = 0b00000000
            return
        else:
            self.replay_recording_data[self.replay_stage_num].append(self.pad_data_h)   #リプレイデータリストにパッド入力データを記録追加します
            self.replay_recording_data[self.replay_stage_num].append(self.pad_data_l)
            self.pad_data_h = 0b00000000             #次のフレーム時の記録のためにデータを初期化してあげます
            self.pad_data_l = 0b00000000

    #リプレイデータ再生用のインデックス値を1増やしていく関数(リプレイフレームインデックス値の更新)
    def update_replay_frame_index(self):
        if self.replay_frame_index < len(self.replay_data[self.replay_stage_num]) - 2:
            self.replay_frame_index += 2  #インデックス値がリストの大きさを超えていなかったら2(PADデータは2バイト長(16ビット長)なので次のデータに移行するには2増やす)増やして次のデータを取り込めるようにしてやります

    #リプレイデータ(ステータス関連)をバックアップする(プッシュする感じみたいな？？？)
    def update_replay_data_status(self):
        self.backup_rnd_seed         = self.master_rnd_seed  #乱数の種(ゲームスタート時)をバックアップ
        self.backup_game_difficulty  = self.game_difficulty  #難易度をバックアップ
        self.backup_stage_number     = self.stage_number     #ステージ数をバックアップ
        self.backup_stage_loop       = self.stage_loop       #ループ数をバックアップ

    #リプレイデータ(リスト本体)をバックアップする(プッシュする感じみたいな？？？)
    def update_replay_data_list(self):
        self.replay_data      = self.replay_recording_data    #録画されたリプレイデータをデータリストを登録

    #リプレイデータをリストアする(ポップする感じみたいな？？？)
    def update_restore_replay_data(self):
        self.master_rnd_seed   = self.backup_rnd_seed         #乱数の種(ゲームスタート時)をリストア
        self.game_difficulty   = self.backup_game_difficulty  #難易度をリストア
        self.stage_number      = self.backup_stage_number     #ステージ数をリストア
        self.stage_loop        = self.backup_stage_loop       #ループ数をリストア

    #リプレイデータ記録中に使用するステージスタート時のパラメータのセーブ
    def update_save_replay_stage_data(self):
        self.replay_mode_stage_data[self.replay_stage_num][ST_SCORE]                       = self.score          #リプレイファイルに記録されたスコアをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_MY_SHIELD]                   = self.my_shield      #リプレイファイルに記録されたシールド値をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_MY_SPEED]                    = self.my_speed       #リプレイファイルに記録された自機移動スピードをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SELECT_SHOT_ID]              = self.select_shot_id #リプレイファイルに記録されたショットIDをセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_EXP]                    = self.shot_exp       #リプレイファイルに記録された自機ショットの経験値をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_LEVEL]                  = self.shot_level     #リプレイファイルに記録された自機ショットのレベルをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_SPEED_MAGNIFICATION]    = self.shot_speed_magnification #リプレイファイルに記録された自機ショットのスピードに掛ける倍率をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_RAPID_OF_FIRE]          = self.shot_rapid_of_fire       #リプレイファイルに記録された自機ショットの連射数をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_EXP]                 = self.missile_exp              #リプレイファイルに記録された自機ミサイルの経験値をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_LEVEL]               = self.missile_level            #リプレイファイルに記録された自機ミサイルのレベルをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_SPEED_MAGNIFICATION] = self.missile_speed_magnification #リプレイファイルに記録された自機ミサイルのスピードに掛ける倍率をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_RAPID_OF_FIRE]       = self.missile_rapid_of_fire   #リプレイファイルに記録された自機ミサイルの連射数をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_SELECT_SUB_WEAPON_ID]        = self.select_sub_weapon_id    #リプレイファイルに記録された現在使用しているサブウェポンのIDナンバーをセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_TYPE]                   = self.claw_type               #リプレイファイルに記録されたクローのタイプをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_NUMBER]                 = self.claw_number             #リプレイファイルに記録されたクローの装備数をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_DIFFERENCE]             = self.claw_difference         #リプレイファイルに記録されたクロ―同士の角度間隔をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_TRACE_CLAW_INDEX]            = self.trace_claw_index        #リプレイファイルに記録されたトレースクロー（オプション）時のトレース用配列のインデックス値をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_TRACE_CLAW_DISTANCE]         = self.trace_claw_distance     #リプレイファイルに記録されたトレースクロー同士の間隔をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_FIX_CLAW_MAGNIFICATION]      = self.fix_claw_magnification  #リプレイファイルに記録されたフイックスクロー同士の間隔の倍率をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_REVERSE_CLAW_SVX]            = self.reverse_claw_svx        #リプレイファイルに記録されたリバースクロー用の攻撃方向ベクトル(x軸)をセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_REVERSE_CLAW_SVY]            = self.reverse_claw_svy        #リプレイファイルに記録されたリバースクロー用の攻撃方向ベクトル(y軸)をセーブ
        
        self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_SHOT_SPEED]             = self.claw_shot_speed         #リプレイファイルに記録されたクローショットのスピードをセーブ
        self.replay_mode_stage_data[self.replay_stage_num][ST_LS_SHIELD_HP]                = self.ls_shield_hp            #リプレイファイルに記録されたL'sシールドの耐久力をセーブ

    #リプレイデータ記録中に使用するステージスタート時のパラメータのロード
    def update_load_replay_stage_data(self):
        self.score     = self.replay_mode_stage_data[self.replay_stage_num][ST_SCORE]                #リプレイファイルに記録されたスコアをロード
        self.my_shield = self.replay_mode_stage_data[self.replay_stage_num][ST_MY_SHIELD]            #リプレイファイルに記録されたシールド値をロード
        self.my_speed  = self.replay_mode_stage_data[self.replay_stage_num][ST_MY_SPEED]             #リプレイファイルに記録された自機移動スピードをロード
        
        self.select_shot_id  = self.replay_mode_stage_data[self.replay_stage_num][ST_SELECT_SHOT_ID] #リプレイファイルに記録されたショットIDをロード
        
        self.shot_exp                 = self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_EXP]                 #リプレイファイルに記録された自機ショットの経験値をロード
        self.shot_level               = self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_LEVEL]               #リプレイファイルに記録された自機ショットのレベルをロード
        self.shot_speed_magnification = self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_SPEED_MAGNIFICATION] #リプレイファイルに記録された自機ショットのスピードに掛ける倍率をロード
        self.shot_rapid_of_fire       = self.replay_mode_stage_data[self.replay_stage_num][ST_SHOT_RAPID_OF_FIRE]       #リプレイファイルに記録された自機ショットの連射数をロード
        
        self.missile_exp                 = self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_EXP]                 #リプレイファイルに記録された自機ミサイルの経験値をロード
        self.missile_level               = self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_LEVEL]               #リプレイファイルに記録された自機ミサイルのレベルをロード
        self.missile_speed_magnification = self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_SPEED_MAGNIFICATION] #リプレイファイルに記録された自機ミサイルのスピードに掛ける倍率をロード
        self.missile_rapid_of_fire       = self.replay_mode_stage_data[self.replay_stage_num][ST_MISSILE_RAPID_OF_FIRE]       #リプレイファイルに記録された自機ミサイルの連射数をロード
        
        self.select_sub_weapon_id        = self.replay_mode_stage_data[self.replay_stage_num][ST_SELECT_SUB_WEAPON_ID] #リプレイファイルに記録された現在使用しているサブウェポンのIDナンバーをロード
        
        self.claw_type                   = self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_TYPE]       #リプレイファイルに記録されたクローのタイプをロード
        self.claw_number                 = self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_NUMBER]     #リプレイファイルに記録されたクローの装備数をロード
        self.claw_difference             = self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_DIFFERENCE] #リプレイファイルに記録されたクロ―同士の角度間隔をロード
        
        self.trace_claw_index            = self.replay_mode_stage_data[self.replay_stage_num][ST_TRACE_CLAW_INDEX]     #リプレイファイルに記録されたトレースクロー（オプション）時のトレース用配列のインデックス値をロード
        self.trace_claw_distance         = self.replay_mode_stage_data[self.replay_stage_num][ST_TRACE_CLAW_DISTANCE]  #リプレイファイルに記録されたトレースクロー同士の間隔をロード
        
        self.fix_claw_magnification      = self.replay_mode_stage_data[self.replay_stage_num][ST_FIX_CLAW_MAGNIFICATION] #リプレイファイルに記録されたフイックスクロー同士の間隔の倍率をロード
        
        self.reverse_claw_svx            = self.replay_mode_stage_data[self.replay_stage_num][ST_REVERSE_CLAW_SVX]  #リプレイファイルに記録されたリバースクロー用の攻撃方向ベクトル(x軸)をロード
        self.reverse_claw_svy            = self.replay_mode_stage_data[self.replay_stage_num][ST_REVERSE_CLAW_SVY]  #リプレイファイルに記録されたリバースクロー用の攻撃方向ベクトル(y軸)をロード
        
        self.claw_shot_speed             = self.replay_mode_stage_data[self.replay_stage_num][ST_CLAW_SHOT_SPEED]  #リプレイファイルに記録されたクローショットのスピードをロード
        self.ls_shield_hp                = self.replay_mode_stage_data[self.replay_stage_num][ST_LS_SHIELD_HP]     #リプレイファイルに記録されたL'sシールドの耐久力をロード

    #乱数0_9関数(0~9)の更新
    def update_rnd0_9(self):
        self.rnd0_9_num  = pyxel.frame_count %  10 #フレームカウント数を 10で割った余りが変数rnd0_9_numに入ります(0~9の数値が1フレームごとに変化する)

    #乱数099関数(0~999)の更新
    def update_rnd0_99(self):
        self.rnd0_99_num = pyxel.frame_count % 100 #フレームカウント数を100で割った余りが変数rnd0_99_numに入ります(0~99の数値が1フレームごとに変化する)

    #リプレイデータ・ファイルロード
    def update_replay_data_file_load(self):
        self.replay_data          = [[] for i in range(50)] #リプレイデータが入るリスト(50ステージ分)を初期化
        self.replay_control_data_size = []                  #ステージ毎のコントロールデータのサイズが入るリストを初期化
        slot_num = "slot_" + str(self.replay_slot_num)      #これからアクセスするスロットナンバーを取得
        pyxel.load("assets/replay/" + slot_num + "/replay_status.pyxres") #リプレイステータスファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
        
        #各種設定値読み込み 数字の[0]はアスキーコード16番なので16引いて文字から数字としての0にしてやります
        self.master_rnd_seed  = pyxel.tilemap(0).get(0,0)       #乱数の種(ゲームスタート時)を読み込み(そのまま取得します)
        self.game_difficulty  = pyxel.tilemap(0).get(0,1) - 16  #難易度読み込み
        self.stage_number     = pyxel.tilemap(0).get(0,2) - 16  #ステージ数読み込み
        self.stage_loop       = pyxel.tilemap(0).get(0,3) - 16  #ループ数読み込み
        self.replay_stage_num = pyxel.tilemap(0).get(0,4) - 16  #リプレイファイルとして記録する総ステージ数を読み込み
        self.boss_test_mode   = pyxel.tilemap(0).get(0,5) - 16  ##ボステストモードのフラグを読み込み
        
        #ステージ毎ごとの自機関連パラメーターのロード---------------------------------------------------------------------------
        for i in range(self.replay_stage_num + 1):
            self.replay_mode_stage_data[i][ST_SCORE]           = self.read_system_data_num(5   -1+10,10+i, 10)        #座標(5,10+i)から10ケタのスコア(整数)を読み込みます
            self.replay_mode_stage_data[i][ST_MY_SHIELD]       = self.read_system_data_num(16  -1 +5,10+i,  5)        #座標(16,10+i)から5ケタのシールド値を読み込みます
            self.replay_mode_stage_data[i][ST_MY_SPEED]        = self.read_system_data_num(22  -1 +3,10+i,  3) // 100 #座標(22,10+i)から3ケタの自機スピード(0.75とか1.25とか小数点第2位まで行くので100でわった値を読み込みます)
            
            self.replay_mode_stage_data[i][ST_SELECT_SHOT_ID]  = self.read_system_data_num(27  -1 +2,10+i,  2)    #座標(27,10+i)から2ケタのショットIDを読み込みます
            
            self.replay_mode_stage_data[i][ST_SHOT_EXP]                 = self.read_system_data_num(31  -1 +4,10+i,  4)         #座標(31,10+i)から4ケタのショットの経験値を読み込みます
            self.replay_mode_stage_data[i][ST_SHOT_LEVEL]               = self.read_system_data_num(36  -1 +2,10+i,  2)         #座標(36,10+i)から2ケタのショットのレベルを読み込みます
            self.replay_mode_stage_data[i][ST_SHOT_SPEED_MAGNIFICATION] = self.read_system_data_num(39  -1 +5,10+i,  5) // 1000 #座標(39,10+i)から5ケタのショットのスピードに掛ける倍率を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            self.replay_mode_stage_data[i][ST_SHOT_RAPID_OF_FIRE]       = self.read_system_data_num(45  -1 +2,10+i,  2)         #座標(45,10+i)から2ケタのショットの連射数を読み込みます
            
            self.replay_mode_stage_data[i][ST_MISSILE_EXP]                 = self.read_system_data_num(49  -1 +4,10+i,  4)         #座標(49,10+i)から4ケタのミサイルの経験値を読み込みます
            self.replay_mode_stage_data[i][ST_MISSILE_LEVEL]               = self.read_system_data_num(54  -1 +2,10+i,  2)         #座標(54,10+i)から2ケタのミサイルのレベルを読み込みます
            self.replay_mode_stage_data[i][ST_MISSILE_SPEED_MAGNIFICATION] = self.read_system_data_num(57  -1 +5,10+i,  5) // 1000 #座標(57,10+i)から5ケタのミサイルのスピードに掛ける倍率を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            self.replay_mode_stage_data[i][ST_MISSILE_RAPID_OF_FIRE]       = self.read_system_data_num(63  -1 +2,10+i,  2)         #座標(63,10+i)から2ケタのミサイルの連射数を読み込みます
            
            self.replay_mode_stage_data[i][ST_SELECT_SUB_WEAPON_ID] = self.read_system_data_num(68  -1 +2,10+i,  2)   #座標(68,10+i)から2ケタの現在使用しているサブウェポンのIDナンバーを読み込みます
            
            self.replay_mode_stage_data[i][ST_CLAW_NUMBER]          = self.read_system_data_num(74  -1 +2,10+i,  2)   #座標(74,10+i)から2ケタのクローの装備数を読み込みます
            self.replay_mode_stage_data[i][ST_CLAW_TYPE]            = self.read_system_data_num(71  -1 +2,10+i,  2)   #座標(71,10+i)から2ケタのクローのタイプを読み込みます
            self.replay_mode_stage_data[i][ST_CLAW_DIFFERENCE]      = self.read_system_data_num(77  -1 +4,10+i,  4)   #座標(77,10+i)から4ケタのクロ―同士の角度間隔を読み込みます
            
            self.replay_mode_stage_data[i][ST_TRACE_CLAW_INDEX]        = self.read_system_data_num(82  -1 +2,10+i,  2)          #座標(82,10+i)から2ケタのトレースクロー（オプション）時のトレース用配列のインデックス値を読み込みます
            self.replay_mode_stage_data[i][ST_TRACE_CLAW_DISTANCE]     = self.read_system_data_num(85  -1 +5,10+i,  5) // 1000  #座標(85,10+i)から5ケタのトレースクロー同士の間隔を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            
            self.replay_mode_stage_data[i][ST_FIX_CLAW_MAGNIFICATION]  =  self.read_system_data_num(91  -1 +5,10+i,  5) // 1000 #座標(91,10+i)から5ケタのフイックスクロー同士の間隔の倍率を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            
            self.replay_mode_stage_data[i][ST_REVERSE_CLAW_SVX]        = self.read_system_data_num(97  -1 +5,10+i,  5) // 1000  #座標(97,10+i)から5ケタのリバースクロー用の攻撃方向ベクトル(x軸)を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            self.replay_mode_stage_data[i][ST_REVERSE_CLAW_SVY]        = self.read_system_data_num(103 -1 +5,10+i,  5) // 1000  #座標(103,10+i)から5ケタのリバースクロー用の攻撃方向ベクトル(y軸)を読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            
            self.replay_mode_stage_data[i][ST_CLAW_SHOT_SPEED]         = self.read_system_data_num(109 -1 +5,10+i,  5) // 1000  #座標(109,10+i)から5ケタのクローショットのスピードを読み込みます(小数点第3位まで行くので1000で割った値を読み込みます)
            self.replay_mode_stage_data[i][ST_LS_SHIELD_HP]            = self.read_system_data_num(115 -1 +4,10+i,  4)          #座標(115,10+i)から4ケタのL'sシールドの耐久力を読み込みます
            pad_data_size = self.read_system_data_num(128 -1 +8,10+i,  8) #座標(128,10+i)からの8ケタのコントロールパッド入力データが記録されたファイルのデータサイズを読み込みます
            self.replay_control_data_size.append(pad_data_size)           #コントロールデータのファイルサイズリストにサイズを追加していきます
        
        #各ステージのパッド入力データのロード---------------------------------------------------------------------------------------
        for st in range(self.replay_stage_num + 1): #st(ステージ指定用に作った変数は0始まりなので注意)
            file_number = "{:>03}".format(st + 1)
            file_name = "assets/replay/" + slot_num + "/" + file_number + ".pyxres"
            pyxel.load(file_name) #リプレイパッド入力データファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
            replay_control_data_count = self.replay_control_data_size[st] #stステージ目のreplay_dataのリスト長(要素数)を代入
            
            for i in range (replay_control_data_count):
                x = int(i % 256)                      #x座標は現在のカウント値iを256で割った余り
                y = int(i // 256) % 256               #y座標は現在のカウント値iを256で割った数(切り捨て)を更に256で割った余り
                z = int(i // 65536)                   #z座標(この場合はタイルマップナンバーになります)は65536で割った数(切り捨て)
                num = pyxel.tilemap(z).get(x,y)       #numにタイルマップ(z),座標(x,y)から読み取ったコントロールパッド入力データを代入
                self.replay_data[st].append(int(num))    #リストにパッド入力データ記録！getで読み取ったのは文字(str)なので数値(int)に変換してリストにアペンドします

    #リプレイデータ・ファイルセーブ
    def update_replay_data_file_save(self):
        self.replay_control_data_size = [] #まず最初にステージ毎のコントロールデータのサイズが入るリストを初期化
        slot_num = "slot_" + str(self.replay_slot_num) #これからアクセスするスロットナンバーを取得
        
        #各ステージのパッド入力データのセーブ---------------------------------------------------------------------------------------
        for st in range(self.replay_stage_num + 1): #st(ステージ指定用に作った変数は0始まりなので注意)
            file_number = "{:>03}".format(st + 1)
            file_name = "assets/replay/" + slot_num + "/" + file_number + ".pyxres"
            pyxel.load(file_name) #リプレイパッド入力データファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
            replay_control_data_count = len(self.replay_data[st])        #stステージ目のreplay_dataのリスト長(要素数)を代入
            self.replay_control_data_size.append(replay_control_data_count) #ステージ毎のコントロールデータのサイズをリストに追加していきます
            for z in range(8): #データクリア処理-------------------------------------
                for y in range(256):
                    for x in range(256):
                        # pyxel.tilemap(z).set(x,y,128-16+6-16)
                        pyxel.tilemap(z).set(x,y,0)
            
            #カウント65536でタイルマップを1枚埋め尽くす事になります
            #カウント65537だとタイルマップ1枚と次のタイルマップ1マス分必要となります
            #タイルマップ1ページ分はカウントが0~65536間の場合書き込み開始 65537だとエラーになります(なんか書き込む(SET)時は座標が256越えてもエラーが出ないみたい)
            #う～ん上手く行ってるのか謎・・・・
            for i in range (replay_control_data_count):
                num = int(self.replay_data[st][i])    #リストからパッド入力データ取得
                x = int(i % 256)                   #x座標は現在のカウント値iを256で割った余り
                y = int(i // 256) % 256            #y座標は現在のカウント値iを256で割った数(切り捨て)を更に256で割った余り
                z = int(i // 65536)                #z座標(この場合はタイルマップナンバーになります)は65536で割った数(切り捨て)
                pyxel.tilemap(z).set(x,y,num) #numをタイルマップ(z),座標(x,y)に書き込む
            
            pyxel.save(file_name) #リプレイパッド入力データファイルをセーブ！
        
        #リプレイファイル本体のデータをセーブする---------------------------------------------------------------------------------------
        pyxel.load("assets/replay/" + slot_num + "/replay_status.pyxres") #リプレイステータスファイルにアクセスするためにローディングだけしてやります(グラフイック関連のアセットをローディングしている時がほとんどなので)
        #各種設定値書き込み 数字の[0]はアスキーコード16番なので16足してアスキーコードとしての0にしてやります
        pyxel.tilemap(0).set(0,0,self.master_rnd_seed)          #乱数の種(ゲームスタート時)を書き込み(数文字には変換しない)
        pyxel.tilemap(0).set(0,1,self.game_difficulty + 16)     #難易度書き込み
        pyxel.tilemap(0).set(0,2,self.start_stage_number + 16)  #ゲーム開始時のステージ数書き込み
        pyxel.tilemap(0).set(0,3,self.start_stage_loop + 16)    #ゲーム開始時のループ数書き込み
        pyxel.tilemap(0).set(0,4,self.replay_stage_num + 16)    #リプレイファイルとして記録する総ステージ数を書き込み
        pyxel.tilemap(0).set(0,5,self.boss_test_mode   + 16)    #ボステストモードのフラグを書き込み
        
        #ステージ毎ごとの自機関連パラメーターのセーブ--------------------------------------------------------------------------------
        for i in range(self.replay_stage_num + 1):
            self.write_system_data_num(5   -1+10,10+i, 10,int(self.replay_mode_stage_data[i][ST_SCORE]))           #座標(5,10+i)に10ケタのスコア(整数)を書き込みます
            self.write_system_data_num(16  -1 +5,10+i,  5,int(self.replay_mode_stage_data[i][ST_MY_SHIELD]))       #座標(16,10+i)に5ケタのシールド値を書き込みます
            self.write_system_data_num(22  -1 +3,10+i,  3,int(self.replay_mode_stage_data[i][ST_MY_SPEED]*100))    #座標(22,10+i)に3ケタの自機スピード(0.75とか1.25とか小数点第2位まで行くので100倍した値を書き込みます)
            
            self.write_system_data_num(27  -1 +2,10+i,  2,int(self.replay_mode_stage_data[i][ST_SELECT_SHOT_ID]))  #座標(27,10+i)に2ケタのショットIDを書き込みます
            
            self.write_system_data_num(31  -1 +4,10+i,  4,int(self.replay_mode_stage_data[i][ST_SHOT_EXP]))              #座標(31,10+i)に4ケタのショットの経験値を書き込みます
            self.write_system_data_num(36  -1 +2,10+i,  2,int(self.replay_mode_stage_data[i][ST_SHOT_LEVEL]))            #座標(36,10+i)に2ケタのショットのレベルを書き込みます
            self.write_system_data_num(39  -1 +5,10+i,  5,int(self.replay_mode_stage_data[i][ST_SHOT_SPEED_MAGNIFICATION] * 1000)) #座標(39,10+i)に5ケタのショットのスピードに掛ける倍率を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            self.write_system_data_num(45  -1 +2,10+i,  2,int(self.replay_mode_stage_data[i][ST_SHOT_RAPID_OF_FIRE]))    #座標(45,10+i)に2ケタのショットの連射数を書き込みます
            
            self.write_system_data_num(49  -1 +4,10+i,  4,int(self.replay_mode_stage_data[i][ST_MISSILE_EXP]))                  #座標(49,10+i)に4ケタのミサイルの経験値を書き込みます
            self.write_system_data_num(54  -1 +2,10+i,  2,int(self.replay_mode_stage_data[i][ST_MISSILE_LEVEL]))                #座標(54,10+i)に2ケタのミサイルのレベルを書き込みます
            self.write_system_data_num(57  -1 +5,10+i,  5,int(self.replay_mode_stage_data[i][ST_MISSILE_SPEED_MAGNIFICATION]* 1000))  #座標(57,10+i)に5ケタのミサイルのスピードに掛ける倍率を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            self.write_system_data_num(63  -1 +2,10+i,  2,int(self.replay_mode_stage_data[i][ST_MISSILE_RAPID_OF_FIRE]))        #座標(63,10+i)に2ケタのミサイルの連射数を書き込みます
            
            self.write_system_data_num(68  -1 +2,10+i,  2,int(self.replay_mode_stage_data[i][ST_SELECT_SUB_WEAPON_ID]))   #座標(68,10+i)に2ケタの現在使用しているサブウェポンのIDナンバーを書き込みます
            
            self.write_system_data_num(74  -1 +2,10+i,  2,int(self.replay_mode_stage_data[i][ST_CLAW_NUMBER]))            #座標(74,10+i)に2ケタのクローの装備数を書き込みます
            self.write_system_data_num(71  -1 +2,10+i,  2,int(self.replay_mode_stage_data[i][ST_CLAW_TYPE]))              #座標(71,10+i)に2ケタのクローのタイプを書き込みます
            self.write_system_data_num(77  -1 +4,10+i,  4,int(self.replay_mode_stage_data[i][ST_CLAW_DIFFERENCE]))        #座標(77,10+i)に4ケタのクロ―同士の角度間隔を書き込みます
            
            self.write_system_data_num(82  -1 +2,10+i,  2,int(self.replay_mode_stage_data[i][ST_TRACE_CLAW_INDEX]))       #座標(82,10+i)に2ケタのトレースクロー（オプション）時のトレース用配列のインデックス値を書き込みます
            self.write_system_data_num(85  -1 +5,10+i,  5,int(self.replay_mode_stage_data[i][ST_TRACE_CLAW_DISTANCE] * 1000))    #座標(85,10+i)に5ケタのトレースクロー同士の間隔を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            
            self.write_system_data_num(91  -1 +5,10+i,  5,int(self.replay_mode_stage_data[i][ST_FIX_CLAW_MAGNIFICATION] * 1000)) #座標(91,10+i)に5ケタのフイックスクロー同士の間隔の倍率を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            
            self.write_system_data_num(97  -1 +5,10+i,  5,int(self.replay_mode_stage_data[i][ST_REVERSE_CLAW_SVX] * 1000))       #座標(97,10+i)に5ケタのリバースクロー用の攻撃方向ベクトル(x軸)を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            self.write_system_data_num(103 -1 +5,10+i,  5,int(self.replay_mode_stage_data[i][ST_REVERSE_CLAW_SVY] * 1000))       #座標(103,10+i)に5ケタのリバースクロー用の攻撃方向ベクトル(y軸)を書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            
            self.write_system_data_num(109 -1 +5,10+i,  5,int(self.replay_mode_stage_data[i][ST_CLAW_SHOT_SPEED] * 1000))        #座標(109,10+i)に5ケタのクローショットのスピードを書き込みます(小数点第3位まで行くので1000倍した値を書き込みます)
            self.write_system_data_num(115 -1 +4,10+i,  4,int(self.replay_mode_stage_data[i][ST_LS_SHIELD_HP]))           #座標(115,10+i)に4ケタのL'sシールドの耐久力を書き込みます
            self.write_system_data_num(128 -1 +8,10+i,  8,int(self.replay_control_data_size[i])) #座標(128,10+i)に8ケタのコントロールパッド入力データが記録されたファイルのデータサイズを書き込みます
        pyxel.save("assets/replay/" + slot_num + "/replay_status.pyxres") #プレイステータスファイルをセーブ！
App()