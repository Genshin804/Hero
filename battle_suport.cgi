require './battle_command.cgi';

#パラメータ等取得
sub PARA{
	#アビリティ情報
	($msk[0],$msk[1]) = split(/,/,$msk);
	($esk[0],$esk[1],$esk[2],$esk[3]) = split(/,/,$esk);
	open(IN,"./data/ability.cgi");
	@ABILITY = <IN>;
	close(IN);
        ($marmstas[0],$marmstas[1])=split(/:/,$marmsta);
        ($mprostas[0],$mprostas[1])=split(/:/,$mprosta);
        ($maccstas[0],$maccstas[1])=split(/:/,$maccsta);
        ($mpetstas[0],$mpetstas[1])=split(/:/,$mpetsta);
        ($earmstas[0],$earmstas[1])=split(/:/,$earmsta);
        ($eprostas[0],$eprostas[1])=split(/:/,$eprosta);
        ($eaccstas[0],$eaccstas[1])=split(/:/,$eaccsta);
        ($epetstas[0],$epetstas[1])=split(/:/,$epetsta);
	#武裝上的奧義總數
	$esta_eq_count=0;
	$msta_eq_count=0;
	#神之封印作用次數
	$esta_eq_disable=0;
	$msta_eq_disable=0;
	foreach(@ABILITY){
		($abno,$abname,$abcom,$abdmg,$abrate,$abpoint,$abclass,$abtype)=split(/<>/);
                 #神之必殺效果減半
                if($abno eq"75" && $god_kill eq"2"){$abdmg=35;}
		if($msk[0] eq $abno || $msk[1] eq $abno || $marmstas[0] eq $abno || $mprostas[0] eq $abno || $maccstas[0] eq $abno || $mpetstas[0] eq $abno || $marmstas[1] eq $abno || $mprostas[1] eq $abno || $maccstas[1] eq $abno || $mpetstas[1] eq $abno){
			$mab[$abtype]=1;
			$mabdmg[$abtype]=$abdmg;
			$mabname[$abno]=$abname;
			$mabtype[$abno]=$abtype;
			if($msk[0] ne $abno && $msk[1] ne $abno){
				$msta_eq_count++;
				$msta_eq[$msta_eq_count]=$abno;
			}
		}
		if($esk[0] eq $abno || $esk[1] eq $abno || $esk[2] eq $abno || $esk[3] eq $abno || $earmstas[0] eq $abno || $eprostas[0] eq $abno || $eaccstas[0] eq $abno || $epetstas[0] eq $abno || $earmstas[1] eq $abno || $eprostas[1] eq $abno || $eaccstas[1] eq $abno || $epetstas[1] eq $abno){
			$eab[$abtype]=1;
			$eabdmg[$abtype]=$abdmg;
			$eabname[$abno]=$abname;
			$eabtype[$abno]=$abtype;
			if($esk[0] ne $abno && $esk[1] ne $abno && $esk[2] ne $abno && $esk[3] ne $abno){
        	                $esta_eq_count++;
	                        $esta_eq[$esta_eq_count]=$abno;
			}
		}
	}
	#地形效果
	if($mab[19]){$tup=$mabdmg[19]/100;}
	if($eab[19]){$etup=$eabdmg[19]/100;}

	if($iflg){$tt_ele=$town2_ele;}
	else{$tt_ele=$town_ele;}

	if($tt_ele eq $mele){$maddstr=int($mstr*(0.1 + $tup));$madddef=int($mvit*(0.1 + $tup));$chi1="<font color=red>↑</font>";}
	elsif($tt_ele eq $ANELE[$mele]){$maddstr=-int($mstr*(0.1));$madddef=-int($mvit*0.1);$chi1="<font color=blue>↓</font>";}
	if($tt_ele eq $eele){$eaddstr=int($estr*(0.1 + $etup));$eadddef=int($evit*(0.1 + $etup));$chi2="<font color=red>↑</font>";}
	elsif($tt_ele eq $ANELE[$eele]){$eaddstr=-int($estr*(0.1));$eadddef=-int($evit*0.1);$chi2="<font color=blue>↓</font>";}
	
	#魔法劍
	if($mab[18]){$marmdmg+=int($mint*$mabdmg[18]/100);}
	if($eab[18]){$earmdmg+=int($eint*$eabdmg[18]/100);}
	#物理攻擊計算
	$mat=$mstr + $marmdmg + int($marmwei/5) + $maddstr + $mpetdmg;
$mat2=$mat;
	$eat=$estr + $earmdmg + int($earmwei/5) + $eaddstr + $epetdmg;
$eat2=$eat;
	
	
	#物理防御計算
	$mdef=$mvit + $mprodmg + $maccdmg + $madddef + $mpetdef;
	$edef=$evit + $eprodmg + $eaccdmg + $eadddef + $epetdef;

	#魔法防御計算
	$mmdef=int(($mfai+$mpetdef)/2);
	#if(int($msk/10) eq 4){$mmdef+=int($msklv)/10*$mmdef;}
	
	$emdef=int(($efai+$epetdef)/2);

	#クリティカル計算
	#$mcl=$marmcl;
	$mcl=20;
	$mcl+=int($mdex/3);
	$ecl=20;
	$ecl+=int($edex/3);
	if($mab[10]){$mcl+=$mabdmg[10]*10;}
	if($eab[10]){$ecl+=$eabdmg[10]*10;}
	if($mcl>250){$mcl=250;}
	if($ecl>250){$ecl=250;}

	#回避率計算
	$msh=int($mdex/3);
	$esh=int($edex/3);
	if($msh>400){$msh=400;}
	if($esh>400){$esh=400;}
	if($mab[8]){$msh2=$mabdmg[8]*10;}
	if($eab[8]){$esh2=$eabdmg[8]*10;}
	
	#攻擊回數
	$madagi=0;
	$eadagi=0;

	if($mab[4]){$madkai=$mabdmg[4];}#ヘイスト
	if($eab[4]){$eadkai=$eabdmg[4];}#ヘイスト
		
	$mspeed=$magi-$marmwei-$mprowei-$maccwei+$madagi + $madkai * 50 + $mpetspeed;
	$espeed=$eagi-$earmwei-$eprowei-$eaccwei+$eadagi + $eadkai * 50 + $epetspeed;
	
	#敵HP計算
if($eid eq $GMID){
	if ($emaxhp<$mmaxhp){$emaxhp=$mmaxhp;}
}
	$ehp=$emaxhp;
	$emp=$emaxmp;

	#富豪之力
	$mgolddmg=1;
	$egolddmg=1;

	#損血量
	$mlose_hp=0;
	$elose_hp=0;
}

#技データ取得
sub TEC_OPEN {

	open(IN,"./data/tec.cgi") or &error('檔案無法開啟(battle_suport.cgi)95。');
	@TEC = <IN>;
	close(IN);
	($mtec1,$mtec2,$mtec3,$mmprate,$mhprate)=split(/,/,$mtec);
	
	if($mtec1 eq ""){$mtec1=0;}
	if($mtec2 eq ""){$mtec2=0;}
	if($mtec3 eq ""){$mtec3=0;}

	($mtec_name[0],$mtec_str[0],$mtec_hit[0],$mtec_mp[0],$mtec_ab[0],$mtec_sta[0],$mtec_class[0]) = split(/<>/,$TEC[$mtec1]);
	($mtec_name[1],$mtec_str[1],$mtec_hit[1],$mtec_mp[1],$mtec_ab[1],$mtec_sta[1],$mtec_class[1]) = split(/<>/,$TEC[$mtec2]);
	($mtec_name[2],$mtec_str[2],$mtec_hit[2],$mtec_mp[2],$mtec_ab[2],$mtec_sta[2],$mtec_class[2]) = split(/<>/,$TEC[$mtec3]);
	
	if($estr){
		($etec1,$etec2,$etec3,$emprate,$ehprate)=split(/,/,$etec);
		if($etec1 eq ""){$etec1=0;}
		if($etec2 eq ""){$etec2=0;}
		if($etec3 eq ""){$etec3=0;}

		($etec_name[0],$etec_str[0],$etec_hit[0],$etec_mp[0],$etec_ab[0],$etec_sta[0],$etec_class[0]) = split(/<>/,$TEC[$etec1]);
		($etec_name[1],$etec_str[1],$etec_hit[1],$etec_mp[1],$etec_ab[1],$etec_sta[1],$etec_class[1]) = split(/<>/,$TEC[$etec2]);
		($etec_name[2],$etec_str[2],$etec_hit[2],$etec_mp[2],$etec_ab[2],$etec_sta[2],$etec_class[2]) = split(/<>/,$TEC[$etec3]);
	}

}


1;

