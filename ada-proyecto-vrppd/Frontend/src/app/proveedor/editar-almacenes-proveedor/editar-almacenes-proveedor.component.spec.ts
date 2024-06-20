import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditarAlmacenesProveedorComponent } from './editar-almacenes-proveedor.component';

describe('EditarAlmacenesProveedorComponent', () => {
  let component: EditarAlmacenesProveedorComponent;
  let fixture: ComponentFixture<EditarAlmacenesProveedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EditarAlmacenesProveedorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditarAlmacenesProveedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
