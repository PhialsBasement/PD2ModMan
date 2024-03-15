import platform
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
from urllib.parse import unquote
def download_dependency_mod(mod_number):
    # Open the mod page
    driver2 = webdriver.Chrome()  # Make sure you have the appropriate webdriver installed
    mod_url = f"https://modworkshop.net/mod/{mod_number}"
    dependencies_url = f"{mod_url}?tab=instructions"
    driver2.get(dependencies_url)
    mod_name = driver2.find_elements(By.CSS_SELECTOR, "span[class='mod-title']")[0]
    dependency_links = driver2.find_elements(By.CSS_SELECTOR, "a[href^='/mod/']")
    for dependency_link in dependency_links:
        if(dependency_link.accessible_name != "Thumbnail" and  dependency_link.accessible_name != "BeardLib" and dependency_link.accessible_name != "SuperBLT" and not dependency_link.accessible_name.__contains__(" Download") and not dependency_link.accessible_name == mod_name.text):
            dependency_mod_number = dependency_link.get_attribute("href").split("/")[-1]
            download_dependency_mod(dependency_mod_number)

    instructions_url = dependencies_url
    driver2.get(mod_url)
    # Find the download button
    download_button = driver2.find_element(By.CSS_SELECTOR, "a.button.button-primary.large-button.flex-1")

    # Get the download link
    download_link = download_button.get_attribute("href")
    driver2.get(download_link)
    download_link = WebDriverWait(driver2, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[download][href*='storage.modworkshop.net']"))
    )
    download_link = download_link[0].get_attribute("href")
    # Download the mod file
    response = requests.get(download_link)

    # Extract the filename from the Content-Disposition header
    content_disposition = response.headers.get("Content-Disposition")
    if content_disposition:
        filename = unquote(content_disposition.split("filename=")[1].strip('"'))
    else:
        filename = os.path.basename(download_link.split("?")[0])


    # Check if the instructions page contains "mod_overrides"

    driver2.get(instructions_url)
    instructions_text = WebDriverWait(driver2, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "nav-menu-content"))
    )
    instructions_text = instructions_text[0].text

    if "CustomOST" in instructions_text or "customost" in instructions_text or "Customost" in instructions_text or "customOST" in instructions_text or "CustomOst" in instructions_text:
        # Create the "assets/mod_overrides" folder if it doesn't exist
        customost_folder = os.path.join(payday2_path, "mods", "CustomOSTTracks")
        os.makedirs(customost_folder, exist_ok=True)

        # Save the downloaded ZIP file temporarily
        zip_file_path = os.path.join(customost_folder, filename)
    elif "mod_overrides" in instructions_text:
        # Create the "assets/mod_overrides" folder if it doesn't exist
        mod_overrides_folder = os.path.join(payday2_path, "assets", "mod_overrides")
        os.makedirs(mod_overrides_folder, exist_ok=True)

        # Save the downloaded ZIP file temporarily
        zip_file_path = os.path.join(mod_overrides_folder, filename)
    else:
        # Create the "mods" folder if it doesn't exist
        mods_folder = os.path.join(payday2_path, "mods")
        os.makedirs(mods_folder, exist_ok=True)

        # Save the downloaded ZIP file temporarily
        zip_file_path = os.path.join(mods_folder, filename)

    with open(zip_file_path, "wb") as file:
        file.write(response.content)

    # Extract the contents of the ZIP file to the appropriate folder
    if not zip_file_path.__contains__("rar"):
        with zipfile.ZipFile(zip_file_path, "r") as zip_file:
            if "CustomOST" in instructions_text or "customost" in instructions_text or "Customost" in instructions_text or "customOST" in instructions_text or "CustomOst" in instructions_text:
                zip_file.extractall(customost_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {customost_folder}")
            elif "mod_overrides" in instructions_text:
                zip_file.extractall(mod_overrides_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {mod_overrides_folder}")
            else:
                zip_file.extractall(mods_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {mods_folder}")
    else:
        import rarfile
        rarfile.UNRAR_TOOL = os.path.join(os.path.dirname(__file__), "bin", "unrar.exe")
        with rarfile.RarFile(zip_file_path, "r") as rar_file:
            if "CustomOST" in instructions_text or "customost" in instructions_text or "Customost" in instructions_text or "customOST" in instructions_text or "CustomOst" in instructions_text:
                rar_file.extractall(customost_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {customost_folder}")
            elif "mod_overrides" in instructions_text:
                rar_file.extractall(mod_overrides_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {mod_overrides_folder}")
            else:
                rar_file.extractall(mods_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {mods_folder}")

    # Delete the downloaded ZIP file
    os.remove(zip_file_path)


    driver2.close()












# Configure the webdriver (e.g., Chrome)
driver = webdriver.Chrome()  # Make sure you have the appropriate webdriver installed






def search_mods(query):
    search_url = f"https://modworkshop.net/g/payday-2?query={query}"
    driver.get(search_url)

    # Wait for the presence of the mod-title elements
    mod_title_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "mod-title"))
    )

    # Display the list of mods
    for i, mod_title in enumerate(mod_title_elements, start=1):
        title = mod_title.text
        print(f"{i}. {title}")
    print("Enter 99 to search again!")
    # Prompt the user to select a mod or search again
    while True:
        selected_index = int(input("Enter the index of the mod you want to download (or 99 to search again): ")) - 1

        if selected_index == 98:
            query = input("Enter the text to search for mods: ")
            search_mods(query)
            break
        elif 0 <= selected_index < len(mod_title_elements):
            return mod_title_elements[selected_index]
        else:
            print("Invalid selection. Please try again.")

while True:
    # Open the website
    url = "https://modworkshop.net/g/payday-2"
    driver.get(url)
    # Check if Payday 2 is installed
    payday2_path = r"C:\Program Files (x86)\Steam\steamapps\common\PAYDAY 2"
    if not os.path.exists(payday2_path):
        print("Payday 2 not found. Please ensure the game is installed.")
        driver.quit()
        exit()

    # Check if IPHLPAPI.dll or WSOCK32.dll exist in the Payday 2 install folder
    iphlpapi_path = os.path.join(payday2_path, "IPHLPAPI.dll")
    wsock32_path = os.path.join(payday2_path, "WSOCK32.dll")

    if not os.path.exists(iphlpapi_path) and not os.path.exists(wsock32_path):
        # Check if the OS is Windows 10 or higher
        if os.name == 'nt' and int(platform.release()) >= 10:
            # Download and extract payday2bltwsockdll-3.3.8.zip
            dll_url = "https://sblt-update.znix.xyz/pd2update/download/payday2bltwsockdll/payday2bltwsockdll-3.3.8.zip"
            dll_response = requests.get(dll_url)
            dll_zip_path = os.path.join(payday2_path, "payday2bltwsockdll-3.3.8.zip")
            with open(dll_zip_path, "wb") as dll_zip_file:
                dll_zip_file.write(dll_response.content)

            # Extract the contents of the ZIP file to the Payday 2 install folder
            with zipfile.ZipFile(dll_zip_path, 'r') as dll_zip:
                dll_zip.extractall(payday2_path)

            # Remove the downloaded ZIP file
            os.remove(dll_zip_path)
            print("IPHLPAPI.dll and WSOCK32.dll have been downloaded and extracted.")
        else:
            print("IPHLPAPI.dll and WSOCK32.dll not found, and the OS is not Windows 10 or higher.")

    # Check if BreadLib exists in the Payday 2 mods folder
    breadlib_path = os.path.join(payday2_path, "mods", "BeardLib")
    if not os.path.exists(breadlib_path):
        # Download and extract BeardLib.zip
        breadlib_url = "https://storage.modworkshop.net/mods/files/14924_11_A61DYJvDsVyAJONqPdNa5sUPxSdcIe8NGkpiU2Jr.zip?response-content-disposition=attachment;filename=BeardLib.zip"
        breadlib_response = requests.get(breadlib_url)
        breadlib_zip_path = os.path.join(payday2_path, "mods", "BeardLib.zip")
        with open(breadlib_zip_path, "wb") as breadlib_zip_file:
            breadlib_zip_file.write(breadlib_response.content)

        # Extract the contents of the ZIP file to the Payday 2 mods folder
        with zipfile.ZipFile(breadlib_zip_path, 'r') as breadlib_zip:
            breadlib_zip.extractall(os.path.join(payday2_path, "mods"))

        # Remove the downloaded ZIP file
        os.remove(breadlib_zip_path)
        print("BeardLib has been downloaded and extracted.")
    # Wait for the presence of the mod-title elements
    mod_title_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "mod-title"))
    )

    # Display the list of mods
    for i, mod_title in enumerate(mod_title_elements, start=1):
        title = mod_title.text
        print(f"{i}. {title}")
    print("Enter 99 to search again!")
    # Prompt the user to select a mod or search for mods
    while True:
        selected_index = int(input("Enter the index of the mod you want to download (or 99 to search for mods): ")) - 1
        if selected_index == 98:
            query = input("Enter the text to search for mods: ")
            selected_mod_title = search_mods(query)
            dependencies_url = f"{selected_mod_title.get_attribute('href')}?tab=instructions"
            mod_link = selected_mod_title.get_attribute("href")
            driver.get(dependencies_url)

            dependency_links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/mod/']")
            for dependency_link in dependency_links:
                if(dependency_link.accessible_name != "Thumbnail" and  dependency_link.accessible_name != "BeardLib" and dependency_link.accessible_name != "SuperBLT" and not dependency_link.accessible_name.__contains__(" Download")):
                    dependency_mod_number = dependency_link.get_attribute("href").split("/")[-1]
                    download_dependency_mod(dependency_mod_number)
            break
        elif 0 <= selected_index < len(mod_title_elements):
            dependencies_url = f"{mod_title_elements[selected_index].get_attribute('href')}?tab=instructions"
            selected_mod_title = mod_title_elements[selected_index]
            mod_link = selected_mod_title.get_attribute("href")
            driver.get(dependencies_url)

            dependency_links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/mod/']")
            for dependency_link in dependency_links:
                if(dependency_link.accessible_name != "Thumbnail" and  dependency_link.accessible_name != "BeardLib" and dependency_link.accessible_name != "SuperBLT" and not dependency_link.accessible_name.__contains__(" Download")):
                    dependency_mod_number = dependency_link.get_attribute("href").split("/")[-1]
                    download_dependency_mod(dependency_mod_number)

            break
        else:
            print("Invalid selection. Please try again.")



    # Open the mod page
    driver.get(mod_link)

    # Find the download button
    download_button = driver.find_element(By.CSS_SELECTOR, "a.button.button-primary.large-button.flex-1")

    # Get the download link
    download_link = download_button.get_attribute("href")
    driver.get(download_link)
    download_link = driver.find_element(By.CSS_SELECTOR, "a[download][href*='storage.modworkshop.net']").get_attribute("href")

    # Download the mod file
    response = requests.get(download_link)

    # Extract the filename from the Content-Disposition header
    content_disposition = response.headers.get("Content-Disposition")
    if content_disposition:
        filename = unquote(content_disposition.split("filename=")[1].strip('"'))
    else:
        filename = os.path.basename(download_link.split("?")[0])


    instructions_url = dependencies_url

    # Check if the instructions page contains "mod_overrides"

    driver.get(instructions_url)
    instructions_text = driver.find_element(By.CLASS_NAME, "nav-menu-content")
    instructions_text = instructions_text.text

    if "CustomOST" in instructions_text or "customost" in instructions_text or "Customost" in instructions_text or "customOST" in instructions_text or "CustomOst" in instructions_text:
        # Create the "assets/mod_overrides" folder if it doesn't exist
        customost_folder = os.path.join(payday2_path, "mods", "CustomOSTTracks")
        os.makedirs(customost_folder, exist_ok=True)

        # Save the downloaded ZIP file temporarily
        zip_file_path = os.path.join(customost_folder, filename)
    elif "mod_overrides" in instructions_text:
        # Create the "assets/mod_overrides" folder if it doesn't exist
        mod_overrides_folder = os.path.join(payday2_path, "assets", "mod_overrides")
        os.makedirs(mod_overrides_folder, exist_ok=True)

        # Save the downloaded ZIP file temporarily
        zip_file_path = os.path.join(mod_overrides_folder, filename)
    else:
        # Create the "mods" folder if it doesn't exist
        mods_folder = os.path.join(payday2_path, "mods")
        os.makedirs(mods_folder, exist_ok=True)

        # Save the downloaded ZIP file temporarily
        zip_file_path = os.path.join(mods_folder, filename)

    with open(zip_file_path, "wb") as file:
        file.write(response.content)

    # Extract the contents of the ZIP file to the appropriate folder
    if not zip_file_path.__contains__("rar"):
        with zipfile.ZipFile(zip_file_path, "r") as zip_file:
            if "CustomOST" in instructions_text or "customost" in instructions_text or "Customost" in instructions_text or "customOST" in instructions_text or "CustomOst" in instructions_text:
                zip_file.extractall(customost_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {customost_folder}")
            elif "mod_overrides" in instructions_text:
                zip_file.extractall(mod_overrides_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {mod_overrides_folder}")
            else:
                zip_file.extractall(mods_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {mods_folder}")
    else:
        import rarfile
        rarfile.UNRAR_TOOL = os.path.join(os.path.dirname(__file__), "bin", "unrar.exe")
        with rarfile.RarFile(zip_file_path, "r") as rar_file:
            if "CustomOST" in instructions_text or "customost" in instructions_text or "Customost" in instructions_text or "customOST" in instructions_text or "CustomOst" in instructions_text:
                rar_file.extractall(customost_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {customost_folder}")
            elif "mod_overrides" in instructions_text:
                rar_file.extractall(mod_overrides_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {mod_overrides_folder}")
            else:
                rar_file.extractall(mods_folder)
                print(f"Extracted: {filename}")
                print(f"Saved to: {mods_folder}")

    # Delete the downloaded ZIP file
    os.remove(zip_file_path)


