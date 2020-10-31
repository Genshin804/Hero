#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
&decode;
#if($ENV{'HTTP_REFERER'} !~ /cgi$/ ){ &error2("資料傳輸有誤，<a href='./login.cgi'>請重新登入</a>。"); }
&chara_open;
&town_open;
&con_open;
&ext_open;
                $ext_tmpxs=$ext_lock-$date;
                $ext_tmpx=int(($ext_tmpxs)/60/60);
                if($ext_tmpxs>0){
	$error_msg="ERROR<>你的帳號已被封鎖,需要$ext_tmpx小時($ext_tmpxs秒)才會解除";
		}else{
if ($ext_lock ne "" && $ext_robot >3){
	$ext_lock="";$ext_robot="";&ext_input;
}
#取得目前城鎮所屬國
foreach(@CON_DATA){
        ($con2_id,$con2_name,$con2_ele,$con2_gold,$con2_king,$con2_yaku,$con2_cou,$con2_mes,$con2_etc)=split(/<>/);
        $CONELE[$con2_id]=$con2_ele;
        $CONNAME[$con2_id]=$con2_name;
        $c_no++;
}
$hit=0;
foreach(@CON_DATA){
        ($con2_id,$con2_name,$con2_ele,$con2_gold,$con2_king,$con2_yaku,$con2_cou,$con2_mes,$con2_etc)=split(/<>/);
        if("$con2_id" eq "$town_con"){$hit=1;last;}
}
if(!$hit){$con2_ele=0;$con2_name="無所屬";$con2_id=0;}
if($ext_show_mode_maplog ne"N"){

	#情報頻
	open(IN,"./data/maplogtime.cgi");
	$LOGTIME = <IN>;
	close(IN);
	if($LOGTIME ne $in{'logtime'}){
		open(IN,"./data/maplog.cgi");
		@MAP = <IN>;
		close(IN);
		foreach(@MAP){
		        $maplog.="MAPLOG<>$MAP[$l]";
		        $l++;
		}
	
		open(IN,"./data/maplog5.cgi");
		@MAP2 = <IN>;
		close(IN);
		foreach(@MAP2){
		        $maplog2.="MAPLOG2<>$MAP2[$l2]";
		        $l2++;
		}
	}
}
##聊天傳送
#世頻
open(IN,"./meslog/all.cgi");
        @MES_DATA1 = <IN>;
        close(IN);
#國頻
open(IN,"./meslog/$con_id.cgi");
        @MES_DATA2 = <IN>;
        close(IN);
#私頻
open(IN,"./logfile/mes/$mid.cgi");
        @MES_DATA3 = <IN>;
        close(IN);
#隊頻
open(IN,"./meslog/unit/$munit.cgi");
        @MES_DATA4 = <IN>;
        close(IN);
        $tts=$in{'tt'};
        if($tts eq""){$tts=0;}
        $chattime=0;
        foreach(@MES_DATA4){
                ($lid,$laite,$leid,$lchara,$lname,$lmes,$tt)=split(/<>/);
                &time_data2;
                if($chattime<$tt){$chattime=$tt;}
                if($tts<$tt){
                        $atable.="CHAT<>4<>$lchara<>$lname<>$lmes<>$daytime<>\n";
                }
        }
        foreach(@MES_DATA3){
                ($lid,$laite,$leid,$lchara,$lname,$lmes,$tt)=split(/<>/);
                $klist="";
                &time_data2;
                if($lid ne $mid && $leid ne $mid){$klist="<a href=\"#down2\" onclick=\"javascript:void(document.getElementById('aite').value='$leid');\"><font color=yellow>[回]</font></a>";}
                if($chattime<$tt){$chattime=$tt;}
                if($tts<$tt){
                        $atable.="CHAT<>3<>$lchara<>$klist$lname<>$lmes<>$daytime<>\n";
                }
        }
        foreach(@MES_DATA2){
                ($lid,$laite,$leid,$lchara,$lname,$lmes,$tt)=split(/<>/);
                &time_data2;
                if($chattime<$tt){$chattime=$tt;}
                if($tts<$tt){
                        $atable.="CHAT<>2<>$lchara<>$lname<>$lmes<>$daytime<>\n";
                }
        }
        foreach(@MES_DATA1){
                ($lid,$laite,$leid,$lchara,$lname,$lmes,$tt)=split(/<>/);
                &time_data2;
                if($chattime<$tt){$chattime=$tt;}
                if($tts<$tt){
                        $atable.="CHAT<>1<>$lchara<>$lname<>$lmes<>$daytime<>\n";
                }
        }
##線上玩家傳送
	$guestlist="";
    open(IN,"./data/guest_list.cgi");
    @guest = <IN>;
    close(IN);
    &host_name;
    $timer = time();@newguest=();
    $playcount=0;
    foreach(@guest) {
            ($gname,$gtime,$gcon,$ghost,$gid)=split(/<>/);
            if($timer>$gtime+($CMDTIME*100)){next;}
            elsif($mname eq $gname){
                $ghit=1;
                push(@newguest,"$mname<>$timer<>$con_ele<>$host<>$mid<>\n");
				$pid = &id_change("$mid");
                $guestlist.="GUEST<>$pid<>$ELE_BG[$gcon]<>$mname<>\n";
                $playcount++;
            }
            else{
				$pid = &id_change("$gid");
                push(@newguest,"$gname<>$gtime<>$gcon<>$ghost<>$gid<>\n");
                $guestlist.="GUEST<>$pid<>$ELE_BG[$gcon]<>$gname<>\n";
                $playcount++;
            }
    }
    if(!$ghit){
    		$pid = &id_change("$mid");
            push(@newguest,"$mname<>$timer<>$con_ele<>$host<>$mid<>\n");
            $guestlist.="GUEST<>$pid<>$ELE_BG[$gcon]<>$mname<>\n";
            $playcount++;
    }
    $guestlist.="GUESTCOUNT<>$playcount<>\n";
    if($ext_show_mode_guest eq"N"){$guestlist="";}
    if($in{'inv'} ne"true"){
	    open(OUT,">./data/guest_list.cgi");
	    print OUT @newguest;
	    close(OUT);
    }
        if($playcount>$ADDTIMEMAX){
                $BTIME+=($playcount-$ADDTIMEMAX);
		if($BTIME>35){$BTIME=35;}
        }
        if($member_fix_time){
                $BTIME=15;
        }
        if ($mid eq $GMID){
                $BTIME=5;
        }
	$BTIME = $BTIME - $date + $mdate;
	if($mflg<2){
	    #Ajax城鎮情報
	    $town_data="TOWN<>$town_id<>$town_name<>$con2_name<>$ELE[$town_ele]<>$town_gold<>$town_arm<>$town_pro<>$town_acc<>$town_ind<>$town_tr<>$town_s<>$town_x<>$town_y<>$town_build<>$town_etc\n";
	    #城鎮守備
	    open(IN,"./data/def.cgi");
	    @DEF = <IN>;
	    close(IN);
	    foreach(@DEF){
            ($name,$id,$pos)=split(/<>/);
            if($pos eq "$mpos"){
		$pid = &id_change("$id");
		$town_def_list.="<>$name $pid";
	    }
	    }
	    $town_def_list="TOWNDEF$town_def_list";
	}
    #戰鬥地圖
        if ($nowmap eq""){
                $nowmap="入口";
        }elsif($nowmap eq"25"){
		$nowmap="王座";
		$giveupmap.="放棄王座,giveup2<>";
	}else{
                $nowmap.="層";
        }
    $dun="$town_name $SEN[1],1<>$town_name $SEN[2],2<>$town_name $SEN[3],3<>$town_name $SEN[4],4<>$town_name $SEN[30],30<>$town_name 禁地$nowmap,31<>魔王城,40<>===============,<>訓練,kunren<>討伐,toubatsu<>$giveupmap";
#    $dun="$town_name $SEN[1],1<>$town_name $SEN[2],2<>$town_name $SEN[3],3<>$town_name $SEN[4],4<>$town_name $SEN[30],30<>===============,<>訓練,kunren<>討伐,toubatsu<>$giveupmap";

	##顯示試鍊
	$moya2=$moya%1000;
        if($mex%11 eq "0" && $mex < 9900){$dun="$SEN[5],5<>$dun";}
        if($moya%40 eq "0"){$dun="$SEN[6],6<>$dun";}
        if($moya%80 eq "7"){$dun="$SEN[7],7<>$dun";}
        if($moya%300 eq "8"){$dun="$SEN[8],8<>$dun";}
	if($moya eq "55555"){$dun="$SEN[12],12<>$dun";}
	if($moya%1000 eq "9"){$dun="$SEN[9],9<>$dun";}
        if($moya%2500 eq "17"){$dun="$SEN[11],11<>$dun";}
        if($moya eq "775" || $moya eq "776"){$dun="$SEN[15],15<>$dun";}
        if($moya%5000 eq "773"){$dun="$SEN[13],13<>$dun";}
        if($moya eq "777"){$dun="$SEN[10],10<>$dun";}
        if($moya eq "77777"){$dun="$SEN[14],14<>$dun";}
        if ($mtotal > 100 && $mtotal%100 eq "1"){
                $dun="$SEN[20],20<>$dun";}
        if ($mtotal > 100 && $mtotal%300 eq "2"){
                $dun="$SEN[21],21<>$dun";}
        if ($mtotal > 100 && $mtotal%600 eq "3"){
               $dun="$SEN[22],22<>$dun";}
        if ($mtotal > 100 && $mtotal%3000 eq "4"){
                $dun="$SEN[23],23<>$dun";}
        if ($mtotal > 100 && $mtotal%10000 eq "5"){
                $dun="$SEN[24],24<>$dun";}
	
        open(IN,"./data/townmonster.cgi");
        @tmdata = <IN>;
        close(IN);
        ($tename,$teab,$tetec,$tesk,$te_ex,$te_gold,$tetown,$telv)=split(/<>/,$tmdata[0]);
	if($tetown eq $town_id){
	        $dun2.="神獸,townmonster<>";
	}
	$dun="BATTLE<>$dun$dun2";
#其他選項
	$acton="ACTION<>活動兌換屋,action";
	if($moya%1000 eq "1"){$townsp="TOWNSP<>魔女的店,rshop";}
	if($moya eq "6666"){$townsp="TOWNSP<>傳說中的馴獸師,rpetup";}
	if($moya%5000 eq "37"){$status="STATUSSP<>改名神殿,name_change";}
#贊助會員
	if($member_point ne""){
		$member="MEMBER<>$member_fix_time<>";
	}
	}#鎖帳結束
    print "Cache-Control: no-cache\n";
    print "Pragma: no-cache\n";
    print "Content-type: text/html\n\n";
    print <<"EOF";
VER<>$AJAXVER<>
$atable
$guestlist
$ajax_chara_data
$ajax_con_data
$town_data$maplog$maplog2
$town_def_list
ALLTIME<>$timer<>$mdate<>$chattime<>$LOGTIME<>$BTIME<>
$dun
$acton
$townsp
$status
$member
$error_msg
EOF

exit;

