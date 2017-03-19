Name:          sailfishos-tabletui
Version:       0.2
Release:       1
Summary:       Tablet UI
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      sailfish-version >= 2.0.5, patchmanager, sailfish-content-graphics-closed-z1.0
Conflicts:     sailfishos-uithemer =< 0.3
Packager: fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
A set of patches to enable and tune the Sailfish OS tablet UI.

%files
%defattr(-,root,root,-)
/usr/share/*

%preun
patchmanager -u sailfishos-forcelargecovers
patchmanager -u sailfishos-quickactionssidebar
patchmanager -u sailfishos-quickactionssidebar-2

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/patchmanager/patches/sailfishos-forcelargecovers
rm -rf /usr/share/patchmanager/patches/sailfishos-quickactionssidebar
rm -rf /usr/share/patchmanager/patches/sailfishos-quickactionssidebar-2
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
patchmanager -u sailfishos-forcelargecovers
patchmanager -u sailfishos-quickactionssidebar
patchmanager -u sailfishos-quickactionssidebar-2
fi
fi

%changelog
* Sun Mar 19 2017 0.2
- Settings icon hidden (thanks to Ancelad).

* Sun Mar 19 2017 0.1
- First build.
