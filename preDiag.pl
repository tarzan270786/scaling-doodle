#!/usr/bin/perl 

sub error_check {
	my $generate = (split/\./, (split/\//, $_[0])[-1])[-2];
	print $generate,"\n" ;
	my $key = (split /\_/, $generate)[0];
	$key = uc $key ;
	$param1 = $_[1];
	print " $key \n" ;
	print "param1 => $param1 \n";
}
my $key = "lower_case" ;
error_check("T_WORK/oraunzip_exec_CEN.log", $key);
error_check("T_WORK/ssl_walletexec_CEN.log", uc ($key));
