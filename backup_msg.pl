	$tt = time ;
        ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime(time);
        $year += 1900;
        $mon++;
        $ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
        $daytime = sprintf("%4d\/%02d\/%02d\/(%s)　%02d時%02d分", $year,$mon,$mday,$ww,$hour,$min);

        open(IN,"/var/www/hero/data/maplog.cgi");
        @data = <IN>;
        close(IN);
        unshift(@data, "<font color=red><b>[系統公告]</b>系統己進行備份。</font>($daytime)\n");
        splice(@data,10);
        open (OUT, "> /var/www/hero/data/maplog.cgi");
        print OUT @data;
        close (OUT);

        open(IN,"/var/www/hero/data/maplog9.cgi");
        @data2 = <IN>;
        close(IN);
        unshift(@data2, "<font color=darkgreen><b>[系統公告]</b></font><font color=blue>系統已進行備份。($daytime)\n");
        splice(@data2,30);
        open (OUT, "> /var/www/hero/data/maplog9.cgi");
        print OUT @data2;
        close (OUT);

