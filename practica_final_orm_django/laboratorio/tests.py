from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio


# Create your tests here.
class LaboratorioTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear un laboratorio de ejemplo para pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre='Laboratorio de Prueba',
            ciudad='Ciudad de Prueba',
            pais='Pais de Prueba'
        )

    def test_laboratorio_data(self):
        # Verificar que los datos en la base de datos coinciden
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, 'Laboratorio de Prueba')
        self.assertEqual(laboratorio.ciudad, 'Ciudad de Prueba')
        self.assertEqual(laboratorio.pais, 'Pais de Prueba')

    def test_laboratorio_list_url(self):
        # respuesta HTTP 200
        response = self.client.get(reverse('laboratorio:laboratorio_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_list.html')

    def test_laboratorio_detail_view(self):
        # detalle del laboratorio devuelve una respuesta HTTP 200,
        # usa la plantilla correcta, y contiene el nombre del laboratorio en el HTML
        url = reverse('laboratorio:laboratorio_detail', args=[self.laboratorio.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_detail.html')
        self.assertContains(response, 'Laboratorio de Prueba')
