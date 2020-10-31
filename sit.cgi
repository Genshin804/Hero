#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
&decode;
&header;

open(IN,"./data/country.cgi");
@CON = <IN>;
close(IN);
open(IN,"./data/towndata.cgi");
@TOWN_DATA = <IN>;
close(IN);

$dir="./logfile/chara";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "查詢：$dir/$file<br>\n";
		if(!open(cha,"$dir/$file")){
			&error("$dir/$fileがみつかりません。<br>\n");
		}
		@cha = <cha>;
		close(cha);
		$list[$i]="$file";
		($rid,$rpass,$rname,$rurl,$rchara,$rsex,$rhp,$rmaxhp,$rmp,$rmaxmp,$rele,$rstr,$rvit,$rint,$rfai,$rdex,$ragi,$rmax,$rcom,$rgold,$rbank,$rex,$rtotalex,$rjp,$rabp,$rcex,$runit,$rcon) = split(/<>/,$cha[0]);
		$KOKUMIN[$rcon]++;
	}
	if($mn>10000){&error("ループ");}
	$mn++;
}
closedir(dirlist);

foreach(@TOWN_DATA){
	($town_id,$town_name,$town_con,$town_ele,$town_gold,$town_arm,$town_pro,$town_acc,$town_ind,$town_tr,$town_s,$town_x,$town_y,$town_build,$town_etc)=split(/<>/);
	$TOWN[$town_con]++;
}

$conlist="<table CLASS=FC width=100%>";
$conlist.="<tr><td CLASS=TC><font color=$FCOLOR2>國名</font></td><td CLASS=TC><font color=$FCOLOR2>國王</font></td><td CLASS=TC><font color=$FCOLOR2>國民</font></td><td CLASS=TC><font color=$FCOLOR2>資金</font></td><td CLASS=TC><font color=$FCOLOR2>領土</font></td></tr>";

foreach(@CON){
	($con2_id,$con2_name,$con2_ele,$con2_gold,$con2_king,$con2_yaku,$con2_cou,$con2_mes,$con2_etc)=split(/<>/);
	push(@CONS,"$con2_id<>$con2_name<>$KOKUMIN[$con2_id]<>$con2_gold<>$TOWN[$con2_id]<>\n");
	$CONELE[$con2_id]=$con2_ele;
	$CONNAME[$con2_id]=$con2_name;
	$c_no++;
}

@tmp = map {(split /<>/)[2]} @CONS;
@CONS = @CONS[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
$rank=1;
foreach(@CONS){
	($con3_id,$con3_name)=split(/<>/);
	$KRANK[$con3_id]=$rank;
	$POINT[$con3_id]+=($c_no-$rank)*2;
	if($rank eq 1){$KRANK1="$con3_name";}
	$rank++;
}
@tmp = map {(split /<>/)[3]} @CONS;
@CONS = @CONS[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

$rank=1;
foreach(@CONS){
	($con3_id,$con3_name)=split(/<>/);
	$GRANK[$con3_id]=$rank;
	$POINT[$con3_id]+=($c_no-$rank);
	if($rank eq 1){$GRANK1="$con3_name";}
	$rank++;
}
@tmp = map {(split /<>/)[4]} @CONS;
@CONS = @CONS[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

$rank=1;
foreach(@CONS){
	($con3_id,$con3_name)=split(/<>/);
	$TRANK[$con3_id]=$rank;
	$POINT[$con3_id]+=($c_no-$rank);
	if($rank eq 1){$TRANK1="$con3_name";}
	push(@NCONS,"$con3_id<>$con3_name<>$KRANK[$con3_id]<>$GRANK[$con3_id]<>$TRANK[$con3_id]<>$POINT[$con3_id]<>\n");
	$rank++;
}


foreach(@CON){
	($con2_id,$con2_name,$con2_ele,$con2_gold,$con2_king,$con2_yaku,$con2_cou,$con2_mes,$con2_etc)=split(/<>/);
	open(IN,"./logfile/chara/$con2_king.cgi");
	@K_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname,$kurl,$kchara,$ksex)=split(/<>/,$K_DATA[0]);
	$conlist.="<tr><td bgcolor=$ELE_BG[$con2_ele]><font color=$ELE_C[$con2_ele]>$con2_name國($ELE[$con2_ele])</font></td><td bgcolor=$ELE_C[$con2_ele]>$kname</td><td bgcolor=$ELE_C[$con2_ele] align=right>$KOKUMIN[$con2_id]人($KRANK[$con2_id]位)</td><td bgcolor=$ELE_C[$con2_ele] align=right>$con2_gold Gold($GRANK[$con2_id]位)</td><td bgcolor=$ELE_C[$con2_ele] align=right>$TOWN[$con2_id]($TRANK[$con2_id]位)</td></tr>";

}
$conlist.="</table>";


##マップ表示
$tpr="<table bgcolor=663300><TD width=15 height=10 bgcolor=ffffcc CLASS=GC>　</TD>";
for($i=0;$i<6;$i++){
	$tpr.= "<TD width=15 height=10 bgcolor=ffffcc><font size=1>$i</font></TD>";
}
for($i=0;$i<6;$i++){
	$n = $i;
	$tpr.= "<TR><TD bgcolor=ffffcc><font size=1>$n</font></td>";
	for($j=0;$j<6;$j++){
		$m_hit=0;$tx=0;
		foreach(@TOWN_DATA){
			($town2_id,$town2_name,$town2_con,$town2_ele,$town2_gold,$town2_arm,$town2_pro,$town2_acc,$town2_ind,$town2_tr,$town2_s,$town2_x,$town2_y)=split(/<>/);
			if("$town2_x" eq "$j" && "$town2_y" eq "$i"){$m_hit=1;last;}
			$tx++;
		}
		$col="";
		if($m_hit){
			
			$col = $ELE_BG[$CONELE[$town2_con]];
			
			if($town2_id eq 0){
				$tpr.= "<TH bgcolor=$col><img src=\"$IMG/town/m_2.gif\" title=\"$town2_name【$CONNAME[$town2_con]國】\" width=15 height=10></TH>";
			}else{
				$tpr.= "<TH bgcolor=$col><img src=\"$IMG/town/m_4.gif\" title=\"$town2_name【$CONNAME[$town2_con]國】\" width=15 height=10></TH>";
			}
		}else{
			$tpr.= "<TH>　</TH>";
		}
	}
	$tpr.= "</TR>";
}
$tpr.="</table>";

$m=0;
open(IN,"./data/maplog2.cgi");
@MA = <IN>;
close(IN);
foreach(@MA){
	$mapl.="<b><font color=$FCOLOR>●$MA[$m]</font></b><BR>";
	$m++;
}


#状況解説

@tmp = map {(split /<>/)[5]} @NCONS;
@NCONS = @NCONS[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
($c_id,$c_name,$korank,$grank,$trank,$point)=split(/<>/,$NCONS[0]);
if($c_no>4){
	($c_id2,$c_name2,$korank2,$grank2,$trank2,$point2)=split(/<>/,$NCONS[1]);
	($c_id3,$c_name3,$korank3,$grank3,$trank3,$point3)=split(/<>/,$NCONS[2]);
}
$c_no2=$c_no-1;
($c_idl,$c_namel,$korankl,$grankl,$trankl,$pointl)=split(/<>/,$NCONS[$c_no2]);
if($c_no>1){
	$com.="目前有$c_no國。「$c_name國」最為強大。<BR>";
	if($c_no>4){
		$com.="其次為「$c_name2國」及「$c_name3國」。<BR>";
	}
	$com.="人口最多為「$KRANK1國」、財力最富的為「$GRANK1國」、領土最大為「$TRANK1國」。<BR>";
	if($korank eq 1){
		$com.="「$c_name國」的人口目前最多、今後「$c_name國」將成為世界發展的指標。<BR>";
	}else{
		$hit=1;
		$com.="但「$KRANK1國」人民數量多於「$c_name國」、今後發展值得觀注。是「$c_name」最大的威脅。<BR>";
	}if($grank ne 1 && !$hit){
		$com.="「$GRANK1國」的戰力處於劣勢、但國家財力雄厚，會不會直起急追是值得觀察的。<BR>";
	}
	if($c_no>2){
		$com.="「$c_namel國」的情勢不如預期樂觀、他們需要更多優秀的人才。到底未來會如何發展下去，就看他們自己了。<BR>";
	}
	if($c_no eq 2){
		$com.="冒險世界有兩個國家在競爭，只要一方失敗，另一方將會統一這個世界・・・<BR>";
	}
}elsif($c_no>0){
	$com.="目前冒險世界只有「$c_name國」。如果沒有其他的競爭者，「$c_name國」將會統一這個世界。<BR>";
}else{
	$com.="目前還沒有人建立國家<BR>";
}
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#660033" width="700" cellspacing="5" height="509">
  <TBODY>
    <TR>
      <TD colspan="2" width="696" align="center"><FONT style="font-size:30px" font color="#ffff99">世界情勢</FONT></TD>
    </TR>
    <TR>
      <TD align="center" bgcolor="#330000" width="30%" height="80">
	$tpr<BR>
      </TD>
　　　<TD colspan="1" align="left" bgcolor="#844200" width="70%" height="80">
	<FONT style="font-size:17px" font face="標楷體" color="#ffffcc"><各國情況><BR>$com</FONT>
      </TD>
    </TR>
    <TR>
      <TD colspan="2" bgcolor="#330000">
	<FONT style="font-size:15px" font face="標楷體" color="#660000">$conlist</FONT>
      </TD>
    </TR>
    <TR>
      <TD colspan="2" bgcolor="#ffffcc">
	<FONT style="font-size:15px" font face="標楷體" color="#660000"><歷史><BR>$mapl</FONT>
	</TD>
    </TR>
  </TBODY>
</TABLE>
</CENTER>

<hr>
EOF

&mainfooter;
exit;
