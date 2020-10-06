%global         __strip /bin/true
%global         debug_package %{nil}

%global         __requires_exclude ^(libQt5Gui\\.so\\..*(Qt_5_PRIVATE_API).*)$

Name:           master-pdf-editor
Version:        5.6.49
Release:        1%{?dist}
Summary:        Edit PDF documents
License:        Proprietary
URL:            https://code-industry.net/free-pdf-editor/

ExclusiveArch:  x86_64

Source0:        http://code-industry.net/public/%{name}-%{version}-qt5.x86_64.tar.gz
Source1:        %{name}-wrapper
Patch1:         %{name}-desktop.patch

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

Requires(post):     desktop-file-utils
Requires(postun):   desktop-file-utils
Requires:           openssl

%description
Master PDF Editor is the optimal solution for editing PDF files in Linux. It
enables you to create, edit, view, encrypt, sign and print interactive PDF
documents.

%prep
%autosetup -p1 -n %{name}-5

%build
# Nothing to build

%install
chrpath -d masterpdfeditor5

mkdir -p %{buildroot}%{_libdir}/%{name}
cp -afr * %{buildroot}%{_libdir}/%{name}

# Wrapper script
mkdir -p %{buildroot}%{_bindir}
cat %{SOURCE1} | sed -e 's|INSTALL_DIR|%{_libdir}/%{name}|g' \
    > %{buildroot}%{_bindir}/masterpdfeditor5
chmod +x %{buildroot}%{_bindir}/masterpdfeditor5

install -p -m 644 -D masterpdfeditor5.png %{buildroot}%{_datadir}/pixmaps/masterpdfeditor5.png
install -p -m 644 -D masterpdfeditor5.desktop %{buildroot}/%{_datadir}/applications/masterpdfeditor5.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/masterpdfeditor5.desktop

%if 0%{?rhel} == 7

%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :

%endif

%files
%doc license.txt
%{_bindir}/masterpdfeditor5
%{_datadir}/applications/masterpdfeditor5.desktop
%{_datadir}/pixmaps/masterpdfeditor5.png
%{_libdir}/%{name}

%changelog
* Tue Oct 06 2020 Simone Caronni <negativo17@gmail.com> - 5.6.49-1
- Update to 5.6.49.

* Wed Jul 24 2019 Simone Caronni <negativo17@gmail.com> - 5.4.38-1
- Update to 5.4.38.

* Mon Jun 10 2019 Simone Caronni <negativo17@gmail.com> - 5.4.20-1
- First build.
