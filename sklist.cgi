#! /usr/bin/perl
require './jcode.pl';
	require './sub.cgi';
	require './conf.cgi';
	require './data/abini.cgi';
	&decode;
	&header;

    open(IN,"./data/ability.cgi");
    @ABILITY = <IN>;
    close(IN);

    
    #@jlist = split(/,/,$AJOB[$mclass]);
    $ij=0;
    foreach(@ABILITY){
            ($abno,$abname,$abcom,$abdmg,$abrate,$abpoint,$abclass,$abtype)=split(/<>/);
                   	@jlist = split(/,/,$AJOB[$abclass]);
                   	$ij=0;
                   	$clname="";
                   	foreach(@jlist){
                   		if($clname ne ""){
                   			$clname.="、";
                  		}
                   		$clname.=$JOB[$jlist[$ij]];
                   		$ij++;
                   	}
		if ($clname eq "") {
			$clname="<font color=gray>(無法習得)</font>";
			$abpoint="X";
		}
                    $stable.="<tr bgColor=#FFFFFF><td><font color=\"#0000ff\">$abname</font></td><td><font color=\"#008000\">$abcom</font></td><td align=right><font color=AA3333>$abpoint</font></td><td><font color=AA3333>$clname</font></td></tr>";
    }
       print <<"EOF";
<p align="center">
<i><b><font size="5" color=yellow>奧義清單</font></b></i>
<table id="table1" cellSpacing="0" cellPadding="0" border="1" width="600">
	<tr>
		<td bgColor="#ccffcc" width="120"><b>名稱</b></td>
		<td bgColor="#ccffcc" width="250"><b>說明</b></td>
                <td bgColor="#ccffcc" width="80"><b>需要熟練</b></td>
		<td bgColor="#ccffcc" width="150"><b>可習得職對</b></td>
	</tr>
	$stable
</table>
<p align=left><font color="yellow">
PS:<b>[富豪之力]</b>每回合傷害＝對手最大HP/5<BR>
每回合失去的錢＝每回合富豪之力造成的傷害ｘ１０００<BR>
當身上的金額大於２０萬才會發動<BR>
富豪之力不作用在天下武道會及神獸<BR><BR>

<b>[霸氣]</b>及覺醒之力可累加<BR><BR>

<b>[魔神爆發]</b>裝備技能名稱後有"(魔)"字,才會發動<BR><BR>

<b>[十字封印]</b>封印防護無法對十字封印作用，當兩人都安裝時，先攻者有效，只可安裝在職業奧義<BR><BR>

<b>[亡命鎖鏈]</b>每回合扣除已方１０％生命.並給于對方己方生命２０％的傷害<BR><BR>

<b>[吸血鬼之吻]</b>吸取對手的ＨＰ及ＭＰ<BR>
ＨＰ吸取＝自身(最大HP-現回合HP)/10+[0~(運+速)]<BR>
ＭＰ吸取＝自身(最大MP-現回合MP)/10+[0~(運+速)]<BR>
<BR>
<B>五階技能說明</B>
<table border="1" width="100%" id="table1" bgcolor="#FFFFFF">
	<tr>
		<td>
		<p align="center"><b>職業名稱</b></td>
		<td>
		<p align="center"><b>技能名稱</b></td>
		<td>
		<p align="center"><b>技能說明</b></td>
	</tr>
	<tr>
		<td><b>劍宗</b></td>
		<td><font color="#0000FF">三刀流(絕技)</font></td>
		<td><font color="#808000">(rand(力量)+智力+精神)x威力-對手魔防</font></td>
	</tr>
	<tr>
		<td>　</td>
		<td><font color="#0000FF">魔斬</font></td>
		<td><font color="#808000">扣除對手ＭＰ(智力/2+rand(精神x2))</font></td>
	</tr>
	<tr>
		<td><b>大法師</b></td>
		<td><font color="#0000FF">血魔大法</font></td>
		<td><font color="#808000">耗損目前1/10ＨＰ，回覆1/10最大ＨＰ的ＭＰ</font></td>
	</tr>
	<tr>
		<td>　</td>
		<td><font color="#0000FF">煉獄之火(超魔)</font></td>
		<td><font color="#808000">威力x(智力+rand(精神)+rand(運))</font></td>
	</tr>
	<tr>
		<td><b>大祭司長</b></td>
		<td><font color="#0000FF">聖杯之水</font></td>
		<td><font color="#808000">回復1/10ＨＰ及ＭＰ</font></td>
	</tr>
	<tr>
		<td>　</td>
		<td><font color="#0000FF">聖光槍(超魔)</font></td>
		<td><font color="#808000">威力x(智力+rand(精神)+rand(運))</font></td>
	</tr>
	<tr>
		<td><b>熾天使</b></td>
		<td><font color="#0000FF">熾燄之槍(絕技)</font></td>
		<td><font color="#808000">運氣+rand(運氣x威力)(無視對方防禦)</font></td>
	</tr>
	<tr>
		<td>　</td>
		<td><font color="#0000FF">熾燄亂舞(絕技)</font></td>
		<td><font color="#808000">運氣+rand(運氣x威力)(無視對方防禦)</font></td>
	</tr>
	<tr>
		<td><b>羅煞</b></td>
		<td><font color="#0000FF">奪命之眼(絕技)</font></td>
		<td><font color="#808000">失去目前所有ＭＰ，造成對方1～失去ＭＰ的傷害</font></td>
	</tr>
	<tr>
		<td>　</td>
		<td><font color="#0000FF">嗜血羅煞(絕技)</font></td>
		<td><font color="#808000">生命力+rand(運x威力)(無視對方防禦)</font></td>
	</tr>
	<tr>
		<td><b>吸血鬼</b></td>
		<td><font color="#0000FF">血之牙(絕技)</font></td>
		<td><font color="#808000">吸取(rand(精神)+速度)ＨＰ</font></td>
	</tr>
	<tr>
		<td>　</td>
		<td><font color="#0000FF">魔之牙(絕技)</font></td>
		<td><font color="#808000">吸取(rand(精神)+速度)ＭＰ</font></td>
	</tr>
</table>

EOF
&mainfooter;
exit;

