	$tt = time ;
        ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime(time);
        $year += 1900;
        $mon++;
        $ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
        $daytime = sprintf("%4d\/%02d\/%02d\/(%s)　%02d時%02d分", $year,$mon,$mday,$ww,$hour,$min);
        open(IN,"/var/www/hero/data/townmonster.cgi");
	@mdata = <IN>;
	close(IN);
        ($ename,$eab,$etec,$esk,$e_ex,$e_gold,$etown,$elv)=split(/<>/,$mdata[0]);
        ($ehp,$emp,$str,$vit,$eint,$efai,$edex,$eagi,$eele)=split(/,/,$eab);
	if ($ehp eq"0" || $ename eq""){
	        open(IN,"/var/www/hero/data/monster.cgi");
        	@MON_DATA = <IN>;
	        close(IN);
		$mcount=0;
		$no=0;
		foreach(@MON_DATA){
			($ename,$eab,$etec,$esk,$e_ex,$e_gold,$etown,$elv)=split(/<>/);
			($ehp,$emp,$str,$vit,$eint,$efai,$edex,$eagi,$eele)=split(/,/,$eab);
			if($elv eq "99" && $eele eq 0){
				#$godm[$mcount]=$MON_DATA[$no];
				$mcount++;
				last;
			}
			$no++;
		}
		if($mcount){
		#($ename,$eab,$etec,$esk,$e_ex,$e_gold,$etown,$elv)=split(/<>/,$godm[int(rand($mcount))]);
		$etown=1+int(rand(21));
		$mdata[0]="$ename<>$eab<>$etec<>$esk<>$e_ex<>$e_gold<>$etown<>$elv";
		open (OUT, "> /var/www/hero/data/townmonster.cgi");
		print OUT @mdata;
		close (OUT);
        	open(IN,"/var/www/hero/data/maplog.cgi");
	        @data = <IN>;
        	close(IN);
	        unshift(@data, "<font color=red><b>[神獸]</b>$ename出現在世界的某個角落，請各位玩家小心。</font>($daytime)\n");
	        splice(@data,10);
	        open (OUT, "> /var/www/hero/data/maplog.cgi");
	        print OUT @data;
		}
	}
