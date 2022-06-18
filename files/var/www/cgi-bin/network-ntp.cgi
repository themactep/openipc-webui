#!/usr/bin/haserl
<%in _common.cgi %>
<%
get_system_info

page_title="$tPageTitleNtpSettings"
%>
<%in _header.cgi %>
<%
if [ "$(cat /etc/TZ)" != "$TZ" ]; then
  alert_ "danger"
    h6 "$tMsgTimezoneNeedsUpdating"
    p "$tMsgPleaseRestart"
    button_link_to "$tButtonRestart" "/cgi-bin/reboot.cgi" "danger"
  _alert
fi

row_ "row-cols-1 row-cols-md-2 row-cols-xxl-4 g-3 mb-3"
  tag "datalist" "" "id=\"tz_list\""

  col_card_ "$tHeaderTimezone"
    form_ "/cgi-bin/network-tz-update.cgi" "post"
      field_text "tz_name" "list=\"tz_list\""
      field_text "tz_data" "readonly"
      button_submit "$tButtonFormSubmit" "primary"
    _form
  _col_card

  col_card_ "TimeZone Settings"
    ex "cat /etc/TZ"
    ex "echo \$TZ"
    ex "/bin/date"
  _col_card

  col_card_ "$tHeaderNtpServers"
    form_ "/cgi-bin/network-ntp-update.cgi" "post"
      for i in 0 1 2 3; do
        x=$(expr $i + 1)
        eval "ntp_server_${i}=$(sed -n ${x}p /etc/ntp.conf | cut -d' ' -f2)"
        field_text "ntp_server_${i}" "placeholder=\"${i}.pool.ntp.org\" data-pattern=\"host-ip\""
      done
      button_submit "$tButtonFormSubmit" "primary"
    _form
  _col_card

  col_card_ "NTP Settings"
    ex "cat /etc/ntp.conf"
    button_link_to "$tButtonResetToDefaults" "/cgi-bin/network-ntp-reset.cgi" "danger"
  _col_card
_row
%>

<script>
// based on https://raw.githubusercontent.com/openwrt/luci/master/modules/luci-base/luasrc/sys/zoneinfo/tzdata.lua
const TZ=[{n:'Africa/Abidjan',v:'GMT0'},{n:'Africa/Accra',v:'GMT0'},{n:'Africa/Addis Ababa',v:'EAT-3'},{n:'Africa/Algiers',v:'CET-1'},{n:'Africa/Asmara',v:'EAT-3'},{n:'Africa/Bamako',v:'GMT0'},{n:'Africa/Bangui',v:'WAT-1'},{n:'Africa/Banjul',v:'GMT0'},{n:'Africa/Bissau',v:'GMT0'},{n:'Africa/Blantyre',v:'CAT-2'},{n:'Africa/Brazzaville',v:'WAT-1'},{n:'Africa/Bujumbura',v:'CAT-2'},{n:'Africa/Cairo',v:'EET-2'},{n:'Africa/Casablanca',v:'<+01>-1'},{n:'Africa/Ceuta',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Africa/Conakry',v:'GMT0'},{n:'Africa/Dakar',v:'GMT0'},{n:'Africa/Dar es Salaam',v:'EAT-3'},{n:'Africa/Djibouti',v:'EAT-3'},{n:'Africa/Douala',v:'WAT-1'},{n:'Africa/El Aaiun',v:'<+01>-1'},{n:'Africa/Freetown',v:'GMT0'},{n:'Africa/Gaborone',v:'CAT-2'},{n:'Africa/Harare',v:'CAT-2'},{n:'Africa/Johannesburg',v:'SAST-2'},{n:'Africa/Juba',v:'CAT-2'},{n:'Africa/Kampala',v:'EAT-3'},{n:'Africa/Khartoum',v:'CAT-2'},{n:'Africa/Kigali',v:'CAT-2'},{n:'Africa/Kinshasa',v:'WAT-1'},{n:'Africa/Lagos',v:'WAT-1'},{n:'Africa/Libreville',v:'WAT-1'},{n:'Africa/Lome',v:'GMT0'},{n:'Africa/Luanda',v:'WAT-1'},{n:'Africa/Lubumbashi',v:'CAT-2'},{n:'Africa/Lusaka',v:'CAT-2'},{n:'Africa/Malabo',v:'WAT-1'},{n:'Africa/Maputo',v:'CAT-2'},{n:'Africa/Maseru',v:'SAST-2'},{n:'Africa/Mbabane',v:'SAST-2'},{n:'Africa/Mogadishu',v:'EAT-3'},{n:'Africa/Monrovia',v:'GMT0'},{n:'Africa/Nairobi',v:'EAT-3'},{n:'Africa/Ndjamena',v:'WAT-1'},{n:'Africa/Niamey',v:'WAT-1'},{n:'Africa/Nouakchott',v:'GMT0'},{n:'Africa/Ouagadougou',v:'GMT0'},{n:'Africa/Porto-Novo',v:'WAT-1'},{n:'Africa/Sao Tome',v:'GMT0'},{n:'Africa/Tripoli',v:'EET-2'},{n:'Africa/Tunis',v:'CET-1'},{n:'Africa/Windhoek',v:'CAT-2'},{n:'America/Adak',v:'HST10HDT,M3.2.0,M11.1.0'},{n:'America/Anchorage',v:'AKST9AKDT,M3.2.0,M11.1.0'},{n:'America/Anguilla',v:'AST4'},{n:'America/Antigua',v:'AST4'},{n:'America/Araguaina',v:'<-03>3'},{n:'America/Argentina/Buenos Aires',v:'<-03>3'},{n:'America/Argentina/Catamarca',v:'<-03>3'},{n:'America/Argentina/Cordoba',v:'<-03>3'},{n:'America/Argentina/Jujuy',v:'<-03>3'},{n:'America/Argentina/La Rioja',v:'<-03>3'},{n:'America/Argentina/Mendoza',v:'<-03>3'},{n:'America/Argentina/Rio Gallegos',v:'<-03>3'},{n:'America/Argentina/Salta',v:'<-03>3'},{n:'America/Argentina/San Juan',v:'<-03>3'},{n:'America/Argentina/San Luis',v:'<-03>3'},{n:'America/Argentina/Tucuman',v:'<-03>3'},{n:'America/Argentina/Ushuaia',v:'<-03>3'},{n:'America/Aruba',v:'AST4'},{n:'America/Asuncion',v:'<-04>4<-03>,M10.1.0/0,M3.4.0/0'},{n:'America/Atikokan',v:'EST5'},{n:'America/Bahia',v:'<-03>3'},{n:'America/Bahia Banderas',v:'CST6CDT,M4.1.0,M10.5.0'},{n:'America/Barbados',v:'AST4'},{n:'America/Belem',v:'<-03>3'},{n:'America/Belize',v:'CST6'},{n:'America/Blanc-Sablon',v:'AST4'},{n:'America/Boa Vista',v:'<-04>4'},{n:'America/Bogota',v:'<-05>5'},{n:'America/Boise',v:'MST7MDT,M3.2.0,M11.1.0'},{n:'America/Cambridge Bay',v:'MST7MDT,M3.2.0,M11.1.0'},{n:'America/Campo Grande',v:'<-04>4'},{n:'America/Cancun',v:'EST5'},{n:'America/Caracas',v:'<-04>4'},{n:'America/Cayenne',v:'<-03>3'},{n:'America/Cayman',v:'EST5'},{n:'America/Chicago',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/Chihuahua',v:'MST7MDT,M4.1.0,M10.5.0'},{n:'America/Costa Rica',v:'CST6'},{n:'America/Creston',v:'MST7'},{n:'America/Cuiaba',v:'<-04>4'},{n:'America/Curacao',v:'AST4'},{n:'America/Danmarkshavn',v:'GMT0'},{n:'America/Dawson',v:'MST7'},{n:'America/Dawson Creek',v:'MST7'},{n:'America/Denver',v:'MST7MDT,M3.2.0,M11.1.0'},{n:'America/Detroit',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Dominica',v:'AST4'},{n:'America/Edmonton',v:'MST7MDT,M3.2.0,M11.1.0'},{n:'America/Eirunepe',v:'<-05>5'},{n:'America/El Salvador',v:'CST6'},{n:'America/Fort Nelson',v:'MST7'},{n:'America/Fortaleza',v:'<-03>3'},{n:'America/Glace Bay',v:'AST4ADT,M3.2.0,M11.1.0'},{n:'America/Goose Bay',v:'AST4ADT,M3.2.0,M11.1.0'},{n:'America/Grand Turk',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Grenada',v:'AST4'},{n:'America/Guadeloupe',v:'AST4'},{n:'America/Guatemala',v:'CST6'},{n:'America/Guayaquil',v:'<-05>5'},{n:'America/Guyana',v:'<-04>4'},{n:'America/Halifax',v:'AST4ADT,M3.2.0,M11.1.0'},{n:'America/Havana',v:'CST5CDT,M3.2.0/0,M11.1.0/1'},{n:'America/Hermosillo',v:'MST7'},{n:'America/Indiana/Indianapolis',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Indiana/Knox',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/Indiana/Marengo',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Indiana/Petersburg',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Indiana/Tell City',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/Indiana/Vevay',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Indiana/Vincennes',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Indiana/Winamac',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Inuvik',v:'MST7MDT,M3.2.0,M11.1.0'},{n:'America/Iqaluit',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Jamaica',v:'EST5'},{n:'America/Juneau',v:'AKST9AKDT,M3.2.0,M11.1.0'},{n:'America/Kentucky/Louisville',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Kentucky/Monticello',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Kralendijk',v:'AST4'},{n:'America/La Paz',v:'<-04>4'},{n:'America/Lima',v:'<-05>5'},{n:'America/Los Angeles',v:'PST8PDT,M3.2.0,M11.1.0'},{n:'America/Lower Princes',v:'AST4'},{n:'America/Maceio',v:'<-03>3'},{n:'America/Managua',v:'CST6'},{n:'America/Manaus',v:'<-04>4'},{n:'America/Marigot',v:'AST4'},{n:'America/Martinique',v:'AST4'},{n:'America/Matamoros',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/Mazatlan',v:'MST7MDT,M4.1.0,M10.5.0'},{n:'America/Menominee',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/Merida',v:'CST6CDT,M4.1.0,M10.5.0'},{n:'America/Metlakatla',v:'AKST9AKDT,M3.2.0,M11.1.0'},{n:'America/Mexico City',v:'CST6CDT,M4.1.0,M10.5.0'},{n:'America/Miquelon',v:'<-03>3<-02>,M3.2.0,M11.1.0'},{n:'America/Moncton',v:'AST4ADT,M3.2.0,M11.1.0'},{n:'America/Monterrey',v:'CST6CDT,M4.1.0,M10.5.0'},{n:'America/Montevideo',v:'<-03>3'},{n:'America/Montserrat',v:'AST4'},{n:'America/Nassau',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/New York',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Nipigon',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Nome',v:'AKST9AKDT,M3.2.0,M11.1.0'},{n:'America/Noronha',v:'<-02>2'},{n:'America/North Dakota/Beulah',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/North Dakota/Center',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/North Dakota/New Salem',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/Nuuk',v:'<-03>3<-02>,M3.5.0/-2,M10.5.0/-1'},{n:'America/Ojinaga',v:'MST7MDT,M3.2.0,M11.1.0'},{n:'America/Panama',v:'EST5'},{n:'America/Pangnirtung',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Paramaribo',v:'<-03>3'},{n:'America/Phoenix',v:'MST7'},{n:'America/Port of Spain',v:'AST4'},{n:'America/Port-au-Prince',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Porto Velho',v:'<-04>4'},{n:'America/Puerto Rico',v:'AST4'},{n:'America/Punta Arenas',v:'<-03>3'},{n:'America/Rainy River',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/Rankin Inlet',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/Recife',v:'<-03>3'},{n:'America/Regina',v:'CST6'},{n:'America/Resolute',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/Rio Branco',v:'<-05>5'},{n:'America/Santarem',v:'<-03>3'},{n:'America/Santiago',v:'<-04>4<-03>,M9.1.6/24,M4.1.6/24'},{n:'America/Santo Domingo',v:'AST4'},{n:'America/Sao Paulo',v:'<-03>3'},{n:'America/Scoresbysund',v:'<-01>1<+00>,M3.5.0/0,M10.5.0/1'},{n:'America/Sitka',v:'AKST9AKDT,M3.2.0,M11.1.0'},{n:'America/St Barthelemy',v:'AST4'},{n:'America/St Johns',v:'NST3:30NDT,M3.2.0,M11.1.0'},{n:'America/St Kitts',v:'AST4'},{n:'America/St Lucia',v:'AST4'},{n:'America/St Thomas',v:'AST4'},{n:'America/St Vincent',v:'AST4'},{n:'America/Swift Current',v:'CST6'},{n:'America/Tegucigalpa',v:'CST6'},{n:'America/Thule',v:'AST4ADT,M3.2.0,M11.1.0'},{n:'America/Thunder Bay',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Tijuana',v:'PST8PDT,M3.2.0,M11.1.0'},{n:'America/Toronto',v:'EST5EDT,M3.2.0,M11.1.0'},{n:'America/Tortola',v:'AST4'},{n:'America/Vancouver',v:'PST8PDT,M3.2.0,M11.1.0'},{n:'America/Whitehorse',v:'MST7'},{n:'America/Winnipeg',v:'CST6CDT,M3.2.0,M11.1.0'},{n:'America/Yakutat',v:'AKST9AKDT,M3.2.0,M11.1.0'},{n:'America/Yellowknife',v:'MST7MDT,M3.2.0,M11.1.0'},{n:'Antarctica/Casey',v:'<+11>-11'},{n:'Antarctica/Davis',v:'<+07>-7'},{n:'Antarctica/DumontDUrville',v:'<+10>-10'},{n:'Antarctica/Macquarie',v:'AEST-10AEDT,M10.1.0,M4.1.0/3'},{n:'Antarctica/Mawson',v:'<+05>-5'},{n:'Antarctica/McMurdo',v:'NZST-12NZDT,M9.5.0,M4.1.0/3'},{n:'Antarctica/Palmer',v:'<-03>3'},{n:'Antarctica/Rothera',v:'<-03>3'},{n:'Antarctica/Syowa',v:'<+03>-3'},{n:'Antarctica/Troll',v:'<+00>0<+02>-2,M3.5.0/1,M10.5.0/3'},{n:'Antarctica/Vostok',v:'<+06>-6'},{n:'Arctic/Longyearbyen',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Asia/Aden',v:'<+03>-3'},{n:'Asia/Almaty',v:'<+06>-6'},{n:'Asia/Amman',v:'EET-2EEST,M2.5.4/24,M10.5.5/1'},{n:'Asia/Anadyr',v:'<+12>-12'},{n:'Asia/Aqtau',v:'<+05>-5'},{n:'Asia/Aqtobe',v:'<+05>-5'},{n:'Asia/Ashgabat',v:'<+05>-5'},{n:'Asia/Atyrau',v:'<+05>-5'},{n:'Asia/Baghdad',v:'<+03>-3'},{n:'Asia/Bahrain',v:'<+03>-3'},{n:'Asia/Baku',v:'<+04>-4'},{n:'Asia/Bangkok',v:'<+07>-7'},{n:'Asia/Barnaul',v:'<+07>-7'},{n:'Asia/Beirut',v:'EET-2EEST,M3.5.0/0,M10.5.0/0'},{n:'Asia/Bishkek',v:'<+06>-6'},{n:'Asia/Brunei',v:'<+08>-8'},{n:'Asia/Chita',v:'<+09>-9'},{n:'Asia/Choibalsan',v:'<+08>-8'},{n:'Asia/Colombo',v:'<+0530>-5:30'},{n:'Asia/Damascus',v:'EET-2EEST,M3.5.5/0,M10.5.5/0'},{n:'Asia/Dhaka',v:'<+06>-6'},{n:'Asia/Dili',v:'<+09>-9'},{n:'Asia/Dubai',v:'<+04>-4'},{n:'Asia/Dushanbe',v:'<+05>-5'},{n:'Asia/Famagusta',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Asia/Gaza',v:'EET-2EEST,M3.4.4/48,M10.5.5/1'},{n:'Asia/Hebron',v:'EET-2EEST,M3.4.4/48,M10.5.5/1'},{n:'Asia/Ho Chi Minh',v:'<+07>-7'},{n:'Asia/Hong Kong',v:'HKT-8'},{n:'Asia/Hovd',v:'<+07>-7'},{n:'Asia/Irkutsk',v:'<+08>-8'},{n:'Asia/Jakarta',v:'WIB-7'},{n:'Asia/Jayapura',v:'WIT-9'},{n:'Asia/Jerusalem',v:'IST-2IDT,M3.4.4/26,M10.5.0'},{n:'Asia/Kabul',v:'<+0430>-4:30'},{n:'Asia/Kamchatka',v:'<+12>-12'},{n:'Asia/Karachi',v:'PKT-5'},{n:'Asia/Kathmandu',v:'<+0545>-5:45'},{n:'Asia/Khandyga',v:'<+09>-9'},{n:'Asia/Kolkata',v:'IST-5:30'},{n:'Asia/Krasnoyarsk',v:'<+07>-7'},{n:'Asia/Kuala Lumpur',v:'<+08>-8'},{n:'Asia/Kuching',v:'<+08>-8'},{n:'Asia/Kuwait',v:'<+03>-3'},{n:'Asia/Macau',v:'CST-8'},{n:'Asia/Magadan',v:'<+11>-11'},{n:'Asia/Makassar',v:'WITA-8'},{n:'Asia/Manila',v:'PST-8'},{n:'Asia/Muscat',v:'<+04>-4'},{n:'Asia/Nicosia',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Asia/Novokuznetsk',v:'<+07>-7'},{n:'Asia/Novosibirsk',v:'<+07>-7'},{n:'Asia/Omsk',v:'<+06>-6'},{n:'Asia/Oral',v:'<+05>-5'},{n:'Asia/Phnom Penh',v:'<+07>-7'},{n:'Asia/Pontianak',v:'WIB-7'},{n:'Asia/Pyongyang',v:'KST-9'},{n:'Asia/Qatar',v:'<+03>-3'},{n:'Asia/Qostanay',v:'<+06>-6'},{n:'Asia/Qyzylorda',v:'<+05>-5'},{n:'Asia/Riyadh',v:'<+03>-3'},{n:'Asia/Sakhalin',v:'<+11>-11'},{n:'Asia/Samarkand',v:'<+05>-5'},{n:'Asia/Seoul',v:'KST-9'},{n:'Asia/Shanghai',v:'CST-8'},{n:'Asia/Singapore',v:'<+08>-8'},{n:'Asia/Srednekolymsk',v:'<+11>-11'},{n:'Asia/Taipei',v:'CST-8'},{n:'Asia/Tashkent',v:'<+05>-5'},{n:'Asia/Tbilisi',v:'<+04>-4'},{n:'Asia/Tehran',v:'<+0330>-3:30<+0430>,J79/24,J263/24'},{n:'Asia/Thimphu',v:'<+06>-6'},{n:'Asia/Tokyo',v:'JST-9'},{n:'Asia/Tomsk',v:'<+07>-7'},{n:'Asia/Ulaanbaatar',v:'<+08>-8'},{n:'Asia/Urumqi',v:'<+06>-6'},{n:'Asia/Ust-Nera',v:'<+10>-10'},{n:'Asia/Vientiane',v:'<+07>-7'},{n:'Asia/Vladivostok',v:'<+10>-10'},{n:'Asia/Yakutsk',v:'<+09>-9'},{n:'Asia/Yangon',v:'<+0630>-6:30'},{n:'Asia/Yekaterinburg',v:'<+05>-5'},{n:'Asia/Yerevan',v:'<+04>-4'},{n:'Atlantic/Azores',v:'<-01>1<+00>,M3.5.0/0,M10.5.0/1'},{n:'Atlantic/Bermuda',v:'AST4ADT,M3.2.0,M11.1.0'},{n:'Atlantic/Canary',v:'WET0WEST,M3.5.0/1,M10.5.0'},{n:'Atlantic/Cape Verde',v:'<-01>1'},{n:'Atlantic/Faroe',v:'WET0WEST,M3.5.0/1,M10.5.0'},{n:'Atlantic/Madeira',v:'WET0WEST,M3.5.0/1,M10.5.0'},{n:'Atlantic/Reykjavik',v:'GMT0'},{n:'Atlantic/South Georgia',v:'<-02>2'},{n:'Atlantic/St Helena',v:'GMT0'},{n:'Atlantic/Stanley',v:'<-03>3'},{n:'Australia/Adelaide',v:'ACST-9:30ACDT,M10.1.0,M4.1.0/3'},{n:'Australia/Brisbane',v:'AEST-10'},{n:'Australia/Broken Hill',v:'ACST-9:30ACDT,M10.1.0,M4.1.0/3'},{n:'Australia/Darwin',v:'ACST-9:30'},{n:'Australia/Eucla',v:'<+0845>-8:45'},{n:'Australia/Hobart',v:'AEST-10AEDT,M10.1.0,M4.1.0/3'},{n:'Australia/Lindeman',v:'AEST-10'},{n:'Australia/Lord Howe',v:'<+1030>-10:30<+11>-11,M10.1.0,M4.1.0'},{n:'Australia/Melbourne',v:'AEST-10AEDT,M10.1.0,M4.1.0/3'},{n:'Australia/Perth',v:'AWST-8'},{n:'Australia/Sydney',v:'AEST-10AEDT,M10.1.0,M4.1.0/3'},{n:'Etc/GMT',v:'GMT0'},{n:'Etc/GMT+1',v:'<-01>1'},{n:'Etc/GMT+10',v:'<-10>10'},{n:'Etc/GMT+11',v:'<-11>11'},{n:'Etc/GMT+12',v:'<-12>12'},{n:'Etc/GMT+2',v:'<-02>2'},{n:'Etc/GMT+3',v:'<-03>3'},{n:'Etc/GMT+4',v:'<-04>4'},{n:'Etc/GMT+5',v:'<-05>5'},{n:'Etc/GMT+6',v:'<-06>6'},{n:'Etc/GMT+7',v:'<-07>7'},{n:'Etc/GMT+8',v:'<-08>8'},{n:'Etc/GMT+9',v:'<-09>9'},{n:'Etc/GMT-1',v:'<+01>-1'},{n:'Etc/GMT-10',v:'<+10>-10'},{n:'Etc/GMT-11',v:'<+11>-11'},{n:'Etc/GMT-12',v:'<+12>-12'},{n:'Etc/GMT-13',v:'<+13>-13'},{n:'Etc/GMT-14',v:'<+14>-14'},{n:'Etc/GMT-2',v:'<+02>-2'},{n:'Etc/GMT-3',v:'<+03>-3'},{n:'Etc/GMT-4',v:'<+04>-4'},{n:'Etc/GMT-5',v:'<+05>-5'},{n:'Etc/GMT-6',v:'<+06>-6'},{n:'Etc/GMT-7',v:'<+07>-7'},{n:'Etc/GMT-8',v:'<+08>-8'},{n:'Etc/GMT-9',v:'<+09>-9'},{n:'Europe/Amsterdam',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Andorra',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Astrakhan',v:'<+04>-4'},{n:'Europe/Athens',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Belgrade',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Berlin',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Bratislava',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Brussels',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Bucharest',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Budapest',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Busingen',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Chisinau',v:'EET-2EEST,M3.5.0,M10.5.0/3'},{n:'Europe/Copenhagen',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Dublin',v:'IST-1GMT0,M10.5.0,M3.5.0/1'},{n:'Europe/Gibraltar',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Guernsey',v:'GMT0BST,M3.5.0/1,M10.5.0'},{n:'Europe/Helsinki',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Isle of Man',v:'GMT0BST,M3.5.0/1,M10.5.0'},{n:'Europe/Istanbul',v:'<+03>-3'},{n:'Europe/Jersey',v:'GMT0BST,M3.5.0/1,M10.5.0'},{n:'Europe/Kaliningrad',v:'EET-2'},{n:'Europe/Kiev',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Kirov',v:'<+03>-3'},{n:'Europe/Lisbon',v:'WET0WEST,M3.5.0/1,M10.5.0'},{n:'Europe/Ljubljana',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/London',v:'GMT0BST,M3.5.0/1,M10.5.0'},{n:'Europe/Luxembourg',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Madrid',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Malta',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Mariehamn',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Minsk',v:'<+03>-3'},{n:'Europe/Monaco',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Moscow',v:'MSK-3'},{n:'Europe/Oslo',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Paris',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Podgorica',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Prague',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Riga',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Rome',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Samara',v:'<+04>-4'},{n:'Europe/San Marino',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Sarajevo',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Saratov',v:'<+04>-4'},{n:'Europe/Simferopol',v:'MSK-3'},{n:'Europe/Skopje',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Sofia',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Stockholm',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Tallinn',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Tirane',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Ulyanovsk',v:'<+04>-4'},{n:'Europe/Uzhgorod',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Vaduz',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Vatican',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Vienna',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Vilnius',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Volgograd',v:'<+03>-3'},{n:'Europe/Warsaw',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Zagreb',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Europe/Zaporozhye',v:'EET-2EEST,M3.5.0/3,M10.5.0/4'},{n:'Europe/Zurich',v:'CET-1CEST,M3.5.0,M10.5.0/3'},{n:'Indian/Antananarivo',v:'EAT-3'},{n:'Indian/Chagos',v:'<+06>-6'},{n:'Indian/Christmas',v:'<+07>-7'},{n:'Indian/Cocos',v:'<+0630>-6:30'},{n:'Indian/Comoro',v:'EAT-3'},{n:'Indian/Kerguelen',v:'<+05>-5'},{n:'Indian/Mahe',v:'<+04>-4'},{n:'Indian/Maldives',v:'<+05>-5'},{n:'Indian/Mauritius',v:'<+04>-4'},{n:'Indian/Mayotte',v:'EAT-3'},{n:'Indian/Reunion',v:'<+04>-4'},{n:'Pacific/Apia',v:'<+13>-13'},{n:'Pacific/Auckland',v:'NZST-12NZDT,M9.5.0,M4.1.0/3'},{n:'Pacific/Bougainville',v:'<+11>-11'},{n:'Pacific/Chatham',v:'<+1245>-12:45<+1345>,M9.5.0/2:45,M4.1.0/3:45'},{n:'Pacific/Chuuk',v:'<+10>-10'},{n:'Pacific/Easter',v:'<-06>6<-05>,M9.1.6/22,M4.1.6/22'},{n:'Pacific/Efate',v:'<+11>-11'},{n:'Pacific/Fakaofo',v:'<+13>-13'},{n:'Pacific/Fiji',v:'<+12>-12<+13>,M11.2.0,M1.2.3/99'},{n:'Pacific/Funafuti',v:'<+12>-12'},{n:'Pacific/Galapagos',v:'<-06>6'},{n:'Pacific/Gambier',v:'<-09>9'},{n:'Pacific/Guadalcanal',v:'<+11>-11'},{n:'Pacific/Guam',v:'ChST-10'},{n:'Pacific/Honolulu',v:'HST10'},{n:'Pacific/Kanton',v:'<+13>-13'},{n:'Pacific/Kiritimati',v:'<+14>-14'},{n:'Pacific/Kosrae',v:'<+11>-11'},{n:'Pacific/Kwajalein',v:'<+12>-12'},{n:'Pacific/Majuro',v:'<+12>-12'},{n:'Pacific/Marquesas',v:'<-0930>9:30'},{n:'Pacific/Midway',v:'SST11'},{n:'Pacific/Nauru',v:'<+12>-12'},{n:'Pacific/Niue',v:'<-11>11'},{n:'Pacific/Norfolk',v:'<+11>-11<+12>,M10.1.0,M4.1.0/3'},{n:'Pacific/Noumea',v:'<+11>-11'},{n:'Pacific/Pago Pago',v:'SST11'},{n:'Pacific/Palau',v:'<+09>-9'},{n:'Pacific/Pitcairn',v:'<-08>8'},{n:'Pacific/Pohnpei',v:'<+11>-11'},{n:'Pacific/Port Moresby',v:'<+10>-10'},{n:'Pacific/Rarotonga',v:'<-10>10'},{n:'Pacific/Saipan',v:'ChST-10'},{n:'Pacific/Tahiti',v:'<-10>10'},{n:'Pacific/Tarawa',v:'<+12>-12'},{n:'Pacific/Tongatapu',v:'<+13>-13'},{n:'Pacific/Wake',v:'<+12>-12'},{n:'Pacific/Wallis',v:'<+12>-12'}];

function findTimezone(tz) {
  return tz.n == $("#tz_name").value;
}

function updateTimezone() {
  const tz = TZ.filter(findTimezone);
  if (tz.length == 0) {
    $("#tz_data").value = "";
  } else {
    $("#tz_data").value = tz[0].v;
  }
}

function useBrowserTimezone(event) {
  event.preventDefault();
  $("#tz_name").value = Intl.DateTimeFormat().resolvedOptions().timeZone;
  updateTimezone();
}

window.addEventListener('load', () => {
  if (navigator.userAgent.includes("Android") && navigator.userAgent.includes("Firefox")) {
    const inp = $("#tz_name");
    const sel = document.createElement("select");
    sel.classList.add("form-select");
    sel.name = "tz_name";
    sel.id = "tz_name";
    sel.options.add(new Option());
    let opt;
    TZ.forEach(function(tz) {
      opt = new Option(tz.n);
      opt.selected = (tz.n == inp.value);
      sel.options.add(opt);
    });
    inp.replaceWith(sel);
  } else {
    const el = $("#tz_list");
    el.innerHTML="";
    TZ.forEach(function(tz) {
      const o = document.createElement("option");
      o.value = tz.n;
      el.appendChild(o);
    });
  }
  $("#tz_name").addEventListener("focus", ev => ev.target.select());
  $("#tz_name").addEventListener("selectionchange", updateTimezone);
  $("#tz_name").addEventListener("change", updateTimezone);
  $("#frombrowser").addEventListener("click", useBrowserTimezone);
  updateTimezone();
});
</script>

<%in _footer.cgi %>
