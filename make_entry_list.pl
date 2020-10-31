        $tt = time ;
        ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime(time);
        $year += 1900;
        $mon++;
        $ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
        $daytime = sprintf("%4d\/%02d\/%02d\/(%s)　%02d時%02d分", $year,$mon,$mday,$ww,$hour,$min);

        open(IN,"/var/www/hero/data/entry_list.cgi");
        @ENTRY = <IN>;
        close(IN);
	$hit=0;
	#分組
        foreach(@ENTRY){
                ($ejoin,$eid,$ename,$echara,$etotal)=split(/<>/);
                if($ejoin eq"0"){
                	push(@CL_DATA0,"$eid<>$ename<>$echara<>$etotal<><>1<><>\n");
			$hit=1;
			$hit0=1;
                }elsif($ejoin eq"1"){
                	push(@CL_DATA1,"$eid<>$ename<>$echara<>$etotal<><>1<><>\n");
                        $hit=1;
			$hit1=1;
                }elsif($ejoin eq"2"){
                	push(@CL_DATA2,"$eid<>$ename<>$echara<>$etotal<><>1<><>\n");
                        $hit=1;
			$hit2=1;
                }elsif($ejoin eq"3"){
                        push(@CL_DATA3,"$eid<>$ename<>$echara<>$etotal<><>1<><>\n");
                        $hit=1;
                        $hit3=1;
                }
		$rr[$ejoin]++;
        }
	if($hit){
	$rj=0;
	#輸出名單
	for($rj=0;$rj<@CL_DATA0;$rj++){
		$tvalue=$CL_DATA0[ rand @CL_DATA0];
		$hit=0;
		foreach(@CL_D0){
			if ($_ eq"$tvalue"){
				$hit=1;
				last;
			}
		}
		if($hit){
			$rj--;
		}else{
			push(@CL_D0,$tvalue);	
		}
	}
	#最強的放最後
if($hit0){
	$lastentry=0;$lasti=0;
	$ni=0;
	foreach(@CL_D0){
		($eid,$ename,$echara,$etotal,$estatus,$ebattletime)=split(/<>/);
		if($etotal>$lastentry){
			$lasti=$ni;
			$lastentry=$etotal;
		}
		$ni++;
	}
	$tni=$ni-1;
	$tmps=$CL_D0[$tni];
	$CL_D0[$tni]=$CL_D0[$lasti];
	$CL_D0[$lasti]=$tmps;
}
        for($rj=0;$rj<@CL_DATA1;$rj++){
                $tvalue=$CL_DATA1[ rand @CL_DATA1];
                $hit=0;
                foreach(@CL_D1){
                        if ($_ eq"$tvalue"){
                                $hit=1;
                                last;
                        }
                }
                if($hit){
                        $rj--;
                }else{
                        push(@CL_D1,$tvalue);
                }
        }
        #最強的放最後
if($hit1){
        $lastentry=0;$lasti=0;
        $ni=0;
        foreach(@CL_D1){
                ($eid,$ename,$echara,$etotal,$estatus,$ebattletime)=split(/<>/);
                if($etotal>$lastentry){
                        $lasti=$ni;
                        $lastentry=$etotal;
                }
                $ni++;
        }
        $tni=$ni-1;
        $tmps=$CL_D1[$tni];
        $CL_D1[$tni]=$CL_D1[$lasti];
        $CL_D1[$lasti]=$tmps;
}
        for($rj=0;$rj<@CL_DATA2;$rj++){
                $tvalue=$CL_DATA2[ rand @CL_DATA2];
                $hit=0;
                foreach(@CL_D2){
                        if ($_ eq"$tvalue"){
                                $hit=1;
                                last;
                        }
                }
                if($hit){
                        $rj--;
                }else{
                        push(@CL_D2,$tvalue);
                }
        }
        #最強的放最後
if($hit2){
        $lastentry=0;$lasti=0;
        $ni=0;
        foreach(@CL_D2){
                ($eid,$ename,$echara,$etotal,$estatus,$ebattletime)=split(/<>/);
                if($etotal>$lastentry){
                        $lasti=$ni;
                        $lastentry=$etotal;
                }
                $ni++;
        }
        $tni=$ni-1;
        $tmps=$CL_D2[$tni];
        $CL_D2[$tni]=$CL_D2[$lasti];
        $CL_D2[$lasti]=$tmps;
}
        for($rj=0;$rj<@CL_DATA3;$rj++){
                $tvalue=$CL_DATA3[ rand @CL_DATA3];
                $hit=0;
                foreach(@CL_D3){
                        if ($_ eq"$tvalue"){
                                $hit=1;
                                last;
                        }
                }
                if($hit){
                        $rj--;
                }else{
                        push(@CL_D3,$tvalue);
                }
        }
        #最強的放最後
if($hit3){
        $lastentry=0;$lasti=0;
        $ni=0;
        foreach(@CL_D3){
                ($eid,$ename,$echara,$etotal,$estatus,$ebattletime)=split(/<>/);
                if($etotal>$lastentry){
                        $lasti=$ni;
                        $lastentry=$etotal;
                }
                $ni++;
        }
        $tni=$ni-1;
        $tmps=$CL_D3[$tni];
        $CL_D3[$tni]=$CL_D3[$lasti];
        $CL_D3[$lasti]=$tmps;
}
        open(OUT,">./data/entry_list_0.cgi");
        print OUT @CL_D0;
        close(OUT);
        open(OUT,">./data/entry_list_1.cgi");
        print OUT @CL_D1;
        close(OUT);
        open(OUT,">./data/entry_list_2.cgi");
        print OUT @CL_D2;
        close(OUT);
        open(OUT,">./data/entry_list_3.cgi");
        print OUT @CL_D3;
        close(OUT);
                        open(IN,"/var/www/hero/data/maplog.cgi");
                        @data = <IN>;
                        close(IN);
                        unshift(@data, "<font color=darkgreen><b>[天下第一武道會]對戰名單已出爐</b></font>($daytime)\n");
                        splice(@data,10);
                        open (OUT, "> /var/www/hero/data/maplog.cgi");
                        print OUT @data;
        open (OUT, "> /var/www/hero/data/maplogtime.cgi");
        print OUT $tt;
        close (OUT);
        open (OUT, "> /var/www/hero/data/entry_list.cgi");
        print OUT "";
        close (OUT);
        open (OUT, "> /var/www/hero/data/battle_time.cgi");
        print OUT "1<>1<>1<>1<>1<>1<>";
        close (OUT);
        open (OUT, "> /var/www/hero/data/entry_comp.cgi");
        print OUT "";
        close (OUT);
	}
