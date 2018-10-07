Name:          sailfishos-patch-tabletui
Version:       0.6
Release:       2
Summary:       Tablet UI
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      sailfish-version >= 2.2.1, patchmanager, sailfish-content-graphics-closed-z1.0
Conflicts:      sailfishos-uithemer =< 0.3, sailfishos-tabletui =< 0.2
Obsoletes:     sailfishos-tabletui =< 0.2
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
A set of patches to enable and tune the Sailfish OS tablet UI.

%files
%defattr(-,root,root,-)
/usr/share/*

%preun
patchmanager -u sailfishos-patch-forcelargecovers
patchmanager -u sailfishos-patch-tabletui
patchmanager -u sailfishos-patch-launcherpadding
patchmanager -u sailfishos-patch-launcherpadding-combined

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
	rm -rf /usr/share/patchmanager/patches/sailfishos-patch-forcelargecovers
	rm -rf /usr/share/patchmanager/patches/sailfishos-patch-tabletui
	rm -rf /usr/share/patchmanager/patches/sailfishos-patch-launcherpadding
	rm -rf /usr/share/patchmanager/patches/sailfishos-patch-launcherpadding-combined
	rm /usr/share/jolla-settings/entries/sailfishos-patch-tabletui.json
	rm -rf /usr/share/jolla-settings/pages/sailfishos-patch-tabletui
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
	echo "Upgrading"
	patchmanager -u sailfishos-patch-forcelargecovers
	patchmanager -u sailfishos-patch-tabletui
	patchmanager -u sailfishos-patch-launcherpadding
	patchmanager -u sailfishos-patch-launcherpadding-combined
fi
fi

%changelog
* Sun Oct 7 2018 0.6
- Added settings page.

* Wed Sep 5 2018 0.5
- Sailfish OS 2.2.1 compatibility.

* Fri Jun 8 2018 0.4
- Sailfish OS 2.2.0 compatibility.

* Fri Jul 21 2017 0.3
- Large padding in Launcher patch.

* Sun Mar 19 2017 0.2
- Settings icon hidden (thanks to Ancelad).

* Sun Mar 19 2017 0.1
- First build.
