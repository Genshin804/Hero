
sub PARA{
        open(IN,"./data/ability.cgi");
        @ABILITY = <IN>;
        close(IN);

        ($esk[0],$esk[1]) = split(/,/,$esk);
        foreach(@ABILITY){
                ($abno,$abname,$abcom,$abdmg,$abrate,$abpoint,$abclass,$abtype)=split(/<>/);
                if($esk[0] eq $abno || $esk[1] eq $abno || $earmsta eq $abno || $eprosta eq $abno || $eaccsta eq $abno || $epetsta eq $abno){
                        $eab[$abtype]=1;
                        $eabdmg[$abtype]=$abdmg;
                        $eabname[$abno]=$abname;
                        $eabtype[$abno]=$abtype;
                }
        }

        $temp_unit_no=0;
	$first_kill=0;
        foreach(@unit_msk){
	        #奧義
	        ($msk[0],$msk[1]) = split(/,/,$unit_msk[$temp_unit_no]);
	        
	        foreach(@ABILITY){
	                ($abno,$abname,$abcom,$abdmg,$abrate,$abpoint,$abclass,$abtype)=split(/<>/);
	                if($msk[0] eq $abno || $msk[1] eq $abno || $unit_marmsta[$temp_unit_no] eq $abno || $unit_mprosta[$temp_unit_no] eq $abno || $unit_maccsta[$temp_unit_no] eq $abno || $unit_mpetsta[$temp_unit_no] eq $abno || $unit_marmsta2[$temp_unit_no] eq $abno || $unit_mprosta2[$temp_unit_no] eq $abno || $unit_maccsta2[$temp_unit_no] eq $abno || $unit_mpetsta2[$temp_unit_no] eq $abno){
				if($unit_mabcount[$abtype] eq ""){$unit_mabcount[$abtype]=0;}
				$unit_mabcount[$abtype]++;
				if($unit_mabcount[$abtype] eq 3){
	                	        $unit_mab[$abtype]=1;
	        	                if($unit_mabdmg[$abtype]<$abdmg){
	                        		$unit_mabdmg[$abtype]=$abdmg;
	                	        }
	        	                $unit_mabname[$abno]=$abname;
		                        $unit_mabtype[$abno]=$abtype;
		                }
			}
	        }
		$temp_unit_no++;
        }
        #地形效果
        if($unit_mab[19]){$tup=$unit_mabdmg[19]/100;}
        if($eab[19]){$etup=$eabdmg[19]/100;}

        $tt_ele=$town_ele;

        if($tt_ele eq $con_ele){$maddstr=int($mstr*(0.1 + $tup));$madddef=int($mvit*(0.1 + $tup));$chi1="<font color=red>↑</font>";}
        elsif($tt_ele eq $ANELE[$con_ele]){$maddstr=-int($mstr*(0.1));$madddef=-int($mvit*0.1);$chi1="<font color=blue>↓</font>";}

        #魔法劍
        if($unit_mab[18]){$unit_marmdmg+=int($mint*$unit_mabdmg[18]/100);}
        if($eab[18]){$earmdmg+=int($eint*$eabdmg[18]/100);}

        #物理攻擊計算
        $mat=$mstr + $unit_marmdmg + int($marmwei/5) + $maddstr + $unit_mpetdmg;
        #if($unit_mab[2]){$mat+=int($unit_mabdmg[2]/100*$mat);}#力&#12450;&#12483;&#12503;
        $eat=$estr + $earmdmg + int($earmwei/5) + $eaddstr + $epetdmg;
        #if($eab[2]){$eat+=int($eabdmg[2]/100*$eat);}#力&#12450;&#12483;&#12503;

        #if($unit_mab[3]){$eat-=int($unit_mabdmg[2]/100*$eat);}#傷害&#36605;減
        #if($eab[3]){$mat-=int($eabdmg[2]/100*$mat);}#傷害&#36605;減

        #物理防御計算
        $mdef=$mvit + $unit_mprodmg + $unit_maccdmg + $madddef + $unit_mpetdef;
        $edef=$evit + $eprodmg + $eaccdmg + $eadddef + $epetdef;

        #魔法防御計算
        $mmdef=int(($mfai+$unit_mpetdef)/2);
        if(int($msk/10) eq 4){$mmdef+=int($msklv)/10*$mmdef;}

        $emdef=int(($efai+$epetdef)/2);

        #&#12463;&#12522;&#12486;&#12451;&#12459;&#12523;計算
        #$mcl=$marmcl;
        $mcl=20;
        $mcl+=int($mdex/3);
        $ecl=20;
        $ecl+=int($edex/3);
        if($unit_mab[10]){$mcl+=$unit_mabdmg[10]*10;}
        if($eab[10]){$ecl+=$eabdmg[10]*10;}
        if($mcl>250){$mcl=250;}
        if($ecl>250){$ecl=250;}

        #回避率計算
        $msh=int($mdex/3);
        $esh=int($edex/3);
	if($msh>200){$msh=200;}
	if($esh>200){$esh=200;}
        if($unit_mab[8]){$msh2=$unit_mabdmg[8]*10;}
        if($eab[8]){$esh2=$eabdmg[8]*10;}

        #攻擊回數
        $madagi=0;
        $eadagi=0;

        if($unit_mab[4]){$madkai=$unit_mabdmg[4];}#&#12504;&#12452;&#12473;&#12488;
        if($eab[4]){$eadkai=$eabdmg[4];}#&#12504;&#12452;&#12473;&#12488;

        $mspeed=$unit_magi-$unit_marmwei-$unit_mprowei-$unit_maccwei+$unit_madagi + $unit_madkai * 50 + $unit_mpetspeed;
	$mspeed=int($mspeed/$temp_unit_no);
        $espeed=$eagi-$earmwei-$eprowei-$eaccwei+$eadagi + $eadkai * 50 + $epetspeed;

        #敵HP計算
        $ehp=$emaxhp;
        $emp=$emaxmp;
}

#技&#12487;&#12540;&#12479;取得
sub TEC_OPEN {

        open(IN,"./data/tec.cgi") or &error('檔案無法開&#25931;(battle_group.cgi)95。');
        @TEC = <IN>;
        close(IN);
        ($mtec1,$mtec2,$mtec3,$unit_mmprate,$unit_mhprate)=split(/,/,$mtec);

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

#自分的攻擊處理
sub MATT{
        if(!$mpara2){
                if($unit_mab[1]){
                        $hpsai=int($unit_mabdmg[1]/100*$unit_mmaxhp);
                        $unit_mhp+=$hpsai;
                        if($unit_mhp>$unit_mmaxhp){$unit_mhp=$unit_mmaxhp;}
                        $bmess.="[再生]$unit_name隊回復<font color=blue><b>$hpsai</b></font>HP。<BR>";
                }
                $mkai = int($mspeed/100 + rand($mspeed/100)) + 1;
                #束縛
                if($eab[45]){$mkai-=int(rand(2))-1;}
                if($mkai<1){$mkai=1;}
                if($mkai>=10){$mkai=10;}

                $bmess.="<font color=blue size=4><b>$unit_name隊</b></font>的<font color=blue size=4><b>$mkai</b></font>回攻擊！<BR>";
                if($mpara){
			if($unit_mab[42] && $unit_mabdmg[42]>int(rand(100))){
                                $bmess.="<font color=green>成功解掉身上的毒</font><BR>";
                        }else{
	                        $unit_mhpd=int(rand($unit_mmaxhp*$mpara/10));
        	                $unit_mhp-=$unit_mhpd;
                	        if($unit_mhp<=1){$unit_mhp=1;}
                        	$bmess.="<font color=red>[中毒]失去<b>$unit_mhpd</b>HP。</font><BR>";
			}
                }

                for($kou=0;$kou<$mkai;$kou++){
                        $rand=int(rand(100));$at=0;$msv=0;
                        if($unit_mhp/($unit_mmaxhp+1)*100<=$unit_mhprate){$magic=2;}
                        elsif($unit_mmp/($unit_mmaxmp+1)*100<=$unit_mmprate){$magic=1;}
                        else{$magic=0;}

                        ##技發動
                        $mpdown=$mtec_mp[$magic];
                        if($unit_mab[6]){$mpdown-=int($mtec_mp[$magic]*$unit_mabdmg[6]/100);}

                        if($unit_mab[25]){
                                $mhitup=1.5;
                        }else{
                                $mhitup=1;
                        }
                        if($mtec_hit[$magic]*$mhitup>$rand && $mpdown<=$unit_mmp){
                                $bmess.="<font color=red size=4><b>$mtec_name[$magic] </b></font>";
                                if($unit_mab[6]){$bmess.="<font color=blue><b>(消費$unit_mabdmg[6]％減輕)</b></font>";}
                                $unit_mmp-=$mpdown;
                                if($mtec_sta[$magic] eq 1){
                                        $unit_mhpup=$mtec_str[$magic] + int(rand($mfai/2));
                                        $unit_mhp+=$unit_mhpup;
                                        if($unit_mhp>$unit_mmaxhp){$unit_mhp=$unit_mmaxhp;}
                                        $bmess.="回復<font color=blue><b>$unit_mhpup</b></font>HP。<BR>";
                                }elsif($mtec_sta[$magic] eq 2){
                                        $unit_mhp+=int($unit_mmaxhp/10);
                                        $unit_mmp+=int($unit_mmaxmp/10);
                                        if($unit_mhp>$unit_mmaxhp){$unit_mhp=$unit_mmaxhp;}
                                        if($unit_mmp>$unit_mmaxmp){$unit_mmp=$unit_mmaxmp;}
                                        $bmess.="<font color=blue>ＨＰ及ＭＰ回復。</font><BR>";
                                }elsif($mtec_sta[$magic] eq 3){
                                        $mat+=int($mfai*($mtec_str[$magic]/100));
                                        $bmess.="<font color=blue>攻擊力上昇。</font><BR>";
                                }elsif($mtec_sta[$magic] eq 4){
                                        $mdef+=int($mfai*($mtec_str[$magic]/100));
                                        $bmess.="<font color=blue>耐久力上昇。</font><BR>";
                                }elsif($mtec_sta[$magic] eq 5){
                                        $mmdef+=int($mfai*($mtec_str[$magic]/100));
                                        $bmess.="<font color=blue>魔法耐久力上昇。</font><BR>";
                                }elsif($mtec_sta[$magic] eq 6){
                                        $mdmg=$mtec_str[$magic] + int(rand($mint))-int($emdef);
                                        $msv=6;
                                        $at=1;
                                }elsif($mtec_sta[$magic] eq 7){
                                        $msmp=int(rand($emaxmp)/5);
                                        $emp-=$msmp;
                                        if($emp<0){$emp=0;}
                                        $unit_mmp+=$msmp;
                                        if($unit_mmp>$unit_mmaxmp){$unit_mmp=$unit_mmaxmp;}
                                        $bmess.="$ename被吸取了<font color=red>$msmp</font>MP。<BR>";
                                }elsif($mtec_sta[$magic] eq 8){
                                        $ehp=int($ehp-$ehp/$mtec_hit[$magic]);
                                        $bmess.="$ename失去了<font color=red>$mtec_str[$magic]</font>HP。<BR>";
                                }else{
                                        $mdmg=$mtec_str[$magic] + int(rand($mint))-int($emdef);
                                        if($unit_mab[5]){
                                                $mdmg+=int($mdmg*$unit_mabdmg[5]/100);
                                                $bmess.="<font color=blue><b>(傷害+$unit_mabdmg[5]％) </b></font>";
                                        }
                                        if($eab[7]){
                                                $mdmg-=int($mdmg*$eabdmg[7]/100);
                                                $bmess.="<font color=blue><b>(傷害-$eabdmg[7]％) </b></font>";
                                        }

                                        $at=1;
                                        if($mtec_sta[$magic] eq 9){$msv=1;$at=1;}#即死
                                        if($mtec_sta[$magic] eq 10){$msv=2;$at=1;}#防御&#12480;&#12454;&#12531;
                                        if($mtec_sta[$magic] eq 11){$msv=3;$at=1;}#毒
                                        if($mtec_sta[$magic] eq 12){$msv=4;$at=1;}#命中&#12480;&#12454;&#12531;
                                        if($mtec_sta[$magic] eq 13){$msv=5;$at=1;}#麻痺
                                        if($mtec_sta[$magic] eq 14){$msv=7;$at=1;}#鈍化

                                }
                                $bmess.="<br>";
                        }else{##通常攻擊
                                $mdmg=int(rand($mat-$edef/2));
                                if($unit_mab[2]){
                                        $mdmg+=int($mdmg*$unit_mabdmg[2]/100);
                                }
                                if($eab[3]){
                                        $mdmg-=int($mdmg*$eabdmg[3]/100);
                                }
                                $at=1;
                        }
                        if($at){
                                ##回避&#12539;&#12463;&#12522;&#12486;&#12451;&#12459;&#12523;
                                $hitrand=int(rand(2));
				$tmp_efai=1200-$efai;
				if($tmp_efai<500){$tmp_efai=500;}
                                if($eab[12] && 100>int(rand($tmp_efai))){
					if($unit_mab[43] && $unit_mabdmg[43]>int(rand(100))){
	                                        $bmess.="<font color=blue size=3>$ename的反擊發動！</font>但被對方回避";
					}else{
	                                        $edmg=int(($mdmg+int(rand($estr)))/2*$eabdmg[12]);
        	                                if($edmg<1){$edmg=1;}
                	                        $unit_mhp-=$edmg;
                        	                if($unit_mhp<1){$unit_mhp=1;}
                                	        $mdmg=0;
                                        	$hitrand=0;
	                                        $bmess.="<font color=blue size=3>$ename的反擊發動！</font><BR>$unit_name隊受<font color=red size=4><b>$edmg</b></font>傷害。<br>";
					}
                                }elsif($esh>int(rand(10000))){
                                        $bmess.="<font color=blue size=3>$ename閃避了攻擊。<BR></font>";
                                        $mdmg=0;
                                        $hitrand=0;
                                }elsif($esh2>int(rand(10000))){
                                        $bmess.="<font color=blue size=3>$ename擋住了攻擊。<BR></font>";
                                        $mdmg=0;
                                        $hitrand=0;
                                }elsif($mcl>int(rand(10000)) && !$eab[44]){
                                        $bmess.="<font color=blue size=4>爆擊！</font>";
                                        $mdmg=int($mdmg*1.5);
                                        if($unit_mab[23]){
                                                $mdmg=int($mdmg*$unit_mabdmg[23]);
                                        }
                                }
                                ##傷害
                                if($mdmg<=0 && $hitrand eq 0){
                                        $mdmg=0;
					$bmess.="<BR>";
                                        #$bmess.="<font color=red>$ename</font>未受到傷害。<BR>";
                                }elsif($mdmg<=0){
                                        $mdmg=1;
                                }
                                if($mdmg){
                                        $bmess.="<font color=red>$ename</font>受到<font color=red size=4><b>$mdmg</b></font>傷
害。<BR>";
                                        if($msv eq 2){
                                                $edef-=int($edef/10);
                                                if($edef < 0){$edef=0;}
                                                $bmess.="$ename的防御力下降。<BR>";
                                        }
                                        elsif(int(rand(4)) eq 2 && $msv eq 3 || $unit_mab[14] && int(rand(6)) < 1){
                                                $epara=$unit_mabdmg[14];
                                                if(!$epara){$epara=1;}
                                                $bmess.="<font color=red>$ename中毒。</font><BR>";
                                        }
                                        elsif($msv eq 4 && $msh<1000){
                                                $msh+=40;
                                                $bmess.="<font color=red>$ename的命中率下降。</font><BR>";
                                        }
                                        elsif(int(rand(8)) eq 2 && $msv eq 5 || $unit_mab[24] && int(rand(15)) eq 1){
                                                $epara2=1;
                                                $bmess.="<font color=red>$ename麻痺。</font><BR>";
                                        }
                                        elsif($msv eq 6 || $unit_mab[28] && int(rand(4)) eq 1){
                                                $unit_mhpup=int($mdmg/2);
                                                $unit_mhp+=$unit_mhpup;
                                                if($unit_mhp>$unit_mmaxhp){$unit_mhp=$unit_mmaxhp;}
                                                $bmess.="$unit_name隊吸取了<font color=blue>$unit_mhpup</font>HP。<BR>";
                                        }
                                        elsif(int(rand(8)) eq 2 && $msv eq 7 || $unit_mab[16] && int(rand(100)) < $unit_mabdmg[16]){
                                                $espeed-=50;
                                                if($espeed<0){$espeed=0;}
                                                $bmess.="<font color=red>$ename速度下降。</font><BR>";
                                        }
                                        elsif($unit_mab[26] && int(rand(3)) eq 1){
                                                $addmg = int(rand(200));
                                                $bmess.="<font color=red size=2>追加<b>$addmg</b>的傷害。</font><BR>";
                                                $mdmg += $addmg;
                                        }
                                        elsif($unit_mab[27] && int(rand(3)) eq 1){
                                                $msmp=int(rand(150));
                                                $emp-=$msmp;
                                                if($emp<0){$emp=0;}
                                                $unit_mmp+=$msmp;
                                                if($unit_mmp>$unit_mmaxmp){$unit_mmp=$unit_mmaxmp;}
                                                $bmess.="$ename的<font color=red>$msmp</font>ＭＰ被奪走。<BR>";
                                        }
                                        elsif($unit_mab[31] && int(rand(2)) eq 1){
                                                if($eab[41] && $eabdmg[41]>int(rand(100))){
                                                        $bmess.="封印失敗！";
                                                }else{
	                                                $abrand = int(rand(2));
        	                                        $iab = $esk[$abrand];
                	                                $atype = $eabtype[$iab];
                        	                        if($eab[$atype]){
                                	                        $eab[$atype] = 0;
                                        	                #先攻、神風需要清掉威力
                                                	        if ($atype eq 15) {
                                                                $eabdmg[15]=0;
                                                        	}
	                                                        $bmess.="<font color=red>$ename的能力:$eabname[$iab]被封住了！</font><BR>";
        	                                        }
						}
                                        }

                                        if($ename ne "要塞" && int(rand(30)) eq 7 && $msv eq 1 || $ename ne "要塞" && $unit_mab[9] && int(rand(1000)) < $unit_mabdmg[9]){
                                                if($ehp<10000){
							$ehp=0;
                                                	$bmess.="<font color=red>$ename即死。</font><BR>";
						}else{
							$msv=0;
						}
                                        }
                                }
                                $ehp-=$mdmg;
                                if($maxdmg < $mdmg){$maxdmg = $mdmg;}
                        }
                        if($ehp<=0){
                                $bmess.="<BR><font color=red size=4><b>$ename倒下！</b></font><BR>";
                        }
                        if($ehp<=0 && $eab[11]  && int(rand(100)) < $eabdmg[11] && !$mhflg){
                                $ehp=int($emaxhp/2);
                                $mhflg=1;
                                $bmess.="<font color=red>$ename復活！</font><BR>";
                        }elsif($ehp<=0){
                                $ehp=0;
                                $win=1;
                        }

                        if($kou>10){&error;}
                        if($win){last;}
                }
                $bmess.="<BR>";
        }else{$bmess.="<font color=red>$unit_name隊無法行動。</font><BR>";}
        $mpara2=0;
}

#敵的攻擊處理
sub EATT{
        if(!$epara2){
                $hpsai=int($emaxhp/(int(rand(10))+5));
                $ehp+=$hpsai;
                if($ehp>$emaxhp){$ehp=$emaxhp;}
		$mmess.="[神獸的加護]$ename回復<font color=blue><b>$hpsai</b></font>HP。<BR>";
                if($eab[1]){
                        $hpsai=int($eabdmg[1]/100*$emaxhp);
                        $ehp+=$hpsai;
                        if($ehp>$emaxhp){$ehp=$emaxhp;}
                        $mmess.="[再生]$ename回復<font color=blue><b>$hpsai</b></font>HP。<BR>";
                }
                $ekai = int($espeed/100 + rand($espeed/100)) + 1;
                #束縛
                if($unit_mab[45]){$ekai-=int(rand(2))-1;}
                if($ekai<1){$ekai=1;}
                if($ekai>=12){$ekai=12;}

                $mmess.="<font color=red size=4><b>$ename</b></font>的<font color=blue size=4><b>$ekai</b></font>回攻擊！<BR>";
                if($epara){
			if($eab[42] && $eabdmg[42]>int(rand(100))){
                                $mmess.="<font color=green>成功解掉身上的毒</font>";
                        }else{
	                        $ehpd=int(rand($emaxhp*$epara)/40);
        	                $ehp-=$ehpd;
                	        if($ehp<=1){$ehp=1;}
                        	$mmess.="<font color=red>[中毒]失去<b>$ehpd</b>HP。</font><BR>";
			}
                }

                for($kou=0;$kou<$ekai;$kou++){
                        $rand=int(rand(100));$at=0;$esv=0;
                        if($ehp/($emaxhp+1)*100<=$ehprate){$magic=2;}
                        elsif($emp/($emaxmp+1)*100<=$emprate){$magic=1;}
                        else{$magic=0;}

                        ##技發動
                        $mpdown=$etec_mp[$magic];
                        if($eab[6]){$mpdown-=int($etec_mp[$magic]*$eabdmg[6]/100);}

                        if($eab[25]){
                                $ehitup=1.5;
                        }else{
                                $ehitup=1;
                        }
                        if($etec_hit[$magic]*$ehitup>$rand && $mpdown<=$emp){
                                $mmess.="<font color=red size=4><b>$etec_name[$magic] </b></font>";
                                if($eab[6]){$mmess.="<font color=blue><b>(減少$eabdmg[6]％MP耗費)</b></font>";}
                                $emp-=$mpdown;
                                if($etec_sta[$magic] eq 1){
                                        $ehpup=$etec_str[$magic] + int(rand($efai/2));
                                        $ehp+=$ehpup;
                                        if($ehp>$emaxhp){$ehp=$emaxhp;}
                                        $mmess.="回復<font color=blue><b>$ehpup</b></font>回復。<BR>";
                                }elsif($etec_sta[$magic] eq 2){
                                        $ehp+=int($emaxhp/10);
                                        $emp+=int($emaxmp/10);
                                        if($ehp>$emaxhp){$ehp=$emaxhp;}
                                        if($emp>$emaxmp){$emp=$emaxmp;}
                                        $mmess.="<font color=blue>ＨＰ與ＭＰ回復。</font><BR>";
                                }elsif($etec_sta[$magic] eq 3){
                                        $eat+=int($efai*($etec_str[$magic]/100));
                                        $mmess.="<font color=blue>攻擊力上昇。</font><BR>";
                                }elsif($etec_sta[$magic] eq 4){
                                        $edef+=int($efai*($etec_str[$magic]/100));
                                        $mmess.="<font color=blue>耐久力上昇。</font><BR>";
                                }elsif($etec_sta[$magic] eq 5){
                                        $emdef+=int($efai*($etec_str[$magic]/100));
                                        $mmess.="<font color=blue>魔法耐久力上昇。</font><BR>";
                                }elsif($etec_sta[$magic] eq 6){
                                        $edmg=$etec_str[$magic] + int(rand($eint))-int($mmdef);
                                        $esv=6;
                                        $at=1;
                                }elsif($etec_sta[$magic] eq 7){
                                        $esmp=int(rand($unit_mmaxmp)/5);
                                        $unit_mmp-=$esmp;
                                        if($unit_mmp<0){$unit_mmp=0;}
                                        $emp+=$esmp;
                                        if($emp>$emaxmp){$emp=$emaxmp;}
                                        $mmess.="$unit_name隊被吸取<font color=red><b>$esmp</b></font>MP。<BR>";
                                }elsif($etec_sta[$magic] eq 8){
                                        $unit_mhp=int($unit_mhp-$unit_mhp/$etec_hit[$magic]);
                                        $mmess.="$unit_name隊失去了$etec_str[$magic]HP。<BR>";
                                }else{
                                        $edmg=$etec_str[$magic] + int(rand($eint))-int($mmdef);
                                        if($eab[5]){
                                                $edmg+=int($edmg*$eabdmg[5]/100);
                                                $mmess.="<font color=blue><b>(傷害+$eabdmg[5]％) </b></font>";
                                        }
                                        if($unit_mab[7]){
                                                $edmg-=int($edmg*$unit_mabdmg[7]/100);
                                                $mmess.="<font color=blue><b>(傷害-$unit_mabdmg[7]％) </b></font>";
                                        }
                                        $at=1;
                                        if($etec_sta[$magic] eq 9){$esv=1;}#即死
                                        if($etec_sta[$magic] eq 10){$esv=2;}#防御&#12480;&#12454;&#12531;
                                        if($etec_sta[$magic] eq 11){$esv=3;}#毒
                                        if($etec_sta[$magic] eq 12){$esv=4;}#命中&#12480;&#12454;&#12531;
                                        if($etec_sta[$magic] eq 13){$esv=5;}#麻痺
                                        if($etec_sta[$magic] eq 14){$esv=7;}#鈍化
                                }

                                $mmess.="<br>";
                        }else{##通常攻擊
                                $edmg=int(rand($eat-$mdef/2));
                                if($eab[2]){
                                        $edmg+=int($edmg*$eabdmg[2]/100);
                                }
                                if($unit_mab[3]){
                                        $edmg-=int($edmg*$unit_mabdmg[3]/100);
                                }

                                $at=1;
                        }
                        if($at){
                                ##回避、&#12463;&#12522;&#12486;&#12451;&#12459;&#12523;
                                $hitrand=int(rand(2));
				$tmp_mfai=1200-$mfai;
				if($tmp_mfai<500){$tmp_mfai=500;}
                                if($unit_mab[12] && 100>int(rand($tmp_mfai))){
					if($eab[43] && $eabdmg[43] > int(rand(100))){
                                                $mmess.="<font color=blue size=3>$unit_name隊的反擊發動！</font>但被對方回避了。<br>";
                                        }else{
	                                        $mdmg=int(($edmg+int(rand($mstr)))/2*$unit_mabdmg[12]);
        	                                if($mdmg<1){$mdmg=1;}
                	                        $ehp-=$mdmg;
                        	                if($ehp<1){$ehp=1;}
                                	        $edmg=0;
                                        	$hitrand=0;
	                                        $mmess.="<font color=blue size=3>$unit_name隊的反擊發動！</font><BR>$ename受到<font color=red size=4><b>$mdmg</b></font>的傷害。<br>";
					}
                                }elsif($msh>int(rand(10000))){
                                        $mmess.="<font color=blue size=3>$unit_name隊閃避了攻擊。<BR></font>";
                                        $edmg=0;
                                        $hitrand=0;
                                }elsif($msh2>int(rand(10000))){
                                        $mmess.="<font color=blue size=3>$unit_name隊擋住了攻擊。<BR></font>";
                                        $edmg=0;
                                        $hitrand=0;
                                }elsif($ecl>int(rand(10000)) && !$mab[44]){
                                        $mmess.="<font color=blue size=4>爆擊！</font>";
                                        $edmg=int($edmg*1.5);
                                        if($eab[23]){
                                                $edmg=int($edmg*$eabdmg[23]);
                                        }
                                }
                                ##傷害
                                if($edmg<=0 && $hitrand eq 0){
                                        $edmg=0;
					$mmess.="<BR>";
                                        #$mmess.="<font color=blue>$unit_name隊</font>未受到傷害。<BR>";
                                }elsif($edmg<=0){
                                        $edmg=1;
                                }
                                if($edmg){
                                        $mmess.="<font color=blue>$unit_name隊</font>受到<font color=red size=4><b>$edmg</b></font>的傷害。<BR>";
                                        if($esv eq 2){
                                                $mdef-=int($mdef/10);
                                                if($mdef < 0){$mdef=0;}
                                                $mmess.="$unit_name隊的防御力下降。<BR>";
                                        }
                                        elsif(int(rand(4)) eq 2 && $esv eq 3 || $eab[14] && int(rand(6)) < 1){
                                                $mpara=$eabdmg[14];
                                                if(!$mpara){$mpara=1;}
                                                $mmess.="<font color=red>$unit_name隊中毒。</font><BR>";
                                        }
                                        elsif($esv eq 4 && $esh<1000){
                                                $esh+=40;
                                                $mmess.="<font color=red>$unit_name隊的命中率下降。</font><BR>";
                                        }
                                        elsif(int(rand(8)) eq 2 && $esv eq 5 || $eab[24] && int(rand(15)) eq 1){
                                                $mpara2=1;
                                                $mmess.="<font color=red>$unit_name隊麻痺。</font><BR>";
                                        }
                                        elsif($esv eq 6 || $eab[28] && int(rand(4)) eq 1){
                                                $ehpup=int($edmg/2);
                                                $ehp+=$ehpup;
                                                if($ehp>$emaxhp){$ehp=$emaxhp;}
                                                $mmess.="$ename吸取了<font color=blue>$ehpup</font>HP。<BR>";
                                        }
                                        elsif(int(rand(8)) eq 2 && $esv eq 7 || $eab[16] && int(rand(1000)) < $eabdmg[16]){
                                                $mspeed-=50;
                                                if($mspeed<0){$mspeed=0;}
                                                $mmess.="<font color=red>$unit_name隊速度下降。</font><BR>";
                                        }
                                        elsif(int(rand(30)) eq 7 && $esv eq 1 || $eab[9] && int(rand(1000)) < $eabdmg[9]){
                                                $unit_mhp=0;
                                                $mmess.="<font color=red>$unit_name隊即死。</font><BR>";
                                        }
                                        elsif($eab[26] && int(rand(3)) eq 1){
                                                $addmg = int(rand(200));
                                                $mmess.="追加<font color=red size=2><b>$addmg</b></font>的傷害。<BR>";
                                                $edmg += $addmg;
                                        }
                                        elsif($eab[27] && int(rand(3)) eq 1){
                                                $esmp=int(rand(150));
                                                $unit_mmp-=$esmp;
                                                if($unit_mmp<0){$unit_mmp=0;}
                                                $emp+=$esmp;
                                                if($emp>$emaxmp){$emp=$emaxmp;}
                                                $mmess.="$unit_name隊被奪走了<font color=red>$esmp</font>MP。<BR>";
                                        }
                                        elsif($eab[31] && int(rand(7)) eq 5){
                                                if($unit_mab[41] && $unit_mabdmg[41]>int(rand(100))){
                                                        $mmess.="封印失敗！";
                                                }else{
	                                                $abrand = int(rand(2));
        	                                        $iab = $msk[$abrand];
                	                                $atype = $unit_mabtype[$iab];
                        	                        if($unit_mab[$atype]){
	                                                        $unit_mab[$atype] = 0;
        	                                                #先攻、神風需要清掉威力
                	                                        if ($atype eq 15) {
                        	                                        $unit_mabdmg[15]=0;
                                	                        }
	                                                        $mmess.="<font color=red>$unit_name隊的奧義:$unit_mabname[$iab]被封住了！</font><BR>";
							}
						}
                                        }
                                }
                                $unit_mhp-=$edmg;
                        }
                        if($unit_mhp<=0){
                                $mmess.="<BR><font color=red size=4><b>$unit_name隊倒下。</b></font><BR>";
                        }
                        if($unit_mhp<=0 && $unit_mab[11]  && int(rand(100)) < $unit_mabdmg[11] && !$ehflg){
                                $unit_mhp=int($unit_mmaxhp/2);
                                $ehflg=1;
                                $mmess.="<font color=red>$unit_name隊復活！</font><BR>";
                        }elsif($unit_mhp<=0){
                                $unit_mhp=0;
                                $lose=1;
                        }
                        if($kou>12){&error("回合數出現錯誤");}
                        if($lose){last;}
                }
                $mmess.="<BR>";
        }else{$mmess.="<font color=red>$ename無法行動。</font><BR>";}
        $epara2=0;
}

#回合別戰鬥結果表示
sub BPRINT{
        print <<"EOF";
<CENTER>
<TABLE border="0" width="80%" bgcolor="#000000" CLASS=TC>
  <TBODY>
    <TR>
      <TD colspan="8" align="center" bgcolor="$FCOLOR"><B><a href="#lower"><FONT color="#ffffcc">第$turn回合</FONT></a></B></TD>
    </TR>
    <TR>
      <TD colspan="4" bgcolor="000063" align="center"><FONT color="$FCOLOR2"><B><FONT size="-1">$unit_name隊</FONT></B></FONT></TD>
      <TD colspan="4" bgcolor="9c0000" align="center"><B><FONT size="-1" color="$FCOLOR2">$ename</FONT></B></TD>
    </TR>
    <TR>
      <TD colspan="4" bgcolor="$FCOLOR2" align="center"><font size=-1>$bmess</font></TD>
      <TD colspan="4" bgcolor="$FCOLOR2" align="center"><font size=-1>$mmess</font></TD>
    </TR>
        <TR>
      <TD bgcolor="#ccffff" width=12.5%>HP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$unit_mhp/$unit_mmaxhp</TD>
      <TD bgcolor="#ccffff" width=12.5%>MP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$unit_mmp/$unit_mmaxmp</TD>
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

sub MPRINT{
        print <<"EOF";
<CENTER>
<TABLE border="0" width="80%" bgcolor="#000000" CLASS=TC>
  <TBODY>
    <TR>
      <TD colspan="8" align="center" bgcolor="$FCOLOR"><B><a href="#lower"><FONT color="#ffffcc">第$turn回合</FONT></a></B></TD>
    </TR>
    <TR>
          <TD colspan="4" bgcolor="9c0000" align="center"><B><FONT size="-1" color="$FCOLOR2">$ename</FONT></B></TD>
      <TD colspan="4" bgcolor="000063" align="center"><FONT color="$FCOLOR2"><B><FONT size="-1">$unit_name隊</FONT></B></FONT></TD>
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
      <TD bgcolor="#ccffff" width=12.5%>$unit_mhp/$unit_mmaxhp</TD>
      <TD bgcolor="#ccffff" width=12.5%>MP</TD>
      <TD bgcolor="#ccffff" width=12.5%>$unit_mmp/$unit_mmaxmp</TD>
        </TR>
  </TBODY>
</TABLE>
</CENTER>
<P>
EOF
}
1;

