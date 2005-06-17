Summary:	Weeder - binary file identifier
Summary(pl):	Weeder - narzêdzie do identyfikowania plików binarnych
Name:		weeder
Version:	0.9.7
Release:	0.9
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

%description -l pl
Weeder to narzêdzie pobieraj±ce odciski (sumy kontrolne i rozmiar)
plików. Po pobraniu odcisku mo¿e wy¶wietliæ albo usun±æ dplikaty du¿ej
liczby plików. Zwykle przydaje siê to przy zarz±dzaniu kolekcj±
obrazów lub archiwów. Mo¿e s³u¿yæ te¿ do sprawdzania spójno¶ci. Weeder
jest zaprojektowany tak, by dzia³a³ z nieograniczon± liczb± plików
oraz pod k±tem szybko¶ci.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C src \
	DATADIR=%{_datadir}/ \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}
sed -e 's,/var/weeder,%{_datadir},g' %{name}.1 > $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%post
# move data from old original sources
if [ -d /var/%{name} ] && [ ! -L /var/%{name} ]; then
	mv /var/%{name}/* %{_datadir}
	rmdir /var/%{name}
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README history.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%dir %attr(1777,root,root) %{_datadir}
