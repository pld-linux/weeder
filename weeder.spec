Summary:	Weeder - binary file identifier
Name:		weeder
Version:	0.9.7
Release:	0.4
Epoch:		0
License:	GPL
Group:		Applications/Console
Source0:	http://members.teleweb.at/erikajo/%{name}-%{version}.tgz
# Source0-md5:	744a45626d1dfde49e456fb9ffb35380
Patch0:		%{name}-FHS.patch
URL:		http://members.teleweb.at/erikajo/weeder.htm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_localstatedir}/lib/%{name}

%description
Weeder is a utility which takes fingerprints (crc and length) of
files. Once a fingerprint is taken it can display or delete duplicates
in vast amounts of files. Usually this applies to the maintenance of
collections of pictures or archives. It serves as well for integrity
checking purposes. Weeder is designed to be unlimited in the number of
files processed and for speed.

%prep
%setup -q

%build
%{__make} -C src \
	DATADIR=%{_datadir}/ \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}
sed -e 's,/var/weeder,%{_datadir},g' %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README history.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%dir %verify(not group mode user) %{_datadir}
