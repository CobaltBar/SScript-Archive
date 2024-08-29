import os, argparse, requests, subprocess, tempfile, traceback, sys

ANSI_RESET = '\033[0m'
ANSI_ULINE = '\033[4m'
ANSI_BOLD = '\033[1m'
ANSI_RED = '\033[31m'
ANSI_YLW = '\033[33m'
ANSI_BLK = '\033[30m'
ANSI_WHT_BG = '\033[47m'

VERSION = '0.0.2'

def check(config):
	config = config.replace('\\', '/')
	cwd = os.getcwd()

	if os.path.exists(os.path.join(cwd, '.haxelib')):
		# Haxelib repo detected
		if not os.path.exists(os.path.join(cwd, 'Project.xml')):
			print(f'{ANSI_RESET}{ANSI_ULINE}{ANSI_RED}No Project.xml detected!{ANSI_RESET} {ANSI_BOLD}{ANSI_YLW}(Are you sure you\'re running this in the right place?){ANSI_RESET}')
	else:
		print(f'{ANSI_RESET}{ANSI_YLW}{ANSI_BOLD}No haxelib repo detected in CWD!{ANSI_RESET} Any installs will go to {ANSI_BLK}{ANSI_WHT_BG}{ANSI_BOLD}{config}{ANSI_RESET}')

	if os.path.exists(os.path.join(config, 'SScript/.current')):
		command = input(f'{ANSI_RESET}{ANSI_YLW}{ANSI_BOLD}SScript is already installed!{ANSI_RESET} Do you wish to remove it? {ANSI_BOLD}[y/n]{ANSI_RESET} ').lower().strip()
		if command == 'y':
			print(f'Attempting to remove {ANSI_RESET}{ANSI_BOLD}SScript ' + open(os.path.join(config, 'SScript/.current'), 'r').read().strip() + f'{ANSI_RESET}...')

			try:
				subprocess.run(['haxelib', 'remove', 'SScript'])
			except Exception as uninstall_exception:
				print(f'{ANSI_RESET}{ANSI_RED}Failed to remove SScript{ANSI_RESET}')
				traceback.print_exception(uninstall_exception)
				sys.exit()
		elif command == 'n':
			print('SScript will not be removed.')
		else:
			print(f'{ANSI_RESET}{ANSI_RED}Invalid option{ANSI_RESET}: ' + command)
			sys.exit()

def main():
	header = f'SScript Archive Installer [{VERSION}]'
	print('=' * (len(header) + 6), f'\n   {header}\n' + ('=' * (len(header) + 6)))

	haxepath = subprocess.run(['haxelib', 'config'], capture_output=True, text=True)
	if (haxepath.returncode != 0):
		print(haxepath.stderr)
		return
	haxeconfig = haxepath.stdout.strip()
	check(config=haxeconfig)

	parser = argparse.ArgumentParser(prog='SScript Archive Installer')
	parser.add_argument('version', help='SScript version to download')
	version = parser.parse_args().version.strip().lower().replace('.', ',')

	versionRequest = requests.get('https://api.github.com/repos/CobaltBar/SScript-Archive/contents/archives')
	versionRequest.raise_for_status()
	versionJson = versionRequest.json()

	versions = {versionJson[i]['name'].replace('SScript-', '').replace('.zip', '').strip().lower(): versionJson[i] for i in range(len(versionJson))}

	if not version in versions.keys():
		versionNames = [version for version in versions.keys()]

		def sort_versions(version_list):
			def version_key(version):
				return tuple(map(int, version.split('-')[0].split(',')))
			return sorted(version_list, key=version_key, reverse=True)

		versionNames = sort_versions(versionNames)

		version_table = []
		columns = 6
		for chunk in range(0, len(versionNames), columns):
			version_table.append([v.replace(',', '.') for v in versionNames[chunk:chunk + columns]])

		column_width = max(max(len(item) for item in row) for row in version_table) + 2
		print(f'{ANSI_RESET}{ANSI_BOLD}{ANSI_RED}Invalid version.{ANSI_RESET} Valid versions:')
		for row in version_table:
			print("".join(item.ljust(column_width) for item in row))

		return
	
	fileRequest = requests.get(versions[version]['download_url'])
	fileRequest.raise_for_status()

	with tempfile.TemporaryDirectory() as tmpDir:
		path = os.path.join(tmpDir, 'SScript-' + str(version) + '.zip')

		with open(path, 'wb') as f:
			f.write(fileRequest.content)
			f.close()

		print(f'{ANSI_RESET}Attempting to install {ANSI_BOLD}SScript-{str(version)}.zip{ANSI_RESET}')
		try:
			subprocess.run(['haxelib', 'install', path])
		except Exception as install_exception:
			print(f'{ANSI_RESET}{ANSI_RED}Failed to install{ANSI_RESET}')
			traceback.print_exception(install_exception)


if __name__ == '__main__':
	main()