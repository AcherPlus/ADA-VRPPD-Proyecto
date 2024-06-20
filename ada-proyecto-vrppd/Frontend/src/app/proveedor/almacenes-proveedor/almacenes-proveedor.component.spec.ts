import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlmacenesProveedorComponent } from './almacenes-proveedor.component';

describe('AlmacenesProveedorComponent', () => {
  let component: AlmacenesProveedorComponent;
  let fixture: ComponentFixture<AlmacenesProveedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AlmacenesProveedorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AlmacenesProveedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
