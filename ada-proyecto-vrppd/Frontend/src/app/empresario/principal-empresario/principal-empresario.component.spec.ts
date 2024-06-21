import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PrincipalEmpresarioComponent } from './principal-empresario.component';

describe('PrincipalEmpresarioComponent', () => {
  let component: PrincipalEmpresarioComponent;
  let fixture: ComponentFixture<PrincipalEmpresarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PrincipalEmpresarioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PrincipalEmpresarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
