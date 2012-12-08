Name:           ht2html
Version:        2.0
Release:        %mkrel 16
Epoch:          0
Summary:        The www.python.org Web site generator
URL:            http://ht2html.sourceforge.net/
Source0:        http://osdn.dl.sourceforge.net/ht2html/%{name}-%{version}.tar.bz2
Source1:        %{name}.sh
License:        Public Domain
Group:          Development/Python
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildArch:      noarch

%description
The www.python.org Web site generator.

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 755 %{SOURCE1} %{buildroot}%{_bindir}

%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__install} -m 755 calcroot.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 755 ht2html.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 BAWGenerator.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 Banner.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 HTParser.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 IPC8Generator.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 JPyGenerator.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 JPyLocalGenerator.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 LinkFixer.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 PDOGenerator.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 SelfGenerator.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 Sidebar.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 Skeleton.py %{buildroot}%{_datadir}/%{name}
%{__install} -m 644 StandardGenerator.py %{buildroot}%{_datadir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README doc/*.{html,png}
%{_datadir}/%{name}
%attr(0755,root,root) %{_bindir}/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0:2.0-15mdv2011.0
+ Revision: 665479
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.0-14mdv2011.0
+ Revision: 605881
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.0-13mdv2010.1
+ Revision: 522850
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0:2.0-12mdv2010.0
+ Revision: 425154
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0:2.0-11mdv2009.0
+ Revision: 221346
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0:2.0-10mdv2008.1
+ Revision: 150277
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Adam Williamson <awilliamson@mandriva.org> 0:2.0-9mdv2008.0
+ Revision: 48516
- rebuild for 2008
- Import ht2html



* Fri Sep 08 2006 David Walluck <walluck@mandriva.org> 0:2.0-8mdv2007.0
- rebuild
- change Group

* Fri Aug 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0:2.0-7mdk
- rebuild 
- spec cleanup

* Wed Jul 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0:2.0-6mdk 
- rpmbuilupdate aware

* Sun Feb 22 2004 David Walluck <walluck@linux-mandrake.com> 0:2.0-5mdk
- rebuild to fix my email address

* Sun Mar 30 2003 David Walluck <walluck@linux-mandrake.com> 2.0-4mdk
- replace my previous spec versions with Guillaume Rousse's

* Wed Mar 26 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 2.0-1mdk
- contributed by David Walluck <david@anti-microsoft.org>
- wrapper script
