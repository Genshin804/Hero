#自分的攻擊處理
sub MATT{
	if(!$mpara2){
		#自武特效
		#回合上限
		$mmaxcountadd=0;
		#戰技發動
		$mhitup2=0;
		#減戰技傷
		$mdsta=0;
		#戰鬥次數
		$mcountadd=0;
		#減物傷
		$mddmg=0;
		#必中
		$mallhit=0;
		if($marmno eq"mix" && (int(rand($mtotal+10000))>5000) && $ename ne "要塞"){
			if($marmele eq"1"){
				$ehpd=int($emaxhp/10);
                                if($ehpd>1000){$ehpd=1000;}
				if($marmele ne $mele){$ehpd=int($ehpd/2);}
				$ehp-=$ehpd;
				$bmess.="<font color=blue>$mname</font>手中的<font color=red>$marmname</font>獲得火神祝福，使用了祝融之怒，給予了<b>$ehpd</b>傷害<BR>";
			}elsif($marmele eq"2"){
				$ehpd=int($emaxhp/20);
                                if($ehp>500){$ehpd=500;}
				if($marmele ne $mele){$ehpd=int($ehpd/2);}
                                $ehp-=$ehpd;
				$mhp+=$ehpd;
                                $bmess.="<font color=blue>$mname</font>手中的<font color=red>$marmname</font>獲得水神祝福，使用了吸蝕天雨，吸收了<b>$ehpd</b>體力<BR>";

                        }elsif($marmele eq"3"){
				if($marmele eq $mele || int(rand(10))>3){
					$mcountadd+=int(rand(2)+1);
					$mmaxcountadd=$mcountadd;
					$bmess.="<font color=blue>$mname</font>手中的<font color=red>$marmname</font>獲得風神祝福，使用了極速魔音，本回合增加攻擊次數$mcountadd<BR>";
				}
                        }elsif($marmele eq"4"){
				if($marmele eq $mele || int(rand(10))>4){
					$mallhit=1;
                                	$bmess.="<font color=blue>$mname</font>手中的<font color=red>$marmname</font>獲得星神祝福，現在百發百中了<BR>";
				}
                        }elsif($marmele eq"5" && $turn % 3 eq 0){
				$tmp_safe=0;
				if($earmele eq"5" && $earmno eq"mix"){
					if($eele eq"5"){
						$tmp_safe=1;
					}elsif(int(rand(10))>4){
						$tmp_safe=1;
					}
				}
				if($tmp_safe eq 1){
                                $bmess.="<font color=blue>因雙方手中的武都受雷神的祝褔</font>，<font color=red>所以麻痺效果抵消了</font><BR>";
				}else{
					if($marmele eq $mele || int(rand(10))>4){
	                                $epara2=1;$msv=0;
        	                        $bmess.="<font color=blue>$mname</font>手中的<font color=red>$marmname</font>獲得雷神祝福，使用了天降奔雷，對手被麻痺了<BR>";
					}
				}
                        }elsif($marmele eq"6"){
                        }elsif($marmele eq"7"){
			}
		}
		#自防特效
                if($mprono eq"mix" && (int(rand($mtotal+10000))>5000) && $ename ne "要塞"){
                        if($mproele eq"1"){
                        }elsif($mproele eq"2"){
                                $ehpd=int($mmaxhp/10);
				if($ehpd>1000){$ehpd=1000;}
				if($mproele ne $mele){$ehpd=int($ehpd/2);}
                                $mhp+=$ehpd;
                                $bmess.="<font color=blue>$mname</font>身上的<font color=red>$mproname</font>獲得水神加護，使用了海洋恩惠，恢復了<b>$ehpd</b>體力<BR>";
                        }elsif($mproele eq"3"){
				if($mproele eq $mele || int(rand(10))>3){
#                                $mmaxcountadd+=1;
				$mcountadd+=1;
				$mmaxcountadd=$mcountadd;
                                $bmess.="<font color=blue>$mname</font>身上的<font color=red>$mproname</font>獲得風神加護，使用了颶風之變，本回合增加攻擊次數增1<BR>";
				}
                        }elsif($mproele eq"4"){
                        }elsif($mproele eq"5"){
                        }elsif($mproele eq"6"){
                        }elsif($mproele eq"7"){
                        }
                }
		#他自武特效
                if($earmno eq"mix" && (int(rand($etotal+10000))>5000) && $ename ne "要塞"){
                        if($earmele eq"1"){
                        }elsif($earmele eq"2"){
                        }elsif($earmele eq"3"){
                        }elsif($earmele eq"4"){
                        }elsif($earmele eq"5"){
                        }elsif($earmele eq"6"){
				if($earmele eq $eele){
                                	$mdsta+=25;
				}else{
					$mdsta+=18;
				}
                                $mmess.="<font color=blue>$ename</font>手中的<font color=red>$earmname</font>獲得光神祝福，使用了天音聖歌，增加自身戰技防禦力$mdsta%<BR>";
                        }elsif($earmele eq"7"){
				if($earmele eq $eele){
	                                $mhitup2+=0.5;
				}else{
					$mhitup2+=0.25;
				}
				$tmp_show=$mhitup2*100;
                                $bmess.="<font color=blue>$ename</font>手中的<font color=red>$earmname</font>獲得闇神祝福，使用了禁語咒殺，減少$tmp_show%戰技發動率<BR>";
                        }
                }
		#他自防特效
                if($eprono eq"mix" && (int(rand($etotal+10000))>5000) && $ename ne "要塞"){
                        if($eproele eq"1"){
                                $ehpd=int($emaxhp/10);
                                if($ehpd>1000){$ehpd=1000;}
				if($eproele ne $eele){$ehpd=int($ehpd/2);}
                                $mhp-=$ehpd;
                                $bmess.="<font color=blue>$ename</font>身上的<font color=red>$eproname</font>獲得火神加護，使用了地獄煉火，給予了<b>$ehpd</b>傷害<BR>";
                        }elsif($eproele eq"2"){
                        }elsif($eproele eq"3"){
                        }elsif($eproele eq"4"){
				if($eproele eq $eele || int(rand(10))>3){
                                $mcountadd-=1;
				$mmaxcountadd-=1;
                                $bmess.="<font color=blue>$ename</font>身上的<font color=red>$eproname</font>獲得星神加護，使用了七星連鎖，本回合減少攻擊次數一<BR>";
				}
                        }elsif($eproele eq"5"){
				if($eproele eq $eele || int(rand(10))>3){
                                $mcountadd-=1;
				$mmaxcountadd-=1;
                                $bmess.="<font color=blue>$ename</font>身上的<font color=red>$eproname</font>獲得雷神加護，使用了絕雷之牢，本回合減少攻擊次數一<BR>";
				}
                        }elsif($eproele eq"6"){
				if($eproele eq $eele){
	                                $mdsta+=50;
				}else{
					$mdsta+=25;
				}
                                $mmess.="<font color=blue>$ename</font>身上的<font color=red>$eproname</font>獲得光神加護，使用了天使護環，增加自身戰技防禦力$mdsta%<BR>";
                        }elsif($eproele eq"7"){
				if($eproele eq $eele){
                                	$mddmg+=20;
				}else{
					$mddmg+=10;
				}
                                $bmess.="<font color=blue>$ename</font>身上的<font color=red>$eproname</font>獲得闇神祝福，使用了黑洞嗜咒，減少$mddmg%物理傷害<BR>";
                        }
                }
                if($ehp<=1){$ehp=1;}
                if($mhp>$mmaxhp){$mhp=$mmaxhp;}
		if($mhp<=1){$mhp=1;}
		if($mab[1]){
			$hpsai=int($mabdmg[1]/100*$mmaxhp);
			$mhp+=$hpsai;
			if($mhp>$mmaxhp){$mhp=$mmaxhp;}
			$bmess.="[再生]$mname回復<font color=blue><b>$hpsai</b></font>HP。<BR>";
		}
		if($mab[54]){
			$smhp=$mhp;
			$mhp_tmp=int($smhp*0.1);
			$bmess.="<font color=red><b>[亡命鎖鏈]自身扣血$mhp_tmp</b></font><BR>";
			$mhp-=$mhp_tmp;
                        $mhp_tmp=int($smhp*0.2);
                        $bmess.="<font color=red><b>[亡命鎖鏈]$ename扣血$mhp_tmp</b></font><BR>";
			$ehp-=$mhp_tmp;
			if($ehp<1){$ehp=1;}
		}
                if($mab[55]){
                        $mhp_tmp=int(($mmaxhp-$mhp)/$mabdmg[55])+int(rand($mdex+$magi));
                        $mmp_tmp=int(($mmaxmp-$mmp)/$mabdmg[55])+int(rand($mdex+$magi));
                        if($mhp_tmp>=$ehp){$mhp_tmp=$ehp-1;}
                        if($mmp_tmp>$emp){$mmp_tmp=$emp-1;}
			if($emp eq"0"){$mmp_tmp=0;}
                        $mhp+=$mhp_tmp;
                        $ehp-=$mhp_tmp;
			$mmp+=$mmp_tmp;
			$emp-=$mmp_tmp;
			if($mhp>$mmaxhp){$mhp=$mmaxhp;}
			if($mmp>$mmaxmp){$mmp=$mmaxmp;}
                        $bmess.="<font color=blue><b>[吸血鬼之吻]吸收對方$mhp_tmpＨＰ、$mmp_tmpＭＰ<BR>";
                }
		if($mhp<=1){$mhp=1;}
		$mkai = int($mspeed/100 + rand($mspeed/100)) + 1;
                $mkai += $mcountadd;
		if($mkai>=(10+$mmaxcountadd)){$mkai=10+$mmaxcountadd;}
		if($mab[53]){$mkai+=$mabdmg[53];}
                #束縛
                if($eab[45]){$mkai-=(int(rand(2))+1);}

		if($mkai<1){$mkai=1;}	
		$bmess.="<font color=blue size=4><b>$mname</b></font>的<font color=blue size=4><b>$mkai</b></font>回攻擊！<BR>";
		if($mpara){
                        if($mab[1]){$tmp_rand=200;}else{$tmp_rand=100;}
                        if($mab[42] && $mabdmg[42]>int(rand($tmp_rand))){
                                $bmess.="<font color=green>成功解掉身上的毒</font><BR>";
                        }else{
                                if($mab[1]){
					$mabdmg_tmp=int($mabdmg[1]/5);
                                        $mabdmg[1]-=int($mpara*5);
                                        if ($mabdmg[1]<0){
                                                $mabdmg[1]=0;
                                        }
                                        if("$mabdmg[1]" eq"0"){
                                                $mab[1]=0;
					}
					$mpara-=$mabdmg_tmp;
                                        if($mpara<0){$mpara=0;}
                                        $eab[14]=0;
                                        $eabdmg[14]=0;
                                        $bmess.="<font color=red>[中毒]毒性與身上的再生技進行中合，再生降為$mabdmg[1]％。</font><BR>";
                                }else{
                                        $mhpd=int(rand($mmaxhp*$mpara/10));
                                        if($mhpd>5000){$mhpd=5000;}
                                        $mhp-=$mhpd;$mlose_hp+=$mhpd;
                                        if($mhp<=1){$mhp=1;}
                                        $bmess.="<font color=red>[中毒]失去<b>$mhpd</b>HP。</font><BR>";
                                }
                        }
		}
		#富豪之力
		if($mab[46] && $mgolddmg){
			$ehpd=int($ehpmax/5);
			$mgoldlose=$ehpd*1000;
			if($mgold>=$mgoldlose){
				$mgold-=$mgoldlose;
				$ehp-=$ehpd;$elose_hp+=$ehpd;
				if($ehp<1){$ehp=1;}
				$bmess.="<font color=red size=3>$mname將$mgoldlose Gold丟到$ename的臉上，造成$ehpd傷害及心靈上的創傷！</font><BR>";
			}
		}
		for($kou=0;$kou<$mkai;$kou++){
			$rand=int(rand(100));$at=0;$msv=0;
			if($mhp/($mmaxhp+1)*100<=$mhprate){$magic=2;}
			elsif($mmp/($mmaxmp+1)*100<=$mmprate){$magic=1;}
			else{$magic=0;}

			##技發動
			$mpdown=$mtec_mp[$magic];
			if($mab[6]){$mpdown-=int($mtec_mp[$magic]*$mabdmg[6]/100);}

			if($mab[25]){
				$mhitup=1.5;
			}else{
				$mhitup=1;
			}
			if($mtec_hit[$magic]*($mhitup-$mhitup2)>$rand && $mpdown<=$mmp){
				$bmess.="<font color=red size=4><b>$mtec_name[$magic] </b></font>";
				if($mab[6]){$bmess.="<font color=blue><b>(消費$mabdmg[6]％減輕)</b></font>";}
				$mmp-=$mpdown;
				if($mtec_sta[$magic] eq 1){
					$mhpup=$mtec_str[$magic] + int(rand($mfai/2));
					$mhp+=$mhpup;
					if($mhp>$mmaxhp){$mhp=$mmaxhp;}
					$bmess.="回復<font color=blue><b>$mhpup</b></font>HP。<BR>";
				}elsif($mtec_sta[$magic] eq 2){
					$tmp_hp=int($mmaxhp/10);
					$tmp_mp=int($mmaxmp/10);
					$mhp+=$tmp_hp;
					$mmp+=$tmp_mp;
					if($mhp>$mmaxhp){$tmp_hp=$tmp_hp-$mhp+$mmaxhp;$mhp=$mmaxhp;}
					if($mmp>$mmaxmp){$tmp_mp=$tmp_mp-$mmp+$mmaxmp;$mmp=$mmaxmp;}
					$bmess.="<font color=blue>$tmp_hpＨＰ及$tmp_mpＭＰ回復。</font><BR>";
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
					if($msmp>800){$msmp=800;}
					$emp-=$msmp;
					if($emp<0){$emp=0;}
					$mmp+=$msmp;
					if($mmp>$mmaxmp){$mmp=$mmaxmp;}
					$bmess.="$ename被吸取了<font color=red>$msmp</font>MP。<BR>";
				}elsif($mtec_sta[$magic] eq 8){
                                        $ehpd=int($ehp/$mtec_str[$magic]);
                                        $ehp-=$ehpd;$elose_hp+=$ehpd;
                                        $bmess.="$ename失去了$ehpd HP。<BR>";
				}elsif($mtec_sta[$magic] eq 18){
					$tmp_hp=int($mhp/10);
					$tmp_maxhp=int($mmaxhp/10);
					$mhp-=$tmp_hp;
					$mmp+=$tmp_maxhp;
					if($mmp>$mmaxmp){$mmp=$mmaxmp;}
					$bmess.="<font color=red>失去$tmp_hpＨＰ</font>、<font color=blue>增加$tmp_maxhpＭＰ。</font><BR>";
                                }elsif($mtec_sta[$magic] eq 20){
                                        $tmp_mp=int(rand($mmp));
                                        $ehp-=$tmp_mp;
					$mmp=0;
                                        if($ehp<1){$ehp=0;}
                                        $bmess.="$ename<font color=red>失去$tmp_mpＨＰ</font><BR>";
                                }elsif($mtec_sta[$magic] eq 22){
					$tmp_hp=int(rand($mfai)+$magi);
					$mhp+=$tmp_hp;
					$ehp-=$tmp_hp;
					if($mhp>$mmaxhp){$mhp=$mmaxhp;}
					if($ehp<1){$ehp=1;}
                                        $bmess.="$ename被吸取了<font color=red>$tmp_hp</font>ＨＰ。<BR>";
                                }elsif($mtec_sta[$magic] eq 23){
                                        $tmp_mp=int(rand($mfai)+$magi);
                                        $mmp+=$tmp_mp;
                                        $emp-=$tmp_mp;
                                        if($mmp>$mmaxmp){$mmp=$mmaxmp;}
                                        if($emp<1){$emp=0;}
                                        $bmess.="$ename被吸取了<font color=red>$tmp_mp</font>ＭＰ。<BR>";
                                }elsif($mtec_sta[$magic] eq 24){
					$tmp_mp=int($mint/2+rand($mfai*2));
					$emp-=$tmp_mp;
					if($emp<1){$emp=0;}
                                        $bmess.="$emane<font color=red>失去$tmp_mpＭＰ</font><BR>";
				}else{
$at=1;
					if($mtec_sta[$magic] eq 15){
						$mdmg=$mtec_str[$magic]*(int(rand($mstr))+$mint)-int($emdef);
$at=2;
					}elsif($mtec_sta[$magic] eq 16){
						$mdmg=$mtec_str[$magic]+(int(rand($mfai))+$mint)-int($emdef);
$at=2;
                                        }elsif($mtec_sta[$magic] eq 17){
                                                $mdmg=($mint+int(rand($mfai))+int(rand($mdex)))*$mtec_str[$magic]-int($emdef);
$at=2;
                                        }elsif($mtec_sta[$magic] eq 19){
						$mdmg=$mdex+int(rand($mdex*$mtec_str[$magic]));
$at=2;
                                        }elsif($mtec_sta[$magic] eq 21){
						$mdmg=$mvit+int(rand($mdex*$mtec_str[$magic]));
$at=2;
					}else{
	                                        $mdmg=$mtec_str[$magic] + int(rand($mint)) -int($emdef);
					}
					if($mab[51] && ($mtec_sta[$magic] eq 16 || $mtec_sta[$magic] eq 17)){
						$mdmg*=2;
                                                $bmess.="<font color=blue><b>(傷害x２) </b></font>";
					}
					if($mtec_str[$magic]<1000){
						$mdmg+=int(($mint+$mfai)*$mtec_str[$magic]/4000);
					}else{
						$mdmg+=int(($mint+$mfai)/4);
					}
					if($mab[5]){
						$mdmg+=int($mdmg*$mabdmg[5]/100);
						$bmess.="<font color=blue><b>(傷害+$mabdmg[5]％) </b></font>";
					}
					if($eab[7]){
						$mdmg-=int($mdmg*$eabdmg[7]/100);
						$bmess.="<font color=blue><b>(傷害-$eabdmg[7]％) </b></font>";
					}
					if($mdsta>1){
					        $mdmg-=int($mdmg*$mdsta/100);
                                                $bmess.="<font color=blue><b>(傷害-$mdsta％) </b></font>";
					}
					if($mtec_sta[$magic] eq 9 && $turn > 1){$msv=1;$at=1;}#即死
					if($mtec_sta[$magic] eq 10){$msv=2;$at=1;}#防御ダウン
					if($mtec_sta[$magic] eq 11){$msv=3;$at=1;}#毒
					if($mtec_sta[$magic] eq 12){$msv=4;$at=1;}#命中ダウン
					if($mtec_sta[$magic] eq 13){$msv=5;$at=1;}#麻痺
					if($mtec_sta[$magic] eq 14){$msv=7;$at=1;}#鈍化
					
				}
				$bmess.="<br>";
			}else{##通常攻擊
				$mdmg=int(rand($mat-$edef/2));
				if($mab[47] || $mab[50]){
					$tmp_dmg=$mabdmg[47] + $mabdmg[50];
					$mdmg+=int($mdmg*$tmp_dmg*$turn/100);
				}	
                                if($mab[2]){
                                        $mdmg+=int($mdmg*$mabdmg[2]/100);
                                }
                                if($eab[3]){
#$dddd=int($mdmg*$eabdmg[3]/100);
#$bmess.="(物防效果$eabdmg[3]%,原傷害$mdmg,減傷效果$dddd)";
                                        $mdmg-=int($mdmg*$eabdmg[3]/100);
                                }
                                if($mddmg>0){
                                        $mdmg-=int($mdmg*$mddmg/100);
                                }
				$at=1;
			}
			if($at){
				##回避・クリティカル
				$hitrand=int(rand(2));
				if($at eq 1){
				$tmp_speed=$espeed-$mspeed;
				if($tmp_speed>400){$tmp_speed=400;}
				$tmp_efai=1200-$efai;
				if($tmp_efai<500){$tmp_efai=500;}
                                $tmp_esh=$esh;
                                if($mab[56]){
					$tmp_esh=int($tmp_esh/$mabdmg[56]);
					$tmp_speed=int($tmp_speed/$mabdmg[56]);
				}
				if($eab[12] && 100>int(rand($tmp_efai))){
					if($mab[43] && $mabdmg[43]>int(rand(100))){
                                                $bmess.="<font color=blue size=3>$ename的反擊發動！</font>，但被對方回避了<BR>";
                                        }else{
						$edmg=int(($mdmg+int(rand($estr)))/2*$eabdmg[12]);
						if($edmg<1){$edmg=1;}
						$mhp-=$edmg;$mlose_hp+=$edmg;
						if($mhp<1){$mhp=1;}
						$mdmg=0;
						$hitrand=0;
						$bmess.="<font color=blue size=3>$ename的反擊發動！</font><BR>$mname受<font color=red size=4><b>$edmg</b></font>傷害。<BR>";
					}
				}elsif($tmp_esh>int(rand(1000)) && $mallhit eq 0){
					$bmess.="<font color=blue size=3>$ename閃避了攻擊。<BR></font>";
					$mdmg=0;
					$hitrand=0;
				}elsif($esh2>int(rand(1000))){
					$bmess.="<font color=blue size=3>$ename擋住了攻擊。<BR></font>";
					$mdmg=0;
					$hitrand=0;
				}elsif($mcl>int(rand(1000)) && !$eab[44]){
					$bmess.="<font color=blue size=4>爆擊！</font>";
					$mdmg=int($mdmg*1.5);
					if($mab[23]){
						$mdmg=int($mdmg*$mabdmg[23]);
					}
					if($mdmg<=0 && $hitrand eq 0){
						$bmess.="<font color=red>$ename</font>未受到傷害。<BR>";
					}
				}elsif($tmp_speed>int(rand(1000)) && $mallhit eq 0){
					$bmess.="<font color=green size=3>$ename躲避了攻擊。<BR></font>";
                                        $mdmg=0;
                                        $hitrand=0;
				}
                              }elsif($mcl>int(rand(1500)) && !$eab[44]){ #at=2
                                      $bmess.="<font color=blue size=4>爆擊！</font>";
                                      $mdmg=int($mdmg*1.5);
                                      if($mab[23]){
                                              $mdmg=int($mdmg*$mabdmg[23]);
                                      }
                                      if($mdmg<=0 && $hitrand eq 0){
                                              $bmess.="<font color=red>$ename</font>未受到傷害。<BR>";
                                      }
				} #at=2
				#elsif($mdmg<=0){
			#		$bmess.="<font color=red>$ename</font>未受到傷害。<BR>";
				#}
				##傷害
				if($mdmg<=0 && $hitrand eq 0){
					$mdmg=0;
					#$bmess.="<BR>";
					$bmess.="<font color=red>$ename</font>未受到傷害。<BR>";
				}elsif($mdmg<=0){
					$mdmg=1;
				}
				if($mdmg){
					$bmess.="<font color=red>$ename</font>受到<font color=red size=4><b>$mdmg</b></font>傷害。<BR>";
					if($msv eq 2){
						$edef-=int($edef/10);
						if($edef < 0){$edef=0;}
						$bmess.="$ename的防御力下降。<BR>";
					}
					elsif(int(rand(4)) eq 2 && $msv eq 3 || $mab[14] && int(rand(6)) < 1){
						$epara=$mabdmg[14];
						if(!$epara){$epara=1;}
						$bmess.="<font color=red>$ename中毒。</font><BR>";
					}
					elsif($msv eq 4 && $msh<1000 && int(rand(3)) eq 1){
						$msh+=40;
						$bmess.="<font color=red>$ename的命中率下降。</font><BR>";
					}
					elsif(int(rand(8)) eq 2 && $msv eq 5 || $mab[24] && int(rand(15)) eq 1){
						$epara2=1;
						$msv=0;
						$bmess.="<font color=red>$ename麻痺。</font><BR>";
					}
					elsif($msv eq 6 || $mab[28] && int(rand(4)) eq 1){
						$mhpup=int($mdmg/2);
						$mhp+=$mhpup;
						if($mhp>$mmaxhp){$mhp=$mmaxhp;}
						$bmess.="$mname吸取了<font color=blue>$mhpup</font>HP。<BR>";
					}
					elsif(int(rand(8)) eq 2 && $msv eq 7 || $mab[16] && int(rand(100)) < $mabdmg[16]){
						$espeed-=50;
						if($espeed<0){$espeed=0;}
						$bmess.="<font color=red>$ename速度下降。</font><BR>";
					}
					elsif($mab[26] && int(rand(3)) eq 1){
						$addmg = int(rand(200));
						$bmess.="<font color=red size=2>追加<b>$addmg</b>的傷害。</font><BR>";
						$mdmg += $addmg;
					}
					elsif($mab[27] && int(rand(3)) eq 1){
						$msmp=int(rand(150));
						$emp-=$msmp;
						if($emp<0){$emp=0;}
						$mmp+=$msmp;
						if($mmp>$mmaxmp){$mmp=$mmaxmp;}
						$bmess.="$ename的<font color=red>$msmp</font>ＭＰ被奪走。<BR>";
					}elsif($mab[57] && int(rand(2)) eq 1 && $msta_eq_disable<2 && $esta_eq_count>0){
						if($msta_eq_disable eq 0){
							$abrand=int(rand($esta_eq_count))+1;
							$iab = $esta_eq[$abrand];
							$atype = $eabtype[$iab];
							$eab[$atype]=0;
							$eabdmg[$atype]=0;
							$mab[57]=int(rand(2));
							$mabdmg[57]=$mab[57];
							$msta_eq_disable++;
                                                        $bmess.="<font color=red>[神之封印]$ename的奧義:$eabname[$iab]被封住了！</font><BR>";
						}elsif($msta_eq_disable eq 1){
							$mab[57]=0;
							$mabdmg[57]=0;
							$msta_eq_disable++;
							if($eab[41]){
	                                                        $bmess.="因封印防護作用，神之封印失敗！";
							}elsif(int(rand(2)) eq 1){
		                                                $abrand=int(rand($esta_eq_count))+1;
                	                                        $iab = $esta_eq[$abrand];
                        	                                $atype = $eabtype[$iab];
                                	                        $eab[$atype]=0;
                                        	                $eabdmg[$atype]=0;
        	                                                $bmess.="<font color=red>[神之封印]$ename的能力:$eabname[$iab]被封住了！</font><BR>";

							}else{
                                                                $bmess.="第二次神之封印發動失敗！";
							}
						}
					}elsif($mab[31] && int(rand(2)) eq 1 || $mab[52]){
                                                if(($eab[41] || $eabdmg[41]>int(rand(100))) && !$mab[52]){
                                                        $bmess.="封印失敗！";
                                                }else{
                                                $abrand = int(rand(2));
                                                $iab = $esk[$abrand];
                                                $atype = $eabtype[$iab];
if($atype ne 11){
                                                if($eab[$atype]){
                                                        $eab[$atype] = 0;
                                                        $eabdmg[$atype]=0;
                                                        $bmess.="<font color=red>$ename的能力:$eabname[$iab]被封住了！</font><BR>";
                                                }
                                                }
}
					}

					if(($ename ne "要塞" && int(rand(30)) eq 7 && $msv eq 1 || $ename ne "要塞" && $mab[9] && int(rand(1000)) < $mabdmg[9]) && $turn>1){
						if($eab[40] && $eabdmg[40]>int(rand(100))){
							$msv=0;
							$bmess.="<font color=red>不死鳥保護住$ename。</font><BR>";
						}elsif($eab[49] && $eabdmg[49]>int(rand(100))){
							$mhp=1;
                                                        $bmess.="<font color=red>$mname對死神使出即死，但死神將即死回報給對方。</font><BR>";
						}elsif($eab[49]){
							$msv=0;
							$bmess.="<font color=red>死神保護住$ename。</font><BR>";
						}else{
							$ehp=0;
							$bmess.="<font color=red>$ename即死。</font><BR>";
						}
					}
				}
				$ehp-=$mdmg;$elose_hp+=$mdmg;
				if($maxdmg < $mdmg){$maxdmg = $mdmg;}
			}
			if($ehp<=0){
				$bmess.="<BR><font color=red size=4><b>$ename倒下！</b></font><BR>";
			}
			if($ehp<=0 && $eab[11]  && int(rand(100)) < $eabdmg[11] && !$mhflg){
				$ehp=int($emaxhp/2);
				if($eabdmg[11] eq"100"){$ehp=$ehp*2;}
				if ($eabdmg[11]<100){$mhflg=1;}
				$bmess.="<font color=red>$ename復活！</font><BR>";
			}elsif($ehp<=0){
				$ehp=0;
				$win=1;
			}
		
			if($kou>20){&error;}
			if($win){last;}
		}
		$bmess.="<BR>";
	}else{
		$bmess.="<font color=red>$mname無法行動。</font><BR>";
	}
	$mpara2=0;
	}

#敵的攻擊處理
sub EATT{
	if(!$epara2){
                #自武特效
                $emaxcountadd=0;
                $ehitup2=0;
		$ecountadd=0;
		$edsta=0;
		$eddmg=0;
		$eallhit=0;
		if($ename eq"要塞"){
			$mhp-=$eadd_dmg;
			if($eadd_dmg>0){
				$mmess.="<font color=red>箭塔傷害$eadd_dmg</font>";
			}
		}
                if($earmno eq"mix" && (int(rand($etotal+10000))>5000)){
                        if($earmele eq"1"){
                                $mhpd=int($mmaxhp/10);
                                if($mhpd>1000){$mhpd=1000;}
				if($earmele ne $eele){$mhpd=int($mhpd/2);}
                                $mhp-=$mhpd;
                                $mmess.="<font color=blue>$ename</font>手中的<font color=red>$earmname</font>獲得火神祝福，使用了祝融之怒，給予了<b>$mhpd</b>傷害<BR>";
                        }elsif($earmele eq"2"){
                                $mhpd=int($mmaxhp/20);
                                if($mhpd>500){$mhpd=500;}
				if($earmele ne $eele){$mhpd=int($mhpd/2);}
                                $mhp-=$mhpd;
                                $ehp+=$mhpd;
                                $mmess.="<font color=blue>$ename</font>手中的<font color=red>$earmname</font>獲得水神祝福，使用了吸蝕天雨，吸收了<b>$mhpd</b>ＨＰ<BR>";
                        }elsif($earmele eq"3"){
				if($earmele eq $eele || int(rand(10))>3){
                                $ecountadd+=int(rand(2)+1);
				$emaxcountadd=$ecountadd;
                                $mmess.="<font color=blue>$ename</font>手中的<font color=red>$earmname</font>獲得風神祝福，使用了極速魔音，本回合增加攻擊次數$ecountadd<BR>";
				}
                        }elsif($earmele eq"4"){
				if($earmele eq $eele || int(rand(10))>4){
                                $eallhit=1;
                                $mmess.="<font color=blue>$ename</font>手中的<font color=red>$earmname</font>獲得星神祝福，現在百發百中了<BR>";
				}
                        }elsif($earmele eq"5" && $turn % 3 eq 0){
                                $tmp_safe=0;
                                if($marmele eq"5" && $marmno eq"mix"){
                                        if($mele eq"5"){
                                                $tmp_safe=1;
                                        }elsif(int(rand(10))>4){
                                                $tmp_safe=1;
                                        }
                                }
                                if($tmp_safe eq 1){
					$mmess.="<font color=blue>因雙方手中的武都受雷神的祝褔</font>，<font color=red>所以麻痺效果抵消了</font><BR>";
				}else{
					if($earmele eq $eele || int(rand(10))>4){
        	                        $mpara2=1;
	                                $mmess.="<font color=blue>$ename</font>手中的<font color=red>$earmname</font>獲得雷神祝福，使用了天降奔雷，對手被麻痺了<BR>";
					}
				}
                        }elsif($earmele eq"6"){
                        }elsif($earmele eq"7"){
                        }
                }
                #自防特效
                if($eprono eq"mix" && (int(rand($etotal+10000))>5000)){
                        if($eproele eq"1"){
                        }elsif($eproele eq"2"){
                                $mhpd=int($mmaxhp/10);
				if($mhpd>1000){$mhpd=1000;}
				if($eproele ne eele){$mhpd=int($mhpd/2);}
                                $ehp+=$mhpd;
                                $mmess.="<font color=blue>$ename</font>身上的<font color=red>$eproname</font>獲得水神加護，使用了海洋恩惠，恢復了<b>$mhpd</b>體力<BR>";
                        }elsif($eproele eq"3"){
				if($eproele eq $eele || int(rand(10))>3){
#                                $emaxcountadd+=1;
				$ecountadd+=1;
				$emaxcountadd=$ecountadd;
                                $mmess.="<font color=blue>$ename</font>身上的<font color=red>$eproname</font>獲得風神加護，使用了颶風之變，本回合增加攻擊次數1<BR>";
				}
                        }elsif($eproele eq"4"){
                        }elsif($eproele eq"5"){
                        }elsif($eproele eq"6"){
                        }elsif($eproele eq"7"){
                        }
                }
                #他自武特效
                if($marmno eq"mix" && (int(rand($mtotal+10000))>5000)){
                        if($marmele eq"1"){
                        }elsif($marmele eq"2"){
                        }elsif($marmele eq"3"){
                        }elsif($marmele eq"4"){
                        }elsif($marmele eq"5"){
                        }elsif($marmele eq"6"){
				if($marmele eq $mele){
                                	$edsta+=25;
				}else{
					$edsta+=18;
				}
                                $bmess.="<font color=blue>$mname</font>手中的<font color=red>$marmname</font>獲得光神祝福，使用了天音聖歌，增加自身戰技防禦力$edsta%<BR>";
                        }elsif($marmele eq"7"){
				if($marmele eq $mele){
                                	$ehitup2+=0.5;
				}else{
					$ehitup2+=0.25;
				}
				$tmp_show=$ehitup2*100;
                                $mmess.="<font color=blue>$mname</font>手中的<font color=red>$marmname</font>獲得闇神祝福，使用了禁語咒殺，減少$tmp_show%戰技發動率<BR>";
                        }
                }
                #他自防特效
                if($mprono eq"mix" && (int(rand($mtotal+10000))>5000)){
                        if($mproele eq"1"){
                                $mhpd=int($emaxhp/10);
                                if($mhpd>1000){$mhpd=1000;}
				if($mproele ne $mele){$mhpd=int($mhpd/2);}
                                $ehp-=$mhpd;
                                $mmess.="<font color=blue>$mname</font>身上的<font color=red>$mproname</font>獲得火神加護，使用了地獄煉火，給予了<b>$mhpd</b>傷害<BR>";
                        }elsif($mproele eq"2"){
                        }elsif($mproele eq"3"){
                        }elsif($mproele eq"4"){
				if($mproele eq $mele || int(rand(10))>4){
                                $ecountadd-=1;
				$emaxcountadd-=1;
                                $mmess.="<font color=blue>$mname</font>身上的<font color=red>$mproname</font>獲得星神加護，使用了七星連鎖，本回合減少攻擊次數一１<BR>";
				}
                        }elsif($mproele eq"5"){
				if($mproele eq $mele || int(rand(10))>3){
                                $ecountadd-=1;
				$emaxcountadd-=1;
                                $mmess.="<font color=blue>$mname</font>身上的<font color=red>$mproname</font>獲得雷神加護，使用了絕雷之牢，本回合減少攻擊次數一<BR>";
				}

                        }elsif($mproele eq"6"){
				if($mproele eq $mele){
                                	$edsta+=50;
				}else{
					$edsta+=25;
				}
                                $bmess.="<font color=blue>$mname</font>身上的<font color=red>$mproname</font>獲得光神加護，使用了天使護環，增加自身戰技防禦力$edsta%<BR>";
                        }elsif($mproele eq"7"){
				if($mproele eq $mele){
	                                $eddmg+=20;
				}else{
					$eddmg+=10;
				}
                                $mmess.="<font color=blue>$mname</font>身上的<font color=red>$mproname</font>獲得闇神祝福，使用了黑洞嗜咒，減少$eddmg%物理傷害<BR>";
                        }
                }
                if($ehp<=1){$ehp=1;}
                if($ehp>$emaxhp){$ehp=$emaxhp;}
                if($mhp<=1){$mhp=1;}
		if($eab[1]){
			$hpsai=int($eabdmg[1]/100*$emaxhp);
			$ehp+=$hpsai;
			if($ehp>$emaxhp){$ehp=$emaxhp;}
			$mmess.="[再生]$ename回復<font color=blue><b>$hpsai</b></font>HP。<BR>";
		}
                if($eab[54]){
			$sehp=$ehp;
                        $ehp_tmp=int($sehp*0.1);
                        $mmess.="<font color=red><b>[亡命鎖鏈]自身扣血$ehp_tmp</b></font><BR>";
                        $ehp-=$ehp_tmp;
                        $ehp_tmp=int($sehp*0.2);
                        $mmess.="<font color=red><b>[亡命鎖鏈]$mname扣血$ehp_tmp</b></font><BR>";
                        $mhp-=$ehp_tmp;
			if($mhp<1){$mhp=1;}
                }
		if($eab[55]){
			$ehp_tmp=int(($emaxhp-$ehp)/$eabdmg[55])+int(rand($edex+$eagi));
                        $emp_tmp=int(($emaxmp-$emp)/$eabdmg[55])+int(rand($edex+$eagi));
                        if($ehp_tmp>=$mhp){$ehp_tmp=$mhp-1;}
                        if($emp_tmp>$mmp){$emp_tmp=$mmp-1;}
			if($mmp eq"0"){$emp_tmp=0;}
                        $ehp+=$ehp_tmp;
                        $mhp-=$ehp_tmp;
                        $emp+=$emp_tmp;
                        $mmp-=$emp_tmp;
                        if($ehp>$emaxhp){$ehp=$emaxhp;}
                        if($emp>$emaxmp){$emp=$emaxmp;}
			$mmess.="<font color=blue><b>[吸血鬼之吻]吸收對方$ehp_tmpＨＰ、$emp_tmpＭＰ<BR>";
		}
                if($ehp<=1){$ehp=1;}
		$ekai = int($espeed/100 + rand($espeed/100)) + 1;
                $ekai += $ecountadd;
		if($ekai>=(10+$emaxcountadd)){$ekai=10+$emaxcountadd;}
		if($eab[53]){$ekai+=$eabdmg[53];}
                #束縛
                if($mab[45]){$ekai-=(int(rand(2))+1);}

		if($ekai<1){$ekai=1;}
		$mmess.="<font color=red size=4><b>$ename</b></font>的<font color=blue size=4><b>$ekai</b></font>回攻擊！<BR>";
		if($epara){
                        if($eab[1]){$tmp_rand=200;}else{$tmp_rand=100;}
                        if($eab[42] && $eabdmg[42]>int(rand($tmp_rand))){
                                $mmess.="<font color=green>成功解掉身上的毒</font><BR>";
                        }else{
                                if($eab[1]){
					$eabdmg_tmp=int($eabdmg[1]/5);
                                        $eabdmg[1]-=int($epara*5);
                                        if ($eabdmg[1]<0){
                                                $eabdmg[1]=0;
                                        }
                                        if("$eabdmg[1]" eq"0"){
                                                $eab[1]=0;
                                        }
					$epara-=$eabdmg_tmp;
					if($epara<0){$epara=0};
                                        $mab[14]=0;
                                        $mabdmg[14]=0;
                                        $mmess.="<font color=red>[中毒]毒性與身上的再生技進行中合，再生降為$eabdmg[1]％。</font><BR>";
                                }else{
                                        $ehpd=int(rand($emaxhp*$epara/10));
                                        if($ehpd>5000){$ehpd=5000;}
                                        $ehp-=$ehpd;$elose_hp+=$ehpd;
				if($ehp<=1){$ehp=1;}
				$mmess.="<font color=red>[中毒]失去<b>$ehpd</b>HP。</font><BR>";
			}
		}
	}

	#富豪之力
	if($eab[46] && $egolddmg){
		$mhpd=int($mhpmax/5);
		$egoldlose=$mhpd*1000;
		if($egold>=$egoldlose){
			$egold-=$egoldlose;
			$mhp-=$mhpd;$mlose_hp+=$mhpd;
			if($mhp<1){$mhp=1;}
			$mmess.="<font color=red size=3>$ename將$egoldlose Gold丟到$mname的臉上，造成$mhpd傷害及心靈上的創傷！</font><BR>";
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
		if($etec_hit[$magic]*($ehitup-$ehitup2)>$rand && $mpdown<=$emp){
			$mmess.="<font color=red size=4><b>$etec_name[$magic] </b></font>";
			if($eab[6]){$mmess.="<font color=blue><b>(減少$eabdmg[6]％MP耗費)</b></font>";}
			$emp-=$mpdown;
			if($etec_sta[$magic] eq 1){
				$ehpup=$etec_str[$magic] + int(rand($efai/2));
				$ehp+=$ehpup;
				if($ehp>$emaxhp){$ehp=$emaxhp;}
				$mmess.="回復<font color=blue><b>$ehpup</b></font>回復。<BR>";
			}elsif($etec_sta[$magic] eq 2){
				$tmp_hp=int($emaxhp/10);
				$tmp_mp=int($emaxmp/10);
				$ehp+=$tmp_hp;
				$emp+=$tmp_mp;
				if($ehp>$emaxhp){$tmp_hp=$tmp_hp-$ehp+$emaxhp;$ehp=$emaxhp;}
				if($emp>$emaxmp){$tmp_mp=$tmp_mp-$emp+$emaxmp;$emp=$emaxmp;}
				$mmess.="<font color=blue>$tmp_hpＨＰ及$tmp_mpＭＰ回復。</font><BR>";
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
				$esmp=int(rand($mmaxmp)/5);
				if($esmp>800){$esmp=800;}
				$mmp-=$esmp;
				if($mmp<0){$mmp=0;}
				$emp+=$esmp;
				if($emp>$emaxmp){$emp=$emaxmp;}
				$mmess.="$mname被吸取<font color=red><b>$esmp</b></font>MP。<BR>";
			}elsif($etec_sta[$magic] eq 8){
				$mhpd=int($mhp/$etec_str[$magic]);
				$mhp-=$mhpd;$mlose_hp+=$mhpd;
				$mmess.="$mname失去了$mhpd HP。<BR>";
			}elsif($etec_sta[$magic] eq 18){
				$tmp_hp=int($ehp/10);
				$tmp_maxhp=int($emaxhp/10);
				$ehp-=$tmp_hp;
				$emp+=$tmp_maxhp;
				if($emp>$emaxmp){$emp=$emaxmp;}
                                        $mmess.="<font color=red>失去$tmp_hpＨＰ</font>、<font color=blue>增加$tmp_maxhpＭＰ。</font><BR>";
                                }elsif($etec_sta[$magic] eq 20){
                                        $tmp_mp=int(rand($emp));
                                        $mhp-=$tmp_mp;
					$emp=0;
                                        if($mhp<1){$mhp=0;}
                                        $mmess.="$mname<font color=red>失去$tmp_mpＨＰ</font><BR>";
                                }elsif($etec_sta[$magic] eq 22){
                                        $tmp_hp=int(rand($efai)+$eagi);
                                        $ehp+=$tmp_hp;
                                        $mhp-=$tmp_hp;
                                        if($ehp>$emaxhp){$ehp=$emaxhp;}
                                        if($mhp<1){$mhp=1;}
                                        $mmess.="$mname被吸取了<font color=red>$tmp_hp</font>ＨＰ。<BR>";
                                }elsif($etec_sta[$magic] eq 23){
                                        $tmp_mp=int(rand($efai)+$eagi);
                                        $emp+=$tmp_mp;
                                        $mmp-=$tmp_mp;
                                        if($emp>$emaxmp){$emp=$emaxmp;}
                                        if($mmp<1){$mmp=0;}
                                        $mmess.="$mname被吸取了<font color=red>$tmp_mp</font>ＭＰ。<BR>";
                                }elsif($etec_sta[$magic] eq 24){
					$tmp_mp=int($eint/2+rand($efai*2));
					$mmp-=$tmp_mp;
					if($mmp<1){$mmp=0;}
                                        $mmess.="$mname<font color=red>失去$tmp_mpＭＰ</font><BR>";
				}else{
$at=1;
                                        if($etec_sta[$magic] eq 15){
                                                $edmg=$etec_str[$magic]*(int(rand($estr))+$eint)-int($mmdef);
$at=2;
                                        }elsif($etec_sta[$magic] eq 16){
                                                $edmg=$etec_str[$magic]+(int(rand($efai))+$eint)-int($mmdef);
$at=2;
					}elsif($etec_sta[$magic] eq 17){
						$edmg=($eint+int(rand($efai))+int(rand($edex)))*$etec_str[$magic]-int($mmdef);
$at=2;
                                        }elsif($etec_sta[$magic] eq 19){
						$edmg=$edex+int(rand($edex*$etec_str[$magic]));
$at=2;
                                        }elsif($etec_sta[$magic] eq 21){
						$edmg=$evit+int(rand($edex*$etec_str[$magic]));
					}else{
	                                        $edmg=$etec_str[$magic] + int(rand($eint))-int($mmdef);
					}
                                        if($eab[51] && ($etec_sta[$magic] eq 16 || $etec_sta[$magic] eq 17)){
                                                $edmg*=2;
                                                $mmess.="<font color=blue><b>(傷害x２) </b></font>";
                                        }
                                        if($etec_str[$magic]<1000){
                                                $edmg+=int(($eint+$efai)*$etec_str[$magic]/4000);
                                        }else{
                                                $edmg+=int(($eint+$efai)/4);
                                        }
					if($eab[5]){
						$edmg+=int($edmg*$eabdmg[5]/100);
						$mmess.="<font color=blue><b>(傷害+$eabdmg[5]％) </b></font>";
					}
					if($mab[7]){
						$edmg-=int($edmg*$mabdmg[7]/100);
						$mmess.="<font color=blue><b>(傷害-$mabdmg[7]％) </b></font>";
					}
                                        if($edsta>1){
                                                $edmg-=int($edmg*$edsta/100);
                                                $mmess.="<font color=blue><b>(傷害-$edsta％) </b></font>";
                                        }
					if($etec_sta[$magic] eq 9 && $turn >2){$esv=1;}#即死
					if($etec_sta[$magic] eq 10){$esv=2;}#防御ダウン
					if($etec_sta[$magic] eq 11){$esv=3;}#毒
					if($etec_sta[$magic] eq 12){$esv=4;}#命中ダウン
					if($etec_sta[$magic] eq 13){$esv=5;}#麻痺
					if($etec_sta[$magic] eq 14){$esv=7;}#鈍化
				}
				
				$mmess.="<br>";
			}else{##通常攻擊
				$edmg=int(rand($eat-$mdef/2));
                                if($eab[47] || $eab[50]){
                                        $tmp_dmg=$eab[47] + $eab[50];
                                        $edmg+=int($edmg*$tmp_dmg*$turn/100);
                                }
				if($eab[2]){
					$edmg+=int($edmg*$eabdmg[2]/100);
				}
				if($mab[3]){
#$dddd=int($edmg*$mabdmg[3]/100);
#$mmess.="(物防效果$mabdmg[3]%,原傷害$edmg,減傷效果$dddd)";
					$edmg-=int($edmg*$mabdmg[3]/100);
				}
				if($eddmg>0){
				  $edmg-=int($edmg*$eddmg/100);
        }
				$at=1;
			}
			if($at){
				##回避、クリティカル
				$hitrand=int(rand(2));
				if($at eq 1){
                                $tmp_speed=$mspeed-$espeed;
                                if($tmp_speed>400){$tmp_speed=400;}
				$tmp_mfai=1200-$mfai;
				if($tmp_mfai<500){$tmp_mfai=500;}
				$tmp_msh=$msh;
				if($eab[56]){
					$tmp_msh=int($tmp_msh/$eabdmg[56]);
					$tmp_speed=int($tmp_speed/$eabdmg[56]);
				}
				if($mab[12] && 100>int(rand($tmp_mfai))){
					if($eab[43] && $eabdmg[43]>int(rand(100))){	
                                                $mmess.="<font color=blue size=3>$mname的反擊發動！</font>，但被對方回避了<BR>";
                                        }else{
						$mdmg=int(($edmg+int(rand($mstr)))/2*$mabdmg[12]);
						if($mdmg<1){$mdmg=1;}
						$ehp-=$mdmg;$elose_hp+=$mdmg;
						if($ehp<1){$ehp=1;}
						$edmg=0;
						$hitrand=0;
						$mmess.="<font color=blue size=3>$mname的反擊發動！</font><BR>$ename受到<font color=red size=5><b>$mdmg</b></font>的傷害。<BR>";
                                        }
				}elsif($tmp_msh>int(rand(1000)) && $eallhit eq 0){
					$mmess.="<font color=blue size=3>$mname閃避了攻擊。<BR></font>";
					$edmg=0;
					$hitrand=0;
				}elsif($msh2>int(rand(1000))){
					$mmess.="<font color=blue size=3>$mname擋住了攻擊。<BR></font>";
					$edmg=0;
					$hitrand=0;
				}elsif($ecl>int(rand(1000)) && !$mab[44]){
					$mmess.="<font color=blue size=4>爆擊！</font>";
					$edmg=int($edmg*1.5);
					if($eab[23]){
						$edmg=int($edmg*$eabdmg[23]);
					}
					if($edmg<=0 && $hitrand eq 0){
						$mmess.="<font color=blue>$mname</font>未受到傷害。<BR>";
					}
				}elsif($tmp_speed>int(rand(1000)) && $eallhit eq 0){
                                        $mmess.="<font color=green size=3>$mname躲避了攻擊。<BR></font>";
                                        $edmg=0;
                                        $hitrand=0;
                                }
                                }elsif($ecl>int(rand(1500)) && !$mab[44]){ #at=2
                                        $mmess.="<font color=blue size=4>爆擊！</font>";
                                        $edmg=int($edmg*1.5);
                                        if($eab[23]){
                                                $edmg=int($edmg*$eabdmg[23]);
                                        }
                                        if($edmg<=0 && $hitrand eq 0){
                                                $mmess.="<font color=blue>$mname</font>未受到傷害。<BR>";
                                        }

				}#at=2
				#elsif($edmg<=0){
				#	$mmess.="<font color=blue>$mname</font>未受到傷害。<BR>";
				#}
				##傷害
				if($edmg<=0 && $hitrand eq 0){
					$edmg=0;
					#$mmess.="<BR>";
					$mmess.="<font color=blue>$mname</font>未受到傷害。<BR>";
				}elsif($edmg<=0){
					$edmg=1;
				}
				if($edmg){
					$mmess.="<font color=blue>$mname</font>受到<font color=red size=4><b>$edmg</b></font>的傷害。<BR>";
					if($esv eq 2){
						$mdef-=int($mdef/10);
						if($mdef < 0){$mdef=0;}
						$mmess.="$mname的防御力下降。<BR>";
					}
					elsif(int(rand(4)) eq 2 && $esv eq 3 || $eab[14] && int(rand(6)) < 1){
						$mpara=$eabdmg[14];
						if(!$mpara){$mpara=1;}
						$mmess.="<font color=red>$mname中毒。</font><BR>";
					}
					elsif($esv eq 4 && $esh<3000 && int(rand(3)) eq 2){
						$esh+=40;
						$mmess.="<font color=red>$mname的命中率下降。</font><BR>";
					}
					elsif(int(rand(8)) eq 2 && $esv eq 5 || $eab[24] && int(rand(15)) eq 1){
						$mpara2=1;
						$mmess.="<font color=red>$mname麻痺。</font><BR>";
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
						$mmess.="<font color=red>$mname速度下降。</font><BR>";
					}
					elsif((int(rand(30)) eq 7 && $esv eq 1 || $eab[9] && int(rand(1000)) < $eabdmg[9]) && $turn>2){
						if($mab[40] && $mabdmg[40]>int(rand(100))){
							$esv=0;
							$mmess.="<font color=red>不死鳥保護住$mname。</font><BR>";
						}elsif($mab[49] && $mabdmg[49]>int(rand(100))){
                                                        $ehp=1;
                                                        $mmess.="<font color=red>$ename對死神使出即死，對死神使出即死，但死神將即死回報給對方。</font><BR>";
						}elsif($mab[49]){
							$esv=0;
							$mmess.="<font color=red>死神保護住$mname。</font><BR>";
						}else{
							$mhp=0;
							$mmess.="<font color=red>$mname即死。</font><BR>";
						}
					}
					elsif($eab[26] && int(rand(3)) eq 1){
						$addmg = int(rand(200));
						$mmess.="追加<font color=red size=2><b>$addmg</b></font>的傷害。<BR>";
						$edmg += $addmg;
					}
					elsif($eab[27] && int(rand(3)) eq 1){
						$esmp=int(rand(150));
						$mmp-=$esmp;
						if($mmp<0){$mmp=0;}
						$emp+=$esmp;
						if($emp>$emaxmp){$emp=$emaxmp;}
						$mmess.="$mname被奪走了<font color=red>$esmp</font>MP。<BR>";
					}elsif($eab[57] && int(rand(2)) eq 1 && $esta_eq_disable<2 && $msta_eq_count>0){
                                                if($esta_eq_disable eq 0){
                                                        $abrand=int(rand($msta_eq_count))+1;
                                                        $iab = $msta_eq[$abrand];
                                                        $atype = $mabtype[$iab];
                                                        $mab[$atype]=0;
                                                        $mabdmg[$atype]=0;
                                                        $eab[57]=int(rand(2));
                                                        $eabdmg[57]=$mab[57];
							$esta_eq_disable++;
                                                        $mmess.="<font color=red>[神之封印]$mname的奧義:$mabname[$iab]被封住了！</font><BR>";
                                                }elsif($esta_eq_disable eq 1){
                                                        $eab[57]=0;
                                                        $eabdmg[57]=0;
							$esta_eq_disable++;
                                                        if($eab[41]){
                                                                $mmess.="因封印防護作用，神之封印失敗！";
                                                        }elsif(int(rand(2)) eq 1){
                                                                $abrand=int(rand($msta_eq_count))+1;
                                                                $iab = $msta_eq[$abrand];
                                                                $atype = $mabtype[$iab];
                                                                $mab[$atype]=0;
                                                                $mabdmg[$atype]=0;
                                                                $mmess.="<font color=red>[神之封印]$mname的奧義:$mabname[$iab]被封住了！</font><BR>";

                                                        }else{
                                                                $mmess.="第二次神之封印發動失敗！";
                                                        }
                                                }
                                        }elsif($eab[31] && int(rand(2)) eq 1 || $eab[52]){
                                                if(($mab[41] || $mabdmg[43]>int(rand(100))) && !$eab[52]){
                                                        $mmess.="封印失敗！";
                                                }else{
                                                        $abrand = int(rand(2));
                                                        $iab = $msk[$abrand];
                                                        $atype = $mabtype[$iab];
                                                        if($abtype ne 11){
                                                                if($mab[$atype]){
                                                                        $mab[$atype] = 0;
                                                                        #先攻、神風需要清掉威力
                                                                        $mabdmg[$atype]=0;
                                                                        $mmess.="<font color=red>$mname的屬性:$mabname[$iab]>被封住了！</font><BR>";
                                                                }
                                                        }
                                                }
					}
				}
				$mhp-=$edmg;$mlose_hp+=$edmg;
			}
			if($mhp<=0){
					$mmess.="<BR><font color=red size=4><b>$mname倒下。</b></font><BR>";
			}
			if($mhp<=0 && $mab[11]  && int(rand(100)) < $mabdmg[11] && !$ehflg){
				$mhp=int($mmaxhp/2);
				if($mabdmg[11] eq"100"){$mhp=$mhp*2;}
				if($mabdmg[11]<100){$ehflg=1;}
				$mmess.="<font color=red>$mname復活！</font><BR>";
			}elsif($mhp<=0){
				$mhp=0;
				$lose=1;
			}
			if($kou>20){&error("錯誤");}
			if($lose){last;}
		}
		$mmess.="<BR>";
	}else{
		$mmess.="<font color=red>$ename無法行動。</font><BR>";
	}
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

#レベルアップ時的處理
sub LVUP{
	$mlv2=int($mex/100)+1;
	if($mlv2>100){
		$mlv2=100;
		$mex=9999;
	}
	if($ext_tl_lvup eq ""){$ext_tl_lvup=0;}
	if($mlv2>$mlv){
		for($i=0;$i<$mlv2-$mlv;$i++){
			$ext_tl_lvup++;
			$com.="<font color=red>$mname升級！</font><BR>";
			if($mflg3 eq""){$mflg3=0;}
			$hpup=int(rand($mvit/40+$mfai/80+8))+1;$mmaxhp+=$hpup;
			$mpup=int(rand($mint/40+$mfai/80+2));$mmaxmp+=$mpup;
			$strup=int(rand(2));$mstr+=$strup;
			$vitup=int(rand(2));$mvit+=$vitup;
			$intup=int(rand(2));$mint+=$intup;
			$faiup=int(rand(2));$mfai+=$faiup;
			$dexup=int(rand(2));$mdex+=$dexup;
			$agiup=int(rand(2));$magi+=$agiup;
			
			$mmaxmaxhp = $mmaxstr*5 + $mmaxvit*10 + $mmaxmen*3 - 2000;
			$mmaxmaxmp = $mmaxint*5 + $mmaxmen*3 - 800;
$maxmaxhpadd=0;
if($marmno eq"mix" && $mele eq $marmele){$maxmaxhpadd+=1000;}
if($mprono eq"mix" && $mele eq $mproele){$maxmaxhpadd+=1000;}
if($maccno eq"mix" && $mele eq $maccele){$maxmaxmpadd+=1000;}
			if(($mmaxmaxhp+$maxmaxhpadd) < $mmaxhp){$mmaxhp=$mmaxmaxhp+$maxmaxhpadd;$maxcom[0]="<font color=red>（界限值已達上限。）</font>";}
			if(($mmaxmaxmp+$maxmaxmpadd) < $mmaxmp){$mmaxmp=$mmaxmaxmp+$maxmaxmpadd;$maxcom[1]="<font color=red>（界限值已達上限。）</font>";}

			if($mmaxstr < $mstr){$mstr=$mmaxstr;$maxcom[2]="<font color=red>（界限值已達上限。）</font>";}
			if($mmaxvit < $mvit){$mvit=$mmaxvit;$maxcom[3]="<font color=red>（界限值已達上限。）</font>";}
			if($mmaxint < $mint){$mint=$mmaxint;$maxcom[4]="<font color=red>（界限值已達上限。）</font>";}
			if($mmaxmen < $mfai){$mfai=$mmaxmen;$maxcom[5]="<font color=red>（界限值已達上限。）</font>";}
			if($mmaxdex < $mdex){$mdex=$mmaxdex;$maxcom[6]="<font color=red>（界限值已達上限。）</font>";}
			if($mmaxagi < $magi){$magi=$mmaxagi;$maxcom[7]="<font color=red>（界限值已達上限。）</font>";}
                        if($PARA_LIMIT < $mstr && $mtype ne"0"){$mstr=$PARA_LIMIT;$maxcom[2]="<font color=red>（已達能力上限PARA_LIMIT。）</font>";}
                        if($PARA_LIMIT < $mvit && $mtype ne"4"){$mvit=$PARA_LIMIT;$maxcom[3]="<font color=red>（已達能力上限PARA_LIMIT。）</font>";}
                        if($PARA_LIMIT < $mint && $mtype ne"1"){$mint=$PARA_LIMIT;$maxcom[4]="<font color=red>（已達能力上限PARA_LIMIT。）</font>";}
                        if($PARA_LIMIT < $mfai && $mtype ne"2"){$mfai=$PARA_LIMIT;$maxcom[5]="<font color=red>（已達能力上限PARA_LIMIT。）</font>";}
                        if($PARA_LIMIT < $mdex && $mtype ne"3"){$mdex=$PARA_LIMIT;$maxcom[6]="<font color=red>（已達能力上限PARA_LIMIT。）</font>";}
                        if($PARA_LIMIT < $magi && $mtype ne"5"){$magi=$PARA_LIMIT;$maxcom[7]="<font color=red>（已達能力上限PARA_LIMIT。）</font>";}

			
			$com.="HP 增加<font color=blue>$hpup</font>$maxcom[0]<BR>";
			$com.="MP 增加<font color=blue>$mpup</font>$maxcom[1]<BR>";
			if($strup){$com.="力量 增加<font color=blue>$strup</font>$maxcom[2]<BR>";}
			if($vitup){$com.="生命 增加<font color=blue>$vitup</font>$maxcom[3]<BR>";}
			if($intup){$com.="智力 增加<font color=blue>$intup</font>$maxcom[4]<BR>";}
			if($faiup){$com.="精神 增加<font color=blue>$faiup</font>$maxcom[5]<BR>";}
			if($dexup){$com.="運氣 增加<font color=blue>$dexup</font>$maxcom[6]<BR>";}
			if($agiup){$com.="速度 增加<font color=blue>$agiup</font>$maxcom[7]<BR>";}

		}
	}
}


#界限アップ時的處理
sub MAXUP{
	if(int(rand($MAXLVP)) eq 1){
		$coment="<font color=orange><b>$mname界限值上限急速成長！！</b></font>";
		&maplog("<font color=orange>[急成長]</font><font color=blue>$mname</font>的界限值於戰鬥後快速成長！");
		$rate=5;
	}
	elsif(int(rand($SMAXLVP)) eq 1){
		$coment="<font color=red><b>$mname界限值獲得覺醒！！！</b></font>";
		&maplog("<font color=red>[覺醒]</font><font color=blue>$mname</font>的界限值於戰鬥後大幅成長！！");
		$rate=15;
	}
	else{
		$coment="<font color=green><b>$mname的界限值上昇！</b></font>";
		$rate=1;
	}
	$com.="$coment<BR>";
	if ($mmaxstr <400){$mmaxstr += $JMAX[$mtype][0]*$rate;}
	if ($mmaxvit <400){$mmaxvit += $JMAX[$mtype][1]*$rate;}
	if ($mmaxint <400){$mmaxint += $JMAX[$mtype][2]*$rate;}
	if ($mmaxmen <400){$mmaxmen += $JMAX[$mtype][3]*$rate;}
	if ($mmaxdex <400){$mmaxdex += $JMAX[$mtype][4]*$rate;}
	if ($mmaxagi <400){$mmaxagi += $JMAX[$mtype][5]*$rate;}
	#$mmaxvit += $JMAX[$mtype][1]*$rate;
	#$mmaxint += $JMAX[$mtype][2]*$rate;
	#$mmaxmen += $JMAX[$mtype][3]*$rate;
	#$mmaxdex += $JMAX[$mtype][4]*$rate;
	#$mmaxagi += $JMAX[$mtype][5]*$rate;
	#if($mmaxstr>=400){$mmaxstr = 400;}
	#if($mmaxvit>=400){$mmaxvit = 400;}
	#if($mmaxint>=400){$mmaxint = 400;}
	#if($mmaxmen>=400){$mmaxmen = 400;}
	#if($mmaxdex>=400){$mmaxdex = 400;}
	#if($mmaxagi>=400){$mmaxagi = 400;}
	$mmax="$mmaxstr,$mmaxvit,$mmaxint,$mmaxmen,$mmaxdex,$mmaxagi,$mmaxlv";
}
#寵物成長處理
sub PETLVUP{
	if ($mab[35]) {
		$ej=0;
		$tmppoint=0;
	        if ($mpet ne"") {
        	        foreach(@PETDATA){
	                        if ($PETDATA[$ej][0] eq $mpetname){
                                	$tmppoint=$PETDATA[$ej][5]/20000+($mode*500);
                        	        last;
                	        }
        	                $ej++;
	                }
                        if ($tmppoint ne 0) {
                                if (int(rand($tmppoint)) eq 98 && $mpetlv < 10) {
					($mpetcno,$mpetname,$mpetdmg,$mpetdef,$mpetspeed,$mpetele,$mpetlv,$mpetcl,$mpetsta,$mpettype,$mpetflg) = split(/,/,$mpet);
                                        $mpetlv+=1;
                                        $mpetdmg+=$PETDATA[$ej][1];
                                        $mpetdef+=$PETDATA[$ej][2];
                                        $mpetspeed+=$PETDATA[$ej][3];
                                        $mpet="$mpetcno,$mpetname,$mpetdmg,$mpetdef,$mpetspeed,$mpetele,$mpetlv,$mpetcl,$mpetsta,$mpettype,$mpetflg";
                                        $showmsg="<font color=green><b>你的寵物升級了，威力+$PETDATA[$ej][1]、防禦+$PETDATA[$ej][2]、速度+$PETDATA[$ej][3]</b></font>";
                                }
                        }

	        }

	}
}
1;
