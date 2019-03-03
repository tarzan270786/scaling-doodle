#!/usr/bin/perl 
use File::Basename;
use Cwd 'abs_path' ;
use File::spec;
sub debugwallet {

	#$BASE=system("dirname `readlink -f $0`");
	#	my $dirname = abs_path($0);
	my $dirname = dirname(File::Spec->rel2abs(__FILE__));
	#print "Path is $dirname\n";
	opendir(DIR, ".");
	my @files = grep(/\.sh$/,readdir(DIR));
	closedir(DIR);
	print "The files are => @files \n";

	foreach $file (@files) {
		   print "$file\n";
		   #system("sed -i -e  '/Please look at \$log for details/a /\`/bin/cp \$log \$T_WORK\/\.\`'/ $file");
		   system("sed -i -e  '/Please look at \$log for details/a ##########Checking #######' $file");
		   # system("sed '
	   }
}

&debugwallet();
