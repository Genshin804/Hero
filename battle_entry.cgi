sub start{

	$entry_level[0]="新手組";
	$entry_level[1]="進階組";
	$entry_level[2]="高手組";
        $entry_level[3]="英雄組";
        open(IN,"./data/battle_time.cgi");
	    $BTIMEN = <IN>;
	    close(IN);
	($battle_time[0],$battle_time[1],$battle_time[2],$battle_time[3],$battle_time[4])=split(/<>/,$BTIMEN);
	if($battle_time[$entrylevel]>0){

	open(IN,"./data/entry_list_$entrylevel.cgi");
	@ENTRY = <IN>;
	close(IN);

	$ji=0;$entry_total=0;
	foreach(@ENTRY){
		($eid,$ename,$echara,$etotal,$estatus,$ebattle_time,$elog)=split(/<>/);
		if($ebattle_time eq $battle_time[$entrylevel]){
			if($estatus eq""){
				if($ji eq 0){
					$open_chara_id=$eid;
				}elsif($ji eq 1){
					$open_enemy_id=$eid;
				}
				$ji++;
			}
			$entry_total++;
		}
	}
	$entry_oever=0;
	if($entry_total <3){
		$entry_title="決賽";
		$entry_oever=1;
	}elsif($entry_total <5){
		$entry_title="準決賽";
	}else{
		$entry_title="第$battle_time[$entrylevel]輪比賽";
		$entry_title2="-將進行下一輪比賽";
	}
        if ($open_chara_id eq""){
		$e0[0]="";$e0[1]="";
		$n0[0]="";$n0[0]="";
		$join_count=0;
	        foreach(@ENTRY){
	                ($eid,$ename,$echara,$etotal,$estatus,$ebattle_time,$elog)=split(/<>/);
	                if($estatus eq"W" && $ebattle_time eq $battle_time[$entrylevel]){
	                	$ebattle_time++;
				push(@ENTRY,"$eid<>$ename<>$echara<>$etotal<><>$ebattle_time<><>\n");
	                }
	                if ($estatus eq"W"){$e0[0]="$eid";$n0[0]="$ename";}
        	        elsif($estatus eq"L"){$e0[1]="$eid";$n0[1]="$ename";}
			if(etotal eq"1"){
				$join_count++;
			}
	        }
                    open(OUT,">./data/entry_list_$entrylevel.cgi");
                    print OUT @ENTRY;
                    close(OUT);
                    $battle_time[$entrylevel]++;
		    if($entry_oever){
			$battle_time[$entrylevel]=0;
			$entry_title2="-冠軍:$n0[0],亞軍:$n0[1]";
                open(IN,"./logfile/item/$e0[0].cgi");
                @ITEM = <IN>;
                close(IN);
		$get_gold=0;
                if($entrylevel eq 3){
                                        push(@ITEM,"priv<>3<>武奧石之箱<>10000000<>0<>0<>0<>80<>10<>寶物<>14<><>\n");
                                        push(@ITEM,"priv<>3<>武奧石之箱<>10000000<>0<>0<>0<>80<>10<>寶物<>14<><>\n");
                                        $get_gold=int($join_count*20000000/3);
                 		}elsif($entrylevel eq 2){
					push(@ITEM,"priv<>3<>武奧石之箱<>10000000<>0<>0<>0<>80<>10<>寶物<>14<><>\n");
					push(@ITEM,"priv<>3<>+10賢者之石<>10000000<>10<>0<>0<>80<>10<>寶物<>4<><>\n");
					$get_gold=int($join_count*10000000/3);
				}elsif($entrylevel eq 1){
					push(@ITEM,"priv<>3<>神秘的寶箱<>10000000<>0<>0<>0<>80<>10<>寶物<>23<><>\n");
					push(@ITEM,"priv<>3<>星空入場券<>10000000<>999<>0<>0<>80<>10<>寶物<>10<><>\n");
					$get_gold=int($join_count*6000000/3);
				}elsif($entrylevel eq 0){
					push(@ITEM,"priv<>3<>GM婆的熟練之書<>10000000<>5000<>0<>0<>80<>10<>寶物<>11<><>\n");
					push(@ITEM,"priv<>3<>星空入場券<>10000000<>999<>0<>0<>80<>10<>寶物<>10<><>\n");
					$get_gold=int($join_count*3000000/3);
				}
                open(OUT,">./logfile/item/$e0[0].cgi");
                print OUT @ITEM;
                close(OUT);
	if($e0[1] ne""){
                open(IN,"./logfile/item/$e0[1].cgi");
                @ITEM2 = <IN>;
                close(IN);
		$get_gold2=0;
                if($entrylevel eq 3){
			push(@ITEM2,"priv<>3<>武奧石之箱<>10000000<>0<>0<>0<>80<>10<>寶物<>14<><>\n");
                        $get_gold2=int($join_count*20000000/5);
                }elsif($entrylevel eq 2){
                        push(@ITEM2,"priv<>3<>星空入場券<>10000000<>999<>0<>0<>80<>10<>寶物<>10<><>\n");
			push(@ITEM2,"priv<>3<>星空入場券<>10000000<>999<>0<>0<>80<>10<>寶物<>10<><>\n");
			push(@ITEM2,"priv<>3<>+10賢者之石<>10000000<>10<>0<>0<>80<>10<>寶物<>4<><>\n");
			$get_gold2=int($join_count*10000000/5);
		}elsif($entrylevel eq 1){
			push(@ITEM2,"priv<>3<>星空入場券<>10000000<>999<>0<>0<>80<>10<>寶物<>10<><>\n");
			push(@ITEM2,"priv<>3<>星空入場券<>10000000<>999<>0<>0<>80<>10<>寶物<>10<><>\n");
			$get_gold2=int($join_count*6000000/5);
		}elsif($entrylevel eq 0){
			push(@ITEM2,"priv<>3<>星空入場券<>10000000<>999<>0<>0<>80<>10<>寶物<>10<><>\n");
			$get_gold2=int($join_count*3000000/5);
		}
	}
                open(IN,"./data/entry_comp.cgi");
                @ECOMP = <IN>;
                close(IN);
		unshift(@ECOMP,"$e0[0]<>$n0[0]<>$entrylevel<>\n");
	if($e0[1] ne""){
                unshift(@ECOMP,"$e0[1]<>$n0[1]<>$entrylevel<>\n");
	}
                open(OUT,">./data/entry_comp.cgi");
                print OUT @ECOMP;
                close(OUT);
        if($e0[1] ne""){
                open(OUT,">./logfile/item/$e0[1].cgi");
                print OUT @ITEM2;
	}
                close(OUT);
			$enemy_id=$e0[0];
			&enemy_open;
			$ebank+=$get_gold;
			&enemy_input;
			if ($entrylevel eq 3){
				&ext_enemy_open;
				$ext2_entry_count++;
				&ext_enemy_input;
			}
	        if($e0[1] ne""){
                        $enemy_id=$e0[1];
                        &enemy_open;
                        $ebank+=$get_gold2;
                        &enemy_input;
        	}
		    }
               		&maplog("<font color=green>[天下第一武道大會]$entry_level[$entrylevel]$entry_title賽結束$entry_title2</font>");
 		    $BTIMEN="$battle_time[0]<>$battle_time[1]<>$battle_time[2]<>$battle_time[3]<>";
                    open(OUT,">./data/battle_time.cgi");
                    print OUT $BTIMEN;
                    close(OUT);
                exit;
	}elsif($open_enemy_id eq ""){
		$m_entry_status="W";
		$e_entry_status="L";
		&finish_entry;
		exit;
	}
	
	#開啟角色資料
	&chara_open2;
	$err_open1=0;
	$err_open2=0;
	if($mid ne $open_chara_id){
		$err_open1=1;
	}
	if($eid ne $open_enemy_id){
		$err_open2=1;
	}
	#找不到角色資料
	if($err_open1 || $err_open2){
		$m_entry_status="W";
		$e_entry_status="W";
		if($err_open1){
			$m_entry_status="L";
		}
		if($err_open2){
			$e_entry_status="L";
		}
		&finish_entry;
		exit;
	}
	if ($entrylevel ne 0){
		&equip_open;
	}
        &PARA;
        #富豪之力
        $mgolddmg=0;
        $egolddmg=0;


        &TEC_OPEN;
        $entry_log = <<"EOM";
        <html>
        <head>
        <META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=utf-8">
        <STYLE type="text/css">
        <!--
A:HOVER{
 color: $ALINK
}
.BC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[0] $ELE_BG[0] $ELE_BG[0] $ELE_BG[0];border-style : double double double double;background-color : $ELE_BG[0];color : black;}
or : $ELE_BG[0] $ELE_BG[0] $ELE_BG[0] $ELE_BG[0];border-style : double double double double;background-color : $ELE_BG[0];color : black;}
.TC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $FCOLOR $FCOLOR $FCOLOR $FCOLOR;border-style : double double double double;background-color : $FCOLOR;color : black;}
.CC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$con_ele] $ELE_BG[$con_ele] $ELE_BG[$con_ele] $ELE_BG[$con_ele];border-style : double double double double;background-color : $ELE_BG[$con_ele];color : black;}
.CC2 {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$con2_ele] $ELE_BG[$con2_ele] $ELE_BG[$con2_ele] $ELE_BG[$con2_ele];border-style : double double double double;background-color : $ELE_BG[$con2_ele];color : black;}
.MC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$wele] $ELE_BG[$wele] $ELE_BG[$wele] $ELE_BG[$wele];border-style : double double double double;background-color : $ELE_BG[$wele];color : black;}
.MFC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width : $ELE_BG[$con_ele];border-top-color : $ELE_BG[$con_ele];border-right-color : $ELE_BG[$con_ele];border-bottom-color : $ELE_BG[$con_ele];border-left-color : $ELE_BG[$con_ele];border-style : double double double double;background-color : $ELE_C[$con_ele];color : black;}
.FC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width : $FCOLOR;border-top-color : $FCOLOR;border-right-color : $FCOLOR;border-bottom-color : $FCOLOR;border-left-color : $FCOLOR;border-style : double double double double;background-color : $FCOLOR2;color : black;}
.TOC {border-top-width : medium;border-right-width : medium;border-bottom-width : medium;border-left-width :medium; border-color : $ELE_BG[$town_ele] $ELE_BG[$town_ele] $ELE_BG[$town_ele] $ELE_BG[$town_ele];border-style : double double double double;background-color : $ELE_BG[$town_ele];color : black;}
.dmg { color: #FF0000; font-size: 10pt }
.clit { color: #0000FF; font-size: 10pt }
-->
        </STYLE>
        <title>$TITLE</title></head>
        <body background=\"$BGIF\" bgcolor=\"$BG\">

<TABLE border="0" width="100%" align=center height="144" CLASS=TOC>
  <TBODY>
    <TR>
      <TD colspan="3" align="center" bgcolor="$ELE_BG[$town_ele]" style="font-size:12pt"><FONT color="#ffffcc">天下第一武道大會-$entry_level[$entrylevel]</FONT></TD>
    </TR>
    <TR>
      <TD bgcolor="#cccccc" width="30%">
      <TABLE border="0" width="100%" height="100%" bgcolor=$ELE_BG[$mele] align=right>
        <TBODY>
          <TR>
            <TD rowspan="2"><FONT size="-1"><img src="$IMG/chara/$mchara.gif"></FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">HP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$mhp/$mmaxhp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">攻擊力</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$mstr $chi1(+$marmdmg+<font color=red>$mpetdmg)</font></FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">武器</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$marmname<BR>
            【$marmdmg/$marmwei】</FONT></TD>
          </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">MP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$mmp/$mmaxmp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">防御力</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$mvit $chi1(+$mprodmg+$maccdmg+<font color=red>$mpetdef</font>)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">防具</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$mproname<BR>
            【$mprodmg/$mprowei】</FONT></TD>
          </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$mname$petname2</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">職業</FONT></TD>
            <TD bgcolor=$FCOLOR2>$JOB[$mclass]</TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">速度</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$magi+<font color=red>$mpetspeed</font></FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">飾品</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$maccname<BR>
            【$maccdmg/$maccwei】</FONT></TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
      <TD align="center" bgcolor="$FCOLOR2" width="20%"><a href="#lower"><IMG src="$IMG/etc/arena.jpg" width="150" height="113" border="0"></a></TD>
      <TD bgcolor="#cccccc" width=30%>
      <TABLE border="0" width="100%" height="100%" bgcolor=$ELE_BG[$eele]>
        <TBODY>
          <TR>
            <TD rowspan="2"><FONT size="-1"><img src="$IMG/chara/$echara.gif"></FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">HP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$ehp/$emaxhp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">攻擊力</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$estr $chi2 (+$earmdmg+<font color=red>$epetdmg)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">武器</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$earmname<BR>
            【$earmdmg/$earmwei】</FONT></TD>
          </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">MP</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$emp/$emaxmp</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">防御力</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$evit $chi2(+$eprodmg+$eaccdmg+<font color=red>$epetdef</font>)</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">防具</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$eproname<BR>
            【$eprodmg/$eprowei】</FONT></TD>
         </TR>
          <TR>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$ename$epetname2</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">職業</FONT></TD>
            <TD bgcolor=$FCOLOR2>$JOB[$eclass]</TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">速度</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$eagi+<font color=red>$epetspeed</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">飾品</FONT></TD>
            <TD bgcolor=$FCOLOR2><FONT size="-1">$eaccname<BR>
            【$eaccdmg/$eaccwei】</FONT></TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
    <TR>
      <TD bgcolor=#000000><font color="white" size="-1">「$mcom」</font></TD>
      <TD align=center bgcolor="666600"><font color="white" size="-1">戰鬥宣言</font></TD>
      <TD bgcolor=#000000><font color="white" size="-1">「$ecom」</font></TD>
    </TR>
  </TBODY>
</TABLE>
<BR><BR>
EOM

##戰鬥處理
        $turn=0;$win=0;$lose=0;
        $maxturn=50;
        while($turn<=$maxturn){
                $turn++;
                if($turn>100){&error("回合錯誤");}
                $bmess="";
                $mmess="";
                if($mab[15] && $mabdmg[15]>$eabdmg[15] && int(rand(3-$mabdmg[15])) eq 0){$sensei = 1;}
                elsif($eab[15] && $eabdmg[15]>$mabdmg[15] && int(rand(3-$eabdmg[15])) eq 0){$sensei = 0;}
                elsif(int(rand($mdex)) > int(rand($edex))){$sensei = 1;}
                else{$sensei = 0;}
                if($sensei){
                        if($mhp>0){
                                &MATT;
                        }else{
                                $bmess.="<font size=3 color=#FF0000><b>(你已經沒有體力，躺在地上無法行動．．．)</b></font>";
                        }
                        if($ehp>0){
                                &EATT;

                        }
                }else{
                        if($ehp>0){
                                &EATT;
                        }
                        if($mhp>0){&MATT;}
                }
                if($sensei){
                        &BPRINT2;
                } else {
                        &MPRINT2;
                }
                if($win){
                        $m_entry_status="W";
                        $e_entry_status="L";
                        $entry_log.= <<"EOF";
                        <center><a name=lower></a>
                        <TABLE border="0" width="400" bgcolor="#000000" CLASS=TC>
                        <TBODY><TR>
                        <TD colspan="2" align="center" bgcolor="#FFFFFF" height="40"><FONT color="red"><b>$mname勝出！</b></FONT></TD>
                        </TR>
                        </TBODY></TABLE>
                        </center>
EOF

                        last;
                }elsif($lose){
                        $entry_log.= <<"EOF";
                        <center><a name=lower></a>
                        <TABLE border="0" width="400" bgcolor="#000000" CLASS=TC>
                        <TBODY><TR>
                        <TD colspan="2" align="center" bgcolor="#FFFFFF" height="40"><FONT color="red"><b>$ename勝出！</b></FONT></TD>
                        </TR>
                        </TBODY></TABLE>
                        </center>
EOF

                        $m_entry_status="L";
                        $e_entry_status="W";
                        last;
                }


        }
		if(!$win && !$lose){
			if($elose_hp>$mlose_hp){
	                        $m_entry_status="W";
	                        $e_entry_status="L";
                        	$entry_log.= <<"EOF";
                	        <center><a name=lower></a>
        	                <TABLE border="0" width="400" bgcolor="#000000" CLASS=TC>
	                        <TBODY><TR>
                        	<TD colspan="2" align="center" bgcolor="#FFFFFF"><FONT color="red"><b>$mname被大會裁判判定勝出！</b></FONT></TD></TR><TR>
				<TD colspan="2" align="center" bgcolor="#FFFFFF"><FONT color="red">$mname總傷害輸出$elose_hp<BR>$ename總傷害輸出$mlose_hp</FONT></TD>
                	        </TR>
        	                </TBODY></TABLE>
	                        </center>
EOF

			}else{
                                $entry_log.= <<"EOF";
                                <center><a name=lower></a>
                                <TABLE border="0" width="400" bgcolor="#000000" CLASS=TC>
                                <TBODY><TR>
                                <TD colspan="2" align="center" bgcolor="#FFFFFF"><FONT color="red"><B>$ename被大會裁判判定勝出！</b></FONT></TD>
                                <TD colspan="2" align="center" bgcolor="#FFFFFF"><FONT color="red">$ename總傷害輸出$mlose_hp<BR>$mname總傷害輸出$elose_hp</FONT></TD>
                                </TR>
                                </TBODY></TABLE>
                                </center>
EOF
                                $m_entry_status="L";
                                $e_entry_status="W";
			}
		}
		&finish_entry;
	}
}

sub finish_entry{
        if ($entry_log ne""){
	    &time_data;
	    $elog="$year"."_"."$mon"."_"."$mday"."_"."$hour"."_"."$min"."_".$sec."_"."$entrylevel";
            open(OUT,">/var/www/html/hero_data/html/tmp.html");
            print OUT $entry_log;
            close(OUT);
            open(OUT,">/var/www/html/hero_data/battle/entry/$elog.html");
            print OUT $entry_log;
            close(OUT);
	    $battleurl="<a href=\"/hero_data/battle/entry/$elog.html\" target=_blank>";
        }
	if($m_entry_status eq"W"){
		&maplog("<font color=green>[天下第一武道大會]</font>$entry_level[$entrylevel]$battleurl$entry_title</a>-恭喜<font color=blue>$mname</font>擊敗$ename勝出");
	}elsif($e_entry_status eq"W"){
		&maplog("<font color=green>[天下第一武道大會]$entry_level[$entrylevel]</font>$battleurl$entry_title</a>-恭喜<font color=blue>$ename</font>擊敗$mname勝出");
	}else{
		&maplog("[天下第一武道大會]$entry_level[$entrylevel]$entry_title-$mname及$ename雙方敗出");
	}
	open(IN,"./data/entry_list_$entrylevel.cgi");
    @ENTRY = <IN>;
    close(IN);
    @ENTRY2=();
	foreach(@ENTRY){
		($eid,$ename,$echara,$etotal,$estatus,$ebattle_time,$elog2)=split(/<>/);
		if($eid eq $open_enemy_id && $battle_time[$entrylevel] eq $ebattle_time){
			$estatus=$e_entry_status;
			$elog2=$elog;
		}elsif($eid eq $open_chara_id && $battle_time[$entrylevel] eq $ebattle_time){
			$estatus=$m_entry_status;
			$elog2=$elog;
		}
		push(@ENTRY2,"$eid<>$ename<>$echara<>$etotal<>$estatus<>$ebattle_time<>$elog2<>\n");
	}
    open(OUT,">./data/entry_list_$entrylevel.cgi");
    print OUT @ENTRY2;
    close(OUT);
}

sub chara_open2{
        open(IN,"./logfile/chara/$open_chara_id.cgi");
        @M_DATA = <IN>;
        close(IN);
        ($mid,$mpass,$mname,$murl,$mchara,$msex,$mhp,$mmaxhp,$mmp,$mmaxmp,$mele,$mstr,$mvit,$mint,$mfai,$mdex,$magi,$mmax,$mcom,$mgold,$mbank,$mex,$mtotalex,$mjp,$mabp,$mcex,$munit,$mcon,$marm,$mpro,$macc,$mtec,$msta,$mpos,$mmes,$mhost,$mdate,$msyo,$mclass,$mtotal,$mkati,$mtype,$moya,$msk,$mflg,$mflg2,$mflg3,$mflg4,$mflg5,$mpet) = split(/<>/,$M_DATA[0]);
        $mlv = int($mex/100)+1;
		$mhp=$mmaxhp;
		$mmp=$mmaxmp;
        open(IN,"./logfile/chara/$open_enemy_id.cgi");
        @E_DATA = <IN>;
        close(IN);
        ($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$ejp,$eabp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$esk,$eflg,$eflg2,$eflg3,$eflg4,$eflg5,$epet) = split(/<>/,$E_DATA[0]);
        $elv = int($eex/100)+1;
        $ehp=$emaxhp;
        $emp=$emaxmp;
}

sub equip_open2{
        ($marmno,$marmname,$marmval,$marmdmg,$marmwei,$marmele,$marmhit,$marmcl,$marmsta,$marmtype,$marmflg) = split(/,/,$marm);
        ($mprono,$mproname,$mproval,$mprodmg,$mprowei,$mproele,$mprohit,$mprocl,$mprosta,$mprotype,$mproflg) = split(/,/,$mpro);
        ($maccno,$maccname,$maccval,$maccdmg,$maccwei,$maccele,$macchit,$macccl,$maccsta,$macctype,$maccflg) = split(/,/,$macc);
        ($mpetcno,$mpetname,$mpetdmg,$mpetdef,$mpetspeed,$mpetele,$mpetlv,$mpetcl,$mpetsta,$mpettype,$mpetflg) = split(/,/,$mpet);
        ($msk[0],$msk[1]) = split(/,/,$msk);
        ($tmp_arm_sk[0],$tmp_arm_sk[1]) = split(/,/,$marmsta);
        ($tmp_pro_sk[0],$tmp_pro_sk[1]) = split(/,/,$mprosta);
        ($tmp_acc_sk[0],$tmp_acc_sk[1]) = split(/,/,$maccsta);
        ($tmp_pet_sk[0],$tmp_pet_sk[1]) = split(/,/,$mpetsta);

        if($msk[0] eq "62" || $msk[1] eq "62"){$eleplus = 0.2;}
	elsif($tmp_arm_sk[0] eq "62" || $tmp_arm_sk[0] eq "62"){$eleplus = 0.2;}
	elsif($tmp_pro_sk[0] eq "62" || $tmp_pro_sk[0] eq "62"){$eleplus = 0.2;}
	elsif($tmp_acc_sk[0] eq "62" || $tmp_acc_sk[0] eq "62"){$eleplus = 0.2;}
	elsif($tmp_pet_sk[0] eq "62" || $tmp_pet_sk[0] eq "62"){$eleplus = 0.2;}

        $petname2="";
        if ($mpet eq""){
                $mpetdmg=0;
                $mpetdef=0;
                $mpetspeed=0;
        }else{
                $petname2="<font color=blue>+$mpetname.lv$mpetlv</font>";
        }
        if($mele eq "$marmele" && $marmele ne "0"){
                if($marmno eq"mix"){
                        $marmdmg = int($marmdmg*(1.3 + $eleplus));
                }else{
                        $marmdmg = int($marmdmg*(1.2 + $eleplus));
                }
        }
        if($mele eq "$mproele" && $mproele ne "0"){
                if($mprono eq"mix"){
                        $mprodmg = int($mprodmg*(1.3 + $eleplus));
                }else{
                        $mprodmg = int($mprodmg*(1.2 + $eleplus));
                }
        }
        if($mele eq "$maccele" && $maccele ne "0"){$maccdmg = int($maccdmg*(1.5 + $eleplus));}
        if($mele eq "$mpetele" && $mpetele ne "0"){
                $mpetdmg = int($mpetdmg*(1.2 + $eleplus));
                $mpetdef = int($mpetdef*(1.2 + $eleplus));
                $mpetspeed = int($mpetspeed*(1.2 + $eleplus));
        }
        if($ARM[$mclass] eq "$marmtype"){$marmhit += 10;}

        if($eid){
		($esk[0],$esk[1],$esk[2],$esk[3]) = split(/,/,$esk);
	        ($tmp_arm_sk2[0],$tmp_arm_sk2[1]) = split(/,/,$earmsta);
	        ($tmp_pro_sk2[0],$tmp_pro_sk2[1]) = split(/,/,$eprosta);
	        ($tmp_acc_sk2[0],$tmp_acc_sk2[1]) = split(/,/,$eaccsta);
	        ($tmp_pet_sk2[0],$tmp_pet_sk2[1]) = split(/,/,$epetsta);

                ($earmno,$earmname,$earmval,$earmdmg,$earmwei,$earmele,$earmhit,$earmcl,$earmsta,$earmtype,$earmflg) = split(/,/,$earm);
                ($eprono,$eproname,$eproval,$eprodmg,$eprowei,$eproele,$eprohit,$eprocl,$eprosta,$eprotype,$eproflg) = split(/,/,$epro);
                ($eaccno,$eaccname,$eaccval,$eaccdmg,$eaccwei,$eaccele,$eacchit,$eacccl,$eaccsta,$eacctype,$eaccflg) = split(/,/,$eacc);
                ($epetno,$epetname,$epetdmg,$epetdef,$epetspeed,$epetele,$epetlv,$epetcl,$epetsta,$epettype,$epetflg) = split(/,/,$epet);

                if($esk[0] eq "62" || $esk[1] eq "62"){$eleplus2=0.2;}
		elsif($tmp_arm_sk2[0] eq "62" || $tmp_arm_sk2[0] eq "62"){$eleplus2 = 0.2;}
		elsif($tmp_pro_sk2[0] eq "62" || $tmp_pro_sk2[0] eq "62"){$eleplus2 = 0.2;}
		elsif($tmp_acc_sk2[0] eq "62" || $tmp_acc_sk2[0] eq "62"){$eleplus2 = 0.2;}
		elsif($tmp_pet_sk2[0] eq "62" || $tmp_pet_sk2[0] eq "62"){$eleplus2 = 0.2;}
                if ($epet eq""){
                        $epetdmg=0;
                        $epetdef=0;
                        $epetspeed=0;
                }else{
                        $epetname2="<font color=blue>+$epetname.lv$epetlv</font>";
                }
                $ehpadd=0;
                if($eele eq "$earmele" && $earmele ne "0"){
                        if($earmno eq"mix"){
                                $earmdmg = int($earmdmg*(1.3 + $eleplus2));
                        }else{
                                $earmdmg = int($earmdmg*(1.2 + $eleplus2));
                        }
                }
                if($eele eq "$eproele" && $eproele ne "0"){
                        if($eprono eq"mix"){
                                $eprodmg = int($eprodmg*(1.3 + $eleplus2));
                        }else{
                                $eprodmg = int($eprodmg*(1.2 + $eleplus2));
                        }
                }
                if($eele eq "$eaccele" && $eaccele ne "0"){$eaccdmg = int($eaccdmg*(1.5 + $eleplus2));}
                if($eele eq "$epetele" && $epetele ne "0"){
                        $epetdmg = int($epetdmg*(1.2 + $eleplus2));
                        $epetdef = int($epetdef*(1.2 + $eleplus2));
                        $epetspeed = int($epetspeed*(1.2 + $eleplus2));
                }

                if($ARM[$eclass] eq "$earmtype"){$earmhit += 10;}
        }
}

#回合別戰鬥結果表示
sub BPRINT2{
        $entry_log.= <<"EOF";
<CENTER>
<TABLE border="0" width="80%" bgcolor="#000000" CLASS=TC>
  <TBODY>
    <TR>
      <TD colspan="8" align="center" bgcolor="$FCOLOR"><B><a href="#lower"><FONT color="#ffffcc">第$turn回合</FONT></a></B></TD>
    </TR>
    <TR>
      <TD colspan="4" bgcolor="000063" align="center"><FONT color="$FCOLOR2"><B><FONT size="-1">$mname</FONT></B></FONT></TD>
      <TD colspan="4" bgcolor="9c0000" align="center"><B><FONT size="-1" color="$FCOLOR2">$ename</FONT></B></TD>
    </TR>
    <TR>
      <TD colspan="4" bgcolor="$FCOLOR2" align="center"><font size=-1>$bmess</font></TD>
      <TD colspan="4" bgcolor="$FCOLOR2" align="center"><font size=-1>$mmess</font></TD>
    </TR>
        <TR>
      <TD bgcolor="#ccffff" width=12.5%>HP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$mhp/$mmaxhp</TD>
      <TD bgcolor="#ccffff" width=12.5%>MP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$mmp/$mmaxmp</TD>
      <TD bgcolor="#ccffff" width=12.5%>HP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$ehp/$emaxhp</TD>
      <TD bgcolor="#ccffff" width=12.5%>MP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$emp/$emaxmp</TD>
         </TR>
  </TBODY>
</TABLE>
</CENTER>
<P>
EOF
}
sub MPRINT2{
        $entry_log.= <<"EOF";
<CENTER>
<TABLE border="0" width="80%" bgcolor="#000000" CLASS=TC>
  <TBODY>
    <TR>
      <TD colspan="8" align="center" bgcolor="$FCOLOR"><B><a href="#lower"><FONT color="#ffffcc">第$turn回合</FONT></a></B></TD>
    </TR>
    <TR>
          <TD colspan="4" bgcolor="9c0000" align="center"><B><FONT size="-1" color="$FCOLOR2">$ename</FONT></B></TD>
      <TD colspan="4" bgcolor="000063" align="center"><FONT color="$FCOLOR2"><B><FONT size="-1">$mname</FONT></B></FONT></TD>
    </TR>
    <TR>
          <TD colspan="4" bgcolor="$FCOLOR2" align="center"><font size=-1>$mmess</font></TD>
      <TD colspan="4" bgcolor="$FCOLOR2" align="center"><font size=-1>$bmess</font></TD>
    </TR>
        <TR>
      <TD bgcolor="#ccffff" width=12.5%>HP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$ehp/$emaxhp</TD>
      <TD bgcolor="#ccffff" width=12.5%>MP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$emp/$emaxmp</TD>
      <TD bgcolor="#ccffff" width=12.5%>HP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$mhp/$mmaxhp</TD>
      <TD bgcolor="#ccffff" width=12.5%>MP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$mmp/$mmaxmp</TD>
        </TR>
  </TBODY>
</TABLE>
</CENTER>
<P>
EOF
}
1;

