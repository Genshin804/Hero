#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
	&header;
	print"<table CLASS=TC width=100%><td align=center><font color=$FCOLOR2 size=4>排名情報</font></td></table><BR>";
	open(IN,"./data/country.cgi") or &error2('檔案開啟錯誤ranking.cgi(8)。');
	@COU = <IN>;
	close(IN);
	$con_no=0;
	foreach(@COU){
		($con_id,$con_name,$con_ele,$con_gold,$con_king,$con_yaku,$con_cou,$con_mes,$con_etc)=split(/<>/);
if($con_id ne"a9"){
		$con_name[$con_id]="$con_name";
		$c[$country_no]=0;
		open(IN,"./logfile/chara/$con_king.cgi");
		@KING_DATA = <IN>;
		close(IN);
		($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$efai,$edex,$eagi,$emax,$ecom,$egold,$ebank,$eex,$etotalex,$ejp,$eabp,$ecex,$eunit,$econ,$earm,$epro,$eacc,$etec,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati,$etype,$eoya,$eaup,$eflg,$eflg2,$eflg3,$eflg4,$eflg5,$epet) = split(/<>/,$KING_DATA[0]);
        $scon_gold=int($con_gold/10000);
        if ($scon_gold>9999) {
                $scon_gold=int($scon_gold/10000)."億".($scon_gold%10000)."萬";
        }elsif($con_gold<10000){
                $scon_gold="$con_gold Gold";
        }else{
                $scon_gold.="萬";
        }
		
		$con_ele[$con_id]=$con_ele;
		$con_king[$con_id]="$ename";
		$con_table[$con_id].="<table CLASS=FC>";
		$con_table[$con_id].="<tr><td colspan=14 align=center bgcolor=$ELE_BG[$con_ele]><font color=$FCOLOR2 size=5><b>$con_name國</b></font></td></tr>";
		$con_table[$con_id].="<tr><td colspan=14 align=center CLASS=FC><font color=$FCOLOR>國王：$con_king[$con_id]　屬性：$ELE[$con_ele]　資金：$scon_gold</font></td></tr>";
		$con_table[$con_id].="<tr><td CLASS=TC><font color=$FCOLOR2>名稱</font></td><td CLASS=TC><font color=$FCOLOR2>頭像</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>屬性</font><td width=7% CLASS=TC><font color=$FCOLOR2>HP</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>MP</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>力量</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>生命力</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>智力</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>精神</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>運氣</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>速度</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>名聲</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>職業</font></td><td width=7% CLASS=TC><font color=$FCOLOR2>戰數</font></td></tr>";
		$con_no++;
}
	}
	$con_ele[0]=0;
	$con_table[0].="<table CLASS=FC>";
	$con_table[0].="<tr><td colspan=14 align=center bgcolor=$ELE_BG[0]><font color=$FCOLOR2 size=5><b>無所屬</b></font></td></tr>";
		
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
			($rid,$rpass,$rname,$rurl,$rchara,$rsex,$rhp,$rmaxhp,$rmp,$rmaxmp,$rele,$rstr,$rvit,$rint,$rfai,$rdex,$ragi,$rmax,$rcom,$rgold,$rbank,$rex,$rtotalex,$rjp,$rabp,$rcex,$runit,$rcon,$rarm,$rpro,$racc,$rtec,$rsta,$rpos,$rmes,$rhost,$rdate,$rsyo,$rclass,$rtotal,$rkati,$rtype) = split(/<>/,$cha[0]);
if($rcon ne"a9"){
			push(@CL_DATA,"$rid<>$rpass<>$rname<>$rurl<>$rchara<>$rsex<>$rhp<>$rmaxhp<>$rmp<>$rmaxmp<>$rele<>$rstr<>$rvit<>$rint<>$rfai<>$rdex<>$ragi<>$rmax<>$rcom<>$rgold<>$rbank<>$rex<>$rcex<>$runit<>$rcon<>$rarm<>$rpro<>$racc<>$rtec<>$rsta<>$rpos<>$rmes<>$rhost<>$rdate<>$rsyo<>$rclass<>$rtotal<>$rkati<>$rtype<>\n");
}
		}
		if($mn>10000){&error("ループ");}
		$mn++;
	}
	closedir(dirlist);
	@tmp = map {(split /<>/)[22]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	foreach(@CL_DATA){
		($rid,$rpass,$rname,$rurl,$rchara,$rsex,$rhp,$rmaxhp,$rmp,$rmaxmp,$rele,$rstr,$rvit,$rint,$rfai,$rdex,$ragi,$rmax,$rcom,$rgold,$rbank,$rex,$rcex,$runit,$rcon,$rarm,$rpro,$racc,$rtec,$rsta,$rpos,$rmes,$rhost,$rdate,$rsyo,$rclass,$rtotal,$rkati,$rtype) = split(/<>/);
		$pid = &id_change("$rid");
		if($cont_cou[$rcon]<10 && $rcon ne 0){
			$con_table[$rcon].="<tr><td bgcolor=$ELE_C[$con_ele[$rcon]] size=2><a href=\"javascript:void(0);\" onClick=\"javascript:opstatus('$pid');\">$rname</a></td><td bgcolor=$ELE_C[$con_ele[$rcon]]><img src=\"$IMG/chara/$rchara.gif\"></td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$ELE[$rele]</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$rhp/$rmaxhp</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$rmp/$rmaxmp</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$rstr</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$rvit</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$rint</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$rfai</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$rdex</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$ragi</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$rcex</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$JOB[$rclass]</td><td bgcolor=$ELE_C[$con_ele[$rcon]]>$rtotal戰$rkati勝</td></tr>";
			$cont_cou[$rcon]++;
		}elsif(($cont_cou[$rcon] >=10 || $rcon eq 0) && $rurl eq ""){
			$con_table2[$rcon].="<font color=$ELE_BG[$con_ele[$rcon]] size=2><a href=\"javascript:void(0);\" onClick=\"javascript:opstatus('$pid');\">$rname</a>，</font>";
			$cout_cou[$rcon]++;
		}
	}
	$con_no=0;
	foreach(@COU){
		($con_id,$con_name,$con_ele,$con_gold,$con_king,$con_yaku,$con_cou,$con_mes,$con_etc)=split(/<>/);
		$con_table[$con_id].="<tr><td colspan=14 CLASS=FC>$con_table2[$con_id]</td></tr></table><BR>";
		print"$con_table[$con_id]";
		$con_no++;
	}
	$con_table[0].="<tr><td colspan=14 CLASS=FC>$con_table2[0]</td></tr></table>";
	print"$con_table[0]<BR>";
	print"<center><font color=yellow>遊戲人數：$mn名</font></center><BR>";
	print"\n<script language=javascript>\nfunction opstatus(pid){\nwindow.open('./status_print.cgi?id='+pid, 'newwin', 'width=600,height=400,scrollbars =yes');\n}\n</script>\n";
&mainfooter;
sub id_change {
	local($inpw) = $_[0];

	@yy = unpack("C*", $inpw);
	$word="";
	foreach(@yy){
		$word .= "$_\,";
	}
	chomp($word);
	$encrypt = reverse($word);

	return $encrypt;
}
exit;
