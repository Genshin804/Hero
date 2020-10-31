sub attestation {

	&header;
print <<NEW;
◆ メールに添付された認証キーとＩＤとパスを入力してください。<BR>
◆ 認証キーが登録されますとゲームを開始することができます。<p>

<center><form method=$method action=./newentry.cgi>
<table bgcolor=$TABLE_C><tbody bgcolor=$TD_C3>
<TR><TH bgcolor=$TD_C2 colspan=2>認 証</TH></TR>
<TR><TH>ID</TH><TD>
<input type=text name=id class=text size=10></TD></TR>
<TR><TH>パスワード</TH><TD>
<input type=password name=pass class=text size=10></TD></TR>
<TR><TH>認証キー</TH><TD>
<input type=password name=key class=text size=10></TD></TR>
</TD></TR>
<input type=hidden name=mode value="set_entry">
<TR><TD bgcolor=$TD_C4 colspan=2 align=center><input type=submit value="認証"></TD></TR>
</TBODY></TABLE>
</form>

NEW
	&mainfooter;
	exit;
}

# Sub Set Regist #
sub set_entry {

	&host_name;
	&chara_open;
	$akey = crypt("$mpass",$ATTESTATION_ID);

	if($akey ne $in{'key'}){&error2("暗証キーが違います！\n");}
	if($murl eq ""){&error2("既に認証済みです。");}

	&maplog("<font color=blue><B>[認証]</B></font>$mnameが新たに登録されました！");
	$murl="";

	&chara_input;
	&header;

	print qq|認証が完了しました<br>\n|;
	print qq|IDは$midです。<br>\n|;
	print qq|パスワードは$mpassです。<br><br>\n|;

	print qq|登録手続きはこれで完了です。<br>\n|;
	print qq|ＴＯＰページからログインできます。<br>\n|;

	print qq|<a href="./index.cgi">\[回到城鎮\]</a>\n|;
	&mainfooter;
	exit;
}

#------------------#
#  メール送信處理  #
#------------------#
sub mail_to {
	unless (-e $SENDMAIL) { &error2("sendmailのパスが不正です"); }

	# メールタイトル
	$mail_sub = " 登録完了通知";
	&time_data;

	$a_pass = crypt("$in{'pass'}", $ATTESTATION_ID);
	# メール本文
	$mail_msg = <<"EOM";
$in{'name'} 様

この度は、$TITLE への登録をありがとうございました。
登録內容は以下のとおりですので、ご確認ください。

■登録日時：$daytime
■ホスト名：$host
■參加者名：$in{'name'}
■Ｅメール：$in{'mail'}
■ＩＤ    ：$in{'id'}
■ＰＡＳＳ：$in{'pass'}
■認証キー：$a_pass

認証キーを登録することによってゲームに參加することがで
きます。

[認証キーの設定]
$FH_URL/newentry.cgi?mode=ATTESTATION
(※こちらから登録が出来ます。)

よく參加規約をよく読んでからゲームを開始してください。
また、パスワード、ＩＤ等の再發行は致しませんので大切に
保管しておいて下さい。

_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
$TITLE管理人
  Home:   $LINKURL1
EOM
	# JISコードへ変換
    	&jcode'convert(*mail_sub,'jis');
    	&jcode'convert(*mail_msg,'jis');

	# コメント內の改行とタグを復元
	$mail_msg =~ s/<br>/\n/ig;

	# メール處理
	open(MAIL,"| $SENDMAIL -t") || &E_ERR("メール送信に失敗しました");
	print MAIL "To: $in{'mail'}\n";
	print MAIL "Subject: $mail_sub\n";
	print MAIL "MIME-Version: 1.0\n";
	print MAIL "Content-type: text/plain; charset=ISO-2022-JP\n";
	print MAIL "Content-Transfer-Encoding: 7bit\n";
	print MAIL "X-Mailer: $ver\n\n";
	print MAIL "$mail_msg\n";
	close(MAIL);

}

1;
