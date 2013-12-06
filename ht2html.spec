Summary:	The www.python.org Web site generator
Name:		ht2html
Epoch:		0
Version:	2.0
Release:	18
License:	Public Domain
Group:		Development/Python
Url:		http://ht2html.sourceforge.net/
Source0:	http://osdn.dl.sourceforge.net/ht2html/%{name}-%{version}.tar.bz2
Source1:	%{name}.sh
BuildArch:	noarch
BuildRequires:	pkgconfig(python)

%description
The www.python.org Web site generator.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 755 calcroot.py %{buildroot}%{_datadir}/%{name}
install -m 755 ht2html.py %{buildroot}%{_datadir}/%{name}
install -m 644 BAWGenerator.py %{buildroot}%{_datadir}/%{name}
install -m 644 Banner.py %{buildroot}%{_datadir}/%{name}
install -m 644 HTParser.py %{buildroot}%{_datadir}/%{name}
install -m 644 IPC8Generator.py %{buildroot}%{_datadir}/%{name}
install -m 644 JPyGenerator.py %{buildroot}%{_datadir}/%{name}
install -m 644 JPyLocalGenerator.py %{buildroot}%{_datadir}/%{name}
install -m 644 LinkFixer.py %{buildroot}%{_datadir}/%{name}
install -m 644 PDOGenerator.py %{buildroot}%{_datadir}/%{name}
install -m 644 SelfGenerator.py %{buildroot}%{_datadir}/%{name}
install -m 644 Sidebar.py %{buildroot}%{_datadir}/%{name}
install -m 644 Skeleton.py %{buildroot}%{_datadir}/%{name}
install -m 644 StandardGenerator.py %{buildroot}%{_datadir}/%{name}

%files
%doc README doc/*.{html,png}
%{_datadir}/%{name}
%{_bindir}/*

