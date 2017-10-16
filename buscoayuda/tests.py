#from unittest import TestCase

from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

# Create your tests here.


class Kata_TDD_Test(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

        self.testData = {
            'nombre': 'Juan Daniel',
            'apellidos': 'Arevalo',
            'experiencia': '5',
            'telefono': '3173024578',
            'correo': 'jd.patino1@uniandes.edu.co',
            'imagen': '/home/kubuntu/Pictures/daman.jpeg',
            'nombre_usuario': 'juan645',
            'clave': 'clave123',
        }

        self.testComment = {
            'correo': 'correo@dominio.com',
            'comentario': 'Cortez y eficiente!!'
        }

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        testData = self.testData
        driver = self.browser
        driver.get('http://localhost:8000')
        link = driver.find_element_by_id('id_register')
        link.click()

        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.element_to_be_clickable((By.ID, 'register_modal')))

        nombre = driver.find_element_by_id('id_nombre')
        nombre.send_keys(testData.get('nombre'))

        apellidos = driver.find_element_by_id('id_apellidos')
        apellidos.send_keys(testData.get('apellidos'))

        experiencia = driver.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys(testData.get('experiencia'))

        driver.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = driver.find_element_by_id('id_telefono')
        telefono.send_keys(testData.get('telefono'))

        correo = driver.find_element_by_id('id_correo')
        correo.send_keys(testData.get('correo'))

        imagen = driver.find_element_by_id('id_imagen')
        imagen.send_keys(testData.get('imagen'))

        nombreUsuario = driver.find_element_by_id('id_username')
        nombreUsuario.send_keys(testData.get('nombre_usuario'))

        clave = driver.find_element_by_id('id_password')
        clave.send_keys(testData.get('clave'))

        botonGrabar = driver.find_element_by_id('id_grabar')
        botonGrabar.click()
        driver.implicitly_wait(3)
        span = driver.find_element(
            By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_verDetalle(self):
        driver = self.browser
        driver.get('http://localhost:8000')
        span = driver.find_element(
            By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = driver.find_element(
            By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_login(self):
        testData = self.testData
        driver = self.browser
        driver.get('http://localhost:8000')
        link = driver.find_element_by_id('id_login')
        link.click()

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.element_to_be_clickable((By.ID, 'login_modal')))

        nombreUsuario = driver.find_element_by_id('id_login_username')
        nombreUsuario.send_keys(testData.get('nombre_usuario'))

        clave = driver.find_element_by_id('id_login_password')
        clave.send_keys(testData.get('clave'))

        botonIngresar = driver.find_element_by_id('id_ingresar')
        botonIngresar.click()

        wait.until(
            EC.element_to_be_clickable((By.ID, 'logout')))

        welcome = driver.find_element_by_id('welcome_user')

        self.assertIn(testData.get('nombre'), welcome.text)

    def test_comentario(self):
        testComment = self.testComment
        driver = self.browser
        driver.get('http://localhost:8000')

        span = driver.find_element(
            By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        wait = WebDriverWait(driver, 10)

        submit = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-success')))

        correo = driver.find_element_by_id('correo')
        correo.send_keys(testComment.get('correo'))

        comentario = driver.find_element_by_id('comentario')
        comentario.send_keys(testComment.get('comentario'))

        submit.click()

        paragraph = driver.find_element(
            By.XPATH, '//h4[text()="{}"]'.format(testComment.get('correo')))

        paragraph = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//h4[text()="{}"]'.format(testComment.get('correo')))))

        self.assertIn(testComment.get('correo'), paragraph.text)
