Name: redfish-finder 
Version: 0.3
Release: 6%{?dist}
Summary: Utility for parsing SMBIOS information and configuring canonical BMC access
BuildArch: noarch

License: GPLv2
URL: https://github.com/nhorman/redfish-finder
Source0: %url/archive/V%{version}/%{name}-%{version}.tar.gz

Patch0: redfish-finder-multi-block.patch
Patch1: hostname-null-check.patch
Patch2: hostconfig-dhcp-parse.patch

%{?systemd_requires}
BuildRequires: systemd

Requires: python3 NetworkManager dmidecode

%description
Scans Smbios information for type 42 management controller information, and uses
that to configure the appropriate network interface so that the BMC is
canonically accessible via the host name redfish-localhost

%prep
%autosetup


%build
#noop here

%install
install -D -p -m 0755 redfish-finder %{buildroot}/%{_bindir}/redfish-finder
install -D -p -m 0644 redfish-finder.1 %{buildroot}/%{_mandir}/man1/redfish-finder.1
install -D -p -m 0644 ./redfish-finder.service %{buildroot}/%{_unitdir}/redfish-finder.service

%post
%systemd_post redfish-finder.service

%preun
%systemd_preun redfish-finder.service

%postun
%systemd_postun_with_restart redfish-finder.service


%files
%doc README.md
%license COPYING
%{_bindir}/redfish-finder
%{_mandir}/man1/redfish-finder.1.*
%{_unitdir}/redfish-finder.service

%changelog
* Fri Feb 12 2021 Joel Savitz <jsavitz@redhat.com> - 0.3-6
- Fix typo in spec file (bz1951216)

* Fri Feb 12 2021 Joel Savitz <jsavitz@redhat.com> - 0.3-5
- Fix parsing HostConfig for DHCP (bz1874653)

* Thu Oct 17 2019 Neil Horman <nhorman@redhat.com> - 0.3-4
- Fix null hostname check (bz1729343)

* Mon Jul 01 2019 Neil Horman <nhorman@redhat.com> - 0.3-3
- Enhance to support multiple type 42 blocks (bz1715914)

* Fri Apr 26 2019 Neil Horman <nhorman@redhat.com> - 0.3-2
- Bump release number to test CI gating

* Mon Apr 01 2019 Neil Horman <nhorman@redhat.com> - 0.3-1
- Update to latest upstream release (bz1687111)

* Fri Oct 19 2018 Neil Horman <nhorman@redhat.com> - 0.2-1
- Update to new upstream release

* Thu Oct 04 2018 Neil Horman <nhorman@tuxdriver.com> - 0.1-3
- Fixed missing BuildRequires/Requires
- Fixed missing dist tag
- Fixed Source url

* Wed Oct 03 2018 Neil Horman <nhorman@tuxdriver.com> - 0.1-2
- Updated requires for python3
- Removed unneeded BuildRequires
- Globed the inclusion of man page
- Fixed license file tagging

* Mon Oct 01 2018 Neil Horman <nhorman@tuxdriver.com> - 0.1-1 
- Initial import

