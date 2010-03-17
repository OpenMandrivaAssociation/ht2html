Name:           ht2html
Version:        2.0
Release:        %mkrel 13
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
