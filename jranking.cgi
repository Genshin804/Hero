#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
	&header;
	print"<table CLASS=TC width=100%><td align=center><font color=#FFFFFF size=4>其他排名</font></td></table><BR>";
print"<center><a href=./nranking.cgi><font color=#ffffff><b>本月戰數排名</b></font></a></center>";
	open(IN,"./data/country.cgi") or &error2('檔案開啟錯誤jranking.cgi(8)。');
	@COU = <IN>;
	close(IN);
	$con_no=0;
	
		
	$dir="./logfile/chara";
	opendir(dirlist,"$dir");
	$i=0;
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i && $file ne "$GMID.cgi" ){
			$datames = "查詢：$dir/$file<br>\n";
			if(!open(cha,"$dir/$file")){
				&error("$dir/$fileがみつかりません。<br>\n");
			}
			@cha = <cha>;
			close(cha);
			$list[$i]="$file";
			($rid,$rpass,$rname,$rurl,$rchara,$rsex,$rhp,$rmaxhp,$rmp,$rmaxmp,$rele,$rstr,$rvit,$rint,$rfai,$rdex,$ragi,$rmax,$rcom,$rgold,$rbank,$rex,$rtotalex,$rjp,$rabp,$rcex,$runit,$rcon,$rarm,$rpro,$racc,$rtec,$rsta,$rpos,$rmes,$rhost,$rdate,$rsyo,$rclass,$rtotal,$rkati,$rtype) = split(/<>/,$cha[0]);
			$rpoint=int(($rmaxhp+$rmaxmp)/3)+$rstr+$rvit+$rint+$rfai+$rdex+$ragi;
			($rjp[0],$rjp[1],$rjp[2],$rjp[3],$rjp[4],$rjp[5]) = split(/,/,$rjp);
			($rmaxstr,$rmaxvit,$rmaxint,$rmaxmen,$rmaxdex,$rmaxagi,$rmaxlv) = split(/,/,$rmax);
			$rmaxtotal=$rmaxstr+$rmaxvit+$rmaxint+$rmaxint+$rmaxmen+$rmaxdex+$rmaxagi;
			push(@CL_DATA,"$rid<>$rpass<>$rname<>$rurl<>$rchara<>$rsex<>$rhp<>$rmaxhp<>$rmp<>$rmaxmp<>$rele<>$rstr<>$rvit<>$rint<>$rfai<>$rdex<>$ragi<>$rmax<>$rcom<>$rgold<>$rbank<>$rex<>$rtotalex<>$rjp[0]<>$rjp[1]<>$rjp[2]<>$rjp[3]<>$rjp[4]<>$rjp[5]<>$rabp<>$rcex<>$runit<>$rcon<>$rarm<>$rpro<>$racc<>$rtec<>$rsta<>$rpos<>$rmes<>$rhost<>$rdate<>$rsyo<>$rclass<>$rtotal<>$rkati<>$rtype<>$rpoint<>$rmaxtotal<>\n");
		}
		if($mn>10000){&error("ループ");}
		$mn++;
	}
	closedir(dirlist);

	@tmp1 = map {(split /<>/)[20]} @CL_DATA;
	@tmp2 = map {(split /<>/)[47]} @CL_DATA;
	@tmp3 = map {(split /<>/)[48]} @CL_DATA;
        @tmp4 = map {(split /<>/)[44]} @CL_DATA;
	@CL_DATA1 = @CL_DATA[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
	@CL_DATA2 = @CL_DATA[sort {$tmp2[$b] <=> $tmp2[$a]} 0 .. $#tmp2];
	@CL_DATA3 = @CL_DATA[sort {$tmp3[$b] <=> $tmp3[$a]} 0 .. $#tmp3];
	@CL_DATA4 = @CL_DATA[sort {$tmp4[$b] <=> $tmp4[$a]} 0 .. $#tmp4];
	$NAME[0]="好野人排名";
	$NAME[1]="強者排名";
	$NAME[2]="潛在力排名";
	$NAME[3]="戰數排名";
	for($i=0;$i<4;$i++){
		$con_table[$i].="<table CLASS=FC>";
		$con_table[$i].="<tr>";
		$con_table[$i].="<td colspan=4 align=center bgcolor=$ELE_BG[$con_ele]><font color=$FCOLOR2 size=5><b>$NAME[$i]</b></font></td>";
		$con_table[$i].="</tr>";
		$con_table[$i].="<tr>";
		$con_table[$i].="<td width=25% CLASS=TC><font color=$FCOLOR2>順位</font></td><td width=25% CLASS=TC><font color=$FCOLOR2>名稱</font></td><td width=25% CLASS=TC><font color=$FCOLOR2>頭像</font></td><td width=25% CLASS=TC><font color=$FCOLOR2>數值</font></td>";
		$con_no++;
	}
	
	foreach(@CL_DATA1){
		($rid,$rpass,$rname,$rurl,$rchara,$rsex,$rhp,$rmaxhp,$rmp,$rmaxmp,$rele,$rstr,$rvit,$rint,$rfai,$rdex,$ragi,$rmax,$rcom,$rgold,$rbank,$rex,$rtotalex,$rjp[0],$rjp[1],$rjp[2],$rjp[3],$rjp[4],$rjp[5],$rab,$rcex,$runit,$rcon,$rarm,$rpro,$racc,$rtec,$rsta,$rpos,$rmes,$rhost,$rdate,$rsyo,$rclass,$rtotal,$rkati,$rtype,$rpoint,$rmaxtotal) = split(/<>/);
		$pid = &id_change("$rid");
		if($cont_cou[0]<30){
			$cont_cou[0]++;
			$rank="$cont_cou[0]位";
			if($cont_cou[0] eq 1){
				$rank="<font color=red size=4><b>★$cont_cou[0]位</b></font>";
				$rbank="<font color=red size=4><b>$rbank</b></font>";
			}
			elsif($cont_cou[0] < 4){
				$rank="<font color=blue size=3><b>$cont_cou[0]位</b></font>";
				$rbank="<font color=blue size=3><b>$rbank</b></font>";
			}
			$con_table[0].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rname</td><td bgcolor=$ELE_C[$con_ele[0]]><img src=\"$IMG/chara/$rchara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>－</td></tr>";
		}else{last;}
	}
	foreach(@CL_DATA2){
		($rid,$rpass,$rname,$rurl,$rchara,$rsex,$rhp,$rmaxhp,$rmp,$rmaxmp,$rele,$rstr,$rvit,$rint,$rfai,$rdex,$ragi,$rmax,$rcom,$rgold,$rbank,$rex,$rtotalex,$rjp[0],$rjp[1],$rjp[2],$rjp[3],$rjp[4],$rjp[5],$rab,$rcex,$runit,$rcon,$rarm,$rpro,$racc,$rtec,$rsta,$rpos,$rmes,$rhost,$rdate,$rsyo,$rclass,$rtotal,$rkati,$rtype,$rpoint,$rmaxtotal) = split(/<>/);
		$pid = &id_change("$rid");
		if($cont_cou[1]<30){
			$cont_cou[1]++;
			$rank="$cont_cou[1]位";
			if($cont_cou[1] eq 1){
				$rank="<font color=red size=4><b>★$cont_cou[1]位</b></font>";
				$rpoint="<font color=red size=4><b>$rpoint</b></font>";
			}
			elsif($cont_cou[1] < 4){
				$rank="<font color=blue size=3><b>$cont_cou[1]位</b></font>";
				$rpoint="<font color=blue size=3><b>$rpoint</b></font>";
			}
			$con_table[1].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rname</td><td bgcolor=$ELE_C[$con_ele[0]]><img src=\"$IMG/chara/$rchara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$rpoint</td></tr>";
		}else{last;}
	}
	foreach(@CL_DATA3){
		($rid,$rpass,$rname,$rurl,$rchara,$rsex,$rhp,$rmaxhp,$rmp,$rmaxmp,$rele,$rstr,$rvit,$rint,$rfai,$rdex,$ragi,$rmax,$rcom,$rgold,$rbank,$rex,$rtotalex,$rjp[0],$rjp[1],$rjp[2],$rjp[3],$rjp[4],$rjp[5],$rab,$rcex,$runit,$rcon,$rarm,$rpro,$racc,$rtec,$rsta,$rpos,$rmes,$rhost,$rdate,$rsyo,$rclass,$rtotal,$rkati,$rtype,$rpoint,$rmaxtotal) = split(/<>/);
		$pid = &id_change("$rid");
		if($cont_cou[2]<30){
			$cont_cou[2]++;
			$rank="$cont_cou[2]位";
			if($cont_cou[2] eq 1){
				$rank="<font color=red size=4><b>★$cont_cou[2]位</b></font>";
				$rmaxtotal="<font color=red size=4><b>$rmaxtotal</b></font>";
			}
			elsif($cont_cou[2] < 4){
				$rank="<font color=blue size=3><b>$cont_cou[2]位</b></font>";
				$rmaxtotal="<font color=blue size=3><b>$rmaxtotal</b></font>";
			}
			$con_table[2].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rname</td><td bgcolor=$ELE_C[$con_ele[0]]><img src=\"$IMG/chara/$rchara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$rmaxtotal</td></tr>";
		}else{last;}
	}

        foreach(@CL_DATA4){
                ($rid,$rpass,$rname,$rurl,$rchara,$rsex,$rhp,$rmaxhp,$rmp,$rmaxmp,$rele,$rstr,$rvit,$rint,$rfai,$rdex,$ragi,$rmax,$rcom,$rgold,$rbank,$rex,$rtotalex,$rjp[0],$rjp[1],$rjp[2],$rjp[3],$rjp[4],$rjp[5],$rab,$rcex,$runit,$rcon,$rarm,$rpro,$racc,$rtec,$rsta,$rpos,$rmes,$rhost,$rdate,$rsyo,$rclass,$rtotal,$rkati,$rtype,$rpoint,$rmaxtotal) = split(/<>/);
                $pid = &id_change("$rid");
                if($cont_cou[3]<30){
                        $cont_cou[3]++;
                        $rank="$cont_cou[3]位";
                        if($cont_cou[3] eq 1){
                                $rank="<font color=red size=4><b>★$cont_cou[3]位</b></font>";
                                $rtotal="<font color=red size=4><b>$rtotal</b></font>";
                        }
                        elsif($cont_cou[3] < 4){
                                $rank="<font color=blue size=3><b>$cont_cou[3]位</b></font>";
                                $rtotal="<font color=blue size=3><b>$rtotal</b></font>";
                        }
                        $con_table[3].="<tr><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rank</td><td bgcolor=$ELE_C[$con_ele[0]] size=2>$rname</td><td bgcolor=$ELE_C[$con_ele[0]]><img src=\"$IMG/chara/$rchara.gif\"></td><td bgcolor=$ELE_C[$con_ele[0]]>$rtotal</td></tr>";
                }else{last;}
        }

	$con_no=0;
	for($i=0;$i<4;$i++){
		$con_table[$i].="</table>";
	}
	print"<table colspan=4>";
	for($i=0;$i<4;$i++){
		if($i%4 eq 0){
			print"<tr><td>$con_table[$i]</td>";
		}elsif($i%4 eq 1 || $i%4 eq 2){
			print"<td>$con_table[$i]</td>";
		}else{
			print"<td>$con_table[$i]</td></tr>";
		}
	}
	print"</table>";
	print"<center><font color=yellow>遊戲人數：$mn名</font></center><BR>";
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
