#!/usr/bin/perl
use File::Compare ;
compare_files("diagnosibility.pl","product.pl","OLTSEED");
sub compare_files {

	my ($san_ref,$san_exec,$pdb_for_sanity) = @_ ;
	if(File::Compare::compare("$san_exec","$san_ref") == 0)
	{
		system("touch sanitycheck.suc");
	}
	else
	{

		$msg = "File comaprison has failed for $pdb_for_sanity . Some DB error has occured .Check $san_exec for details ";
		if ($ENV{'IFARM_RUN'} == 1) {

			system("touch sanitycheck.sav");
			#	write_to_tlgfile("sanitycheck.sav is present . Some sanity has failed . Refer WORK\n");
			write_to_file("sanitycheck.sav",$msg);

		}

		else {
			system("touch sanitycheck.dif");
			#write_to_tlgfile("sanitycheck.dif is present . Some sanity has failed . Refer WORK\n");
			write_to_file("sanitycheck.dif",$msg);
		}
	}

}

sub write_to_file {
	my ($file_name , $msg) = @_ ;

	open(FHR,">>" , $file_name) or "Some error $!\n" ;
	print FHR $msg ;
	close(FHR);


}

