import os, zipfile, argparse, requests, shutil, subprocess, tempfile

def main():
	parser = argparse.ArgumentParser(prog='SScript Archive Installer')
	parser.add_argument('version', help='SScript version to download')
	version = parser.parse_args().version.strip().lower().replace('.', ',')

	versionRequest = requests.get('https://api.github.com/repos/CobaltBar/SScript-Archive/contents/archives')
	versionRequest.raise_for_status()
	versionJson = versionRequest.json()

	versions = {versionJson[i]['name'].replace('SScript-', '').replace('.zip', '').strip().lower(): versionJson[i] for i in range(len(versionJson))}

	if not version in versions.keys():
		versionNames = [version for version in versions.keys()]
		def sort(obj):
			return int(obj.split(',')[0])
		versionNames.sort(key=sort, reverse=True)
		print('Invalid version. Valid Versions:\n' + "\n".join(versionNames))
		return
	
	haxepath = subprocess.run(['haxelib', 'config'], capture_output=True, text=True)

	if (haxepath.returncode != 0):
		print(haxepath.stderr)
		return
	
	fileRequest = requests.get(versions[version]['download_url'])
	fileRequest.raise_for_status()

	with tempfile.TemporaryDirectory() as tmpDir:
		path = os.path.join(tmpDir, 'SScript-' + str(version) + '.zip')

		with open(path, 'wb') as f:
			f.write(fileRequest.content)
			f.close()

		with zipfile.ZipFile(path, "r") as zip:
			zip.extractall(os.path.join(tmpDir, 'SScript'))

		os.remove(path)

		shutil.copytree(tmpDir, haxepath.stdout.strip(), dirs_exist_ok=True)


if __name__ == '__main__':
	main()