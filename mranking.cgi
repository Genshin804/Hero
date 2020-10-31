#! /usr/bin/perl
require './jcode.pl';
require './sub.cgi';
require './conf.cgi';
	&header;
	print"<table CLASS=TC width=100%><td align=center><font color=$FCOLOR2 size=4>傳說的英雄</font></td></table><BR>";
	open(IN,"./data/country.cgi") or &error2('檔案開發錯誤mranking.cgi(7)。');
	@COU = <IN>;
	close(IN);
	$con_no=0;

	$con_name[0]="無所屬國";
	foreach(@COU){
		($con_id,$con_name,$con_ele,$con_gold,$con_king,$con_yaku,$con_cou,$con_mes,$con_etc)=split(/<>/);
		$con_name[$con_id]="$con_name國";
		$con_no++;
	}
	
	open(IN,"./data/hero.cgi");
	@HERO = <IN>;
	close(IN);

	$htable.="<table CLASS=FC><tr><td CLASS=TC width=9%><font color=$FCOLOR2>順位</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>能力值</font></td><td CLASS=TC width=6%><font color=$FCOLOR2>名稱</font></td><td CLASS=TC><font color=$FCOLOR2>圖像</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>屬性</font><td width=6% CLASS=TC><font color=$FCOLOR2>HP</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>MP</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>力量</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>生命</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>智力</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>精神</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>運氣</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>速度</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>職業</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>戰績</font></td><td width=6% CLASS=TC><font color=$FCOLOR2>所屬</font></td></tr>";
	
	$i=0;
	foreach(@HERO) {
		($bid,$bpass,$bname,$bchara,$bsex,$bhp,$bmaxhp,$bmp,$bmaxmp,$bele,$bstr,$bvit,$bint,$bfai,$bdex,$bagi,$bmax,$bcon,$bclass,$btotal,$bkati,$bpoint) = split(/<>/);
		$i++;
		$rank="$i位";
		if($i eq 1){
			$rank="<font color=red size=3><b>英雄</b></font>";
			$bpoint="<font color=red size=4><b>$bpoint</b></font>";
		}
		elsif($i < 4){
			$rank="<font color=blue size=3><b>$i位</b></font>";
			$bpoint="<font color=blue size=3><b>$bpoint</b></font>";
		}
		$htable.="<tr><td bgcolor=$ELE_C[$con_ele[$bcon]]>$rank</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$bpoint</td><td bgcolor=$ELE_C[$con_ele[$bcon]]>$bname</td><td bgcolor=$ELE_C[$con_ele[$bcon]]><img src=\"$IMG/chara/$bchara.gif\"></td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$ELE[$bele]<td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$bmaxhp</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$bmaxmp</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$bstr</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$bvit</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$bint</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$bfai</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>";
		$htable.="$bdex</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$bagi</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$JOB[$bclass]</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$btotal戰$bkati勝</td><td width=6% bgcolor=$ELE_C[$con_ele[$bcon]]>$con_name[$bcon]</td></tr>";
	}

	
	$con_no=0;
	
	print"$htable</table></center><BR>";
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
