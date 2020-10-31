#バージョン（※著作権表示に使用。變更不可）
$VER="Farland History Ⅱ Ver2.11";

################
##設定ファイル##
################

#※印が付いているものは設定が必須となります。
#設定GM的帳號
$GMID="";
##タイトル
$TITLE="無限冒險";
##ajax版本，主要是增加這個值來通知用戶端目前最新版本，如果版本不同將讓用戶端自動更新
$AJAXVER="2.0";
$FH_URL="";
##活動開啟0不開,1以上開啟
$ACTOPEN=0;

##能力上限
$PARA_LIMIT=1200;
##活動清單
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime(time);
        $mon++;
if($mon eq 5 && $mday>0 && $mday<9) {
        $ACTOPEN=1;
}elsif($mon eq 5 && $mday>19 && $mday<28) {
        $ACTOPEN=2;
}elsif(($mon eq 6 && $mday>12) || ($mon eq 8 && $mday<15) || $mon eq 7){
	$ACTOPEN=3;
}elsif(($mon eq 8 && $mday>=30) || ($mon eq 9)){
	$ACTOPEN=4;
}elsif($mon eq 10 && $mday>=20){
        $ACTOPEN=5;
}elsif(($mon eq 11 && $mday>16) || $mon eq 12){
        $ACTOPEN=6;
}elsif(($mon eq 1 && $mday>17) || $mon eq 2){
        $ACTOPEN=7;
}elsif(($mon eq 3 && $mday>4) || ($mon eq 4 && $mday<21)){
	$ACTOPEN=8;
}
$ACTNAME[0]="";
$ACTNAME[1]="母親節";
$ACTNAME[2]="端午節";
$ACTNAME[3]="暑期";
$ACTNAME[4]="GM婆＆倫仔生日";
$ACTNAME[5]="萬聖";
$ACTNAME[6]="聖誕";
$ACTNAME[7]="新年";
$ACTNAME[8]="無限冒險週年慶";
$ACTITEM[0]="";
$ACTITEM[1]="康乃馨";
$ACTITEM[2]="肉粽";
$ACTITEM[3]="七彩冰棒";
$ACTITEM[4]="生日蛋糕";
$ACTITEM[5]="萬聖糖";
$ACTITEM[6]="聖誕玩偶";
$ACTITEM[7]="紅包";
$ACTITEM[8]="無限抽獎券";


##背景色・壁紙設定　※壁紙は各自用意してください。(※)
$BG="black";
#$BGIF="/hero_img/bg/bg.jpg";
##フォーム
$FCOLOR="#883300";
$FCOLOR2="#ffffee";

##最大ログイン人數（極端に増やすと危険です。まずはデフォルト值で様子を見てください。）
$LMAX="60";
$ADDTIMEMAX=30;
##
##更新時間（戰鬥）（極端に縮めると危険です。まずはデフォルト值で様子を見てください。）
$BTIME="15";
##留言間格時間
$CONTIME="60";
##更新時間（侵略/國）
$KTIME="600";
##更新時間（侵略/無所屬）
$MTIME="1200";
##更新時間（大会）
$CONV="600";
##閒置時間
$IDLETIME="300";
##指令最短間隔
$CMDTIME="2";
##無所屬の侵略に必要な資金
$INVGOLD="5000000";

##多重登録の制限（１で多重不可）
$DOUBLE="2";
##登録の制限（１で登録不可）
$CHARA_ENT="0";

##メッセージ表示件數(全國)
$MES1="10";
##メッセージ表示件數(國)
$MES2="10";
##メッセージ表示件數(個人)
$MES3="10";
##メッセージ表示件數(隊伍)
$MES3="10";

#圖像總數
$CHARAIMG="627";

#圖檔路徑http://www.xxx.com/images
$IMG="http://www.xxx.com/images";

#街画像
$TOWN_IMG=$IMG."/town/machi.jpg";#昼背景
$TOWN_IMG2=$IMG."/town/machi2.jpg";#夜背景

# 認証(登録にメールを必要とするか。０：不必要　１：必要　使用する場合はIDを任意のアルファベットに變更することex:fg,asd,oi)
$ATTESTATION = "0";
$ATTESTATION_ID = 'ab';
#sendmailのパス
$SENDMAIL = '/usr/bin/sendmail';

#URL設定(※)
$LINK1="首頁";
$LINKURL1="/";
$LINK2="討論區";
$LINKURL2="";
$LINK3="遊戲説明";
$LINKURL3="/hero_data/html/manual.html";
$LINK4="玩家列表";
$LINKURL4="./ranking.cgi";
$LINK5="傳說的英雄";
$LINKURL5="./mranking.cgi";
$LINK6="各項排行";
$LINKURL6="./nranking.cgi";
$LINK7="世界情勢";
$LINKURL7="./sit.cgi";
$LINK8="都市情報";
$LINKURL8="./town_print.cgi";
$LINK9="圖像一覧";
$LINKURL9="./icon.cgi";
$LINK10="FH Link";
$LINKURL10="http://bbbnonikkyi.web.fc2.com/link/link01.html";
$LINK11="紀錄";
$LINKURL11="./syslog.cgi";
$LINK12="裝備清單";
$LINKURL12="./eqlist.cgi";
#$LINK13="";
#$LINKURL13="";
$LINK14="";
$LINKURL14="";

#最大熟練度
$MAXJOB="99999";

#角色最大所持數
$ITM_MAX="15";
#倉庫存放最大數
$STORITM_MAX="30";

# 性別
$SEX[0] = "男";
$SEX[1] = "女";

# 屬性
$ELE[0] = "無";
$ELE[1] = "火";
$ELE[2] = "水";
$ELE[3] = "風";
$ELE[4] = "星";
$ELE[5] = "雷";
$ELE[6] = "光";
$ELE[7] = "闇";

# 相克屬性
$ANELE[1] = "2";
$ANELE[2] = "5";
$ANELE[3] = "1";
$ANELE[4] = "3";
$ANELE[5] = "4";
$ANELE[6] = "7";
$ANELE[7] = "6";

#建國費用
$BUGOLD = "5000000000";

# 屬性色１（濃）
$ELE_BG[0] = "#555555";#無
$ELE_BG[1] = "#800000";#火
$ELE_BG[2] = "#000080";#水
$ELE_BG[3] = "#006000";#風
$ELE_BG[4] = "#A07230";#星
$ELE_BG[5] = "#0f6080";#雷
$ELE_BG[6] = "#bb0099";#光
$ELE_BG[7] = "#6C007B";#闇

#屬性色２（薄）
$ELE_C[0] = "#f1f1f1";#無
$ELE_C[1] = "#FFE2E2";#火
$ELE_C[2] = "#E0EEFF";#水
$ELE_C[3] = "#E2FFE2";#風
$ELE_C[4] = "#FFE9C8";#星
$ELE_C[5] = "#E3FFFB";#雷
$ELE_C[6] = "#FFDDFE";#光
$ELE_C[7] = "#DEDAFF";#闇

#武器の種類
$ARM[0]="劍";
$ARM[1]="斧";
$ARM[2]="杖";
$ARM[3]="弓";
$ARM[4]="拳";
$ARM[5]="刀";
$ARM[6]="槍";
$ARM[7]="爪";
$ARM[3]="箭套";

#職業
$JOB[0]="菜鳥新兵";
$JOB[1]="武士";
$JOB[2]="魔術師";
$JOB[3]="僧侶";
$JOB[4]="弓箭手";
$JOB[5]="格鬥家";
$JOB[6]="盜賊";
$JOB[7]="聖騎士";
$JOB[8]="魔導士";
$JOB[9]="祭司";
$JOB[10]="遊俠";
$JOB[11]="武聖";
$JOB[12]="忍者";
$JOB[13]="煉金術士";
$JOB[14]="時魔道師";
$JOB[15]="魔法劍士";
$JOB[16]="風水師";
$JOB[17]="十字軍";
$JOB[18]="黑魔術使";
$JOB[19]="陰陽師";
$JOB[20]="狙擊手 ";
$JOB[21]="刺客";
$JOB[22]="武神";
$JOB[23]="劍聖";
$JOB[24]="闇黑魔導士 ";
$JOB[25]="大神官";
$JOB[26]="天使";
$JOB[27]="夜使者";
$JOB[28]="阿修羅";
$JOB[29]="馴獸師";
$JOB[30]="鐵匠";
$JOB[31]="劍宗";
$JOB[32]="大法師";
$JOB[33]="大祭司長";
$JOB[34]="熾天使";
$JOB[35]="羅煞";
$JOB[36]="吸血鬼";

##レベルアップ時職種別能力上昇值
$JUP[0]=[2,2,1,1,1,1];
$JUP[1]=[1,1,2,2,1,1];
$JUP[2]=[1,1,2,2,1,1];
$JUP[3]=[2,1,1,1,2,1];
$JUP[4]=[1,2,1,2,1,1];
$JUP[5]=[1,1,2,1,1,2];
$JUP[6]=[0,0,1,0,2,2];

#職種別界限補正
$JMAX[0]=[2,1,0,0,1,0];
$JMAX[1]=[0,0,2,1,0,1];
$JMAX[2]=[0,1,1,2,0,0];
$JMAX[3]=[1,0,0,0,2,1];
$JMAX[4]=[1,2,0,1,0,0];
$JMAX[5]=[0,0,1,0,1,2];

#職種系統
$TYPE[0]="劍術";
$TYPE[1]="魔術";
$TYPE[2]="神術";
$TYPE[3]="弓術";
$TYPE[4]="體術";
$TYPE[5]="忍術";

#0:開啟所有特殊地圖
$CHECK_MAP=1;

##經驗加成倍率 Defalut=1
$ADDEX=1;
##熟練加成倍率 Defalut=1
$ADDABP=1;
##金錢加成倍率 Default=1
$ADDGOLD=1;

##驗證金錢加量
$VERADDGOLD=200000;
##驗證熟加量
$VERADDABP=50;
##驗證經驗加量
$VERADDEX=100;

##快速成長率 Default=15
$MAXLVP=15;
##覺醒率 Default=100
$SMAXLVP=100;

#戰鬥場所
$SEN[1]="草原";
$SEN[2]="沼地";
$SEN[3]="森林";
$SEN[4]="高塔";
$SEN[5]="財寶洞穴";
$SEN[6]="修行者之塔";
$SEN[7]="神秘的湖泊";
$SEN[8]="黃金宮殿";
$SEN[9]="暗黑雪原";
$SEN[10]="星空下的夜";
$SEN[11]="藍天之下";
$SEN[12]="神秘的女神像";
$SEN[13]="飛龍之塔";
$SEN[14]="傳說秘地";
$SEN[15]="滿月下的夜";
$SEN[20]="冒險者的試煉";
$SEN[21]="勇者的試練";
$SEN[22]="英雄的試練";
$SEN[23]="星空迷宮";
$SEN[24]="秘寶迷宮";
$SEN[30]="廢城";
$SEN[31]="禁地";
$SEN[32]="冒險者的任務";
$SEN[40]="魔王城";

#裝備の種類
$EQU[0]="武器";
$EQU[1]="防具";
$EQU[2]="飾品";
$EQU[3]="道具";
$EQU[4]="寵物";
$EQU[5]="材料";
$EQU[6]="活動";
$EQU[7]="奧義石";

#城鎮設施
$town_build_name[0]="保護時間";
$town_build_name[1]="箭塔";
$town_build_name[2]="崗哨";
$town_build_name[3]="軍營";
$town_build_name[4]="訓練所";
$town_build_name[5]="兵器研究所";
$town_build_name[6]="護甲研究所";
$town_build_name[7]="軍學院";
$town_build_name[8]="幕兵所";
$town_build_name[9]="軍醫院";
$town_build_name[10]="集結所";
$town_build_name[11]="攻城研究所";
$town_build_name[12]="戰略學院";

#任務名稱
$QUEST_NAME[0]="討伐怪物";
$QUEST_NAME[1]="贊助裝備";
$QUEST_NAME[2]="挑戰自我";
$QUEST_NAME[5]="原料急送";
#ヒントに表示させるメッセージ
$MES[0]="練功不要太拼命，記得起來多休息。";
$MES[1]="速度越高，戰鬥中攻擊的回合速也會越多。";
$MES[2]="武器、防具及飾品的重量會影響到你的速度。";
$MES[3]="在與自己屬性一樣的城鎮戰鬥將會有加成喔。";
$MES[4]="名聲越高，買東西的折扣越多，最多可到８５折。";

#特別log追蹤
$LOG_ID[0]="";
$BACKTOWNBUTTON="<input type=\"button\" value=\"[F4]回到城鎮\" CLASS=FC onclick=\"javascript:parent.backtown();\">";
