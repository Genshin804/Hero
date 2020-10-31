#!/usr/bin/perl

#################################################################
#   【免責事項】                                                #
#    このスクリプトはフリーソフトです。このスクリプトを使用した #
#    いかなる損害に対して作者は一切の責任を負いません。         #
#    また設置に関する質問はサポート掲示板にお願いいたします。   #
#    直接メールによる質問は一切お受けいたしておりません。       #
#################################################################

require 'jcode.pl';
require './conf.cgi';
require 'sub.cgi';

if($MENTE) { &error2("載入中，請稍後。"); }
&decode;
&STATUS_PRINT2;

sub STATUS_PRINT2 {

	#&SERVER_STOP;
	$chid = decrypt($in{'id'});

	open(IN,"./logfile/chara/$chid.cgi") or &error2("帳號不存在。err no :$in{'id'}");
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$ejp,$eabp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$esk,$eflg,$eflg2,$eflg3,$eflg4,$eflg5,$epet) = split(/<>/,$E_DATA[0]);
	$elv = int($eex/100)+1;
	&equip_open;
		
	open(IN,"./data/ability.cgi");
	@ABILITY = <IN>;
	close(IN);

	$abname1="";
	$abname2="";
	$abname3="";
        $abname4="";
        ($earmstas[0],$earmstas[1])=split(/:/,$earmsta);
        ($eprostas[0],$eprostas[1])=split(/:/,$eprosta);
        ($eaccstas[0],$eaccstas[1])=split(/:/,$eaccsta);
        ($epetstas[0],$epetstas[1])=split(/:/,$epetsta);
        foreach(@ABILITY){
                ($abno,$abname,$abcom,$abdmg,$abrate,$abpoint,$abclass,$abtype)=split(/<>/);

                if($earmstas[0] eq $abno){
                        $abname1=$abname.$abname1;
                }elsif($earmstas[1] eq $abno){
               		$abname1.="、$abname";
                }
                if($eprostas[0] eq $abno){
                        $abname2=$abname.$abname2;
                }elsif($eprostas[1] eq $abno){
               		$abname2.="、$abname";
                }
                if($eaccstas[0] eq $abno){
                        $abname3=$abname.$abname3;
                }elsif($eaccstas[1] eq $abno){
               		$abname3.="、$abname";
                }
                if($epetstas[0] eq $abno){
                        $abname4=$abname.$abname4;
                }elsif($epetstas[1] eq $abno){
               		$abname4.="、$abname";
                }
                $j++;
        }
	if($abname1 eq""){$abname1="－";}
        if($abname2 eq""){$abname2="－";}
        if($abname3 eq""){$abname3="－";}
        if($abname4 eq""){$abname4="－";}
	if($epetname ne""){
		$showpetname="$epetname($ELE[$epetele]).lv$epetlv";
		$showpetval="<font size=2>威力:$epetdmg<BR>防禦:$epetdef<BR>速度:$epetspeed</font>";
	}

	open(IN,"./logfile/prof/$eid.cgi");
	@PROF_DATA = <IN>;
	close(IN);

	if(@PROF_DATA == ()){
		$com1="";
	}
	else{
		$com1="@PROF_DATA";
	}


	open(IN,"./data/country.cgi") or &error2('資料開啟錯誤status_print.cgi(64)。err no :country');
	@COU_DATA = <IN>;
	close(IN);
	$country_no=0;$hit=0;
	foreach(@COU_DATA){
		($con2_id,$con2_name,$con2_ele,$con2_gold,$con2_king,$con2_yaku,$con2_cou,$con2_mes,$con2_etc)=split(/<>/);
		if("$con2_id" eq "$econ"){$hit=1;last;}
		$country_no++;
	}

	if(!$hit){
		$con2_id=0;
		$con2_name="無所屬";
		$con2_ele=0;
	}
	open(IN,"./logfile/history/$eid.cgi");
	@HIS_DATA = <IN>;
	close(IN);
	$history="<table bgcolor=$ELE_BG[$con2_ele] width=100%>";
	$history.="<tr><td><font color=ffffff>所屬</font></td><td><font color=ffffff>時間</font></td><td><font color=ffffff>紀錄</font></td></tr>";
	foreach(@HIS_DATA){
		($hcom,$hcon,$htime)=split(/<>/);
		$history.="<tr><td bgcolor=$ELE_C[$con2_ele]>$hcon國</td><td bgcolor=$ELE_C[$con2_ele] width=15%>$htime</td><td bgcolor=$ELE_C[$con2_ele]>$hcom</td></tr>";
	}
	$history.="</table>";
}
	&header;

print <<"EOM";
<TABLE border="0" width="80%" bgcolor="#000000" align=center>
  <TBODY>
    <TR>
<form action="./verchk_print.cgi" target="_blank">
	<input type=hidden name=id value=$in{'id'}>
      <TD colspan="7" bgcolor="$ELE_BG[$con2_ele]" align="center"><font color=ffffff>【$ename的基本資料】<input type=hidden value=驗證紀錄></font></TD>
</form>
    </TR>
    <TR>
      <TD bgcolor="$ELE_C[$con2_ele]" rowspan="5" width=10%><img src="$IMG/chara/$echara.gif"></TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>所屬國</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$con2_name國</TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>屬性</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$ELE[$eele]</TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>職業</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$JOB[$eclass]</TD>
    </TR>
    <TR>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>LV</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$elv</TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>HP</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$ehp/$emaxhp</TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>MP</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$emp/$emaxmp</TD>
      </TR>
    <TR>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>力</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$estr</TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>生命</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$evit</TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>智力</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$eint</TD>
    </TR>
    <TR>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>精神</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$efai</TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>運氣</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$edex</TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>速度</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$eagi</TD></TR>
    <TR>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>戰績</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$etotal戰$ekati勝</TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>名聲</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$ecex</TD>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>擊倒人數</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]">$eflg2人</TD>
    </TR>
    <TR>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>武器</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]" colspan=3>$earmname($ELE[$earmele])</TD>
      <TD bgcolor="$ELE_C[$con2_ele]" align=center>$abname1</TD>
      <TD bgcolor="$ELE_C[$con2_ele]" colspan=2 align=right>$earmdmg/$earmwei</TD>
    </TR>
    <TR>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>防具</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]" colspan=3>$eproname($ELE[$eproele])</TD>
      <TD bgcolor="$ELE_C[$con2_ele]" align=center>$abname2</TD>
      <TD bgcolor="$ELE_C[$con2_ele]" colspan=2 align=right>$eprodmg/$eprowei</TD>
    </TR>
    <TR>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>飾品</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]" colspan=3>$eaccname($ELE[$eaccele])</TD>
      <TD bgcolor="$ELE_C[$con2_ele]" align=center>$abname3</TD>
      <TD bgcolor="$ELE_C[$con2_ele]" colspan=2 align=right>$eaccdmg/$eaccwei</TD>
    </TR>
    <TR>
      <TD bgcolor="$ELE_BG[$con2_ele]"><font color=$ELE_C[$con2_ele]>寵物</font></TD>
      <TD bgcolor="$ELE_C[$con2_ele]" colspan=3>$showpetname</TD>
      <TD bgcolor="$ELE_C[$con2_ele]" align=center>$abname4</TD>
      <TD bgcolor="$ELE_C[$con2_ele]" colspan=2 align=right>$showpetval</TD>
    </TR>
    <TR>
      <TD colspan="7" bgcolor="$ELE_BG[$con2_ele]"><FONT color="$ELE_C[$con2_ele]">$ename的自傳</FONT></TD>
    </TR>
    <TR>
      <TD colspan="7" bgcolor="$ELE_C[$con2_ele]">$com1</TD>
    </TR>
    <TR>
      <TD colspan="7" bgcolor="$ELE_BG[$con2_ele]"><FONT color="$ELE_C[$con2_ele]">$ename的經歷</FONT></TD>
    </TR>
    <TR>
      <TD colspan="7" bgcolor="$ELE_C[$con2_ele]">$history</TD>
    </TR>
  </TBODY>
</TABLE>

EOM
	&mainfooter;
	exit;
}

#----------------------#
#  パスワード照合處理  #
#----------------------#
sub decrypt {
	local($inpw) = @_;
	$encrypt = reverse($inpw);
	@dec = split(/\,/,"$encrypt");
	$inpw = pack("C*", @dec);
	
	return $inpw;
}
