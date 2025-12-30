
project(
  'coriolis-pdk-ihpsg13g2',
   version:  '2024.10.15',
   meson_version: '>= 1.2.0',
)

py       = import( 'python' ).find_installation( pure:false )
py_deps  = dependency( 'python3', required: true )
pdks_dir = py.get_install_dir() / 'pdks' / 'ihpsg13g2'
openvaf  = find_program( 'openvaf' )

ref_dir  = 'IHP-Open-PDK/ihp-sg13g2/libs.ref'
tech_dir = 'IHP-Open-PDK/ihp-sg13g2/libs.tech'

install_subdir( ref_dir , install_dir:pdks_dir )
install_subdir( tech_dir, install_dir:pdks_dir )

psp103_dir      = tech_dir / 'verilog-a' / 'psp103'
psp103_va       = files( psp103_dir / 'psp103.va' )
psp103t_va      = files( psp103_dir / 'psp103t.va' )
psp103_nqs_va   = files( psp103_dir / 'psp103_nqs.va' )

psp103     = custom_target( 'psp103'
                          , output:      'psp103.osdi'
                          , input:       psp103_va
                          , command:     [ openvaf, '@INPUT@', '-o', '@OUTPUT@' ]
                          , install:     true
                          , install_dir: pdks_dir / 'libs.tech' / 'verilog-a' / 'psp103'
                          )

psp103t    = custom_target( 'psp103t'
                          , output:      'psp103t.osdi'
                          , input:       psp103t_va
                          , command:     [ openvaf, '@INPUT@', '-o', '@OUTPUT@' ]
                          , install:     true
                          , install_dir: pdks_dir / 'libs.tech' / 'verilog-a' / 'psp103'
                          )

psp103_nqs = custom_target( 'psp103_nqs'
                          , output:      'psp103_nqs.osdi'
                          , input:       psp103_nqs_va
                          , command:     [ openvaf, '@INPUT@', '-o', '@OUTPUT@' ]
                          , install:     true
                          , install_dir: pdks_dir / 'libs.tech' / 'verilog-a' / 'psp103'
                          )
