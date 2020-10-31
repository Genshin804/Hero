#!/usr/bin/perl

#################################################################
#   【免責事項】                                                #
#    このスクリプトはフリーソフトです。このスクリプトを使用した #
#    いかなる損害に対して作者は一切の責任を負いません。         #
#    また設置に関する質問はサポート掲示板にお願いいたします。   #
#    直接メールによる質問は一切お受けいたしておりません。       #
#################################################################

require './jcode.pl';
require './conf.cgi';
require './sub.cgi';

&decode;

        open(IN,"./logfile/chara/$in{'fileno'}.cgi") or &error('請輸入正確的帳號及密碼。');
        @CN_DATA = <IN>;
        close(IN);
        ($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);
        if($kpass ne $in{'mpass'}){&error("請輸入正確的帳號及密碼。");}
                        $dir2="./logfile/chara";
                        unlink("$dir2/$in{'fileno'}.cgi");
                        $dir2="./logfile/item";
                        unlink("$dir2/$in{'fileno'}.cgi");
                        $dir2="./logfile/job";
                        unlink("$dir2/$in{'fileno'}.cgi");
                        $dir2="./logfile/ability";
                        unlink("$dir2/$in{'fileno'}.cgi");
                        $dir2="./logfile/history";
                        unlink("$dir2/$in{'fileno'}.cgi");
                        $dir2="./logfile/storage";
                        unlink("$dir2/$in{'fileno'}.cgi");
                        $dir2="./logfile/ext";
                        unlink("$dir2/$in{'fileno'}.cgi");
                        $dir2="./logfile/act";
                        unlink("$dir2/$in{'fileno'}.cgi");
                        $dir2="./logfile/verchk";
                        unlink("$dir2/$in{'fileno'}.cgi");
        #解除守備
        open(IN,"./data/def.cgi");
        @DEF = <IN>;
        close(IN);
        $hit=0;
        @NDEF=();
        foreach(@DEF){
                ($name,$id,$pos)=split(/<>/);
                if($id eq "$kid"){$hit=1;}
                else{push(@NDEF,"$_");}
        }
        if($hit){
                open(OUT,">./data/def.cgi");
                print OUT @NDEF;
                close(OUT);
        }

        &header;
        print <<"EOM";
<center><h2><font color=red>$kname刪除完成。</font></h2><hr size=0>
EOM
